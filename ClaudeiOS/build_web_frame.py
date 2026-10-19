# Builds ClaudeiOS/browse_prototype1_web.html: browse_prototype1.html shown inside an iPhone frame for desktop browsers.
import os
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, 'browse_prototype1.html')
dst = os.path.join(here, 'browse_prototype1_web.html')
s=open(src,newline='').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:70])
    s=s.replace(a,b)
# Simulated iPhone safe areas (a desktop browser reports 0)
s=s.replace('env(safe-area-inset-top)','59px').replace('env(safe-area-inset-bottom)','34px')
rep('<title>MUBI — Browse Prototype 1</title>','<title>MUBI — Browse Prototype 1 (iPhone frame)</title>')
rep('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover, user-scalable=no">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">')
frame_css = """
  /* ─── WEB MOCK: the prototype inside an iPhone 17 frame ───
     Generated from browse_prototype1.html. The phone is drawn at real iPhone 17 point size
     (402x874) plus a 12px bezel = 426x898, then scaled as one unit to fit the browser window.
     Safe areas are simulated (59px top for the Dynamic Island, 34px bottom for the home bar). */
  .stage{ display:flex; align-items:center; justify-content:center; background:#23262E; }
  .phone-scale-wrapper{ position:relative; height:min(94vh,1600px); width:auto; max-width:94vw; aspect-ratio:426/898; }
  .phone{ position:absolute; top:0; left:0; width:426px; height:898px; transform:scale(var(--phone-scale, 1)); transform-origin:top left; }
  .frame{ position:absolute; inset:0; border-radius:55px; padding:12px;
    background:linear-gradient(155deg,#3a3733 0%,#151414 35%,#0a0a0a 60%,#3a3733 100%);
    box-shadow:0 30px 60px rgba(0,0,0,.6), inset 0 0 0 1px rgba(255,255,255,.08); }
  .frame .screen{ border-radius:43px; }
  .side-btn{ position:absolute; border-radius:3px; box-shadow:inset 0 0 0 1px rgba(255,255,255,.1), 0 1px 3px rgba(0,0,0,.45); }
  .side-btn.left{ left:-1.4%; width:1.7%; border-radius:3px 1px 1px 3px; background:linear-gradient(90deg,#1c1e21 0%,#4a4e56 45%,#5b5f68 55%,#26282d 100%); }
  .side-btn.right{ right:-1.4%; width:1.7%; border-radius:1px 3px 3px 1px; background:linear-gradient(270deg,#1c1e21 0%,#4a4e56 45%,#5b5f68 55%,#26282d 100%); }
  .btn-action{ top:11%; height:2.6%; } .btn-vol-up{ top:16.6%; height:4%; } .btn-vol-down{ top:22.1%; height:4%; } .btn-power{ top:17.5%; height:6.6%; }
  .island{ position:absolute; top:11px; left:50%; transform:translateX(-50%); width:126px; height:37px; border-radius:20px; background:#000; z-index:40; }
  .web-statusbar{ position:absolute; top:0; left:0; right:0; height:54px; z-index:39; padding:0 30px 0 44px; pointer-events:none;
    display:flex; justify-content:space-between; align-items:center; color:#18140F; }
  .web-statusbar .time{ font-family:-apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-weight:600; font-size:16px; font-variant-numeric:tabular-nums; }
  .web-statusbar .status-icons{ display:flex; align-items:center; gap:6px; }
  :root[data-theme="dark"] .web-statusbar{ color:#fff; }
  .home-indicator{ position:absolute; bottom:8px; left:50%; transform:translateX(-50%); width:134px; height:5px; border-radius:3px;
    background:rgba(0,0,0,.85); z-index:40; pointer-events:none; }
  :root[data-theme="dark"] .home-indicator{ background:rgba(255,255,255,.85); }
"""
i=s.index('</style>'); s=s[:i]+frame_css+s[i:]
statusbar = """
    <div class="web-statusbar" aria-hidden="true">
      <span class="time">9:41</span>
      <div class="status-icons">
        <svg viewBox="0 0 18 12" width="17" height="11" fill="currentColor"><rect x="0" y="7" width="3" height="5" rx="1"/><rect x="5" y="4.5" width="3" height="7.5" rx="1"/><rect x="10" y="2" width="3" height="10" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg>
        <svg viewBox="0 0 16 12" width="15" height="11" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M1 4.5a10.5 10.5 0 0 1 14 0"/><path d="M3.6 7.3a6.6 6.6 0 0 1 8.8 0"/><circle cx="8" cy="10" r="1" fill="currentColor" stroke="none"/></svg>
        <svg viewBox="0 0 25 12" width="24" height="11" fill="none" stroke="currentColor" stroke-width="1"><rect x="0.5" y="0.5" width="20" height="11" rx="2.5"/><rect x="22" y="4" width="1.6" height="4" rx="0.8" fill="currentColor" stroke="none"/><rect x="2" y="2" width="16.5" height="8" rx="1.2" fill="currentColor" stroke="none"/></svg>
      </div>
    </div>
    <div class="island" aria-hidden="true"></div>
"""
rep("""<div class="stage">
  <div class="screen" id="screen">
""","""<div class="stage">
<div class="phone-scale-wrapper" id="phoneScaleWrapper">
<div class="phone" id="phoneCanvas">
<div class="frame">
  <div class="side-btn left btn-action"></div><div class="side-btn left btn-vol-up"></div>
  <div class="side-btn left btn-vol-down"></div><div class="side-btn right btn-power"></div>
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
</div>

<script>
  // Scale the 426x898 phone canvas to fill its wrapper (keeps every part in proportion).
  (function(){
    var wrapper = document.getElementById('phoneScaleWrapper');
    var canvas = document.getElementById('phoneCanvas');
    function applyScale(){
      var w = wrapper.getBoundingClientRect().width;
      if(w > 0) canvas.style.setProperty('--phone-scale', w / 426);
    }
    if(window.ResizeObserver) new ResizeObserver(applyScale).observe(wrapper);
    else window.addEventListener('resize', applyScale);
    applyScale();
  })();
</script>
""")
s = "<!-- Generated from browse_prototype1.html: the same prototype in an iPhone frame for viewing in a desktop browser. -->\n" + s
open(dst,'w',newline='').write(s)
print('written', len(s))
