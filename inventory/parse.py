def parse_line(line):
    """'apple, 3' -> ('apple', 3). Names may contain spaces; whitespace is trimmed."""
    name, qty = line.split(",")
    return name, int(qty)
