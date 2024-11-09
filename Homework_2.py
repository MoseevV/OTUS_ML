#1
in_value = input("Enter integer: ")
out_value = 0
if in_value.isdigit():
    in_value = int(in_value)
    while True:
        while True:
            out_value += in_value % 10
            in_value = in_value // 10
            if in_value == 0:
                in_value = out_value
                out_value = 0
                break
        if in_value // 10 == 0:
            break
    print(in_value)
else:
    print("Value is't integer")


#2
seats = [[0,1,1,0],[1,0,0,1],[0,0,0,1],[0,0,0,0],[1,0,1,0]]
available_seats = 0
max_available_seats = 0
tickets = input("Enter number of tickets: ")
for i, row in enumerate(seats):
    for j, seat in enumerate (row):
        if seat == 0:
            available_seats += 1
            max_available_seats = available_seats
        else:
            available_seats = 0
    if max_available_seats >= int(tickets):
        print(i)
        break
else:
    print(False)

# 3
in_value = input("Enter symbols: ")
i = 1
count = 1
out_value = ""
while i < len(in_value):
    if in_value[i] == in_value[i-1]:
        count += 1
    else:
        out_value += str(count)
        out_value += str(in_value[i-1])
        count = 1
    i+=1
else:
    out_value += str(count)
    out_value += str(in_value[i - 1])
print (out_value)


# 4
alphabet_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
modified_index = 0
out_value = ''
message = input("Enter message: ")
key = int(input("Enter key: "))
try:
    for symbol in message:
        if symbol == ' ':
            out_value += symbol
        elif symbol.isupper():
            modified_index = (alphabet_up.index(symbol) + key) % 26
            out_value += alphabet_up[modified_index]
        else:
            modified_index = (alphabet_low.index(symbol) + key) % 26
            out_value += alphabet_low[modified_index]
    print(out_value)
except:
    print("Only Latin alphabet and spaces")


# 5
subject_dict = {}
while True:
    input_value = input("Enter 'Subject' 'Name' 'Grade', separated by space: ")
    if input_value == "":
        for subj in subject_dict:
            print (subj)
            for std in subject_dict[subj]:
                print (std, subject_dict[subj][std])
            else:
                print("\n")
        break
    else:
        subject, student, grade = input_value.split(' ', 2)
        if subject not in subject_dict:
            subject_dict[subject] = {student: [grade]}
        else:
            if student not in subject_dict[subject]:
                subject_dict[subject][student] = grade
            else:
                subject_dict[subject][student].append(grade)