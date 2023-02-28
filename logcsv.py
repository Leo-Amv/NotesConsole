from dataservice import *


def create_note(title, body, date, time):
    note_book_list = read_data()
    new_id = add_data(note_book_list, title, body, date, time)
    note_view(str(f'{new_id};{title};{body};{date};{time};\n'))


def delete_note_by_id(id):
    new_list_d = []
    note_data = read_data()
    flag = find_note_by_id(id)
    if flag == 1:
        for note in note_data:
            list_d = str.split(note, ';')
            if int(list_d[0]) == id:
                continue
            new_list_d.append(note)
        save_data(new_list_d)
        return 1
    else:
        return 0


def delete_note_by_keyword(keyword):
    try:
        flag = 0
        note_data = read_data()
        note = find_note_by_keyword(keyword)
        new_note_list = []
        if flag == 0:
            for line in note_data:
                if note in line:
                    flag = 1
                    continue
                new_note_list.append(line)
            save_data(new_note_list)
        return flag
    except TypeError:
        print('Try again,keyword incorrect')


def list_all_notes():
    note_data = read_data()
    for note in note_data:
        note_view(note)


def find_note_by_keyword(keyword):
    flag = 0
    note_data = read_data()
    if flag == 0:
        for note in note_data:
            if keyword in note:
                flag = 1
                note_view(note)
                return note
    if flag == 0:
        print(f'Note with keyword: "{keyword}" not found!')
    return None


def find_note_by_id(id):
    flag = 0
    list_i = []
    note_data = read_data()
    if flag == 0:
        for note in note_data:
            list_i = str.split(note, ';')
            if int(list_i[0]) == id:
                note_view(note)
                flag = 1
    if flag == 0:
        print(f'Note with "ID:{id}" not found!')
    return flag


def find_notes_by_date(day, month, year):
    list_a = []
    flag = 0
    note_data = read_data()
    date_str = str(f'{day}.{month}.{year}')
    if flag == 0:
        for note in note_data:
            list_a = str.split(note, ';')
            if list_a[3] == date_str:
                note_view(note)
                flag = 1
    if flag == 0:
        print(f'This date "{day}.{month}.{year}" not found!')
