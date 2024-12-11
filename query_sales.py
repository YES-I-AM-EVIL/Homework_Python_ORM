from db import session
from models import Publisher, Book, Shop, Stock, Sale
from sqlalchemy import and_

def get_sales_by_publisher(publisher_input):
    # Создаем общее тело запроса на выборку данных и сохраняем в переменную
    query = session.query(
        Book.title, Shop.name, Sale.price, Sale.date_sale
    ).select_from(Shop).\
        join(Stock, Shop.id == Stock.id_shop).\
        join(Book, Stock.id_book == Book.id).\
        join(Publisher, Book.id_publisher == Publisher.id).\
        join(Sale, Stock.id == Sale.id_stock)

    if publisher_input.isdigit():  # Проверяем переданные данные в функцию на то, что строка состоит только из чисел
        sales = query.filter(Publisher.id == int(publisher_input)).all()
    else:
        sales = query.filter(Publisher.name == publisher_input).all()

    for title, shop_name, price, date_sale in sales:  # Проходим в цикле по переменной, в которой сохраняем результат фильтрации, и при каждой итерации получаем кортеж и распаковываем значения в 4 переменные
        print(f"{title: <40} | {shop_name: <10} | {price: <8} | {date_sale.strftime('%d-%m-%Y')}")  # Передаем в форматированную строку переменные, которые содержат имя книги, название магазина, стоимость продажи и дату продажи

if __name__ == '__main__':
    publisher_input = input("Введите имя или идентификатор издателя: ")  # Просим клиента ввести имя или айди публициста и данные сохраняем в переменную
    get_sales_by_publisher(publisher_input)  # Вызываем функцию получения данных из базы, передавая в функцию данные, которые ввел пользователь строкой выше
