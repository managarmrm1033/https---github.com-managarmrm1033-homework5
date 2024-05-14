def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid command."
        except ValueError:
            return "Enter a valid input."
        except IndexError:
            return "Command requires additional arguments."

    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Enter a name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args, contacts):
    if len(args) != 1:
        return "Enter a name."
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def delete_contact(args, contacts):
    if len(args) != 1:
        return "Enter a name."
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "Contact deleted."
    else:
        return "Contact not found."

@input_error
def list_contacts(args, contacts):
    if args:
        return "Command does not require arguments."
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "add":
            args = input("Enter the argument for the command: ").strip().split()
            print(add_contact(args, contacts))
        elif command == "get":
            args = input("Enter the argument for the command: ").strip().split()
            print(get_contact(args, contacts))
        elif command == "delete":
            args = input("Enter the argument for the command: ").strip().split()
            print(delete_contact(args, contacts))
        elif command == "list":
            args = input("Enter the argument for the command: ").strip().split()
            print(list_contacts(args, contacts))
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
