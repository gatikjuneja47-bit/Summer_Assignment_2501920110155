print("The Morse Code Translator")
english_alphabet = [chr(i) for i in range(97, 123)] + ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']
def english_to_morse(text):
    text = text.lower()
    morse_text = ""
    for char in text:
        if char in english_alphabet:
            index = english_alphabet.index(char)
            morse_text += morse_code[index] + " "
        else:
            morse_text += char + " "
    return morse_text.strip()
def morse_to_english(morse):
    morse_list = morse.split()
    english_text = ""
    for code in morse_list:
        if code in morse_code:
            index = morse_code.index(code)
            english_text += english_alphabet[index]
        else:
            english_text += " "
    return english_text.strip()
while True:
    print("1. English to Morse Code")
    print("2. Morse Code to English")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        text = input("Enter English text: ")
        morse = english_to_morse(text)
        print(f"Morse Code: {morse}")
    elif choice == '2':
        morse = input("Enter Morse code: ")
        english = morse_to_english(morse)
        print(f"English Text: {english}")
    elif choice == '3':
        print("Exiting the translator")
        print("Thank you")
        break
    else:
        print("Invalid choice")