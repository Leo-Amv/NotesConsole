from funcs import *


def start():
    print('\t---This is note app!---')
    cmd_list()
    command = input('Enter command:')
    match str.upper(command):
        case 'ADD':
            create()
        case 'UPDATE':
            print('foo')
        case 'LIST':
            print('foo')
        case 'DELETE':
            print('foo')
        case 'FIND':
            print('foo')
        case 'HELP':
            cmd_list()
        case 'EXIT':
            exit()
        case _:
            print('Command not found! Try again!')
            start()
