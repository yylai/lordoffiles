# Lord of Files Dashboard

This repository contains a static HTML dashboard that visualizes score distributions for different department managers. It uses plain HTML, CSS and JavaScript with no build tools.

## Local Development

You can open `index.html` directly in your browser, but running a tiny HTTP server makes testing easier.

### Using the included Python server

Run the helper script to start a local server from the project root:

```bash
python3 serve.py
```

The dashboard will be available at [http://localhost:8000](http://localhost:8000). Use `--port` to change the port or `--dir` to serve a different directory.

### Using Python's built in server directly

Alternatively you can use Python's built-in module:

```bash
python3 -m http.server 8000
```

Both approaches serve the files in the current directory so you can view changes in the browser as you edit them.
