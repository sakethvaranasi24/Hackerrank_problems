def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        row = (s[::-1] + s[1:]).center(4 * size - 3, "-")
        lines.append(row)
        
    print("\n".join(lines[:0:-1] + lines))

