data = int(input('Преобразование секунд в дни, часы и минуты. Введите секунды: '))
days = data // 86400
data_hours = data % 86400
hours = data_hours // 3600
data_minutes = data_hours % 3600
minutes = data_minutes // 60
seconds = data_minutes % 60

print(days, 'день', hours, 'час', minutes, 'минута и секунда', seconds)