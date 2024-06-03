def count_character_in_file(file_name, char):
    try:
        with open(file_name, 'r') as file:
            text = file.read()

        # Count the occurrences of the character
        char_count = text.count(char)
        print(f"The character '{char}' appears {char_count} times in the file.")

        # Split the text into sentences
        sentences = text.split('.')

        # Display sentences that start with an uppercase letter
        print("Sentences starting with an uppercase alphabet:")
        for sentence in sentences:
            stripped_sentence = sentence.strip()
            if stripped_sentence and stripped_sentence[0].isupper():
                print(stripped_sentence + '.')

    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get file name and character from user
file_name = input("Enter the file name: ")
char = input("Enter the character to count: ")

# Validate character input
if len(char) != 1:
    print("Please enter a single character.")
else:
    count_character_in_file(file_name, char)
