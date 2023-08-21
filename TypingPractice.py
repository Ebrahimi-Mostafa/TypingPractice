import random
import colorama # for print colorful text


colorama.init(autoreset=True) #for reset color of text in terminal after each print


NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SIGNS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+','`', '~', '[', ']', '{', '}', '|', ':', ';', '<', '>', ',', '.', '/', '?', '"', '\\', "'"]


def menu_start():
    practice_set = []
    print(colorama.Fore.MAGENTA + "welcome\nchoose one of the options below:") ## print welcome message
    print(colorama.Fore.CYAN + "\t0.numbers\n\t1.signs\n\t2.both of them\n\t3.custom list\n\t4.exit") ## print menu options
    menu_selection = int(input())

    if menu_selection == 0:
        practice_set = NUMBERS
    elif menu_selection == 1:
        practice_set = SIGNS
    elif menu_selection == 2: 
        practice_set = NUMBERS + SIGNS
    elif menu_selection == 3:
        print(colorama.Fore.BLUE + "type finish, if you don't want add new char")
        practice_set = []
        while(True):
            char_input = input()
            if char_input == "finish":
                break
            practice_set.append(char_input)
            print(colorama.Fore.BLUE + str(practice_set))
        print(colorama.Fore.YELLOW + '\nyou chose ' + str(practice_set))
    elif menu_selection == 4:
        exit()

    print(f"for back to menu, type {colorama.Fore.RED}finish\n")
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
                print('\033[5;32m\u2713 \033[0;0m')
                rand_char = random.choice(practice_set)
            else:
                print('\033[5;91mX \033[0;0m')


if __name__ == "__main__":
    main()