#1
def conversion(text: str):
    out_value = ''
    for i, symbol in enumerate(text):
        if symbol.isupper() == True:
            out_value += "_"
            out_value += symbol.lower()
        elif symbol.islower() == True and text[i-1] == "_":
            out_value += symbol.upper()
        elif symbol == "_":
            pass
        else:
            out_value += symbol
    return out_value

in_value = str(input("Enter text: "))
print (conversion(in_value))


# 2
def check_date(data: str):
    day, month, year = list(map(int, data.split('.')))
    if 0 < year < 100000 and 0 < month < 12 and day <= days(month, year):
        return True
    return False


def days(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else:
        if is_leap_year(year) == True:
            return 29
        return 28


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

while True:
    in_value = input("Enter date: ")
    if in_value == "":
        break
    print(check_date(in_value))


# 3
def is_prime_number(number: int):
    for i in range(2, number-1):
        if number % i == 0:
            return False
    return True


while True:
    in_value = int(input("Enter number: "))
    if in_value == "":
        break
    print(is_prime_number(in_value))


# 4
users_dict = {}


def validation(user):
    name, surname, age, key = user.split(' ', 3)
    if name.isalpha() and surname.isalpha() and 17 < int(age) < 61 and 0 < int(key) < 99999999:
        key = str(key.zfill(8))
        if name[0].islower() or surname[0].islower():
            name = str(name).title()
            surname = surname.title()

        users_dict[key] = (name, surname, age)


def dict_to_table(dictionary: dict):
    for key, user_data in dictionary.items():
        name, surname, age = str(user_data).split(', ')
        print(f'{key:10} | {name:20} | {surname:20} | {age:5}')


while True:
    in_value = input("Enter 'Name', 'Surname', 'Age', 'ID', seaprated by space: ")
    if in_value == '':
        break
    validation(in_value)
print(dict_to_table(users_dict))
