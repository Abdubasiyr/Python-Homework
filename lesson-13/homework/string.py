"""
Домашнее задание: 10 mini-утилит в одном скрипте.
Запустите файл и выберите номер задачи из меню.
"""

from datetime import datetime, timedelta
import time
import re
import sys

# Python 3.9+ — встроенный zoneinfo для часовых поясов
try:
    from zoneinfo import ZoneInfo
except ImportError:
    print("Модуль zoneinfo не найден (нужен Python 3.9+). Некоторые функции не будут работать.")
    ZoneInfo = None

# dateutil — для точных разниц дат
try:
    from dateutil.relativedelta import relativedelta
except ImportError:
    print("Библиотека python-dateutil не установлена. Установите:  pip install python-dateutil")
    relativedelta = None


# ──────────────────────────────────────────────────────────────────────────────
# 1. Калькулятор возраста
def age_calculator():
    birth_str = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
    try:
        birth = datetime.strptime(birth_str, "%Y-%m-%d")
    except ValueError:
        print("Неверный формат. Попробуйте ещё раз.")
        return
    today = datetime.now()

    if relativedelta:
        diff = relativedelta(today, birth)
        print(f"Вам {diff.years} лет, {diff.months} месяцев и {diff.days} дней.")
    else:
        # приближённый расчёт без dateutil
        years = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        months = (today.month - birth.month - (today.day < birth.day)) % 12
        days = (today - birth.replace(year=today.year)).days % 365
        print(f"Вам примерно {years} лет, {months} месяцев и {days} дней.")


# 2. Сколько дней до следующего дня рождения
def days_until_next_birthday():
    birth_str = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
    try:
        birth = datetime.strptime(birth_str, "%Y-%m-%d")
    except ValueError:
        print("Неверный формат.")
        return
    today = datetime.now().date()
    next_bday = birth.replace(year=today.year).date()
    if next_bday < today:
        next_bday = next_bday.replace(year=today.year + 1)
    days_left = (next_bday - today).days
    print(f"До вашего следующего дня рождения осталось {days_left} дней.")


# 3. Планировщик встречи
def meeting_scheduler():
    cur_str = input("Текущая дата и время (ГГГГ-ММ-ДД ЧЧ:ММ): ")
    dur_str = input("Длительность встречи (чч:мм): ")
    try:
        start = datetime.strptime(cur_str, "%Y-%m-%d %H:%M")
        dur_h, dur_m = map(int, dur_str.split(":"))
    except ValueError:
        print("Формат введён неверно.")
        return
    end_time = start + timedelta(hours=dur_h, minutes=dur_m)
    print("Встреча закончится:", end_time.strftime("%Y-%m-%d %H:%M"))


# 4. Конвертер часовых поясов
def timezone_converter():
    if ZoneInfo is None:
        print("Эта функция недоступна без модуля zoneinfo.")
        return
    dt_str = input("Введите дату и время (ГГГГ-ММ-ДД ЧЧ:ММ): ")
    tz_from = input("Ваш часовой пояс (например, Asia/Tashkent): ")
    tz_to = input("Целевой часовой пояс: ")
    try:
        tz_from_obj = ZoneInfo(tz_from)
        tz_to_obj = ZoneInfo(tz_to)
    except Exception as e:
        print("Ошибка в названии поясов:", e)
        return
    try:
        naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Неверный формат даты.")
        return
    aware_dt = naive_dt.replace(tzinfo=tz_from_obj)
    converted = aware_dt.astimezone(tz_to_obj)
    print("Преобразованное время:", converted.strftime("%Y-%m-%d %H:%M (%Z)"))


