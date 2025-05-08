class Phonebook:
    def __init__(self):
        self.phonebook = {
            "Amal": "1111111111",
            "Mohammed": "2222222222",
            "Khadijah": "3333333333",
            "Abdullah": "4444444444",
            "Rawan": "5555555555",
            "Faisal": "6666666666",
            "Layla": "7777777777"
        }

    def is_valid_number(self, number):
        return len(number) == 10 and number.isdigit()

    def search_by_number(self, number):
        if not self.is_valid_number(number):
            raise ValueError("This is invalid number")

        for name, phone in self.phonebook.items():
            if phone == number:
                return f"The owner of the number is {name}"

        return "Sorry, the number is not found"

    def search_by_name(self, name):
        name = name.strip().capitalize()
        if name in self.phonebook:
            return f"{name}'s number is {self.phonebook[name]}"
        return f"Sorry, {name} is not in the phonebook"

    def add_contact(self, name, number):
        if not self.is_valid_number(number):
            raise ValueError("This is invalid number")

        if name in self.phonebook:
            raise ValueError(f"{name} is already in the phonebook")

        self.phonebook[name] = number
        return f"{name} has been added to the phonebook."


def main():
    phonebook = Phonebook()

    while True:
        print("\nPhonebook Menu:")
        print("1. Search by number")
        print("2. Search by name")
        print("3. Add new contact")
        print("4. Exit")

        choice = input("Please select an option (1/2/3/4): ")

        if choice == '1':
            number = input("Enter a phone number to search: ")
            try:
                print(phonebook.search_by_number(number))
            except ValueError as e:
                print(e)

        elif choice == '2':
            name = input("Enter a name to search: ")
            print(phonebook.search_by_name(name))

        elif choice == '3':
            add_name = input("Enter the name of the person you want to add: ")
            add_number = input("Enter the phone number of the person: ")
            try:
                print(phonebook.add_contact(add_name, add_number))
            except ValueError as e:
                print(e)

        elif choice == '4':
            print("Exiting phonebook...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()