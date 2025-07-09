import sqlite3

# Создаём соединение с базой данных (создаст файл roster.db)
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Добавляем данные
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", roster_data)
conn.commit()

# Обновление имени Jadzia Dax на Ezri Dax
cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
conn.commit()

# Выводим имя и возраст всех Bajoran
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
results = cursor.fetchall()

for name, age in results:
    print(f"Name: {name}, Age: {age}")

# Закрываем соединение
conn.close()
