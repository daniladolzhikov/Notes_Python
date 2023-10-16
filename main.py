

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Поиск заметки")
        print("3. Изменить заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            search_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
