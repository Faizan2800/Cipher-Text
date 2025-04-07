import string
import art 
print(art.text2art("Cipher Text"))

alphabet = list(string.ascii_letters + string.digits + string.punctuation + " ")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1  # Reverse the shift for decoding
    for letter in original_text:
        if letter not in alphabet:  # Leave characters not in alphabet (like spaces)
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Main loop for encoding/decoding
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")  # Keep the original input (preserving case and symbols)
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":  # Use comparison operator
        should_continue = False
        print("Goodbye for now!")
