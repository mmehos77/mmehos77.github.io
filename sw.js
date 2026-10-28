// Symptom Sorter offline helper.
// Online: always fetch the newest files from GitHub first, and save them for offline use.
// Offline or very weak signal (no answer within 4 seconds): use the saved copy.
// Bump VERSION whenever index.html or the data changes.
const VERSION = 'ss-fm51-2025-v13';
const FILES = ['./', './index.html', './manifest.webmanifest', './icon.svg'];
const TIMEOUT_MS = 4000;

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(FILES.map(f => new Request(f, { cache: 'reload' })))).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
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
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  e.respondWith(
    fromNetwork(req).catch(() =>
      caches.match(req, { ignoreSearch: true }).then(hit => hit || caches.match('./index.html'))
    )
  );
});
