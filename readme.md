<span align="left">
  <img src="logo.svg" width="400" alt="parabin logo">
</span>

# parabin

**parabin** is a parametric generator for 3D-printable modular drawer organizers, inspired by the Gridfinity system. It outputs OpenSCAD code for customizable storage bins and can optionally generate ready-to-print STL files.

parabin gives you full control over bin size, height, side screw holes, and whether or not to include a bottom floor.

---

## Features

- Grid-based bin sizing (e.g., `1x1`, `2x4`, `3x5`)
- Custom screw hole placement on all four sides
- Optional floor using the `--no-bottom` flag
- Clean STL output using OpenSCAD via command line
- Fully parametric and scriptable for batch generation

---

## Requirements

- Python 3.7 or higher
- [OpenSCAD](https://openscad.org/) installed and available in your system's path

---

## Usage

```bash
python3 generate_bin.py SIZE HEIGHT HOLES ZHEIGHT [options]
```

### Positional arguments

| Argument     | Description                                             |
|--------------|---------------------------------------------------------|
| `SIZE`       | Bin size in grid units, format like `2x3`               |
| `HEIGHT`     | Height of the bin in millimeters                        |
| `HOLES`      | Comma-separated screw hole codes (e.g., `a0,b0,d1`)     |
| `ZHEIGHT`    | Height of the screw hole center from the bottom in mm  |

### Options

| Option                 | Description                                               |
|------------------------|-----------------------------------------------------------|
| `-o`, `--output`       | Output `.scad` filename (default: `bin.scad`)             |
| `--stl`                | Export an `.stl` file using OpenSCAD                      |
| `--stl-ofn`            | Custom STL output filename                                |
| `--no-bottom`          | Generate bin without a bottom floor                       |

---

## Example

```bash
python3 generate_bin.py 2x3 28 a0,c1 10 --stl --stl-ofn bin_2x3.stl
```

This will:

- Create a 2x3 bin (84mm x 126mm), 28mm tall
- Add screw holes at positions A0 and C1, 10mm up from the bottom
- Write `bin.scad` as OpenSCAD source
- Export an STL as `bin_2x3.stl` using OpenSCAD

---

## Screw Hole Naming

When facing each side:

- Side A (front): holes numbered left to right (A0, A1, ...)
- Side B (right): holes numbered top to bottom (B0, B1, ...)
- Side C (back): holes numbered left to right (C0, C1, ...) when facing the back
- Side D (left): holes numbered top to bottom (D0, D1, ...) when facing the left

All sides use consistent left-to-right or top
