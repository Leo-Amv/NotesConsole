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
