from controllers import *


def menu():
    clear_terminal()
    print('Добро пожаловать!')
    while True:
        print('1 - Показать все задачи\n'
              '2 - Показать выполненные \n'
              '3 - Показать не выполненные\n'
              '4 - Добавить задачу\n'
              '5 - Изменить задачу\n'
              '6 - Удалить задачу\n'
              '9 - Сохранить изменения\n'
              '0 - Выход')
        while True:
            try:
                num = abs(int(input('Для продолжения работы введите цифру: ')))
                if 0 <= num <= 9:
                    break
            except ValueError:
                print('Wrong input! Try again...')

        match num:
            case 1:
                print_todo(all_task, 1)
            case 2:
                print_todo(all_task, 2)
            case 3:
                print_todo(all_task, 3)
            case 4:
                add_task(all_task)
            case 5:
                edit_task(all_task)
            case 6:
                del_task(all_task)
            case 9:
                save_data(all_task)
            case 0:
                clear_terminal()
                quit()


if __name__ == "__main__":
    menu()