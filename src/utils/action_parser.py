def parse_actions(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split('\n')
                # Filter out empty strings
            words = [word for word in words if word.strip()]
            return words
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def append_action(file_path, new_word):
    try:
        with open(file_path, 'a') as file:
            file.write(new_word + '\n')
        print(f"Appended '{new_word}' to '{file_path}'.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Cannot append.")

