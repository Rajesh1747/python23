def get_name_and_age():
    """
    This function takes user input for name and age and prints them.

    :return: None
    """
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")

    print(f"Your name is {name} and you are {age} years old.")

if __name__ == "__main__":
    get_name_and_age()
