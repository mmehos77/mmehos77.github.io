// Symptom Sorter (WFA) offline helper.
// Online: always fetch the newest files from GitHub first, and save them for offline use.
// Offline or very weak signal (no answer within 4 seconds): use the saved copy.
// Bump VERSION whenever index.html or the data changes.
const VERSION = 'ss-wfa-v5';
const CORE = ['./', './index.html'];                       // must save, or offline use won't work
const EXTRA = ['./manifest.webmanifest', './icon-192.png', './icon-512.png', './apple-touch-icon.png']; // saved if present
const TIMEOUT_MS = 4000;
const PREFIX = 'ss-wfa-';   // this app's saved copies; other apps on the same site use other names
// Only this app's own files (the /wfa/ folder). The FM-51 app at the site root is left alone.
const MINE = new Set(['./', ...CORE, ...EXTRA, './sw.js'].map(f => new URL(f, self.registration.scope).pathname));

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c =>
    c.addAll(CORE.map(f => new Request(f, { cache: 'reload' })))
     .then(() => Promise.all(EXTRA.map(f => c.add(new Request(f, { cache: 'reload' })).catch(() => {}))))
  ).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith(PREFIX) && k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

function fromNetwork(req) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('timeout')), TIMEOUT_MS);
    fetch(req, { cache: 'no-cache' }).then(res => {
      clearTimeout(timer);
      if (res.ok) { const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy)); }
      resolve(res);
    }, err => { clearTimeout(timer); reject(err); });
  });
}

self.addEventListener('fetch', e => {
  const req = e.request;
  const url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin) return;
  if (!MINE.has(url.pathname)) return;     // not this app's file: let the browser handle it
  if (url.searchParams.has('t')) return;   // update checks go straight to the network, never saved
  e.respondWith(
    fromNetwork(req).catch(() =>
      caches.match(req, { ignoreSearch: true }).then(hit => hit || caches.match('./index.html'))
    )
  );
});
