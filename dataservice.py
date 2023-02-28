def read_data():
    note_list = []
    try:
        note_data = open("Notes.csv", "r", encoding="utf8")
        for line in note_data:
            note_list.append(line)
        note_data.close()
    except FileNotFoundError:
        pass
    return note_list


def save_data(new_list):
    new_data = open("Notes.csv", "w", encoding="utf8")
    for item in new_list:
        new_data.write(item)
    new_data.close()


def add_data(notes_list, title, body, date, time):
    notes_list_id = []
    temp_list = []
    max = 0
    with open("Notes.csv", "a+", encoding="utf8") as note_book:
        if notes_list != None:
            for item in notes_list:
                temp_list = list(item.split(';'))
                notes_list_id.append(int(temp_list[0]))
                temp_list.clear()
        for i in notes_list_id:
            if i > max:
                max = i
        new_id = max + 1
        note_book.write(str(f'{new_id};{title};{body};{date};{time};\n'))
    note_book.close()
    return new_id


def note_view(str_note):
    note = list(str(str_note).split(';'))
    return print(f'id: {note[0]}, title: {note[1]}, body: {note[2]}, date: {note[3]}, time: {note[4]}')
