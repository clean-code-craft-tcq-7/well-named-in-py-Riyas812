major_colors = ['White', 'Red', 'Black', 'Yellow', 'Violet']
minor_colors = ['Blue', 'Orange', 'Green', 'Brown', 'Slate']

def get_color_pair_number(major, minor):
    if major not in major_colors or minor not in minor_colors:
        raise ValueError("Invalid major or minor color")
    major_index = major_colors.index(major)
    minor_index = minor_colors.index(minor)
    return major_index * len(minor_colors) + minor_index + 1

def get_color_from_pair_number(pair_number):
    if pair_number < 1 or pair_number > len(major_colors) * len(minor_colors):
        raise ValueError("Invalid pair number")
    zero_based = pair_number - 1
    major_index = zero_based // len(minor_colors)
    minor_index = zero_based % len(minor_colors)
    return major_colors[major_index], minor_colors[minor_index]
