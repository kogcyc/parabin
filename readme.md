<span align="left">
  <img src="logo.svg" width="400" alt="parabin logo">
</span>

# parabin

**parabin** is a command-line Python generator for parametric 3D-printed drawer organizers. It creates OpenSCAD files with optional screw holes, bottom floors, and rounded corners — perfect for organizing with style and precision.

## Features

- Parametric sizing using Gridfinity-style `42 mm` grid units  
- Rounded vertical edges (default, via `minkowski()`)  
- Screw hole support with side-specific placement  
- Optional bottom floor (for open trays)  
- STL export via OpenSCAD CLI  
- Custom wall thickness logic and accurate cavity subtraction  

## Requirements

- Python 3.x  
- [OpenSCAD](https://openscad.org/) with command-line support

### macOS install

```bash
brew install --cask openscad
```

## Usage

```bash
python3 generate_bin.py SIZE HEIGHT SCREW_SIDES SCREW_Z [options]
```

### Positional Arguments

| Argument       | Description                                                   |
|----------------|---------------------------------------------------------------|
| `SIZE`         | Bin size in grid units like `2x3`                              |
| `HEIGHT`       | Height of the bin in mm                                        |
| `SCREW_SIDES`  | Comma-separated screw hole codes (e.g., `a0,b1`, or `none`)    |
| `SCREW_Z`      | Vertical height of screw hole centers in mm                   |

### Optional Flags

| Option                 | Description                                             |
|------------------------|---------------------------------------------------------|
| `-o`, `--output`       | SCAD output filename (default: `bin.scad`)              |
| `--stl`                | Also export STL file using OpenSCAD                     |
| `--stl-ofn`            | Custom STL output filename                              |
| `--no-bottom`          | Remove the bottom floor of the bin                      |
| `--hole-diameter`      | Set screw hole diameter in mm (default: `6.0`)          |
| `--not-rounded-edges`  | Use sharp cube edges (disables rounding via `minkowski()`) |

## Examples

### A 1×2 bin, 25 mm tall, with screws on sides A and C:

```bash
python3 generate_bin.py 1x2 25 a0,c0 12
```

### A 3×3 open bin with no screw holes:

```bash
python3 generate_bin.py 3x3 20 none 10 --no-bottom
```

### Export to STL:

```bash
python3 generate_bin.py 2x2 30 a0,b1 15 --stl --stl-ofn mybox.stl
```

## Output

Parabin generates a `.scad` file which you can view or edit in OpenSCAD.  
You can also export an `.stl` file automatically with the `--stl` flag.

These models are ideal for printing modular organizers on any FDM printer.

## License

MIT License.  
Use, remix, and share freely.

---

Made with ❤️ and Python.
