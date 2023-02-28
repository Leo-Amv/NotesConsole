from datetime import datetime
from logcsv import *


def cmd_list():
    print('Command list:\nADD\nUPDATE\nLIST\nDELETE\nFIND\nHELP\nEXIT')


def create():
    title = input('Header:')
    body = input('Enter note:')
    current_date = datetime.now()
    day = current_date.day
    month = current_date.month
    year = current_date.year
    date = str.format('{}.{}.{}'.format(day, month, year))
    time = str.format('{}:{}:{}'.format(datetime.now().hour,
                      datetime.now().minute, datetime.now().second))
    create_note(title, body, date, time)
    print('Note created!')


def update_success():
    print('Enter changes:')
    create()
    print('Note updated!')


def update_by_id():
    try:
        find_id = int(input('Enter id: '))
        key = delete_note_by_id(find_id)
        if key == 1:
            update_success()
    except ValueError:
        print('Incorrect id, try again!')
        update_by_id()


def delete_by_id():
    try:
        find_id = int(input('Enter id: '))
        key = delete_note_by_id(find_id)
        if key == 1:
            print('Note deleted!')
    except ValueError:
        print('Incorrect id, try again!')
        delete_by_id()


def find_by_id():
    try:
        find_id = int(input('Enter id: '))
        flag = find_note_by_id(find_id)
        if flag == 1:
            print('--DONE--')
    except ValueError:
        print('Incorrect id, try again!')
        find_by_id()


def list_notes():
    print('Show all notes: \n')
    list_all_notes()


def date_note():
    print('Enter date to find note: ')
    try:
        day = int(input('Day: '))
        month = int(input('Month: '))
        year = int(input('Day: '))
        print('Founded notes: ')
        find_notes_by_date(day, month, year)
    except ValueError:
        print('Incorrect date, try again!')
        date_note()
