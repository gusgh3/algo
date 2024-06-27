def solution(numbers):
    answer = 0

    answer = sum(numbers) / len(numbers)

    total = 0
    i = 0

    for number in numbers:
        total += number
        i += 1

    answer = total / i
    
    return answer


    solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])