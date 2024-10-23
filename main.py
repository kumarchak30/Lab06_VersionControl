def encode(password):
    encoded_password = ""
    for char in password:
        new_char = str((int(char) + 3) % 10)  # Shifts each digit by 3 and wraps around if > 9
        encoded_password += new_char
    return encoded_password

def decode(password):
    decoded_password = ""
    for char in password:
        new_char = str((int(char) - 3) % 10)  # shifts each digit by subtracting 3
        decoded_password += new_char
    return decoded_password


def main():
    encoded_password = ""

    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            if encoded_password:
                print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}")
            else:
                print("No password encoded yet!")

        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == '__main__':
    main()