import random
import colorama # for print colorful text


colorama.init(autoreset=True) #for reset color of text in terminal after each print


NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SIGNS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+','`', '~', '[', ']', '{', '}', '|', ':', ';', '<', '>', ',', '.', '/', '?', '"', '\\', "'"]


def menu_start():
    char_list = []
    print(colorama.Fore.MAGENTA + "welcome\nchoose one of the options below:") ## print welcome message
    print(colorama.Fore.CYAN + "\t0.numbers\n\t1.signs\n\t2.both of them\n\t3.custom list\n\t4.exit") ## print menu options
    menu_selection = int(input())

    if menu_selection == 0:
        char_list = NUMBERS
    elif menu_selection == 1:
        char_list = SIGNS
    elif menu_selection == 2: 
        char_list = NUMBERS + SIGNS
    elif menu_selection == 3:
        print(colorama.Fore.BLUE + "type finish, if you don't want add new char")
        char_list = []
        while(True):
            char_input = input()
            if char_input == "finish":
                break
            char_list.append(char_input)
            print(colorama.Fore.BLUE + str(char_list))
        print(colorama.Fore.YELLOW + '\nyou chose ' + str(char_list))
    elif menu_selection == 4:
        exit()

    print(f"for back to menu, type {colorama.Fore.RED}finish\n")
    return char_list

def main():
    while True:
        char_list = menu_start()
        rand_char = random.choice(char_list)
        while True:
            print(rand_char)
            data = input()
            if data == 'finish':
                break
            elif data == rand_char:
                print('\033[5;32m\u2713 \033[0;0m')
                rand_char = random.choice(char_list)
            else:
                print('\033[5;91mX \033[0;0m')


if __name__ == "__main__":
    main()