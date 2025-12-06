from parser import parser, Node
import os

# List all .wmu files
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
            choice = int(input("\nEnter the number of the test file to parse: "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            else:
                print("Invalid choice. Enter a valid number.")
        except ValueError:
            print("Please enter a number.")

# Level-order traversal for AST output
def level_order(root: Node):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        next_q = []
        level_vals = []

        for node in queue:
            level_vals.append(str(node.value))
            for child in node.children:
                next_q.append(child)

        result.append(level_vals)
        queue = next_q

    return result

def print_ast_level_order(root: Node):
    levels = level_order(root)
    print("\n--- AST Level-Order Traversal ---\n")
    for level in levels:
        print(" # ".join(level))
        print()

if __name__ == "__main__":
    filename = choose_file()

    print(f"\n--- Running Parser on: {filename} ---\n")

    with open(filename, "r") as f:
        data = f.read()

    ast = parser.parse(data)

    if ast is None:
        print("Parsing failed: AST is None\n")
    else:
        print_ast_level_order(ast)
