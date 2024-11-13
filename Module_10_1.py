import threading
from time import sleep, perf_counter

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time = perf_counter()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time = perf_counter()
print(f"Работа функций {end_time - start_time:.6f} секунд")

start_time = perf_counter()

threads = [
    threading.Thread(target=write_words, args=(10, "example5.txt")),
    threading.Thread(target=write_words, args=(30, "example6.txt")),
    threading.Thread(target=write_words, args=(200, "example7.txt")),
    threading.Thread(target=write_words, args=(100, "example8.txt")),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = perf_counter()
print(f"Работа потоков {end_time - start_time:.6f} секунд")