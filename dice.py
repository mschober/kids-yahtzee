six_die_display = """
 -------
| *   * |
| *   * |
| *   * |
 -------
 """
five_die_display = """
 -------
| *   * |
|   *   |
| *   * |
 -------
"""
four_die_display = """
 -------
| *   * |
|       |
| *   * |
 -------
"""
three_die_display = """
 -------
| *     |
|   *   |
|     * |
 ------- 
"""
two_die_display = """
 -------
| *     |
|       |
|     * |
 -------
"""
one_die_display = """
 -------
|       |
|   *   |
|       |
 -------
"""

def display_die_face(die_value):
    six_sided = [
        one_die_display,
        two_die_display,
        three_die_display,
        four_die_display,
        five_die_display,
        six_die_display
    ]
    to_display = six_sided[die_value]
    print(to_display)

def six_sided():
    import random
    die_value = random.randint(1,6)
    display_die_face(die_value)
