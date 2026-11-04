# Builds ClaudeiOS/browse_prototype1_ipad.html: browse_prototype1.html shown inside an iPad frame for desktop browsers.
# Sibling of build_web_frame.py (the iPhone version); rerun after editing browse_prototype1.html.
import os
import frame_controls
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, 'browse_prototype1.html')
dst = os.path.join(here, 'browse_prototype1_ipad.html')
s=open(src,newline='').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70])
    s=s.replace(a,b)
# Simulated iPad safe areas (a desktop browser reports 0): 24px status bar, 20px home indicator
s=s.replace('env(safe-area-inset-top)','24px').replace('env(safe-area-inset-bottom)','20px')
# Floating header buttons were pinned just under the iPhone's Dynamic Island; sit them under the iPad status bar
rep('top:54px;','top:30px;',3)
# Counts say "titles" rather than "films" (directors grid, a director's page, the directors sort menu)
rep("d.count + ' film' + (d.count !== 1 ? 's' : '')", "d.count + ' title' + (d.count !== 1 ? 's' : '')")
rep("films.length + ' film' + (films.length !== 1 ? 's' : '')", "films.length + ' title' + (films.length !== 1 ? 's' : '')")
rep('<span>No. of Films</span>','<span>No. of Titles</span>')
# Measure the status-bar inset on screen, so pinned pills are detected when the iPad is scaled up (e.g. landscape)
rep("var top = panel.getBoundingClientRect().top + probe.offsetHeight;",
    "var top = panel.getBoundingClientRect().top + probe.getBoundingClientRect().height;")
# Sort popover sits under the icon that opened it (iOS iPad only; Android keeps a bottom sheet)
rep("    function makeSheet(menu){",
"""    function placePopover(btn, menu){
      if(document.documentElement.classList.contains('os-android')){ menu.style.top = menu.style.right = ''; return; }
      var sr = screenEl.getBoundingClientRect(), k = sr.width / screenEl.offsetWidth, br = btn.getBoundingClientRect();
      menu.style.top = ((br.bottom - sr.top) / k + 8) + 'px';
      menu.style.right = Math.max(16, (sr.right - br.right) / k - 4) + 'px';
    }
    function makeSheet(menu){""")
rep("if(!isOpen){ menu.classList.add('open'); sortScrim.classList.add('open'); }",
    "if(!isOpen){ placePopover(btn, menu); menu.classList.add('open'); sortScrim.classList.add('open'); }")
# Grid view by default (list view off; it can still be turned on in the More tab)
rep("bindMoreToggle('listViewToggle', function(on){ listOn = on; setMode(on); applyTopAlign(); }, true);",
    "bindMoreToggle('listViewToggle', function(on){ listOn = on; setMode(on); applyTopAlign(); }, false);")
# A director's films follow the List view setting: list rows when it's on, image tiles when it's off.
# The list styling only applies to #directorPageGrid.list-mode; hiding the director's own name stays for both.
_keep = ['#directorPageGrid .expl-card p .fd-director{ display:none; }', '#directorPageGrid .expl-card p .fd-meta{ display:inline; }']
for i,k in enumerate(_keep): rep(k, '@@KEEP%d@@' % i)
s = s.replace('#directorPageGrid .expl', '#directorPageGrid.list-mode .expl')
rep('#filmGrid.list-mode, #directorPageGrid, #searchFilmResults{ gap:10px; }', '#filmGrid.list-mode, #directorPageGrid.list-mode, #searchFilmResults{ gap:10px; }')
for i,k in enumerate(_keep): rep('@@KEEP%d@@' % i, k)
rep('#directorPageGrid .expl-card p .fd-meta{ display:inline; }',
    '#directorPageGrid.list-mode .expl-card p .fd-meta, #directorPageGrid .expl-card p .fd-meta{ display:inline; }')
