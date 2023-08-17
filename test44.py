

# generates a multiplication table for a given number:


def multiplication_table(number, limit):
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    try:
        number = int(input("Enter a number: "))
        limit = int(input("Enter the limit: "))
        multiplication_table(number, limit)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
