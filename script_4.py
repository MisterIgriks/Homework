my_list = ["banana", "orange", "grape", "apple", "kiwi"]

fruit_to_check = input("Enter fruit to check: ")

if fruit_to_check in my_list:
    print(f'Yes, the element "{fruit_to_check}" exists.')
else:
    print(f'No, the element "{fruit_to_check}" does not exist.')

