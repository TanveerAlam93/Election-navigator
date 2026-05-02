import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data(filename):
    """Reads content from the specified txt file in the data folder."""
    try:
        path = os.path.join("data", filename)
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: Data file not found."

def main_menu():
    while True:
        clear_screen()
        print("========================================")
        print("   🗳️  ELECTION GUIDE ASSISTANT 🗳️   ")
        print("========================================")
        print("1. United States Election Process")
        print("2. India Election Process")
        print("3. United Kingdom Election Process")
        print("4. Election Glossary (Jargon Buster)")
        print("5. Exit")
        print("========================================")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            clear_screen()
            print(load_data("usa.txt"))
            input("\nPress Enter to return to menu...")
        elif choice == '2':
            clear_screen()
            print(load_data("india.txt"))
            input("\nPress Enter to return to menu...")
        elif choice == '3':
            clear_screen()
            print(load_data("uk.txt"))
            input("\nPress Enter to return to menu...")
        elif choice == '4':
            clear_screen()
            print("--- ELECTION GLOSSARY ---")
            print(load_data("glossary.txt"))
            input("\nPress Enter to return to menu...")
        elif choice == '5':
            print("Thank you for using the Election Guide. Go vote!")
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Created /data folder. Please add your .txt files there.")
    
    main_menu()