import random

def generate_random_integers(n, min_val, max_val):
    # Generate a list of n random integers between min_val and max_val (inclusive)
    return [random.randint(min_val, max_val) for _ in range(n)]

def count_digits(numbers):
    # Create a dictionary to store the count of occurrences of each digit (0 to 9)
    count_dict = {i: numbers.count(i) for i in range(10)}
    return count_dict

def display_digit_counts(counts):
    # Print the number of occurrences for each digit in the count dictionary
    for digit, count in counts.items():
        print(f"Digit {digit}: {count} occurrences")

if __name__ == "__main__":
    # Generate a list of 1000 random integers between 0 and 9
    random_integers = generate_random_integers(1000, 0, 9)

    # Count the occurrences of each digit in the generated list
    digit_counts = count_digits(random_integers)

    # Display the counts for each digit
    display_digit_counts(digit_counts)
