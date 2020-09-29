def get_fibonacci_sequence(count):
    sequence = [1,1]
    for i in range(count-2):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence

fib = get_fibonacci_sequence(10)
print(fib)
