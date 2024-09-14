# vlans = [10, 20, 30, 40, 100]
# for vlan in vlans:
#   print(vlan)


# for letter in 'Test string':
#   print (letter)

# words = ['list', 'dict', 'tuple']
# upper_words = []
# for word in words:
#     upper_words.append(word.upper())
# print(upper_words)

# access_template = ['switchport mode access',
#                    'switchport access vlan',
#                    'spanning-tree portfast',
#                    'spanning-tree bpduguard enable']
# access = {'0/12': 10, '0/14': 11, '0/16': 17, '0/17': 150}

# for intf, vlan in access.items():
#     print('interface FastEthernet' + intf)
#     for command in access_template:
#         if command.endswith('access vlan'):
#             print('  {} {}'.format(command, vlan))
#         else:
#             print('  {}'.format(command))

# -*- coding: utf-8 -*-


username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

password_correct = False

while not password_correct:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
        password = input('Введите пароль еще раз: ')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
        password = input('Введите пароль еще раз: ')
    else:
        print(f'Пароль для пользователя {username} установлен')
        password_correct = True
