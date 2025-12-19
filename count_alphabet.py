import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

#FUNGSI REKURSIF
def count_alpha_recursive(text, idx=0):
    if idx == len(text):
        return 0
    # cek apakah text[idx] alphabet
    current = 1 if text[idx].isalpha() else 0
    return current + count_alpha_recursive(text, idx + 1)

# FUNGSI ITERATIF
def count_alpha_iterative(text):
    count = 0
    for ch in text:
        if ch.isalpha():
            count += 1
    return count

# VARIABEL UNTUK GRAFIK
input_lengths = []
recursive_times = []
iterative_times = []

# FUNGSI UPDATE GRAFIK
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(input_lengths, recursive_times, label='Recursive', marker='o', linestyle='-')
    plt.plot(input_lengths, iterative_times, label='Iterative', marker='o', linestyle='-')
    plt.title('Performance Comparison: Recursive vs Iterative\nCounting Alphabet in a Sentence')
    plt.xlabel('Length of Input String')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Length", "Recursive Time (s)", "Iterative Time (s)"]
    min_len = min(len(input_lengths), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([input_lengths[i], recursive_times[i], iterative_times[i]])
    print(table)

# PROGRAM UTAMA
while True:
    try:
        kalimat = input("Masukkan kalimat (atau ketik EXIT untuk keluar): ")

        if kalimat.lower() == "exit":
            print("Program selesai. Terima kasih!")
            break

        n = len(kalimat)
        input_lengths.append(n)

        # Waktu Rekursif
        start_time = time.time()
        count_alpha_recursive(kalimat)
        recursive_times.append(time.time() - start_time)

        # Waktu Iteratif
        start_time = time.time()
        count_alpha_iterative(kalimat)
        iterative_times.append(time.time() - start_time)

        # Cetak tabel
        print_execution_table()

        # Tampilkan grafik
        update_graph()

    except ValueError:
        print("Input tidak valid!")

# RESET BUTTON
input_lengths = []
recursive_times = []
iterative_times = []
from IPython.display import clear_output
clear_output(wait=True)
print("Data telah direset!")
