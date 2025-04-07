import argparse
import subprocess
import os

def generate_bin_scad(
    size_str,
    bin_height,
    screw_sides,
    screw_z,
    filename="bin.scad",
    export_stl=False,
    stl_ofn=None,
    no_bottom=False
):
    grid = 42
    wall = 2
    screw_radius = 3  # 6mm diameter
    screw_depth = wall + 2
    fn = 64
    floor_thickness = 0 if no_bottom else 2

    # Parse size string like "2x3"
    try:
        width, depth = map(int, size_str.lower().split("x"))
    except:
        raise ValueError(f"Invalid size format: {size_str}. Use format like '2x7'.")

    bin_w = width * grid
    bin_d = depth * grid
    bin_h = bin_height
    hollow_h = bin_h - floor_thickness

    scad = []

    scad.append("difference() {")
    scad.append(f"  cube([{bin_w}, {bin_d}, {bin_h}]);")
    scad.append(f"  translate([{wall}, {wall}, {floor_thickness}])")
    scad.append(f"    cube([{bin_w - 2*wall}, {bin_d - 2*wall}, {hollow_h}]);")

    for code in screw_sides:
        side = code[0].lower()
        try:
            index = int(code[1:])
        except ValueError:
            print(f"⚠️ Skipping invalid code: {code}")
            continue

        x = y = screw_z

        if side == 'a' and index < width:
            x = (index + 0.5) * grid
            y = 0
            scad.append(f"  translate([{x}, {y}, {screw_z}])")
            scad.append(f"    rotate([90, 0, 0]) cylinder(h={screw_depth}, r={screw_radius}, $fn={fn}, center=true);")

        elif side == 'c' and index < width:
            x = ((width - 1 - index) + 0.5) * grid  # Flipped left-to-right
            y = bin_d
            scad.append(f"  translate([{x}, {y}, {screw_z}])")
            scad.append(f"    rotate([90, 0, 0]) cylinder(h={screw_depth}, r={screw_radius}, $fn={fn}, center=true);")

        elif side == 'b' and index < depth:
            x = bin_w
            y = (index + 0.5) * grid
            scad.append(f"  translate([{x}, {y}, {screw_z}])")
            scad.append(f"    rotate([0, 90, 0]) cylinder(h={screw_depth}, r={screw_radius}, $fn={fn}, center=true);")

        elif side == 'd' and index < depth:
            x = 0
            y = ((depth - 1 - index) + 0.5) * grid  # Flipped left-to-right
            scad.append(f"  translate([{x}, {y}, {screw_z}])")
            scad.append(f"    rotate([0, 90, 0]) cylinder(h={screw_depth}, r={screw_radius}, $fn={fn}, center=true);")

        else:
            print(f"⚠️ Skipping out-of-range or invalid code: {code}")

    scad.append("}")

    with open(filename, "w") as f:
        f.write("\n".join(scad))
    print(f"✅ Wrote SCAD file: {filename}")

    if export_stl:
        stl_filename = stl_ofn if stl_ofn else os.path.splitext(filename)[0] + ".stl"
        print(f"🛠 Converting to STL...")
        subprocess.run(["openscad", "-o", stl_filename, filename], check=True)
        print(f"✅ STL written to {stl_filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parabin: Parametric 3D printable bin generator.")
    parser.add_argument("size", help="Bin size in grid units, e.g., 2x7")
    parser.add_argument("bin_height", type=float, help="Bin height in mm")
    parser.add_argument("screw_sides", help="Comma-separated screw hole codes like a0,b2")
    parser.add_argument("screw_z", type=float, help="Screw hole center height in mm")
    parser.add_argument("-o", "--output", default="bin.scad", help="SCAD output filename")
    parser.add_argument("--stl", action="store_true", help="Also export STL using OpenSCAD")
    parser.add_argument("--stl-ofn", help="Custom STL output filename (e.g., mybin.stl)")
    parser.add_argument("--no-bottom", action="store_true", help="Generate bin without a bottom floor")

    args = parser.parse_args()

    # Parse and sort screw hole codes consistently
    def sort_screw_codes(codes):
        def sort_key(code):
            side = code[0].lower()
            index = int(code[1:])
            return (side, index)
        return sorted((s.strip() for s in codes.split(",")), key=sort_key)

    screw_list = sort_screw_codes(args.screw_sides)

    generate_bin_scad(
        size_str=args.size,
        bin_height=args.bin_height,
        screw_sides=screw_list,
        screw_z=args.screw_z,
        filename=args.output,
        export_stl=args.stl,
        stl_ofn=args.stl_ofn,
        no_bottom=args.no_bottom
    )
