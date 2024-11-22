# Sports Tourism FedRu API
SkillFactory - заказ от Федерации Спортивного Туризма России (ФСТР)

Это веб-приложение, разработанное с использованием FastAPI и SQLAlchemy.
Оно предназначено для управления данными о горных перевалах, позволяя 
пользователям добавлять, обновлять и получать информацию из базы данных.

## Установка

### 1. Клонируйте репозиторий:
```bash
git clone https://github.com/bit-trade/SportsTourismFedRu
cd SportsTourismFedRu
```

### 2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Для Windows используйте: venv\Scripts\activate
```

### 3. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 4. Настройте базу данных:
- Убедитесь, что ваша база данных настроена правильно. 
Измените конфигурацию подключения в файле database/connect.py.
- Прежде чем запустить приложение выполните файл database/interaction.py

## Запуск приложения

Запустите сервер с помощью следующей команды:
```bash
uvicorn main:pereval --reload
```

Здесь main — это имя файла, в котором находится FastAPI экземпляр, 
а pereval — это экземпляр FastAPI.

## Эндпоинты

### 1. Получение домашней страницы

- **URL:** /
- **Метод:** GET
- **Параметры запроса:**
  - skip: (необязательный) количество пропускаемых записей (по умолчанию 0)
  - limit: (необязательный) максимальное количество возвращаемых записей (по умолчанию 10)

**Пример запроса:**
```http request
GET http://localhost:8000/?skip=2limit=16
```

### 2. Отправка данных

- **URL:** /submitData
- **Метод:** POST
- **Тело запроса:** JSON-объект со следующими полями:
  - raw_data: данные
  - images: список изображений

**Пример запроса:**
```http request
POST http://localhost:8000/submitData
Content-Type: application/json

{
  "raw_data": {
    "beautyTitle": "пер. ",
	"title": "Пхия",
	"other_titles": "Триев",
	"connect": "",
	"add_time": "2024-11-22 20:08:13",
	"user": {
		"email": "user@email.tld",
		"phone": "79031234567",
		"fam": "Петров",
		"name": "Василий",
		"otc": "Иванович"
	},
	"coords": {
		"latitude": "45.3842",
		"longitude": "7.1525",
		"height": "1200"
	},
	"level": {
		"winter": "",
		"summer": "1А",
		"autumn": "1А",
		"spring": ""
	}
  },
  "images": [
      {"id": 1, "title": "Седловина"},
      {"id": 2, "title": "Подъем"}]
}
```

### 3. Получение данных по ID

- **URL:** /submitData/{pass_id}
- **Метод:** GET

**Пример запроса:**
```http request
GET http://localhost:8000/submitData/1
```

### 4. Обновление данных по ID

- **URL:** /submitData/{pass_id}
- **Метод:** PATCH
- **Тело запроса:** JSON-объект с обновленными данными.

**Пример запроса:**
```http request
PATCH http://localhost:8000/submitData/1
Content-Type: application/json

{
  "moder_status": "accepted",
  "basic_info": {
      "beautyTitle": "реб",
      "title": "Триев",
      "other_titles": "Пхия",
      "connect": "",
      "add_time": "2022-02-22 04:40:13"
  },
  "coords": {
      "latitude": "25.4238",
      "longitude": "37.5251",
      "height": "1000"
  },
  "level": {
      "winter": "AB",
      "summer": "2B",
      "autumn": "3А",
      "spring": "BB"
  },
  "images": [{"id": 2, "title": "Седловина"}]
}
```

### 5. Получение данных по email пользователя

- **URL:** /submitData/user_email/{email}
- **Метод:** GET

**Пример запроса:**
```http request
GET http://localhost:8000/submitData/user_email/user@example.com
```
