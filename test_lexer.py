from lexer import lexer
import os

# List all .wmu test files in the current directory
def list_test_files():
    files = [f for f in os.listdir('.') if f.endswith('.wmu')]
    return sorted(files)

def choose_file():
    files = list_test_files()
    if not files:
        print("No .wmu test files found in this directory.")
        exit()

    print("\nAvailable Test Files:")
    for i, f in enumerate(files, start=1):
        print(f"{i}. {f}")

    while True:
        try:
            choice = int(input("\nEnter the number of the test file to run: "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            else:
                print("Invalid choice. Enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def print_tokens(filename: str):
    print(f"\n--- Running Lexer on: {filename} ---\n")

    with open(filename, "r") as f:
        data = f.read()

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"({tok.type}, {tok.value})")

if __name__ == "__main__":
    filename = choose_file()
    print_tokens(filename)
