import argparse

def get_simbol_and_count(text):
    result = {}
    for letter in text.lower():
        result[letter] = result.get(letter, 0) + 1
    return sorted(result.items(), key=lambda item: item[1])[-1]



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа для определения символа и числа вхождений'
    )
    parser.add_argument("text", help="Строка из латинских символов")
    args = parser.parse_args()
    print(get_simbol_and_count(args.text))