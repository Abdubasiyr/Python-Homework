import json
import random
import requests
import os

# ──────────────────────────────────────────────────────────────
# 1. JSON Parsing — чтение students.json
def parse_students():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for student in data["students"]:
                print(f"Имя: {student['name']}")
                print(f"Возраст: {student['age']}")
                print(f"Курс: {student['course']}\n")
    except FileNotFoundError:
        print("Файл students.json не найден.")
    except Exception as e:
        print("Ошибка чтения JSON:", e)

# ──────────────────────────────────────────────────────────────
# 2. Weather API — запрос погоды по городу (OpenWeatherMap)
def get_weather():
    city = input("Введите название города (например, Tashkent): ")
    api_key = "YOUR_OPENWEATHER_API_KEY"  # 🔁 Вставь сюда свой ключ
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            print(f"Город: {data['name']}")
            print(f"Температура: {data['main']['temp']}°C")
            print(f"Влажность: {data['main']['humidity']}%")
            print(f"Погода: {data['weather'][0]['description']}")
        else:
            print("Ошибка:", data.get("message", "Не удалось получить данные."))
    except Exception as e:
        print("Ошибка запроса:", e)

# ──────────────────────────────────────────────────────────────
# 3. JSON Modification — работа с books.json
def modify_books():
    filename = "books.json"

    # Загружаем книги
    def load_books():
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"books": []}

    # Сохраняем книги
    def save_books(data):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    data = load_books()

    while True:
        print("\n1. Добавить книгу\n2. Обновить книгу\n3. Удалить книгу\n4. Показать все\n0. Назад")
        choice = input("Ваш выбор: ")

        if choice == "1":
            title = input("Название книги: ")
            author = input("Автор: ")
            year = input("Год: ")
            data["books"].append({"title": title, "author": author, "year": year})
            save_books(data)
            print("Книга добавлена.")

        elif choice == "2":
            title = input("Введите название книги для обновления: ")
            found = False
            for book in data["books"]:
                if book["title"].lower() == title.lower():
                    book["author"] = input("Новый автор: ")
                    book["year"] = input("Новый год: ")
                    save_books(data)
                    print("Книга обновлена.")
                    found = True
                    break
            if not found:
                print("Книга не найдена.")

        elif choice == "3":
            title = input("Введите название книги для удаления: ")
            before = len(data["books"])
            data["books"] = [b for b in data["books"] if b["title"].lower() != title.lower()]
            after = len(data["books"])
            save_books(data)
            if before == after:
                print("Книга не найдена.")
            else:
                print("Книга удалена.")

        elif choice == "4":
            for book in data["books"]:
                print(f"{book['title']} — {book['author']} ({book['year']})")

        elif choice == "0":
            break

        else:
            print("Неверный выбор.")

# ──────────────────────────────────────────────────────────────
# 4. Movie Recommendation (OMDB API)
def movie_recommendation():
    genre = input("Введите жанр фильма (например, Action, Comedy): ")
    api_key = "YOUR_OMDB_API_KEY"  # 🔁 Вставь сюда свой ключ
    url = f"http://www.omdbapi.com/?apikey={api_key}&type=movie&s={genre}&page=1"

    try:
        response = requests.get(url)
        data = response.json()
        if "Search" in data:
            movie = random.choice(data["Search"])
            print("🎬 Рекомендованный фильм:")
            print(f"Название: {movie['Title']}")
            print(f"Год: {movie['Year']}")
        else:
            print("Фильмы не найдены.")
    except Exception as e:
        print("Ошибка при запросе:", e)

# ──────────────────────────────────────────────────────────────
# Главное меню
def main():
    while True:
        print("\nВыберите задание:")
        print("1. Прочитать students.json")
        print("2. Получить погоду (OpenWeather)")
        print("3. Модификация books.json")
        print("4. Рекомендовать фильм (OMDB)")
        print("0. Выход")

        choice = input("Ваш выбор: ")
        if choice == "1":
            parse_students()
        elif choice == "2":
            get_weather()
        elif choice == "3":
            modify_books()
        elif choice == "4":
            movie_recommendation()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
