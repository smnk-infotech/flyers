export function initGA(measurementId?: string) {
  if (!measurementId) return
  // Avoid double-inject
  if (document.getElementById('ga4-script')) return
  const s = document.createElement('script')
  s.async = true
  s.id = 'ga4-script'
  s.src = `https://www.googletagmanager.com/gtag/js?id=${measurementId}`
  document.head.appendChild(s)
  const inline = document.createElement('script')
  inline.innerHTML = `
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', '${measurementId}');
  `
  document.head.appendChild(inline)
}
