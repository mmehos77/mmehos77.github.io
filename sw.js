// Retired: the FM-51-only Symptom Sorter that lived at this address is no longer maintained (Nov 2026).
// A device that still has the old app installed picks up this file on its next update check. It then
// deletes the old app's saved copies, stops answering for this address, and reloads the open page,
// which now forwards to the WFA version at /wfa/. The WFA app's own helper and saved copies are left alone.
const PREFIX = 'ss-fm51-';

self.addEventListener('install', () => self.skipWaiting());

self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k.startsWith(PREFIX)).map(k => caches.delete(k)));
    await self.registration.unregister();
    const scope = new URL(self.registration.scope).pathname;
    const open = await self.clients.matchAll({ type: 'window' });
    for (const c of open) {
      const p = new URL(c.url).pathname;
      if (p === scope || p === scope + 'index.html') c.navigate(c.url).catch(() => {});
    }
  })());
});
// No fetch handler: every request goes straight to the network.