# 5. Таймер обратного отсчёта
def countdown_timer():
    target_str = input("Введите будущую дату и время (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
    try:
        target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Неверный формат.")
        return
    print("Нажмите Ctrl+C для остановки.")
    try:
        while True:
            now = datetime.now()
            diff = target - now
            if diff.total_seconds() <= 0:
                print("\nВремя вышло!")
                break
            # очищаем строку и печатаем
            remaining = str(diff).split(".")[0]  # убираем микросекунды
            sys.stdout.write(f"\rОсталось: {remaining}   ")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nТаймер остановлен.")


# 6. Валидатор email
def email_validator():
    email = input("Введите email: ").strip()
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    if re.fullmatch(pattern, email):
        print("Email выглядит корректно.")
    else:
        print("Неверный формат email.")


# 7. Форматирование номера телефона
def phone_formatter():
    raw = input("Введите номер (только цифры, пробелы или символы): ")
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print("Форматированный номер:", formatted)
    else:
        print("Ожидалось 10 цифр, найдено", len(digits))


# 8. Проверка надёжности пароля
def password_strength_checker():
    pwd = input("Введите пароль: ")
    length_ok = len(pwd) >= 8
    upper_ok = bool(re.search(r"[A-Z]", pwd))
    lower_ok = bool(re.search(r"[a-z]", pwd))
    digit_ok = bool(re.search(r"\d", pwd))
    special_ok = bool(re.search(r"[^\w\s]", pwd))
    score = sum([length_ok, upper_ok, lower_ok, digit_ok, special_ok])

    messages = {
        5: "Очень надёжный пароль 💪",
        4: "Хороший пароль 👍",
        3: "Средний пароль 😐",
        2: "Слабый пароль ⚠️",
        1: "Очень слабый пароль ❌",
        0: "Пароль пустой или не соответствует критериям ❌",
    }
    print(messages[score])


# 9. Поиск слова в тексте
def word_finder():
    text = input("Введите текст для поиска: ")
    word = input("Какое слово ищем? ").strip()
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    matches = list(pattern.finditer(text))
    if matches:
        print(f"Найдено {len(matches)} совпадений:")
        for m in matches:
            start, end = m.span()
            snippet = text[max(0, start - 10):min(len(text), end + 10)]
            print(f"  Позиция {start}-{end}: …{snippet}…")
    else:
        print("Совпадений не найдено.")


# 10. Извлечение дат из текста
def date_extractor():
    text = input("Введите текст: ")
    # поддерживаем несколько популярных форматов
    patterns = [
        r"\b\d{4}-\d{2}-\d{2}\b",        # 2025-06-25
        r"\b\d{2}/\d{2}/\d{4}\b",        # 25/06/2025
        r"\b\d{1,2}\.\d{1,2}\.\d{4}\b",  # 25.06.2025
    ]
    dates = []
    for pat in patterns:
        dates.extend(re.findall(pat, text))
    if dates:
        print("Найденные даты:", ", ".join(dates))
    else:
        print("Дат не обнаружено.")


# ──────────────────────────────────────────────────────────────────────────────
# Главное меню
functions = {
    "1": ("Калькулятор возраста", age_calculator),
    "2": ("Дни до следующего дня рождения", days_until_next_birthday),
    "3": ("Планировщик встречи", meeting_scheduler),
    "4": ("Конвертер часовых поясов", timezone_converter),
    "5": ("Таймер обратного отсчёта", countdown_timer),
    "6": ("Валидатор email", email_validator),
    "7": ("Форматирование номера телефона", phone_formatter),
    "8": ("Проверка надёжности пароля", password_strength_checker),
    "9": ("Поиск слова в тексте", word_finder),
    "10": ("Извлечение дат из текста", date_extractor),
}

def main():
    while True:
        print("\nВыберите задание:")
        for k, (title, _) in functions.items():
            print(f"  {k}. {title}")
        print("  0. Выход")

        choice = input("Ваш выбор: ").strip()
        if choice == "0":
            print("До свидания!")
            break
        elif choice in functions:
            print(f"\n--- {functions[choice][0]} ---")
            functions[choice][1]()
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
