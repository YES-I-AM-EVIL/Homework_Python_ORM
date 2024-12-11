import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Параметры подключения к базе данных
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'qwerty')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'netology_db')

# Создание подключения к базе данных
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()
