from funcs import *


def start():
    print('\t---This is note app version 1.0!---')
    cmd_list()
    flag = True
    while (flag):
        command = input('Enter command:')
        match str.upper(command):
            case 'ADD':
                print("\033[H\033[J")
                create()
            case 'UPDATE':
                print("\033[H\033[J")
                update_by_id()
            case 'LIST':
                print("\033[H\033[J")
                list_notes()
            case 'DELETE':
                print("\033[H\033[J")
                delete_by_id()
            case 'FIND':
                print("\033[H\033[J")
                choise = 0
                while (choise < 1 or choise > 3):
                    choise = int(input(
                        'Enter number to choose:\n"1"\t to find by id\n"2"\t to find by keyword\n"3"\t to find by date\nChoose:\t'))
                    if choise == 1:
                        find_by_id()
                    elif choise == 2:
                        find_by_keyword()
                    elif choise == 3:
                        find_by_date()
                    else:
                        print('Incorrect data, try again!')
            case 'HELP':
                print("\033[H\033[J")
                cmd_list()
            case 'EXIT':
                flag = False
                exit()
            case _:
                print('Command not found! Try again!')
