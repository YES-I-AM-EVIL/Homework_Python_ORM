import json
import os
from db import session
from models import Publisher, Shop, Book, Stock, Sale

# Функция для загрузки данных в базу данных
def load_data(file_path):
    # Очистка базы данных
    session.query(Sale).delete()
    session.query(Stock).delete()
    session.query(Book).delete()
    session.query(Shop).delete()
    session.query(Publisher).delete()
    session.commit()

    with open(file_path, 'r', encoding='utf-8') as fd:
        data = json.load(fd)

    for record in data:
        model_class = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]

        fields = record.get('fields')
        if model_class == Sale:
            fields.pop('count', None)  # Удаляем поле 'count'
            fields['price'] = float(fields['price'])  # Преобразование строки в float
        session.add(model_class(id=record.get('pk'), **fields))

    session.commit()

if __name__ == "__main__":
    # Используем абсолютный путь к файлу
    file_path = os.path.join(os.path.dirname(__file__), 'tests_data.json')
    load_data(file_path)
