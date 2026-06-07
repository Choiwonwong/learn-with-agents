"""Local Same-Origin Policy lab.

Run:
    python learning/fundamentals/networking/01-same-origin-policy/practice/sop_lab.py

Then open:
    http://localhost:8000

This intentionally uses two ports so the browser sees two different origins:
    http://localhost:8000  -> page origin
    http://localhost:8001  -> API origin
"""

from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Final

PAGE_PORT: Final = 8000
API_PORT: Final = 8001
ALLOWED_ORIGIN: Final = f"http://localhost:{PAGE_PORT}"


class PageHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/api/message":
            self._send_json({"message": "same-origin response from page server"})
            return

        self._send_html(INDEX_HTML)

    def _send_html(self, body: str) -> None:
        encoded = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def _send_json(self, payload: dict[str, str]) -> None:
        encoded = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


class ApiHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/api/no-cors":
            self._send_json({"message": "cross-origin response without CORS"})
            return

        if self.path == "/api/with-cors":
            self._send_json(
                {"message": "cross-origin response with CORS"},
                cors_origin=ALLOWED_ORIGIN,
            )
            return

        self.send_error(404)

    def _send_json(self, payload: dict[str, str], cors_origin: str | None = None) -> None:
        encoded = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        if cors_origin is not None:
            self.send_header("Access-Control-Allow-Origin", cors_origin)
        self.end_headers()
        self.wfile.write(encoded)


INDEX_HTML: Final = f"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Same-Origin Policy Lab</title>
    <style>
      body {{ font-family: system-ui, sans-serif; max-width: 760px; margin: 40px auto; }}
      button {{ display: block; margin: 12px 0; padding: 8px 12px; }}
      pre {{ background: #f5f5f5; padding: 12px; white-space: pre-wrap; }}
    </style>
  </head>
  <body>
    <h1>Same-Origin Policy Lab</h1>
    <p>Page origin: <code>http://localhost:{PAGE_PORT}</code></p>
    <p>API origin: <code>http://localhost:{API_PORT}</code></p>

    <button onclick="request('/api/message')">Same-origin fetch</button>
    <button onclick="request('http://localhost:{API_PORT}/api/no-cors')">Cross-origin fetch without CORS</button>
    <button onclick="request('http://localhost:{API_PORT}/api/with-cors')">Cross-origin fetch with CORS</button>

    <h2>Result</h2>
    <pre id="result">Click a button.</pre>

    <script>
      async function request(url) {{
        const result = document.querySelector('#result');
        result.textContent = `Requesting ${{url}} ...`;
        try {{
          const response = await fetch(url);
          const text = await response.text();
          result.textContent = `SUCCESS\nstatus=${{response.status}}\nbody=${{text}}`;
        }} catch (error) {{
          result.textContent = `FAILED\n${{error.name}}: ${{error.message}}\n\nCheck the browser console and Network tab.`;
          console.error(error);
        }}
      }}
    </script>
  </body>
</html>
"""


def serve(port: int, handler: type[BaseHTTPRequestHandler]) -> ThreadingHTTPServer:
    server = ThreadingHTTPServer(("localhost", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def main() -> None:
    page_server = serve(PAGE_PORT, PageHandler)
    api_server = serve(API_PORT, ApiHandler)
    print(f"Page server: http://localhost:{PAGE_PORT}")
    print(f"API server:  http://localhost:{API_PORT}")
    print("Press Ctrl+C to stop.")

    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        print("\nStopping servers...")
    finally:
        page_server.shutdown()
        api_server.shutdown()


if __name__ == "__main__":
    main()
