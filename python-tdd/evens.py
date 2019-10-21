def even_number_of_evens(numbers):
    countEven = 0
    if len(numbers) > 0:
        for number in numbers:
            if number % 2 == 0:
                countEven += 1
        if countEven == 0:
            return False
        if countEven % 2 == 0:
            return True
    return False


assert even_number_of_evens([]) is False, "No numbers"
assert even_number_of_evens([2]) is False, "One even number"
assert even_number_of_evens([2, 4]) is True, "Two even numbers"
assert even_number_of_evens([2, 3]) is False, "Two numbers, only one even number"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) is False, "Multiple numbers, three even numbers"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) is True, "Multiple numbers, four even numbers"
assert even_number_of_evens([1, 3, 9]) is False, "No even numbers"

print("All tests passed!")
