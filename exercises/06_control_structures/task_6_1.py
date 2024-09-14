# -*- coding: utf-8 -*-
"""
Задание 6.1

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX Однако, в оборудовании Cisco
MAC-адреса используются в формате XXXX.XXXX.XXXX

Написать код, который преобразует MAC-адреса в формат cisco и добавляет их в новый
список result.
Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

blabla = ' '.join(mac).replace(":", ".").split()
print(blabla)
print(mac)

# ['aabb.cc80.7000', 'aabb.dd80.7340', 'aabb.ee80.7000', 'aabb.ff80.7000']
# save nr 2
>>>>>>> ccde3e44a470d262c379987cefc37e7f2ba166ff

# ['aabb.cc80.7000', 'aabb.dd80.7340', 'aabb.ee80.7000', 'aabb.ff80.7000']
# save nr 2