# src/tooth_numbering.py
# Maps a bbox center to a tooth id using realistic tooth positions for panoramic X-rays

def _universal_id(idx: int) -> int:
    """Convert grid index to Universal numbering (1-32)"""
    return idx + 1  # 1..32

def _fdi_id(idx: int) -> int:
    """Convert grid index to FDI numbering (11-18, 21-28, 31-38, 41-48)"""
    row = idx // 16
    col = idx % 16
    
    if row == 0:  # Upper arch
        return 11 + col if col < 8 else 21 + (col - 8)
    else:  # Lower arch
        return 31 + col if col < 8 else 41 + (col - 8)

def _region(cx, cy, x1, y1, x2, y2, arch):
    """Determine tooth surface region (M/D + O/B)"""
    mx = x1 + (x2 - x1) / 2.0
    mesial = cx < mx
    md = "M" if mesial else "D"
    
    # Occlusal vs Buccal/Lingual determination
    oy = y1 + (y2 - y1) * (0.33 if arch == "upper" else 0.66)
    occlusal = (cy < oy and arch == "upper") or (cy > oy and arch == "lower")
    
    return (md + "O") if occlusal else (md + "B")

def grid_tooth_map(img_size, notation_system="universal"):
    """Create a tooth locator function for the given image size and notation system"""
    W, H = img_size
    
    # Create realistic tooth positions for panoramic X-rays
    # Upper arch: 16 teeth (8 left, 8 right)
    # Lower arch: 16 teeth (8 left, 8 right)
    
    # Define tooth positions as percentages of image width
    # This creates a more realistic tooth layout for panoramic X-rays
    tooth_positions = {
        # Upper arch (row 0) - from left to right
        0: (0.05, 0.15),   # Tooth 1 (upper right 3rd molar)
        1: (0.10, 0.20),   # Tooth 2
        2: (0.15, 0.25),   # Tooth 3
        3: (0.20, 0.30),   # Tooth 4
        4: (0.25, 0.35),   # Tooth 5
        5: (0.30, 0.40),   # Tooth 6
        6: (0.35, 0.45),   # Tooth 7
        7: (0.40, 0.50),   # Tooth 8 (central)
        8: (0.50, 0.60),   # Tooth 9 (central)
        9: (0.55, 0.65),   # Tooth 10
        10: (0.60, 0.70),  # Tooth 11
        11: (0.65, 0.75),  # Tooth 12
        12: (0.70, 0.80),  # Tooth 13
        13: (0.75, 0.85),  # Tooth 14
        14: (0.80, 0.90),  # Tooth 15
        15: (0.85, 0.95),  # Tooth 16 (upper left 3rd molar)
        
        # Lower arch (row 1) - from left to right
        16: (0.05, 0.85),  # Tooth 17 (lower left 3rd molar)
        17: (0.10, 0.80),  # Tooth 18
        18: (0.15, 0.75),  # Tooth 19
        19: (0.20, 0.70),  # Tooth 20
        20: (0.25, 0.65),  # Tooth 21
        21: (0.30, 0.60),  # Tooth 22
        22: (0.35, 0.55),  # Tooth 23
        23: (0.40, 0.50),  # Tooth 24 (central)
        24: (0.50, 0.60),  # Tooth 25 (central)
        25: (0.55, 0.65),  # Tooth 26
        26: (0.60, 0.70),  # Tooth 27
        27: (0.65, 0.75),  # Tooth 28
        28: (0.70, 0.80),  # Tooth 29
        29: (0.75, 0.85),  # Tooth 30
        30: (0.80, 0.90),  # Tooth 31
        31: (0.85, 0.95),  # Tooth 32 (lower right 3rd molar)
    }

    def locator(bbox_xyxy):
        """Locate tooth ID and region for a bounding box"""
        x1, y1, x2, y2 = bbox_xyxy
        cx, cy = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        
        # Normalize coordinates to percentages
        cx_pct = cx / W
        cy_pct = cy / H
        
        # Find the closest tooth position
        min_distance = float('inf')
        closest_tooth = 0
        
        for tooth_idx, (x_start, x_end) in tooth_positions.items():
            # Calculate distance to tooth center
            tooth_center_x = (x_start + x_end) / 2
            distance = abs(cx_pct - tooth_center_x)
            
            if distance < min_distance:
                min_distance = distance
                closest_tooth = tooth_idx
        
        # Determine arch based on Y position
        arch = "upper" if closest_tooth < 16 else "lower"
        
        # Get tooth position for region calculation
        x_start, x_end = tooth_positions[closest_tooth]
        region = _region(cx, cy, x_start * W, 0, x_end * W, H, arch)
        
        # Convert to appropriate numbering system
        if notation_system == "fdi":
            tooth_id = _fdi_id(closest_tooth)
        else:  # universal
            tooth_id = _universal_id(closest_tooth)
        
        return tooth_id, region
    
    return locator
