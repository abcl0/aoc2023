input_file = "input.txt"

with open(input_file, "r") as f:
    lines = f.readlines()

output = 0
for line in lines:
    nums = []
    line = line.strip()
    for c in line:
        if c.isdigit():
            nums.append(c)
    output += int(nums[0] + nums[-1])

print(output)
