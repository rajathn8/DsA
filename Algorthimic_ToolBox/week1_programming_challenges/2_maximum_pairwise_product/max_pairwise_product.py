# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    numbers.sort()

    left = numbers[0] * numbers[1]
    right = numbers[-1] * numbers[-2]

    if left<right:
        max_product = right
    else:
        max_product = left


    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
