"""
Instructions
In this kata you parse RGB colors represented by strings. The formats are primarily used in HTML and CSS. Your task is to implement a function which takes a color as a string and returns the parsed color as a map (see Examples).

Input:
The input string represents one of the following:

6-digit hexadecimal - "#RRGGBB"
e.g. "#012345", "#789abc", "#FFA077"
Each pair of digits represents a value of the channel in hexadecimal: 00 to FF
3-digit hexadecimal - "#RGB"
e.g. "#012", "#aaa", "#F5A"
Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.
Preset color name
e.g. "red", "BLUE", "LimeGreen"
You have to use the predefined map PRESET_COLORS (JavaScript, Python, Ruby), presetColors (Java, C#, Haskell), or preset-colors (Clojure). The keys are the names of preset colors in lower-case and the values are the corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").

parse_html_color('#80FFA0')   # => {'r': 128, 'g': 255, 'b': 160}
parse_html_color('#3B7')      # => {'r': 51,  'g': 187, 'b': 119}
parse_html_color('LimeGreen') # => {'r': 50,  'g': 205, 'b': 50 }
"""


# def hex_to_rgb(value):
#     value = value.lstrip('#')
#     lv = len(value)
#     hexed_value = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
#     return "Hex to RGB: " + str(hexed_value)

def parse_html_color(value):
    rgb = ['r', 'g', 'b']
    value = value.lstrip('#')
    lv = len(value)
    hexed_value = list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    hex_dictionary = dict(zip(rgb, hexed_value))
    return hex_dictionary

# def rgb_to_hex(rgb):
#     return '#%02x%02x%02x' % rgb


print(parse_html_color("#ffffff")    )          # ==> {'r': 255, 'g': 255, 'b': 255}
print(parse_html_color("#ffffffffffff")   )     # ==> {'r': 65535, 'g': 65535, 'b': 65535}
print(parse_html_color("#80FFA0"))              # ==> {'r': 128, 'g': 255, 'b': 160}
# rgb_to_hex((255, 255, 255))        # ==> '#ffffff'
# rgb_to_hex((65535, 65535, 65535))  # ==> '#ffffffffffff'



def parse_html_color(color):
    color = PRESET_COLORS.get(color.lower(), color)
    # for range starting at 1, ending at 6, for every 2 letters
    if len(color) == 7:
        r, g, b = (int(color[i:i+2], 16) for i in range(1, 7, 2))
    else:
        r, g, b = (int(color[i+1]*2, 16) for i in range(3))

    return dict(zip("rgb", (r, g, b)))