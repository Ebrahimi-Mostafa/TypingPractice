import random
# for print colorful text
import colorama

# Unicode CHECK MARK symbol
CHECK_MARK = "\u2713"

# Initialize colorama for colorful text printing
colorama.init(autoreset=True)

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SIGNS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '`', '~', '[', ']', '{', '}', '|', ':', ';', '<', '>', ',', '.', '/', '?', '"', '\\', "'"]

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
        elif char_input == "":
            print(f"{colorama.Fore.RED}Oops! It looks like you didn't enter any characters. Please provide at least one character.")
            continue
        
        custom_set.append(char_input)
        print(colorama.Fore.BLUE + str(custom_set))
    
    print(colorama.Fore.YELLOW + '\nYou chose ' + str(custom_set))
    return custom_set

def menu_start():
    print(colorama.Fore.MAGENTA + "Welcome!\nChoose one of the options below:")
    print(colorama.Fore.CYAN + "\t0. Numbers\n\t1. Signs\n\t2. Both of them\n\t3. Custom list\n\t4. Exit")
    
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

    print(f"For back to the menu, type {colorama.Fore.RED}'finish'\n")
    return practice_set

def main():
    while True:
        practice_set = menu_start()
        rand_char = random.choice(practice_set)
        
        while True:
            print(rand_char)
            practice_input = input()
            
            if practice_input == 'finish':
                break
            elif practice_input == rand_char:
                print(f"{colorama.Fore.GREEN}{CHECK_MARK}")
                rand_char = random.choice(practice_set)
            else:
                print(f"{colorama.Fore.RED}X")

if __name__ == "__main__":
    main()
