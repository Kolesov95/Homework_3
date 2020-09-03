def user_data(name, surname, year, city, email, number):
    return (
        f'Имя: {name}; фамилия: {surname}; год рождения: {year}; город проживания: {city}; email: {email}; '
        f'номер телефона: {number}')


print(user_data(name='Андрей', surname='Колесов', city='Москва',
                year=1995, number='123456789101', email='pranehs@mail.ru'))
