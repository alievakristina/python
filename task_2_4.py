price = [58.43, 15.12, 78.05, 901.02, 105.68, 35.12, 23.87, 2.45, 49.65, 84.3, 1.82, 42.6, 47.29, 88, 97.01]
#Задание под пунктом А
print('Задание под пунктом "А"')
for p in price:
    print(f'{int(p)} руб. {int(p * 100 % 100):02d} коп.', end=', ')

#Задание под пунктом В
print('\n\nЗадание под пунктом "B"')
print(f'Список цен: {price} id списка цен:{id(price)}')
price.sort()
print(f'Список цен после сортировки: {price} id списка цен:{id(price)}')

#Задание под пунктом С
print('\nЗадание под пунктом "C"')
new_price = sorted(price.copy(), reverse=True)
print(f'Новый список цен отсортированный по убыванию: {new_price} id нового списка цен:{id(new_price)}')

#Задание под пунктом D
print('\nЗадание под пунктом "D"')
print(price[-5:])