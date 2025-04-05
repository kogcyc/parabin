# 📦 parabox

**parabox** is a parametric generator for 3D-printable modular drawer organizers, inspired by the [Gridfinity](https://github.com/zackfreedman/gridfinity) system.

Write one command, and it generates:
- 🧱 A `.scad` file (OpenSCAD)
- 📦 An optional `.stl` for printing

Parabox is flexible, fast, and totally scriptable.

---

## ✨ Features

- 📐 Grid-based bin sizing (e.g., `2x3`, `1x1`)
- 🕳 Custom screw hole placement on any side
- 🔲 Optional floor (`--no-bottom` flag)
- 🧼 Clean STL output (with `--stl` or `--stl-ofn`)
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
  --stl-ofn bin_2x3.stl
```

This creates:
- A `2x3` bin (84mm × 126mm), 28mm tall
- Screw holes on sides A0 and C1, 10mm up from the base
- `bin.scad` → OpenSCAD model
- `bin_2x3.stl` → 3D print ready

---

## 🏷 CLI Options

| Flag | Description |
|------|-------------|
| `-o bin.scad`        | Set custom SCAD output file |
| `--stl`              | Export STL file |
| `--stl-ofn file.stl` | Set custom STL output file |
| `--no-bottom`        | Leave bin open underneath (no floor) |

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
