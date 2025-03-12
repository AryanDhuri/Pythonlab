def fibonacci_sequence(j):
    sequence = [0, 1]
    for i in range(2, j):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def main():
    n = int(input("Enter a number: "))
    print(fibonacci_sequence(n))

main()