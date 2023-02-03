def is_string_length_valid(string):
    length = len(string)
    least = 4
    most = 25

    if least <= length <= most:
        return True


def is_characters_valid(string):
    if string.isalnum() or "_" in string:
        return True


def username_validation(string):
    if is_string_length_valid(string) and string[0].isalpha() and is_characters_valid(string) and string[-1] != "_":
        return True
    else:
        return False


print(username_validation(input()))
