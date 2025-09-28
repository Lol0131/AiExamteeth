# src/tooth_numbering.py
# Maps a bbox center to a tooth id using a 2x16 grid (32 teeth) and returns a region like MO/DB (very rough).

def _universal_id(idx: int) -> int:
    return idx + 1  # 1..32

def _region(cx, cy, x1, y1, x2, y2, arch):
    mx = x1 + (x2 - x1) / 2.0
    mesial = cx < mx
    md = "M" if mesial else "D"
    oy = y1 + (y2 - y1) * (0.33 if arch == "upper" else 0.66)
    occlusal = (cy < oy and arch == "upper") or (cy > oy and arch == "lower")
    return (md + "O") if occlusal else (md + "B")

def grid_tooth_map(img_size, notation_system="universal"):
    W, H = img_size
    cw, ch = W / 16.0, H / 2.0

    def locator(bbox_xyxy):
        x1, y1, x2, y2 = bbox_xyxy
        cx, cy = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        col = int(max(0, min(15, cx // cw)))
        row = 0 if cy < ch else 1
        idx = row * 16 + col
        arch = "upper" if row == 0 else "lower"
        region = _region(cx, cy, col * cw, row * ch, (col + 1) * cw, (row + 1) * ch, arch)
        return _universal_id(idx), region
    return locator
