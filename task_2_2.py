def give_sign(x):
    if x[0] in '+-':
        return x[0]

new_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(new_list):
    sign = give_sign(new_list[i])
    if new_list[i].isdigit() or (sign and new_list[i][1:].isdigit()):
        if sign:
            new_list[i] = sign + new_list[i][1:].zfill(2)
        else:
            new_list[i] = new_list[i].zfill(2)

        new_list.insert(i, '"')
        new_list.insert(i + 2, '"')
        i += 2
    i += 1

print(new_list)
str_new_list = " ".join(new_list)
print(str_new_list)

