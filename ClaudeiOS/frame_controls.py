# The iOS / Android switch shown under the device in browse_prototype1_web.html and browse_prototype1_ipad.html.
# Imported by build_web_frame.py and build_ipad_frame.py. It flips the same classes ?platform=android sets
# (os-android, platform-android) and keeps the URL in step, so a reload stays on the picked platform.

CSS = """
  .frame-controls{ position:fixed; right:20px; bottom:20px; z-index:100; display:flex; align-items:center; gap:10px; }
  .frame-controls .rotate-btn{ position:static; }
  .platform-switch{ position:relative; display:flex; height:44px; padding:4px; border-radius:22px;
    background:rgba(255,255,255,.1); border:1px solid rgba(255,255,255,.18);
    backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); box-shadow:0 8px 20px rgba(0,0,0,.35); }
  .platform-switch::before{ content:''; position:absolute; top:4px; bottom:4px; left:4px; width:calc((100% - 8px) / 2); border-radius:18px;
    background:rgba(255,255,255,.2); transition:transform .3s cubic-bezier(.32,.72,0,1); }
  .platform-switch.is-android::before{ transform:translateX(100%); }
  .platform-switch button{ position:relative; z-index:1; width:84px; border:none; background:none; cursor:pointer; border-radius:18px;
    font-family:-apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size:14px; font-weight:600; color:rgba(244,241,233,.6);
    transition:color .2s ease; }
  .platform-switch button[aria-pressed="true"]{ color:#F4F1E9; }
  .platform-switch button:focus-visible{ outline:2px solid #F4F1E9; outline-offset:-2px; }
  @media (prefers-reduced-motion: reduce){ .platform-switch::before{ transition:none; } }
"""

HTML = """<div class="platform-switch" id="platformSwitch" role="group" aria-label="Platform">
  <button type="button" data-platform="ios" aria-pressed="true">iOS</button>
  <button type="button" data-platform="android" aria-pressed="false">Android</button>
</div>"""

JS = """
<script>
  // iOS / Android switch: the same classes ?platform=android sets, plus the URL so a reload keeps the choice.
  (function(){
    var root = document.documentElement;
    var sw = document.getElementById('platformSwitch');
    var btns = Array.prototype.slice.call(sw.querySelectorAll('button'));
    function render(){
      var android = root.classList.contains('os-android');
      sw.classList.toggle('is-android', android);
      btns.forEach(function(b){ b.setAttribute('aria-pressed', String((b.dataset.platform === 'android') === android)); });
    }
    function setPlatform(android){
      root.classList.toggle('os-android', android);
      root.classList.toggle('platform-android', android);
      try{
        var url = new URL(location.href);
        if(android) url.searchParams.set('platform', 'android'); else url.searchParams.delete('platform');
        history.replaceState(null, '', url);
      }catch(e){}
      render();
    }
    btns.forEach(function(b){ b.addEventListener('click', function(){ setPlatform(b.dataset.platform === 'android'); }); });
    render();
  })();
</script>
"""

# Android status-bar icons (wifi, signal, battery), shown instead of the iOS ones when the switch is on Android
ANDROID_ICONS = """<div class="status-icons android-icons">
        <svg viewBox="0 0 24 24" width="17" height="17" fill="currentColor"><path d="M12 20.5 1 8.6a16 16 0 0 1 22 0z"/></svg>
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M21.5 2.5v19h-19z"/></svg>
        <svg viewBox="0 0 12 20" width="9" height="15" fill="currentColor"><rect x="3.5" y="0" width="5" height="2.2" rx=".6"/><rect x="0" y="2" width="12" height="18" rx="2.2"/></svg>
      </div>"""

ANDROID_STATUS_CSS = """
  /* Android: Roboto time on the left, Material status icons on the right */
  .web-statusbar .android-icons{ display:none; gap:5px; }
  .os-android .web-statusbar .status-icons:not(.android-icons){ display:none; }
  .os-android .web-statusbar .android-icons{ display:flex; }
  .os-android .web-statusbar .time{ font-family:Roboto, "Google Sans", system-ui, sans-serif; font-weight:500; letter-spacing:.1px; }
  .os-android .web-statusbar .time .date{ display:none; }
"""

# Android three-button navigation (back, home, recents) on a black bar at the bottom of the screen.
# The frames' bottom safe area is var(--sab): the home-indicator height on iOS, the 48px bar on Android.
NAVBAR_HTML = """<div class="android-navbar" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M17 4.5v15L5.5 12z"/></svg>
      <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><circle cx="12" cy="12" r="7.5"/></svg>
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><rect x="5.5" y="5.5" width="13" height="13" rx="1.5"/></svg>
    </div>"""

NAVBAR_CSS = """
  :root.os-android{ --sab:48px; }
  .android-navbar{ display:none; position:absolute; left:0; right:0; bottom:0; height:48px; z-index:41; pointer-events:none;
    align-items:center; justify-content:center; gap:var(--navbar-gap, 76px); background:#000; color:#fff; }
  .os-android .android-navbar{ display:flex; }
  .os-android .home-indicator{ display:none; }
  /* On a device the system bar overlaps the bottom of the 80px tab bar; in the mockup the black bar sits below it,
     so the tab bar is trimmed to 56px with its icons centred, leaving no empty strip under them. */
  .os-android #screen{ --classic-bar:56px; }
  .os-android .tabbar-wrap.classic .tab{ justify-content:center; padding-top:0; }
"""
