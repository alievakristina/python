first_list = ['инженер-конструктор Игорь',
              'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАЙ',
              'директор аэлита']

for el in first_list:
    first_name = el.split(' ')[-1].capitalize()
    print(f'Привет, {first_name}!')