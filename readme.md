

<div style="text-align: center;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
<rect0 width="400" height="200" x="0" y="0" fill="#fff" />
    
<path d="M00,120 L100,80 L200,120 L100,160 Z" stroke="none" fill="#991111" />
<path d="M100,80 L200,40 L300,80 L200,120 Z" stroke="none" fill="#222299" />
<path d="M100,160 L300,80 L400,120 L200,200 Z" stroke="none" fill="#606000" />
    
<path d="M200,0 L100,40 L100,80 L200,40 Z" stroke="none" fill="#5555dd" />
<path d="M200,0 L300,40 L300,80 L200,40 Z" stroke="none" fill="#3333bb" />
    
<path d="M100,40 L00,80 L00,120 L100,80 Z" stroke="none" fill="#cc5555" />
<path d="M100,40 L200,80 L200,120 L100,80 Z" stroke="none" fill="#bb3333" />
<path d="M00,80 L100,120 L100,160 L00,120 Z" stroke="none" fill="#bb3333" />
    
<path d="M100,120 L300,40 L300,80 L100,160 Z" stroke="none" fill="#bbbb33" />
<path d="M100,120 L200,160 L200,200 L100,160 Z" stroke="none" fill="#777722" />
    
<path d="M300,40 L400,80 L400,120 L300,80 Z" stroke="none" fill="#888822" />
<path d="M200,160 L400,80 L400,120 L200,200 Z" stroke="none" fill="#bbbb33" />
</svg>
</div>



# parabin

**parabin** is a parametric generator for 3D-printable modular drawer organizers, inspired by the [Gridfinity](https://github.com/zackfreedman/gridfinity) system.

Write one command, and it generates:
- A `.scad` file (OpenSCAD)
- An optional `.stl` for printing

parabin is flexible, fast, and totally scriptable.

---

## Features

- Grid-based bin sizing (e.g., `2x3`, `1x1`)
- Custom screw hole placement on any side
- Optional floor (`--no-bottom` flag)
- Clean STL output (with `--stl` or `--stl-ofn`)
- All OpenSCAD output is parametric and readable

---

## 🛠 Requirements

- Python 3.7+
- [OpenSCAD](https://openscad.org/) installed and available on your system PATH

---

## Usage

```bash
python3 generate_bin.py SIZE HEIGHT HOLES ZHEIGHT [options]
```

### Example:

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

## Roadmap

- [ ] Snap-fit lids
- [ ] Gridfinity baseplate pegs/magnets
- [ ] Internal dividers / compartments
- [ ] Embossed labels
- [ ] Web UI + STL preview (via GitHub Pages)
- [ ] Parametric template sharing

---

## Credits

- Inspired by [Zack Freedman’s Gridfinity](https://github.com/zackfreedman/gridfinity)
- Powered by [OpenSCAD](https://openscad.org/) and [Python](https://www.python.org/)
