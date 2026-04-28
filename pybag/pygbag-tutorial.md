# Deploying a Pygame Game to the Web with pygbag

`pygbag` packages a standard Python/pygame project into a WebAssembly bundle that runs in any modern browser — desktop or mobile — with no installation required by the player. This tutorial walks through the full pipeline, from adapting your code to publishing online.

## 1. Install pygbag

```bash
pip install pygbag --upgrade
```

This pulls the latest stable release from PyPI. `pygbag` requires Python 3.8 or newer, and works best with `pygame-ce` (the community edition, which is API-compatible with classic pygame). If you are on Windows, use Python from [python.org](https://python.org) rather than the Microsoft Store to avoid PATH issues.

## 2. Structure your project

Your project folder must contain a file named `main.py` at its root — this is the entry point pygbag looks for. All assets (images, fonts, sounds) must live inside the project folder so they get bundled.

```
my_game/
├── main.py
├── assets/
│   ├── player.png
│   └── music.ogg
└── ...
```

For audio, prefer `.ogg` over `.wav` or `.mp3` — the latter can misbehave on some browsers (notably Chrome).

## 3. Make your game loop async

This is the single most important code change. The browser's event loop cannot be blocked by a `while True:` loop, so your main loop must be an `async` function that yields control each frame via `await asyncio.sleep(0)`.

Here is the minimal template:

```python
import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- game logic & drawing here ---
        screen.fill((30, 30, 40))
        pygame.display.update()

        await asyncio.sleep(0)   # hand control back to the browser
        clock.tick(60)

asyncio.run(main())
```

Two rules to remember: do not call `pygame.quit()` or `sys.exit()` after `asyncio.run(main())` — on the web build, execution continues past that line. And keep the `await asyncio.sleep(0)` argument at exactly `0`; anything higher will throttle your framerate.

## 4. Declare extra dependencies (if any)

If your game imports third-party libraries beyond pygame (e.g. `pytmx`, `pyscroll`, `numpy`), declare them with a [PEP 723](https://peps.python.org/pep-0723/) inline metadata header at the top of `main.py`:

```python
# /// script
# dependencies = [
#   "pygame-ce",
#   "pytmx",
#   "pyscroll",
# ]
# ///
```

Put `import numpy` (or other heavy C-extension imports) at the very top of the file so pygbag detects them during packaging.

## 5. Test locally

From the parent directory of your project folder, run:

```bash
pygbag my_game/
```

pygbag will package your game and start a local test server at `http://localhost:8000`. Open that URL in your browser — you should see a loading screen, then your game. The first load is slower because the Python runtime is being downloaded; subsequent loads are cached.

If you get a `ModuleNotFoundError`, double-check your PEP 723 header. If the command itself is not found, `pygbag` may have installed into a user-local bin directory that is not on your PATH — try `python -m pygbag my_game/` instead.

## 6. Build the distributable bundle

When you are happy with how it runs locally, generate the production build:

```bash
pygbag --build my_game/
```

This produces a `my_game/build/web/` directory containing `index.html`, a `.apk` archive (the packaged game), and supporting JavaScript. These static files are everything you need to host the game.

## 7. Publish online

You have several hosting options for the contents of `build/web/`:

**itch.io** — Zip the contents of `build/web/` (not the folder itself, the files inside it), create a new project on itch.io, set the kind to "HTML", upload the zip, and check "This file will be played in the browser". Set the viewport dimensions to match your game window.

**GitHub Pages** — Push the `build/web/` contents to the root of a `gh-pages` branch (or to a `/docs` folder on `main`), then enable Pages in the repository settings. For automated deploys, the `pygame-web/showroom` repo and the community [Python-Web-Game template](https://github.com/league-curriculum/Python-Web-Game) include ready-made GitHub Actions workflows.

**Any static host** — Netlify, Vercel, Cloudflare Pages, or even a plain Apache/Nginx server will all work. The build output is pure static files.

## 8. Useful flags

A few command-line options worth knowing:

- `--template noctx.tmpl` — required if you use 3D/WebGL (Panda3D, raylib) or `pygame.sdl2`
- `--app_name "My Game"` — sets the window title and app identifier
- `--icon path/to/icon.png` — custom favicon and launcher icon
- `--no_opt` — skips PNG recompression (use this if you ship heightmaps or other PNGs that must not be altered)
- `--PYBUILD 3.12` — pins a specific Python version

## Common pitfalls

Filenames are case-sensitive in the bundle even if your local OS is not, so `Player.png` and `player.png` are treated as different files. Avoid the standard library's blocking I/O (`input()`, `tkinter`, `requests`) — the web runtime is single-threaded and synchronous calls will freeze the browser. For networking, use `pygbag.net` or JavaScript interop rather than `socket`/`urllib`.

If you want to preserve a pixelated look regardless of screen size, add this near the top of `main.py`:

```python
import sys, platform
if sys.platform == "emscripten":
    platform.window.canvas.style.imageRendering = "pixelated"
```

That's the full pipeline. A simple game can go from desktop-only to playable-in-a-browser in under ten minutes once the async loop is in place.
