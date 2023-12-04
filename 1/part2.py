import re

input_file = "input.txt"
with open(input_file, "r") as f:
    lines = f.readlines()

digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def toDigit(word):
    if word.isdigit():
        return int(word)
    else:
        return digit_map[word]


output = 0
for line in lines:
    nums = []
    line = line.strip()
    digits = re.findall(
        r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))",
        line,
        flags=re.IGNORECASE,
    )
    o = toDigit(digits[0]) * 10 + toDigit(digits[-1])
    output += o
print(output)
