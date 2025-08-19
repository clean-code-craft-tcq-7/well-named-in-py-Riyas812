from color_map import major_colors, minor_colors, get_color_from_pair_number

def print_color_code_manual():
    total_pairs = len(major_colors) * len(minor_colors)
    header = f"{'Pair Number':<12} {'Major Color':<12} {'Minor Color':<12}"
    print(header)
    print('-' * len(header))
    for pair_number in range(1, total_pairs + 1):
        major, minor = get_color_from_pair_number(pair_number)
        print(f"{pair_number:<12} {major:<12} {minor:<12}")

def get_color_code_manual_lines():
    """Return list of formatted strings for unit testing"""
    total_pairs = len(major_colors) * len(minor_colors)
    lines = []
    header = f"{'Pair Number':<12} {'Major Color':<12} {'Minor Color':<12}"
    lines.append(header)
    lines.append('-' * len(header))
    for pair_number in range(1, total_pairs + 1):
        major, minor = get_color_from_pair_number(pair_number)
        lines.append(f"{pair_number:<12} {major:<12} {minor:<12}")
    return lines
