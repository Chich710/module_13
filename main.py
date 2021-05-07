result = 0
print('Введите количество билетов: ')
num_of_tickets = int(input())

for i in range(num_of_tickets):
    print('Введите возраст ', i+1,' участника: ')
    age = (int(input()))
    if age < 18:
        result += 0
    elif 18 <= age < 25:
        result += 990
    else:
        result += 1390

if num_of_tickets <= 3:
    print(result, ' - общая стоимость билетов.')
else:
    result = int(result - (0.1 * result))
    print(result, ' - общая стоимость билетов со скидкой 10%')