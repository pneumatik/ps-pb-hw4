cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city_input = input('Введите город: ').lower()

tourists_index = 3
if city_input == tourists[0]['city'].lower():
    tourists_index = 0
elif city_input == tourists[1]['city'].lower():
    tourists_index = 1
elif city_input == tourists[2]['city'].lower():
    tourists_index = 2
if tourists_index != 3:
    print(f"Турист {tourists[tourists_index]['user']['name']} возраст {tourists[tourists_index]['user']['age']}. Посетил город {city_input.title()}")
else:
    print('Такого города нет в списке')


