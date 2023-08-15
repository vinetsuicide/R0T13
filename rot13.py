def enc0de_sh1t(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            offset = ord('a')
            result += chr((ord(char) - offset + 13) % 26 + offset)
        elif 'A' <= char <= 'Z':
            offset = ord('A')
            result += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            result += char
    return result


def dec0d3_sh1t(text):
    return enc0de_sh1t(text)  # reverse


##################################################################


while True:
    option = input("Choose an option Encode/Decode(e/d): ").lower()

    if option == "e":
        input_text = input("Enter the text to encode: ")
        encoded_text = enc0de_sh1t(input_text)
        print("Encoded text:", encoded_text)
        break
    elif option == "d":
        input_text = input("Enter the text to decode: ")
        decoded_text = dec0d3_sh1t(input_text)
        print("Decoded text:", decoded_text)
        break
    else:
        print("Invalid option. Please choose either 'encode' or 'decode'.")
