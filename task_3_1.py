def num_translate():
    number = input('Введите число на английском: ')
    print(numbers.get(number.lower()).title())

numbers = {
    'one' : 'один',
    'two' : 'два',
    'three' : 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять',
}

num_translate()