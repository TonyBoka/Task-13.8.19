# запрашиваем количество билетов, которое пользователь хочет приобрести на мероприятие
all_tickets = int(input('Введите количество билетов: '))

# создаем список, в котором будет храниться возраст посетителей
numbers_ages = []

# запрашиваем возраст посетителя для покупки каждого билета
# заполняем список числами, которые вводит пользователь
for i in range(0, all_tickets):
    input_value = int(input(f'Введите возраст участника №{i + 1}:\n'))
    numbers_ages.append(input_value)

# выбираем стоимость билета, исходя из возраста посетителя
    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

# считаем стоимость всех билетов
    full_price = sum(map(price, numbers_ages))

# делаем скидку 10%, если количество билетов больше 3
discount_price = int(full_price * 0.9)
if all_tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount_price, "руб.")
else:
    print('Стоимость всех билетов: ', full_price, "руб.")
