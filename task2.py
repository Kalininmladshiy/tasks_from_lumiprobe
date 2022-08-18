import argparse
import math
from decimal import Decimal as D

def get_sqrt(num):
    answer = 1
    for _ in range(10):
        new_answer = (D(answer) + D(num) / D(answer)) / 2
        answer = new_answer    
    if int(answer) == D(answer):
        return int(answer)
    else:
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа для извлечения корня'
    )
    parser.add_argument("num", help="Число", type=int)
    args = parser.parse_args()
    print(get_sqrt(args.num))
    