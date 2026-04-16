from random import randint


print('Добро пожаловать в игру "Угадай число"!')
print('Угадайте число от 1 до 200')

correct_number = randint(1, 200)
def main():
    while True:
        guess = (int(input('Введите число: ')))
        if guess > correct_number:
            print('Ваше число больше того, что загадано')
        elif guess < correct_number:
            print('Ваше число меньше того, что загадано')
        elif guess == correct_number:
            print('Отличная интуиция! Вы угадали число :)')
            break

main()
