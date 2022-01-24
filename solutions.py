# Loops

def loops(i):
    numsBefore = list(range(0, i))
    for x in numsBefore:
        print(x ** 2)


# Leap Year

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# String Descending

def strings(num):
    x = 1
    while x < num + 1:
        print(x, end="")
        x = x + 1


# Dictionary Student Grades

def grades(n):
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    total = sum(marks)
    x = (total / 3.00)
    formatted_float = "{:.2f}".format(x)
    print(formatted_float)


# Runner Up

def runner_up(arr):
    values = []
    for x in arr:
        if x not in values:
            values.append(x)
        values.sort()
    print(values[-2])


# Split and Join

def split_and_join(line):
    split = line.split(" ")
    a = "-".join(split)
    return a


# String Concatenation

def print_full_name(first, last):
    template = "Hello " + first + " " + last + "! You just delved into python."
    print(template)


# Find substring in string

def mutate_string(string, position, character):
    list_of_string = list(string)
    list_of_string[position] = character
    string = "".join(list_of_string)
    return string


