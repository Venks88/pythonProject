import requests

class some:
    def count_up_to(n):
        i = 1
        while i <= n:
            i += 1
            return i

    # Create a generator
    counter = count_up_to(5)

    # Iterate over the values
    for number in counter:
        print(number)
