def rimRaqam(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for char in s:
        curr_value = roman_dict[char]
        result += curr_value
        if curr_value > prev_value:
            result -= 2 * prev_value
        prev_value = curr_value

    return result


print(rimRaqam("III"))
print(rimRaqam("IV"))
print(rimRaqam("IX"))
print(rimRaqam("LVIII"))
print(rimRaqam("MCMXCIV"))