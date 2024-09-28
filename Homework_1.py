#1
while True:
    input_value = input("Enter a five-digit number: ")
    if input_value.isdigit() and len(input_value) == 5:
        a = input_value[1:4]
        b = a[::-1]
        print(input_value[0] + b + input_value[-1])
    else:
        print("It's not five-digit number")

# 2
in_value = input("Enter number of days until vacation: ")
if in_value.isdigit():
    if int(in_value) % 7 == 6:
        print(int(in_value) // 7 * 2 + 1)
    else:
        print(int(in_value) // 7 * 2)
else :
    print("Value is't digit")


# 3
length = input("Enter length: ")
width = input("Enter width: ")
in_value = input("Enter chocolate bar size: ")
if length.isdigit() and width.isdigit() and in_value.isdigit():
    if int(in_value) > int(length) * int(width):
        print (False)
    elif int(in_value) % int(width) == 0 or int(in_value) % int(length) == 0:
        print(True)
    else:
        print(False)
else:
    print("Value is't digit")


# 4
ones = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
tens = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
hundreds = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
thousands = {1: 'M', 2: 'MM', 3: 'MMM'}
iteration = {1: ones, 2: tens, 3: hundreds, 4: thousands}
i = 1
list = []
out_value = ''
in_value = input("Enter positive integer: ")
if in_value.isdigit():
    if int(in_value) > 0:
        while True:
            list.insert(0, str(iteration.get(i).get(int(in_value) % 10)))
            i += 1
            if int(in_value) // 10 == 0:
                break
            in_value = int(in_value) // 10
        for j in list:
            out_value += str(j)
        print(out_value)
    else:
        print("Incorrect value")
else:
    print("Incorrect value")


# 5
in_value = input("Enter number: ")
if in_value.count('.') == 1:
    in_value = in_value.replace('.', '')
    if in_value.isdigit():
        print("True, positive")
    elif in_value[0] == "-" and in_value[1:].isdigit():
        print("True, negative")
    else:
        print(False)
elif in_value.isdigit():
    print("True, positive")
elif in_value[0] == "-" and in_value[1:].isdigit():
    print("True, neagtive")
else:
    print(False)
