import argparse


def check_number(s):
    if s > 7:
        return "Hello"
    else:
        return "Number less 7"


def check_john(t):
    if t == "John":
        return "Hello John"
    else:
        return "There is no such name"


def check_array(k):
    list_str = k[1:-1].strip()
    if list_str:
        elements = [item.strip() for item in list_str.split(",")]
    else:
        elements = []
    ans_lst = []
    for elm in elements:
        try:
            num = int(elm)
            if num % 3 == 0:
                ans_lst.append(num)
        except ValueError:
            pass
    return f"Результат: {ans_lst}"


def main():
    parser = argparse.ArgumentParser(description='Запуск функций из консоли.')
    parser.add_argument('--function', choices=['check_number', 'check_john', 'check_array'], required=True,
                        help='Выберите функцию для запуска')
    parser.add_argument('--args', nargs='*', help='Аргументы функции')

    args = parser.parse_args()

    if args.function == 'check_number':
        if not args.args or len(args.args) != 1:
            print("Для функции check_number нужно передать одно число.")
            return
        try:
            s = int(args.args[0])
        except ValueError:
            print("Аргумент должен быть числом.")
            return
        print(check_number(s))

    elif args.function == 'check_john':
        if not args.args or len(args.args) != 1:
            print("Для функции check_john нужно передать имя.")
            return
        t = args.args[0]
        print(check_john(t))

    elif args.function == 'check_array':
        if not args.args or len(args.args) != 1:
            print("Для функции check_array нужно передать строку в виде массива, например: \"[1, 2, 3]\".")
            return
        k = args.args[0]
        print(check_array(k))

if __name__ == '__main__':
    main()
