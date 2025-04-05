# 📦 Parabox

**Parabox** is a parametric generator for 3D-printable modular drawer organizers, inspired by the [Gridfinity](https://github.com/zackfreedman/gridfinity) system.

Write one command, and it generates:
- 🧱 A `.scad` file (OpenSCAD)
- 📦 An optional `.stl` for printing
- 🖼 An optional `.png` preview render (orthographic, open-top view)

Parabox is flexible, fast, and totally scriptable.

---

## ✨ Features

- 📐 Grid-based bin sizing (e.g., `2x3`, `1x1`)
- 🕳 Custom screw hole placement on any side
- 🔲 Optional floor (`--no-bottom` flag)
- 🧼 Clean STL output (with `--stl` or `--stl-ofn`)
- 📸 PNG rendering with visible top opening (`--png`, `--png-ofn`)
- 🧠 All OpenSCAD output is parametric and readable

---

## 🛠 Requirements

- Python 3.7+
- [OpenSCAD](https://openscad.org/) installed and available on your system PATH

---

## 🚀 Usage

```bash
python3 generate_bin.py SIZE HEIGHT HOLES ZHEIGHT [options]
```

### 💡 Example:

```bash
python3 generate_bin.py 2x3 28 a0,c1 10 \
  --stl \
  --png \
  --stl-ofn bin_2x3.stl \
  --png-ofn preview_2x3.png
```

This creates:
- A `2x3` bin (84mm × 126mm), 28mm tall
- Screw holes on sides A0 and C1, 10mm up from the base
- `bin.scad` → OpenSCAD model
- `bin_2x3.stl` → 3D print ready
- `preview_2x3.png` → perspective-free preview image

---

## 🏷 CLI Options

| Flag | Description |
|------|-------------|
| `-o bin.scad`        | Set custom SCAD output file |
| `--stl`              | Export STL file |
| `--stl-ofn file.stl` | Set custom STL output file |
| `--png`              | Render preview PNG |
| `--png-ofn file.png` | Set custom PNG output file |
| `--no-bottom`        | Leave bin open underneath (no floor) |

---

## 🖼 Preview Rendering

PNG previews are generated using:
- Orthographic projection
- Angled camera view
- Wireframe edges for visibility
- Consistent top-facing view

The camera can be customized in the script (currently set to eye at `[200, 200, 150]`, looking at `[42, 42, 0]`).

---

## 🤖 Roadmap

- [ ] Snap-fit lids
- [ ] Gridfinity baseplate pegs/magnets
- [ ] Internal dividers / compartments
- [ ] Embossed labels
- [ ] Web UI + STL preview (via GitHub Pages)
- [ ] Parametric template sharing

---

## 📚 License

MIT — Parabox is free to use, remix, and share.  
Let’s make organizing drawers a beautiful act of code.

---

## 🙌 Credits

- Inspired by [Zack Freedman’s Gridfinity](https://github.com/zackfreedman/gridfinity)
- Powered by [OpenSCAD](https://openscad.org/) and [Python](https://www.python.org/)
