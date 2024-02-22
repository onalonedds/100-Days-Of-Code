chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
         '8', '9', '!', '?', '#', '$', '%', '&', '(', ')', '*', '+',
         ' ', ',', '.', ':', ';']

def caesar_cipher(action, shift, message):
    match action:
        case "e":
            encoded_message = []
            for letter in message:
                index = chars.index(letter) + shift
                encoded_message.append(chars[index])
            return ''.join(encoded_message)
        case "d":
            decoded_message = []
            for letter in message:
                index = chars.index(letter) - shift
                decoded_message.append(chars[index])
            return ''.join(decoded_message)

ui_action = ""
ui_shift = ""
ui_message = ""

while ui_action != "e" and ui_action != "d":
    ui_action = input("Type 'e' to encode, 'd' to decode: ")

while not ui_shift.isnumeric():
    ui_shift = input("Enter a valid number for shift: ")

while len(ui_message) == 0:
    ui_message = input("Type your message: ")

result = caesar_cipher(ui_action, int(ui_shift), ui_message)
print(f"Result: {result}")

