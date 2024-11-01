import base64

def get_capital_letters(input_file):
    # Open the input file in read mode
    with open(input_file, 'r') as infile:
        # Read the file content
        content = infile.read()
    
    # Filter only the capital letters
    capital_letters = ''.join([char for char in content if char.isupper()])

    # Return the string of capital letters
    return capital_letters

def binary_to_base64(binary_string):
    # Step 1: Split binary string into 8-bit chunks and convert to bytes
    byte_data = bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

    # Step 2: Encode the byte data to Base64
    base64_encoded = base64.b64encode(byte_data)

    # Return the Base64 encoded string
    return base64_encoded.decode('utf-8')

def base64_to_ascii(base64_string):
    # Step 1: Decode the Base64 string to bytes
    byte_data = base64.b64decode(base64_string)

    # Step 2: Convert bytes to ASCII string (if the bytes are valid ASCII)
    ascii_string = byte_data.decode('ascii', errors='ignore')  # Ignore non-ASCII characters

    return ascii_string

capital = get_capital_letters("challenge.txt")

app = capital.replace("ZERO", "0")
binary = app.replace("ONE", "1")

base64_string = binary_to_base64(binary)

ascii_string = base64_to_ascii(base64_string)

print(ascii_string)