def is_number_greater_7(s):
    if s > 7:
        return "Hello"
    else:
        return "Number less 7"

def is_john(s):
    if s == "John":
        return "Hello John"
    else:
        return "There is no such name"


def is_multiples_3(s):
    ans_lst = []
    for elm in s:
        try:
            num = int(elm)
            if num % 3 == 0:
                ans_lst.append(num)
        except ValueError:
            pass
    return f"Результат: {ans_lst}"

def main():
    while True:
        user_input = input("Введите число, строку, список или 'end' для выхода: ")

        if user_input.lower() == "end":
            return "Завершение работы."


        input_str = user_input.strip()
        if input_str.startswith("[") and input_str.endswith("]"):
            list_str = input_str[1:-1].strip()
            if list_str:
                elements = [item.strip() for item in list_str.split(",")]
            else:
                elements = []
            print(is_multiples_3(elements))
            continue

        try:
            num = float(input_str)
            if num.is_integer():
                num = int(num)
            print(is_number_greater_7(num))
            continue
        except ValueError:
            pass

        print(is_john(user_input))




if __name__ == '__main__':
    main()