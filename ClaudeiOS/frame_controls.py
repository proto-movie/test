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
