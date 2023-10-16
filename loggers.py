import json
import os
from datetime import datetime

notes_file = 'notes.json'

if os.path.exists(notes_file):
    with open(notes_file, 'r') as file:
        notes = json.load(file)
else:
    notes = []

def save_notes():
    
    with open(notes_file, 'w') as file:
        json.dump(notes, file)

def list_notes():
    
    if not notes:
        print("Список заметок пуст.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"{i}. Заголовок: {note['title']}")
            print(f"   Тело: {note['message']}")
            print(f"   Дата создания: {note['timestamp']}")
            print()

def add_note():
    
    title = input("Введите заголовок заметки: ")
    message = input("Введите тело заметки: ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {'title': title, 'message': message, 'timestamp': timestamp}
    notes.append(note)
    save_notes()
    print("Заметка успешно добавлена.")

def edit_note():
    
    list_notes()
    note_number = int(input("Введите номер заметки для редактирования: ")) - 1
    if 0 <= note_number < len(notes):
        new_title = input("Введите новый заголовок: ")
        new_message = input("Введите новое тело: ")
        notes[note_number]['title'] = new_title
        notes[note_number]['message'] = new_message
        notes[note_number]['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_notes()
        print("Заметка успешно отредактирована.")
    else:
        print("Недопустимый номер заметки.")

def delete_note():
    
    list_notes()
    note_number = int(input("Введите номер заметки для удаления: ")) - 1
    if 0 <= note_number < len(notes):
        del notes[note_number]
        save_notes()
        print("Заметка успешно удалена.")
    else:
        print("Недопустимый номер заметки.")

