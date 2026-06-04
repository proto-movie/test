/**
 * Converts london_cinema_showtimes.csv → cinema_data.js
 * Groups showtimes by cinema+date, enriches with lat/lng coordinates
 */
const fs = require('fs');

const COORDS = {
  'BFI IMAX':                        [51.5054, -0.1132],
  'Barbican Cinema':                  [51.5208, -0.0934],
  'Cineworld Bexleyheath':           [51.4614,  0.1392],
  'Cineworld Feltham':               [51.4452, -0.4100],
  'Cineworld Hounslow':              [51.4680, -0.3600],
  'Cineworld Ilford':                [51.5588,  0.0841],
  'Cineworld Leicester Square':      [51.5127, -0.1288],
  'Cineworld The O2 Greenwich':      [51.5030,  0.0033],
  'Cineworld Wandsworth':            [51.4556, -0.1886],
  'Cineworld Wembley':               [51.5560, -0.2796],
  'Cineworld West India Quay':       [51.5073, -0.0198],
  'Cineworld Wood Green':            [51.5975, -0.1107],
  'Clapham Picturehouse':            [51.4592, -0.1387],
  'Crouch End Picturehouse':         [51.5820, -0.1100],
  'Curzon Aldgate':                  [51.5139, -0.0690],
  'Curzon Bloomsbury':               [51.5174, -0.1245],
  'Curzon Camden':                   [51.5401, -0.1426],
  'Curzon Hoxton':                   [51.5272, -0.0800],
  'Curzon Kingston':                 [51.4126, -0.3038],
  'Curzon Mayfair':                  [51.5099, -0.1439],
  'Curzon Richmond':                 [51.4613, -0.3006],
  'Curzon Soho':                     [51.5133, -0.1315],
  'Curzon Victoria':                 [51.4969, -0.1406],
  'Curzon Wimbledon':                [51.4210, -0.2037],
  'Ealing Cinema':                   [51.5133, -0.3027],
  'East Dulwich Picturehouse':       [51.4561, -0.0801],
  'Everyman Baker Street':           [51.5209, -0.1570],
  'Everyman Borough Yards':          [51.5049, -0.0965],
  'Everyman Canary Wharf':           [51.5055, -0.0218],
  'Everyman Chelsea':                [51.4875, -0.1711],
  "Everyman King's Cross":           [51.5357, -0.1241],
  'Everyman Screen on the Green':    [51.5394, -0.1020],
  'Everyman at The Whiteley':        [51.5131, -0.1904],
  'Finsbury Park Picturehouse':      [51.5641, -0.1061],
  'Gate Picturehouse':               [51.5077, -0.1976],
  'Greenwich Picturehouse':          [51.4761, -0.0126],
  'Hackney Picturehouse':            [51.5447, -0.0549],
  'Odeon Acton':                     [51.5080, -0.2729],
  'Odeon Greenwich':                 [51.4914,  0.0161],
  'Odeon Holloway':                  [51.5653, -0.1099],
  'Odeon Islington':                 [51.5333, -0.1063],
  'Odeon Kingston':                  [51.4126, -0.3060],
  'Odeon Luxe Haymarket':            [51.5099, -0.1322],
  'Odeon Luxe Leicester Square':     [51.5115, -0.1289],
  'Odeon Luxe West End':             [51.5107, -0.1296],
  'Odeon Putney':                    [51.4615, -0.2163],
  'Odeon Richmond':                  [51.4613, -0.3006],
  'Odeon Streatham':                 [51.4276, -0.1241],
  'Odeon Tottenham Court Road':      [51.5182, -0.1330],
  'Phoenix Cinema':                  [51.5913, -0.1767],
  'Picturehouse Central':            [51.5155, -0.1368],
  'Prince Charles Cinema':           [51.5120, -0.1294],
  'Rio Cinema':                      [51.5449, -0.0749],
  'Ritzy Brixton':                   [51.4616, -0.1143],
  'The Garden Cinema':               [51.5110, -0.1234],
  'Vue Finchley Road':               [51.5552, -0.1778],
  'Vue Fulham Broadway':             [51.4812, -0.1882],
  'Vue Islington':                   [51.5333, -0.1063],
  'Vue North Finchley':              [51.6005, -0.1789],
  'Vue Piccadilly':                  [51.5099, -0.1354],
  "Vue Shepherd's Bush":             [51.5042, -0.2238],
  'Vue West End (Leicester Square)': [51.5117, -0.1285],
  'Vue Westfield':                   [51.5069, -0.2263],
  'Vue Westfield Stratford':         [51.5432,  0.0085],
  'Vue Wood Green':                  [51.5975, -0.1107],
  'West Norwood Picturehouse':       [51.4347, -0.1060],
};

function parseCSVLine(line) {
  const result = [];
  let cur = '', inQ = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (c === '"') {
      if (inQ && line[i + 1] === '"') { cur += '"'; i++; }
      else inQ = !inQ;
    } else if (c === ',' && !inQ) {
      result.push(cur); cur = '';
    } else {
      cur += c;
    }
  }
  result.push(cur);
  return result;
}

const csv = fs.readFileSync('london_cinema_showtimes.csv', 'utf8');
const lines = csv.split('\n').filter(l => l.trim());

const cinemaMap = new Map();
let skipped = 0;

for (let i = 1; i < lines.length; i++) {
  const f = parseCSVLine(lines[i]);
  if (f.length < 7) continue;
  const [name, address, date, title, cert, runtime, time] = f;
  if (!name || !date || !title || !time) continue;

  if (!cinemaMap.has(name)) {
    const coords = COORDS[name];
    if (!coords) { skipped++; continue; }
    cinemaMap.set(name, { n: name, a: address, c: coords, s: {} });
  }
  const cinema = cinemaMap.get(name);
  if (!cinema) continue;
  if (!cinema.s[date]) cinema.s[date] = [];
  // Store as compact [title, cert, time] — deduplicate
  const key = `${title}|${time}`;
  if (!cinema.s[date].some(r => `${r[0]}|${r[2]}` === key)) {
    cinema.s[date].push([title, cert || '', time]);
  }
}

const cinemas = [...cinemaMap.values()];
const output = `/* Auto-generated by build_data.js — DO NOT EDIT */\nwindow.CINEMA_DATA=${JSON.stringify({ cinemas })};\n`;
fs.writeFileSync('cinema_data.js', output);

console.log(`✅ cinema_data.js written`);
console.log(`   ${cinemas.length} cinemas with coordinates`);
if (skipped) console.log(`   ${skipped} rows skipped (no coords)`);
const totalShowtimes = cinemas.reduce((s, c) => s + Object.values(c.s).reduce((a, v) => a + v.length, 0), 0);
console.log(`   ${totalShowtimes.toLocaleString()} showtimes total`);
const dates = new Set(cinemas.flatMap(c => Object.keys(c.s)));
console.log(`   Date range: ${[...dates].sort()[0]} → ${[...dates].sort().at(-1)}`);
