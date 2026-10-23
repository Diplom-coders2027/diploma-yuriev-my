import os
import sys
import random
import time

while True:
    difficulty = 1
    how_many_numbers = 0
    sign = ''
    result = 0
    numbers=[]
    # signs=['+','-','*','/']
    signs=['+']

    while how_many_numbers < 2: 
        how_many_numbers = int(input('Введите кол-во чисел: '))

    for i in range(how_many_numbers):
        number = random.randint(-100,100)
        numbers.append(number)
    print(numbers)

    if difficulty == 1:
        random.shuffle(signs)
        sign = signs[0]
        print(f'test3 - "{sign}"')

    if sign == "+":
        result=numbers[0]
        for i in range(len(numbers)):
            result=sum(numbers)
        print(result)

    elif sign == "-":
        result=numbers[0]
        for i in range(len(numbers)):
            result-=numbers[i]
        print(result)

    time.sleep(100)
    os.system('cls')
