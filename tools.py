# No error conversion to Int
def to_int(user_input):
    try:
        int(user_input)  # Attempt to convert to int
        return int(user_input)
    except ValueError:
        return 0


def to_float(user_input):
    try:
        float(user_input)  # Attempt to convert to float
        return float(user_input)
    except ValueError:
        return 0