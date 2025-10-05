"""Files questions."""

# 1.
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
print(result)

# 4.
with open("numbers.txt", "r") as in_file:
    result = 0
    for line in in_file:
        result += int(line)
print(result)
