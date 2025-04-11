def roman_to_int(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(s):
        if char not in roman:
            raise ValueError(f"Invalid Roman numeral character: '{char}'")
        value = roman[char]
        total += -value if value < prev else value
        prev = value
    return total

# Interactive demo (optional)
if __name__ == "__main__":
    while True:
        user_input = input("Enter Roman numeral (or 'quit'): ").strip().upper()
        if user_input == "QUIT":
            break
        try:
            print(f"Result: {roman_to_int(user_input)}\n")
        except ValueError as e:
            print(f"Error: {e}\n")