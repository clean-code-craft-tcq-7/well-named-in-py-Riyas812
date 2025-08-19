from report import print_color_code_manual
if __name__ == "__main__":
    print_color_code_manual()
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ['Blue', 'Orange', 'Green', 'Brown', 'Slate']
def format_color_pair(major, minor):
    return f'{major} {minor}'
def color_from_pair_number(pair_num):
    zero_based = pair_num - 1
    major_idx = zero_based // len(MINOR_COLORS)
    minor_idx = zero_based % len(MINOR_COLORS)
    if major_idx >= len(MAJOR_COLORS) or minor_idx >= len(MINOR_COLORS):
        raise Exception('Color index out of range')
    return MAJOR_COLORS[major_idx], MINOR_COLORS[minor_idx]
def pair_number_from_color(major, minor):
    try:
        major_idx = MAJOR_COLORS.index(major)
        minor_idx = MINOR_COLORS.index(minor)
    except ValueError:
        raise Exception('Color not found')
    return major_idx * len(MINOR_COLORS) + minor_idx + 1
def test_number_to_color(pair_num, expected_major, expected_minor):
    major, minor = color_from_pair_number(pair_num)
    assert major == expected_major and minor == expected_minor
def test_color_to_number(major, minor, expected_num):
    assert pair_number_from_color(major, minor) == expected_num
if __name__ == '__main__':
    test_number_to_color(4, 'White', 'Brown')
    test_number_to_color(5, 'White', 'Slate')
    test_color_to_number('Black', 'Orange', 12)
    test_color_to_number('Violet', 'Slate', 25)
    test_color_to_number('Red', 'Orange', 7)
    print('Done :)')
