import random
password_length = int(input('Введите длину пароля: '))
possible_symbols = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = ''

for i in range(password_length):
  password += str(random.choice(possible_symbols))

print('Ваш пароль: ' + password)
