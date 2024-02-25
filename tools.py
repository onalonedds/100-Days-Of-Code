# No error conversion to Int
def nect_int(user_input):
    """Converts input to Int with no error for Str"""
    if not user_input.isnumeric():
        return 0
    else:
        return int(user_input)