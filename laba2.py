libr = {}

with open('conf.txt') as text:
    for line in text:
        line = line.strip('\n')
        if line.startswith('#') or line.startswith(';'):
            continue
        elif ' ' in line:
            key, value = line.split(' ', 1)
            libr[key] = value
        else:
            libr[line] = None


while True:
    line = input("Введите параметр:")
    if line.startswith('get param '):
        key = line[10:]
        value = libr.get(key)
        if value:
            print(key, ':', value.split('#')[0])
        else:
            print('(данные отсутствуют)')

    flag = True
    res = ''
    while flag:
        res = input("Продолжить? (Да/Нет)")
        if not (res == 'Нет' or res == 'Да'):
          continue
        else:
            break
    if res == 'Нет':
        break
    if res == 'Да':
        continue