rep("[filmGrid, browseTabs, segFilms, segCollections, segDirectors, directorsGrid].forEach(function(el){",
    "[filmGrid, browseTabs, segFilms, segCollections, segDirectors, directorsGrid, document.getElementById('directorPageGrid')].forEach(function(el){")
rep('<title>MUBI — Browse Prototype 1</title>','<title>MUBI — Browse Prototype 1 (iPad frame)</title>')
rep('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover, user-scalable=no">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">')
frame_css = """
  /* ─── WEB MOCK: the prototype inside an iPad Air 11" frame ───
     Generated from browse_prototype1.html. The iPad is drawn at real point size (820x1180, portrait)
     plus an 18px bezel = 856x1216, then scaled as one unit to fit the browser window.
     Safe areas are simulated (24px top status bar, 20px bottom home indicator). */
  .stage{ display:flex; align-items:center; justify-content:center; background:#23262E; }
  .phone-scale-wrapper{ position:relative; width:var(--wrap-w, 600px); height:var(--wrap-h, 852px); }
  .phone{ position:absolute; top:0; left:0; width:856px; height:1216px; transform:scale(var(--phone-scale, 1)); transform-origin:top left; }
  .frame{ position:absolute; inset:0; border-radius:38px; padding:18px;
    background:linear-gradient(155deg,#3a3733 0%,#151414 35%,#0a0a0a 60%,#3a3733 100%);
    box-shadow:0 30px 60px rgba(0,0,0,.6), inset 0 0 0 1px rgba(255,255,255,.08); }
  .frame .screen{ border-radius:20px; }
  .side-btn{ position:absolute; border-radius:3px; box-shadow:inset 0 0 0 1px rgba(255,255,255,.1), 0 1px 3px rgba(0,0,0,.45); }
  .side-btn.right{ right:-.7%; width:.9%; border-radius:1px 3px 3px 1px; background:linear-gradient(270deg,#1c1e21 0%,#4a4e56 45%,#5b5f68 55%,#26282d 100%); }
  .side-btn.top{ top:-.5%; height:.65%; border-radius:3px 3px 1px 1px; background:linear-gradient(0deg,#1c1e21 0%,#4a4e56 45%,#5b5f68 55%,#26282d 100%); }
  .btn-top{ right:8%; width:7%; } .btn-vol-up{ top:9%; height:4.2%; } .btn-vol-down{ top:14.2%; height:4.2%; }
  .ipad-camera{ position:absolute; top:6px; left:50%; transform:translateX(-50%); width:7px; height:7px; border-radius:50%;
    background:radial-gradient(circle at 35% 35%, #2b3a55 0%, #0b0d12 60%); box-shadow:0 0 0 1px rgba(255,255,255,.06); }
  .web-statusbar{ position:absolute; top:0; left:0; right:0; height:24px; z-index:39; padding:0 22px; pointer-events:none;
    display:flex; justify-content:space-between; align-items:center; color:#18140F; }
  .web-statusbar .time{ font-family:-apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-weight:600; font-size:13px; font-variant-numeric:tabular-nums; }
  .web-statusbar .time .date{ margin-left:6px; }
  .web-statusbar .status-icons{ display:flex; align-items:center; gap:6px; font-family:-apple-system, BlinkMacSystemFont, sans-serif; font-weight:600; font-size:12px; }
  :root[data-theme="dark"] .web-statusbar{ color:#fff; }
  .home-indicator{ position:absolute; bottom:7px; left:50%; transform:translateX(-50%); width:300px; height:5px; border-radius:3px;
    background:rgba(0,0,0,.85); z-index:40; pointer-events:none; }
  :root[data-theme="dark"] .home-indicator{ background:rgba(255,255,255,.85); }

  /* ─── iPad layout: more columns, a centred tab bar ─── */
  /* One gap between tiles, across and down, for every list and grid; side margins stay at 20px */
  #screen{ --tile-gap:8px; }
  /* The sort icon itself (not its invisible 48px button) sits 20px from the right edge, matching the side margins */
  .browse-actions-overlay{ right:3.8px; }
  /* A director's page in grid view is white like Browse; it stays grey in list view */
  .director-page:has(#directorPageGrid:not(.list-mode)){ background:var(--ink); }
  .director-page:has(#directorPageGrid:not(.list-mode)) .director-page-nav.collapsed{ background:rgba(255,255,255,.82); }
  /* Director page's collapsed title bar: 98px suited the iPhone's Dynamic Island; the iPad's back button ends at 64px */
  .director-page-nav{ height:72px; }
  /* Tiles sit 4px closer to the pills above them */
  .expl-list, .coll-list, .director-grid{ padding-top:2px; }
  .hero{ aspect-ratio:16/9; }
  .poster{ flex-basis:150px; }
  #filmGrid.poster-mode, #genreDetailGrid.poster-mode, #collectionsGrid.poster-mode{ grid-template-columns:repeat(4,1fr); gap:var(--tile-gap); }
  .director-grid{ grid-template-columns:repeat(5,1fr); gap:var(--tile-gap); }
  #filmGrid.list-mode, #directorPageGrid, #searchFilmResults, #collectionsGrid.list-mode, .director-grid.list-mode{
    display:grid; grid-template-columns:repeat(2,1fr); gap:var(--tile-gap); }
  .coll-list, .expl-list{ display:grid; grid-template-columns:repeat(2,1fr); gap:var(--tile-gap); }
  .tabbar-wrap{ left:calc(50% - 280px); right:calc(50% - 280px); }

  /* ─── Landscape: the iPad turned 90° anticlockwise (1180x820 screen) ───
     Camera moves to the left bezel, the volume buttons to the top edge, the top button to the left edge. */
  .phone.landscape{ width:1216px; height:856px; }
  .phone.landscape .ipad-camera{ top:50%; left:6px; transform:translateY(-50%); }
  .phone.landscape .btn-top{ right:auto; left:-.5%; top:8%; width:.65%; height:5%; border-radius:3px 1px 1px 3px;
    background:linear-gradient(90deg,#1c1e21 0%,#4a4e56 45%,#5b5f68 55%,#26282d 100%); }
  .phone.landscape .side-btn.right{ right:auto; top:-.7%; height:1.3%; border-radius:3px 3px 1px 1px;
    background:linear-gradient(0deg,#1c1e21 0%,#4a4e56 45%,#5b5f68 55%,#26282d 100%); }
  .phone.landscape .side-btn.btn-vol-up{ left:9%; width:3%; } .phone.landscape .side-btn.btn-vol-down{ left:12.6%; width:3%; }
  .phone.landscape .hero{ aspect-ratio:21/9; }
  .phone.landscape #filmGrid.poster-mode, .phone.landscape #genreDetailGrid.poster-mode, .phone.landscape #collectionsGrid.poster-mode{ grid-template-columns:repeat(6,1fr); }
  .phone.landscape .director-grid{ grid-template-columns:repeat(7,1fr); }
  .phone.landscape #filmGrid.list-mode, .phone.landscape #directorPageGrid, .phone.landscape #searchFilmResults,
  .phone.landscape #collectionsGrid.list-mode, .phone.landscape .director-grid.list-mode, .phone.landscape .coll-list, .phone.landscape .expl-list{ grid-template-columns:repeat(3,1fr); }

  .rotate-btn{ position:fixed; right:20px; bottom:20px; z-index:100; display:flex; align-items:center; gap:8px;
    height:44px; padding:0 18px 0 14px; border-radius:22px; cursor:pointer;
    font-family:-apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size:14px; font-weight:600; color:#F4F1E9;
    background:rgba(255,255,255,.1); border:1px solid rgba(255,255,255,.18);
    backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); box-shadow:0 8px 20px rgba(0,0,0,.35); }
  .rotate-btn:hover{ background:rgba(255,255,255,.16); }
  .rotate-btn:focus-visible{ outline:2px solid #F4F1E9; outline-offset:2px; }
  .rotate-btn svg{ transition:transform .5s cubic-bezier(.32,.72,0,1); }
  .rotate-btn.is-landscape svg{ transform:rotate(-90deg); }
  @keyframes ipad-turn-to-landscape{ from{ transform:rotate(90deg) scale(.82); opacity:.4; } to{ transform:none; opacity:1; } }
  @keyframes ipad-turn-to-portrait{ from{ transform:rotate(-90deg) scale(.82); opacity:.4; } to{ transform:none; opacity:1; } }
  .phone-scale-wrapper.turning-landscape{ animation:ipad-turn-to-landscape .5s cubic-bezier(.32,.72,0,1); }
  .phone-scale-wrapper.turning-portrait{ animation:ipad-turn-to-portrait .5s cubic-bezier(.32,.72,0,1); }
  @media (prefers-reduced-motion: reduce){
    .phone-scale-wrapper.turning-landscape, .phone-scale-wrapper.turning-portrait{ animation:none; }
    .rotate-btn svg{ transition:none; }
  }

  /* iPad (iOS): Filter opens as a centred form sheet, Sort as a popover under its icon.
     Android keeps its 640px Material bottom sheets. */
  :root:not(.os-android) .filter-sheet{ top:50%; bottom:auto; left:50%; right:auto; width:min(540px, calc(100% - 48px)); max-height:min(720px, calc(100% - 96px));
    border-radius:24px; border-bottom:1px solid rgba(24,20,15,.08); box-shadow:0 24px 60px rgba(24,20,15,.3);
    opacity:0; pointer-events:none; transform:translate(-50%, calc(-50% + 40px)) scale(.97);
    transition:transform .34s cubic-bezier(.32,.72,0,1), opacity .22s ease; }
  :root:not(.os-android) .filter-sheet.open{ opacity:1; pointer-events:auto; transform:translate(-50%, -50%); }
  :root:not(.os-android) .filter-sheet-grabber{ visibility:hidden; height:4px; margin:6px auto 0; }
  :root:not(.os-android) .filter-sheet-footer{ padding-bottom:16px; }
  :root:not(.os-android) .glass-menu.sort-sheet{ bottom:auto; left:auto; width:300px; padding:6px 8px 8px; border-radius:18px; border:1px solid rgba(24,20,15,.06);
    opacity:0; pointer-events:none; transform:scale(.9); transform-origin:top right;
    transition:transform .24s cubic-bezier(.32,.72,0,1), opacity .18s ease; box-shadow:0 18px 44px rgba(24,20,15,.22), 0 2px 8px rgba(24,20,15,.1); }
  :root:not(.os-android) .glass-menu.sort-sheet.open{ opacity:1; pointer-events:auto; transform:scale(1); box-shadow:0 18px 44px rgba(24,20,15,.22), 0 2px 8px rgba(24,20,15,.1); }
  :root:not(.os-android) .sort-sheet-grabber{ display:none; }
  :root:not(.os-android) .sort-sheet-title{ padding:8px 8px 4px; font-size:13px; opacity:.6; }
  :root:not(.os-android) .sort-sheet .glass-menu-item{ padding:12px 8px; font-size:15px; }
  :root:not(.os-android) .menu-scrim.sheet-dim{ background:transparent; }
"""
i=s.index('</style>'); s=s[:i]+frame_css+frame_controls.CSS+s[i:]
statusbar = """
    <div class="web-statusbar" aria-hidden="true">
      <span class="time">9:41<span class="date">Mon 2 Nov</span></span>
      <div class="status-icons">
        <svg viewBox="0 0 16 12" width="15" height="11" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M1 4.5a10.5 10.5 0 0 1 14 0"/><path d="M3.6 7.3a6.6 6.6 0 0 1 8.8 0"/><circle cx="8" cy="10" r="1" fill="currentColor" stroke="none"/></svg>
        <span>100%</span>
        <svg viewBox="0 0 25 12" width="24" height="11" fill="none" stroke="currentColor" stroke-width="1"><rect x="0.5" y="0.5" width="20" height="11" rx="2.5"/><rect x="22" y="4" width="1.6" height="4" rx="0.8" fill="currentColor" stroke="none"/><rect x="2" y="2" width="16.5" height="8" rx="1.2" fill="currentColor" stroke="none"/></svg>
      </div>
    </div>
"""
rep("""<div class="stage">
  <div class="screen" id="screen">
""","""<div class="stage">
<div class="phone-scale-wrapper" id="phoneScaleWrapper">
<div class="phone" id="phoneCanvas">
<div class="frame">
  <div class="ipad-camera" aria-hidden="true"></div>
  <div class="side-btn top btn-top"></div>
  <div class="side-btn right btn-vol-up"></div><div class="side-btn right btn-vol-down"></div>
  <div class="screen" id="screen">
"""+statusbar)
rep("""            <button class="fs3-apply" id="fs3Apply">Apply</button>
          </div>
        </div>

  </div>
</div>
""","""            <button class="fs3-apply" id="fs3Apply">Apply</button>
          </div>
        </div>

    <div class="home-indicator" aria-hidden="true"></div>
  </div>
</div>
</div>
</div>
<div class="frame-controls">
""" + frame_controls.HTML + """
<button class="rotate-btn" id="rotateBtn" type="button" aria-pressed="false" title="Rotate iPad">
  <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <rect x="7" y="3" width="10" height="18" rx="2"/><path d="M11 18h2"/>
  </svg>
  <span id="rotateLabel">Landscape</span>
</button>
</div>
</div>

<script>
  // Fit the iPad canvas (856x1216 portrait, 1216x856 landscape) inside 94% of the window, scaled as one unit,
  // and switch orientation from the Rotate button.
  (function(){
    var wrapper = document.getElementById('phoneScaleWrapper');
    var canvas = document.getElementById('phoneCanvas');
    var btn = document.getElementById('rotateBtn');
    var label = document.getElementById('rotateLabel');
    function size(){ return canvas.classList.contains('landscape') ? [1216, 856] : [856, 1216]; }
    function applyScale(){
      var d = size();
      var k = Math.min(window.innerWidth * .94 / d[0], window.innerHeight * .94 / d[1]);
      wrapper.style.setProperty('--wrap-w', (d[0] * k) + 'px');
      wrapper.style.setProperty('--wrap-h', (d[1] * k) + 'px');
      canvas.style.setProperty('--phone-scale', k);
    }
    function setOrientation(landscape, animate){
      canvas.classList.toggle('landscape', landscape);
      btn.classList.toggle('is-landscape', landscape);
      btn.setAttribute('aria-pressed', String(landscape));
      label.textContent = landscape ? 'Portrait' : 'Landscape';
      applyScale();
      if(animate){
        wrapper.classList.remove('turning-landscape', 'turning-portrait');
        void wrapper.offsetWidth;
        wrapper.classList.add(landscape ? 'turning-landscape' : 'turning-portrait');
      }
      try{ localStorage.setItem('ipadOrientation', landscape ? 'landscape' : 'portrait'); }catch(e){}
    }
    wrapper.addEventListener('animationend', function(){ wrapper.classList.remove('turning-landscape', 'turning-portrait'); });
    btn.addEventListener('click', function(){ setOrientation(!canvas.classList.contains('landscape'), true); });
    window.addEventListener('resize', applyScale);
    var saved = null;
    try{ saved = localStorage.getItem('ipadOrientation'); }catch(e){}
    setOrientation(saved === 'landscape', false);
  })();
</script>
""" + frame_controls.JS)
s = "<!-- Generated from browse_prototype1.html: the same prototype in an iPad frame for viewing in a desktop browser. -->\n" + s
open(dst,'w',newline='').write(s)
print('written', len(s))
