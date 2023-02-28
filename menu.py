from funcs import *


def start():
    print('\t---This is note app!---')
    cmd_list()
    flag = True
    while (flag):
        command = input('Enter command:')
        match str.upper(command):
            case 'ADD':
                create()
            case 'UPDATE':
                update_by_id()
            case 'LIST':
                list_notes()
            case 'DELETE':
                delete_by_id()
            case 'FIND':
                find_by_id()
            case 'HELP':
                cmd_list()
            case 'EXIT':
                flag = False
                exit()
            case _:
                print('Command not found! Try again!')
