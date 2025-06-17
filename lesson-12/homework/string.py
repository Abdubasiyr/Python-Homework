import threading

# Проверка на простое число
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Потоковая функция
def check_primes_in_range(start, end, result):
    primes = [n for n in range(start, end) if is_prime(n)]
    result.extend(primes)

# Основной код
def threaded_prime_checker(start_range, end_range, num_threads=4):
    threads = []
    result = []
    step = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i < num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes_in_range, args=(start, end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Prime numbers found:", sorted(result))

# Пример запуска
threaded_prime_checker(1, 100, num_threads=4)

import threading
from collections import Counter

# Потоковая функция
def count_words(lines, result_list):
    counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        counter.update(words)
    result_list.append(counter)

# Основной код
def threaded_word_count(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words, args=(lines[start:end], results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Объединяем результаты
    final_result = Counter()
    for counter in results:
        final_result.update(counter)

    # Печать слов и количества
    for word, count in final_result.most_common():
        print(f"{word}: {count}")

# Пример запуска
# Убедись, что есть файл large_text.txt в той же папке
# threaded_word_count("large_text.txt", num_threads=4)
