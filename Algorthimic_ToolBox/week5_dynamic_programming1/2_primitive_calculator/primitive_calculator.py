# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def prim_calculator(n):
    count_of_operation = [0] * (n + 1)

    count_of_operation[1] = 1
    for i in range(2, n + 1):
        count_index = [i - 1]
        if i % 2 == 0:
            count_index.append(i // 2)
        if i % 3 == 0:
            count_index.append(i // 3)

        min_count = min([count_of_operation[x] for x in count_index])
        count_of_operation[i] = min_count + 1

    current_value = n
    value_trail = [current_value]
    while current_value != 1:
        list_of_options = [current_value - 1]
        if current_value % 2 == 0:
            list_of_options.append(current_value // 2)
        if current_value % 3 == 0:
            list_of_options.append(current_value // 3)

        current_value = min(
            [(c, count_of_operation[c]) for c in list_of_options],
            key=lambda x: x[1]
        )[0]
        value_trail.append(current_value)
    return reversed(value_trail)


input = sys.stdin.read()
n = int(input)
sequence = list(prim_calculator(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')