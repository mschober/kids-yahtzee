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
  ------
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
| ------|
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
    if die_value == 1:
        print(one_die_display)
    if die_value == 2:
        print(two_die_display)
    if die_value == 3:
        print(three_die_display)
    if die_value == 4:
        print(four_die_display)
    if die_value == 5:
        print(five_die_display)
    if die_value == 6:
        print(six_die_display)

def six_sided():
    import random
    die_value = random.randint(1,6)
    display_die_face(die_value)
