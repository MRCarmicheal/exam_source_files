"""
CP1401 2020-1 Final Exam - Online Assignment
Name: Wang Qi

Where needed, use additional code files.
Ensure that each question's answer is clearly identifiable.
"""


# 7.
# Explanation:

# Code:
# Refactor the code and explain your reasons
length = float(input("Length? "))
width = float(input("Width "))
if length * width >= 30:
    print("Room of size {} sqm => Big".format(length * width))
elif length * width >= 10:
    print("Medium room of size {} sqm".format(length * width))
else:
    print("Your room is small at only {} sqm".format(length * width))


# 8.
# Explanation: After modifying an element in the list, the value of the element will not be brought into the list, so the list value will not change

# Code:
# Start with lowercase state names
things = ["qld", "nsw", "act"]
print("Original:", things)

# Make them uppercase
for i in range(len(things)):
    thing = things[i].upper()
    things[i] = thing
print("Uppercase names now:", things)


# 9.
# Code:
def main():
    try:
        in_file = open("data.txt")
        data = get_data(in_file)
        in_file.close()
        range(data)
    except:
        print("File open failed!")


def get_data(in_file):
    values = []
    for line in in_file:
        try:
            values.append(int(line))
        except:
            pass
    return values


def range(data):
    data.sort()
    data_range = data[len(data) - 1] - data[0]
    save_file(str(data_range))


def save_file(data):
    try:
        out_file = open("result.txt", "w")
        out_file.write(data)
        out_file.close()
    except:
        print:("File open failed ")


main()


# Explanation:
# 1: open the data file, add try. except statement, avoid the file crashing if it doesn't exist
# 2: try... except statment Prevent crashes caused by input other than numbers
# 3: open result file, add try. except stament, avoid the file crashing if it doesn't exist


# 10.
while True:
    try:
        height = int(input("Please enter your height: "))
    except ValueError:
        print("Age: ", "Invalid Integer")
        continue

    if height == 0:
      print("height: ", "In 10 years, you will be 10")
      continue
    else:
      if height in range(0, 120):
        print("height: ", height*10)
        continue
      else:
        if height not in range(0, 120):
          print("height: ", "height must be between 0 and 120")
          continue
        else:
          break

# 11.
def function(x, y= 2, z= 18):
    return x + y + z


print(function(2, y=5))  # prints 30
print(function(y=10))  # prints 41
print(function(100))  # prints 138


# 12.
d = {4: "good", 1: "hello", 5: "subject", 2: "welcome", 3: "exam"}
result = []
for index, number in enumerate(sorted(d.keys())):
    display = d[number][-1] * number
    result.append(f"{index + 1} is {display}")
for i in result[::-1]:
    print(i)

# 13.
data_string = "date='30/09/2021', temperature='21.286c', uv='7.23'"
data_string = "uv='10.13', date='01/02/2022', temperature='9.327c'"
data = data_string.replace("'", "")
uv_index = data_string.find("temperature")
uv = float(data_string[uv_index +12:uv_index +17])



# 14.
numbers = [10, 20, -13, -20, 55, 107, 200, -100, -222]
print(numbers[-1])
print(numbers[2:7])
print(numbers[0::3])
print(numbers[::-1])
print(([num for num in numbers if num >= 0]))
print("There are " + str(len(numbers)) + " numbers")


# 15.
pairs = ((2010, 'cm'), (1234, 'm'), (129.59, 'km'), (41231, 'm'), (67, 'km'))
for pair in pairs:
    long = pair[0]
    unit = pair[1]
    converted_str = ""
    if unit == "m":
        long_converted = long / 1000
        converted_str = " (converted)"
    elif unit =="cm":
        long_converted = long / 100000
    else:
        long_converted = long
    print("%8s -> %8.2f kilometres%s." % (long, long_converted, converted_str))


# 16.
names = ["Jim Lee", "Sir Ali Baba", "Kathy", "Bob Tim"]
for index, name in enumerate(names):
    print("{}. {} - {} word(s)".format(index + 1, name, len(name)))


# 17.
values = [('Bob', 2), ('Jo', 5), ('Harry', 3), ('Al', 4), ('Gwen', 1)]
sort_values = sorted(values, key=lambda x: (x[1], x[0]))
new_values = ["{}" ": {}".format(number, string) for string, number in sort_values]
print(new_values)


# 18.
# Explanation:

def init_this(things):
    """Initialize empty list"""
    things = [1, 2, 3]

some_things = []
init_this(some_things)
print(some_things)


# 19.
values = [4, 2, -3, 12, 8, 2, 9, -3]
bigger_number = [num for num in values if num >= 4]
print(bigger_number)

# 20. Answer in musicians.py
# 21. Answer in thing.py
# 22. Answer in stamps.py
