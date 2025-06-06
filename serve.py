#!/usr/bin/env python3
"""Simple development server for the static site."""
import argparse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


def run(port: int, directory: Path) -> None:
    """Start an HTTP server serving the given directory."""
    directory = directory.resolve()
    handler_class = SimpleHTTPRequestHandler
    handler_class.directory = str(directory)

    with ThreadingHTTPServer(('0.0.0.0', port), handler_class) as httpd:
        print(f"Serving {directory} at http://localhost:{port}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            print("Shutting down server")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a simple HTTP server for local development.")
    parser.add_argument('-p', '--port', type=int, default=8000, help='Port to listen on (default: 8000).')
    parser.add_argument('-d', '--dir', dest='directory', type=str, default='.', help='Directory to serve (default: current directory).')
    args = parser.parse_args()
    run(args.port, Path(args.directory))


if __name__ == '__main__':
    main()
