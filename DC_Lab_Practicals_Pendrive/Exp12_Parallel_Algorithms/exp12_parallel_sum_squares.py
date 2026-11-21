import multiprocessing


def sum_of_squares(numbers, result, index):
    result[index] = sum(x * x for x in numbers)


def parallel_sum_of_squares(numbers, num_processes):
    num_processes = max(1, min(num_processes, len(numbers)))
    chunk_size = len(numbers) // num_processes
    chunks = [
        numbers[i * chunk_size:(i + 1) * chunk_size]
        for i in range(num_processes)
    ]

    if len(numbers) % num_processes != 0:
        chunks[-1].extend(numbers[num_processes * chunk_size:])

    result = multiprocessing.Array("q", num_processes)
    processes = []

    for i in range(num_processes):
        p = multiprocessing.Process(
            target=sum_of_squares, args=(chunks[i], result, i)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return sum(result)


if __name__ == "__main__":
    n = int(input("How many numbers? "))
    numbers = list(range(1, n + 1))
    num_processes = min(multiprocessing.cpu_count(), max(1, n))
    total = parallel_sum_of_squares(numbers, num_processes)
    print("The sum of squares is:", total)
