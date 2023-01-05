"""
Written by Nahom Atnafu
Date by 1/5/2023

"""


def count_letter(texts):
    """
    This function takes in a text as a parameter
    and counts the occurrence of each letter in it.
    """
    dict = {}
    for text in texts:
        dict[text] = texts.count(text)

    for key, value in dict.items():
        print(f"{key} = {value}")


if __name__ == '__main__':
    user_input = input('Enter a text: ')
    count_letter(user_input)
