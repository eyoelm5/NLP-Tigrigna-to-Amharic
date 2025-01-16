from pre_processing import text_pre_processing
from g2p import grapheme_to_phoneme
from overlap import shared_values
from comparison import compared_values

def clear_screen():
    print("\033[2J\033[H\n", end="", flush=True)

def prompt_continue():
    input("Press Enter to continue...")

def sampleText(choice):
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        else:
            print("Invalid choice. Please select a valid option.")
            clear_screen()

def get_user_input():
    clear_screen()
    print("Do you want to use sample inputs or enter your own?")
    print("\tPress 1 to test by using sample inputs")
    print("\tPress 2 to enter your own text")
    choice = input("\tYour Choice: ")
    if(choice == "1"):
        clear_screen()
        print("\nAvailable parallel texts:")
        print("\tPress 1 for parallel text 1")
        print("\tPress 2 for parallel text 2")
        choice2 = input("\tChoose an option: ")
        return sampleText(choice2), None
    elif(choice == "2"):
        print("\n!!!! Please paste your input as a single line and press enter after each input")
        amharic_file = input("\tEnter the plain Amharic text: ")
        tigrigna_file = input("\tEnter the plain Tigrigna text: ") 
        clear_screen()
        return None, (amharic_file, tigrigna_file)
    else:
        print("Invalid choice. Please select a valid option.")
        exit()


def main():
    parallel_text_number, custom_files = get_user_input()
    text_pre_processing(parallel_text_number, custom_files)
    prompt_continue()
    grapheme_to_phoneme()
    prompt_continue()
    shared_values()
    prompt_continue()
    print(compared_values())


if __name__ == '__main__':
    main()
