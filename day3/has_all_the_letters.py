import string


def has_all_the_letters(text: str) -> bool:
    for letter in string.ascii_lowercase:
        if letter not in text:
            return False
    return True


def has_all_the_letters_dont_do_this(text: str) -> bool:
    for letter in string.ascii_lowercase:
        if letter not in set(text):
            return False
    return True


def has_all_the_letters_faster_and_easy(text: str) -> bool:
    existing_letters = set(text)

    for letter in string.ascii_lowercase:
        if letter not in existing_letters:
            return False

    return True


def has_all_the_letters_faster(text: str) -> bool:
    index_array = [0] * 26
    for letter in text:
        index_array[ord(letter) - ord('a')] = 1

    for letter in string.ascii_lowercase:
        if index_array[(ord(letter) - ord('a'))] == 0:
            return False
    return True


print(has_all_the_letters("hello"))
print(has_all_the_letters("abcdefghijklmnopqrsrtquvwxyz"))

print(has_all_the_letters_faster("hello"))
print(has_all_the_letters_faster("abcdefghijklmnopqrsrtquvwxyz"))
