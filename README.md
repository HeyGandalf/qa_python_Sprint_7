# Sprint_7: Тестирование API Яндекс Самокат

Этот проект содержит автотесты для API учебного сервиса Яндекс Самокат, реализованные с использованием `pytest`, `allure`, `requests` и `faker`.

## 📋 Описание

Реализованы проверки следующих ручек:

- `POST /api/v1/courier` — создание курьера
- `POST /api/v1/courier/login` — авторизация курьера
- `POST /api/v1/orders` — создание заказа
- `GET /api/v1/orders` — получение списка заказов

## 🔧 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/Sprint_7.git
   cd Sprint_7
   ```

2. Создайте виртуальное окружение (рекомендуется):
   - Для Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Для macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Запуск тестов

1. Для запуска всех тестов:
   ```bash
   pytest -v --alluredir=target/allure-results
   ```

2. Для просмотра отчёта Allure:
   ```bash
   allure serve target/allure-results
   ```

## ⚙️ Структура проекта

```
Sprint_7/
├── conftest.py               # фикстуры
├── urls.py                   # базовый URL
├── endpoints.py              # относительные пути к ручкам
├── generator.py              # генерация данных для тестов
├── data.py                   # статичные данные
├── test_create_courier.py    # тесты на создание курьера
├── test_login_courier.py     # тесты на авторизацию курьера
├── test_create_order.py      # тесты на создание заказа
├── test_list_orders.py       # тесты на список заказов
├── requirements.txt          # зависимости проекта
└── .gitignore                # исключённые из репозитория файлы
```

## 📌 Покрытие

Тестами покрыты следующие сценарии:

### ✅ Курьер
- успешное создание курьера  
- невозможность создать двух одинаковых  
- валидация обязательных полей (`login`, `password`)  
- корректные коды ответов (201, 400, 409)  

### ✅ Авторизация
- успешная авторизация (возвращается `id`)  
- ошибки при неправильных/неполных данных  
- ошибки при попытке авторизации несуществующего курьера  

### ✅ Заказ
- заказ с одним, двумя, без цветов  
- `track` в теле ответа  

### ✅ Список заказов
- в теле ответа возвращается список заказов  

## 🧹 Дополнительно

- Добавлена фикстура `new_courier` с `yield` для автоматического удаления созданного курьера.  
- Используется библиотека `faker` для генерации уникальных данных.  
- Использована параметризация тестов там, где это целесообразно.  

## 📄 Allure отчёт

Для коммита отчёта Allure в репозиторий (если `target` в `.gitignore`):

```bash
git add -f ./target/allure-results/.
git commit -m "add allure report"
git push
```

## 📝 .gitignore

Включены типичные исключения для Python-проектов и папки с отчётами Allure:
```
# Python
__pycache__/
*.pyc
.venv/

# Allure
target/
```
