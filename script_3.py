try:
    with open("count", "r") as file:
        numbers = [float(line.strip()) for line in file]

    if numbers:
        largest_number = max(numbers)
        print(f"The largest number is: {largest_number}")
    else:
        print("The file 'count' is empty.")

except FileNotFoundError:
    print("Error: The file 'count' does not exist.")
except ValueError:
    print("Error: The file 'count' contains invalid numerical values.")
except Exception as e:
    print(f"An error occurred: {e}")

