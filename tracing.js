(function(){
  function getGtag(){ return (typeof window !== 'undefined' && typeof window.gtag === 'function') ? window.gtag : null; }

  function sendPerf(){
    try {
      var gt = getGtag();
      if(!gt || !(performance && performance.getEntriesByType)) return;
      var nav = performance.getEntriesByType('navigation')[0];
      if(!nav) return;
      gt('event','page_metrics',{
        dns: Math.round(nav.domainLookupEnd - nav.domainLookupStart) || 0,
        connect: Math.round(nav.connectEnd - nav.connectStart) || 0,
        ttfb: Math.round(nav.responseStart - nav.requestStart) || 0,
        dom_content_loaded: Math.round(nav.domContentLoadedEventEnd - nav.startTime) || 0,
        load: Math.round(nav.loadEventEnd - nav.startTime) || 0
      });
    } catch(_){}
  }

  window.addEventListener('error', function(e){
    try {
      var gt = getGtag();
      if(!gt) return;
      gt('event','page_error',{
        event_category: 'js',
        description: (e && e.message) ? String(e.message) : 'error',
        fatal: false
      });
    } catch(_){}
  });

  window.addEventListener('unhandledrejection', function(e){
    try {
      var gt = getGtag();
      if(!gt) return;
      var desc = 'rejection';
      if(e && e.reason){
        if(typeof e.reason === 'string') desc = e.reason;
        else if(e.reason && e.reason.message) desc = e.reason.message;
        else desc = String(e.reason);
      }
      gt('event','unhandled_rejection',{
        event_category: 'js',
        description: desc
      });
    } catch(_){}
  });

  if (document.readyState === 'complete') sendPerf();
  else window.addEventListener('load', sendPerf);
})();