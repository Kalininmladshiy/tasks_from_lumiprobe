import argparse

def is_correct_bracket(text):
    i = 0
    for bracket in text:
        if (i < 0):
            return False
        if (bracket == '('):
            i += 1
        elif (bracket == ')'):
            i -= 1
    return (i == 0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа для определения скобочной последовательности'
    )
    parser.add_argument("text", help="Скобочная последовательность")
    args = parser.parse_args()
    print(is_correct_bracket(args.text))