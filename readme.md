<span align="left">
  <img src="logo.svg" width="400" alt="parabin logo">
</span>

# parabin

**Parabin** is a parametric SCAD generator for modular 3D printable drawer bins. It produces customizable storage boxes with optional screw holes and smooth rounded corners, ready for slicing and printing.

---

## Features

- 📦 Fully parametric size: width × depth in 42 mm grid units
- 🌀 Rounded vertical edges via `minkowski()` (enabled by default)
- 🕳️ Optional 6 mm screw holes placed on specified sides
- 🔩 Optional floor toggle (`--no-bottom`)
- 📐 Configurable bin height
- 💾 Outputs `.scad` and optionally `.stl` using OpenSCAD CLI

---

## Requirements

- Python 3.x
- OpenSCAD (CLI must be available in your `$PATH`)

### 🔧 macOS installation

```bash
brew install --cask openscad
