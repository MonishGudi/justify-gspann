def justify_paragraph(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_line_length = 0

    for word in words:
        if current_line_length + len(word) + len(current_line) > width:
            lines.append(justify_line(current_line, current_line_length, width))
            current_line = [word]
            current_line_length = len(word)
        else:
            current_line.append(word)
            current_line_length += len(word)

    if len(current_line) == 1:
        lines.append(current_line[0].ljust(width))
    else:
        lines.append(justify_line(current_line, current_line_length, width))

    return lines

def justify_line(words, current_line_length, width):
    if len(words) == 1:
        return words[0].ljust(width)

    spaces_needed = width - current_line_length
    gaps = len(words) - 1
    spaces = spaces_needed // gaps
    extra_spaces = spaces_needed % gaps

    line = words[0]
    for i in range(gaps):
        line += ' ' * (spaces + (1 if i < extra_spaces else 0)) + words[i + 1]

    return line

def main():
    text = input("Enter a paragraph to justify: ").strip()
    if not text:
        print("Text cannot be empty or just whitespace.")
        return

    try:
        width = int(input("Enter the width for justification: ").strip())
        if width <= 0:
            print("Width must be a positive integer.")
            return
        if width < max(len(word) for word in text.split()):
            print(f"Width must be at least as long as the longest word ({max(len(word) for word in text.split())}).")
            return
    except ValueError:
        print("Invalid input. Width must be an integer.")
        return

    justified = justify_paragraph(text, width)
    for line in justified:
        print(f"'{line}'")

if __name__ == "__main__":
    main()

