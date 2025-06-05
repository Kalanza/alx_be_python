def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue

        if choice == 1:
            option = input('Enter the item to add: ')
            shopping_list.append(option)
        elif choice == 2:
            option = input('Type the item you want to remove: ')
            if option in shopping_list:
                shopping_list.remove(option)
            else:
                print(f"{option} is not in the shopping list.")
        elif choice == 3:
            print(shopping_list)
        elif choice == 4:
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again')


if __name__ == "__main__":
    main()