#!/usr/bin/env python3
"""Static server with baseURL prefix rewrite.

The build emits `_nuxt/` at the ROOT of .output/public, but the HTML requests
`/<repo>/_nuxt/entry.js`. Serving the root directly makes every asset 404, and
the fallback-to-index.html then feeds text/html to a module script, so the
browser silently drops it and the page never hydrates. Strip the prefix so
asset requests resolve, and only fall back to index.html for page routes.
"""
import functools
import http.server
import os
import socketserver
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else ".output/public"
BASE = sys.argv[2] if len(sys.argv) > 2 else "/sarkas-bumk-kabut-asap"
PORT = int(sys.argv[3]) if len(sys.argv) > 3 else 4199


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        path = self.path.split("?")[0]
        # Strip the baseURL prefix: /sarkas-bumk-kabut-asap/x -> /x
        if path == BASE or path == BASE + "/":
            self.path = "/index.html"
        elif path.startswith(BASE + "/"):
            self.path = path[len(BASE):] or "/"
        fs_path = self.translate_path(self.path)
        if not os.path.exists(fs_path):
            # SPA fallback ONLY for page routes, never for assets
            if "/_nuxt/" in self.path or "/fonts/" in self.path:
                self.send_error(404, "asset not found")
                return
            self.path = "/index.html"
        return super().do_GET()


class Server(socketserver.TCPServer):
    allow_reuse_address = True


with Server(("127.0.0.1", PORT), functools.partial(Handler, directory=ROOT)) as httpd:
    print(f"serving {ROOT} (base {BASE}) on http://127.0.0.1:{PORT}", flush=True)
    httpd.serve_forever()
