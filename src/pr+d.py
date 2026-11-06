import os
import sys
import random
import time

# ---------- Настройки ----------
MIN_NUM = -100
MAX_NUM = 100
CLEAR_CMD = 'cls' if os.name == 'nt' else 'clear'
def settings():
    print('Настройки')


def clear():
    os.system(CLEAR_CMD)


def get_how_many_numbers():
    """Запрашивает количество чисел (минимум 2)."""
    while True:
        try:
            n = int(input('Сколько чисел использовать? (минимум 2): '))
            if n >= 2:
                return n
            print('⚠️  Нужно минимум 2 числа.')
        except ValueError:
            print('⚠️  Введите целое число.')


def generate_numbers(count):
    return [random.randint(MIN_NUM, MAX_NUM) for _ in range(count)]


def calculate(numbers, sign):
    """Считает результат для выбранного знака."""
    if sign == '+':
        return sum(numbers)
    if sign == '-':
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        return result
    if sign == '*':
        result = 1
        for n in numbers:
            result *= n
        return result
    if sign == '/':
        result = numbers[0]
        for n in numbers[1:]:
            if n == 0:
                return None  # деление на ноль
            result /= n
        return result
    raise ValueError(f'Неизвестный знак: {sign}')


def format_expression(numbers, sign):
    """Красиво оформляет выражение: 5 - (-3) + 7 ..."""
    parts = [str(numbers[0])]
    for n in numbers[1:]:
        parts.append(f'{sign} {n}')
    return ' '.join(parts)


def play_round(score,total_rounds):
    clear()
    
    if total_rounds > 0:
        percent_str=f'{score/total_rounds * 100:.0f}%'
    else:
        percent_str = '-'
    
    print('=' * 70)
    print(f'🎮  МАТЕМАТИЧЕСКИЙ ТРЕНАЖЁР   |   Счёт: {score}    |   Верность: {percent_str}')
    print('=' * 70)

    count = get_how_many_numbers()
    numbers = generate_numbers(count)
    # sign = random.choice(['+', '-', '*', '/'])
    sign = random.choice(['+', '-'])

    # Деление — только на целые числа, иначе пример некрасивый
    if sign == '/':
        numbers = [random.randint(MIN_NUM, MAX_NUM) for _ in range(count)]
        numbers[1:] = [n if n != 0 else 1 for n in numbers[1:]]

    expression = format_expression(numbers, sign)
    correct = calculate(numbers, sign)

    if correct is None:
        print('⚠️  Попалось деление на ноль — пропускаем.')
        time.sleep(1.5)
        return score, False, False

    print(f'\nПример: {expression} = ?')
    try:
        answer = float(input('Ваш ответ: '))
    except ValueError:
        print('❌  Некорректный ввод.')
        time.sleep(1.5)
        return score, False, False

    if abs(answer - correct) < 1e-9:
        print('✅  Верно! +1 очко')
        score += 1
        is_correct = True
    else:
        print(f'❌  Неверно. Правильный ответ: {correct}')
        is_correct = False

    time.sleep(2)
    return score, is_correct, True # Счёт, Верно?, Раунд засчитан?


def main():
    score = 0
    total_rounds=0
    try:
        while True:
            score, is_correct, counted = play_round(score, total_rounds)
            if counted:
                total_rounds+=1
    except KeyboardInterrupt:
        clear()
        
        if total_rounds > 0:
            percent = score / total_rounds * 100
            percent_str = f'{percent:.0f}%'
        else:
            percent_str = '-'
        
        print('=' * 50)
        print(f'🏁 Игра завершена! 🏁')
        print(f'Ваш итоговый счёт: {score} из {total_rounds}')
        print(f'Процент верности: {percent_str}')
        print('=' * 50)
        sys.exit(0)


if __name__ == '__main__':
    main()