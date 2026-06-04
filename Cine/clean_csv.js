/**
 * Deduplicate and clean london_cinema_showtimes.csv
 * Removes:
 *  - duplicate header rows
 *  - exact duplicate rows
 *  - rows with bad data (empty titles, concatenated times, dates as titles, etc.)
 */
const fs = require('fs');
const path = require('path');

const FILE = path.join(__dirname, 'london_cinema_showtimes.csv');
const raw = fs.readFileSync(FILE, 'utf8');
const lines = raw.split('\n').map(l => l.trim()).filter(Boolean);

const HEADER = 'Cinema Name,Address,Date,Film Title,Certificate,Runtime,Showtime,Notes';

// Parse a CSV line (handles quoted fields)
function parseLine(line) {
  const fields = [];
  let cur = '', inQ = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (c === '"') {
      if (inQ && line[i+1] === '"') { cur += '"'; i++; }
      else inQ = !inQ;
    } else if (c === ',' && !inQ) {
      fields.push(cur); cur = '';
    } else {
      cur += c;
    }
  }
  fields.push(cur);
  return fields;
}

function isValidTime(t) {
  // HH:MM format only, no concatenation
  return /^\d{1,2}:\d{2}$/.test(t.trim()) && !t.includes(':') !== t.trim().match(/^\d{1,2}:\d{2}$/);
}

function isValidTitle(t) {
  if (!t || t.length < 2 || t.length > 200) return false;
  // Reject obvious garbage
  if (/^\d{4}-\d{2}-\d{2}/.test(t)) return false;           // date as title
  if (/^(today|tomorrow|monday|tuesday|wednesday|thursday|friday|saturday|sunday)/i.test(t)) return false;
  if (/^\d{1,2}:\d{2}$/.test(t)) return false;               // time as title
  if (/cinema/i.test(t) && t.length < 10) return false;      // "Cinema" alone
  if (/^Thu|^Fri|^Sat|^Sun|^Mon|^Tue|^Wed/.test(t)) return false; // day names
  if (/\d{4}-\d{2}-\d{2}/.test(t)) return false;
  return true;
}

function isValidDate(d) {
  return /^\d{4}-\d{2}-\d{2}$/.test(d) || /^\d{4}-\d{2}-\d{2}T/.test(d);
}

function normaliseDate(d) {
  const m = d.match(/^(\d{4}-\d{2}-\d{2})/);
  return m ? m[1] : d;
}

function normaliseTime(t) {
  t = t.trim();
  // Reject concatenated times like "13:3015:45"
  if (/\d{1,2}:\d{2}\d{1,2}:\d{2}/.test(t)) return null;
  // Reject ISO timestamps used as showtime
  if (t.length > 8) return null;
  return t;
}

const seen = new Set();
const good = [];
let headers = 0, dups = 0, bad = 0;

for (const line of lines) {
  if (line.startsWith('Cinema Name,')) { headers++; continue; }  // skip header rows
  const fields = parseLine(line);
  if (fields.length < 7) { bad++; continue; }

  const [cinema, address, date, title, cert, runtime, time, notes=''] = fields;
  const normDate = normaliseDate(date);
  const normTime = normaliseTime(time);

  if (!isValidTitle(title)) { bad++; continue; }
  if (!isValidDate(normDate)) { bad++; continue; }
  if (!normTime || !/^\d{1,2}:\d{2}$/.test(normTime)) { bad++; continue; }
  if (!cinema || cinema.length < 3) { bad++; continue; }

  const key = `${cinema}|${normDate}|${title.toLowerCase()}|${normTime}`;
  if (seen.has(key)) { dups++; continue; }
  seen.add(key);
  good.push([cinema, address, normDate, title, cert, runtime, normTime, notes]);
}

// Sort: cinema → date → time
good.sort((a, b) =>
  a[0].localeCompare(b[0]) ||
  a[2].localeCompare(b[2]) ||
  a[6].localeCompare(b[6])
);

const csv = HEADER + '\n' +
  good.map(r => r.map(v => `"${(v||'').replace(/"/g,'""')}"`)
    .join(','))
    .join('\n') + '\n';

fs.writeFileSync(FILE, csv);

console.log(`\nClean CSV written: ${good.length} rows`);
console.log(`  Headers removed: ${headers}`);
console.log(`  Duplicates removed: ${dups}`);
console.log(`  Bad rows removed: ${bad}`);

const cinemas = [...new Set(good.map(r => r[0]))].sort();
console.log(`\nCinemas (${cinemas.length}):`);
const byChain = {};
cinemas.forEach(c => {
  const count = good.filter(r => r[0] === c).length;
  const chain = c.includes('Vue') ? 'Vue' : c.includes('Cineworld') ? 'Cineworld' :
    c.includes('Everyman') ? 'Everyman' : c.includes('Curzon') ? 'Curzon' :
    c.includes('Picturehouse') || c.includes('Ritzy') || c.includes('Ealing') ? 'Picturehouse' : 'Independent';
  byChain[chain] = (byChain[chain] || 0) + count;
  console.log(`  ${c}: ${count}`);
});
console.log('\nBy chain:');
Object.entries(byChain).sort((a,b) => b[1]-a[1]).forEach(([k,v]) => console.log(`  ${k}: ${v}`));
