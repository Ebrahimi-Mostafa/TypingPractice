import random
# for print colorful text
import colorama

# Unicode CHECK MARK symbol
CHECK_MARK = "\u2713"

# Reset color after each print
colorama.init(autoreset=True)

NUMBERS = '1234567890'
SIGNS = '!@#$%^&*()-=_+`~[]{}|:;<>,./?"\\\''

def get_custom_char_set():
    print(colorama.Fore.BLUE + "Type 'finish' if you don't want to add new characters")
    custom_set = []

    while True:
        char_input = input()

        if char_input == "finish":
            if not custom_set:
                print(f"{colorama.Fore.RED}You must enter at least one character before finishing.")
                continue
            break
        elif not char_input:
            print(f"{colorama.Fore.RED}Oops! It looks like you didn't enter any characters. Please provide at least one character.")
            continue

        custom_set.append(char_input)
        print(colorama.Fore.BLUE + str(custom_set))

    print(colorama.Fore.YELLOW + '\nYou chose ' + str(custom_set))
    return custom_set

def get_size_of_output():
    print(colorama.Fore.CYAN + "Enter the size of random word:")
    size = int(input())
    while size <= 0:
        print(colorama.Fore.RED + "Size must be a positive integer.")
        size = int(input())
    return size

def choose_practice_set():
    print("Choose one of the options below:")
    print(colorama.Fore.CYAN + "\t0. Numbers\n\t1. Signs\n\t2. Numbers + Signs\n\t3. Custom list\n\t4. Exit")

    menu_selection = int(input())
    practice_set = []

    if menu_selection == 0:
        practice_set = NUMBERS
    elif menu_selection == 1:
        practice_set = SIGNS
    elif menu_selection == 2:
        practice_set = NUMBERS + SIGNS
    elif menu_selection == 3:
        practice_set = get_custom_char_set()
    elif menu_selection == 4:
        exit()

    return practice_set

def menu_start():
    print(colorama.Fore.MAGENTA + "Welcome!")
    practice_set = choose_practice_set()

    size = get_size_of_output()

    print(f"For back to the menu, type {colorama.Fore.RED}'finish'\n")
    return practice_set, size

def generate_rand_string(input_set, size):
    chosen_element = random.choices(input_set, k=size)
    return ''.join(chosen_element)

def typing_practice_loop(practice_set, size):
    rand_string = generate_rand_string(practice_set, size)
    while True:
            print(rand_string)
            practice_input = input()

            if practice_input == 'finish':
                break
            elif practice_input == rand_string:
                print(f"{colorama.Fore.GREEN}{CHECK_MARK}")
                rand_string = generate_rand_string(practice_set, size)
            else:
                print(f"{colorama.Fore.RED}X")

def main():
    while True:
        practice_set, size = menu_start()
        typing_practice_loop(practice_set, size)
    
if __name__ == "__main__":
    main()
