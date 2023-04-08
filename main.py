import random
import time
mod = int(input(
          'Выберите режим работы генерации пароля(1 - упрощенный; 2 - сложный): '))

if mod == 1:
    password_length = int(input('Введите длину пароля: '))
    possible_symbols = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password_simple = ''
    for i in range(password_length):
        password_simple += str(random.choice(possible_symbols))
    print('Ваш пароль: ' + password_simple)
    file_name = input('Введите название файла, который будет хранить пароль: ')
    with open(file_name + '.txt', 'w') as f:
        f.write(password_simple)
elif mod == 2:
    possible_symbols = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password_hard = ''
    for i in range(random.randint(2, 4)):
        password_hard += str(random.choice(possible_symbols)
                             ) + str(time.time())
    print('Ваш пароль: ' + password_hard)
    file_name = input('Введите название файла, который будет хранить пароль: ')
    with open(file_name + '.txt', 'w') as f:
        f.write(password_hard)
else:
    print('Введите правильное число!')
