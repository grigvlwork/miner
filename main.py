from minerobj import Field
from pynput import keyboard


def on_release(key):
    if key == keyboard.Key.esc:
        return False
    elif key == keyboard.Key.right:
        main_field.move_right()
    elif key == keyboard.Key.left:
        main_field.move_left()
    elif key == keyboard.Key.down:
        main_field.move_down()
    elif key == keyboard.Key.up:
        main_field.move_up()
    elif key == keyboard.Key.space:
        main_field.change_flag()
    elif key == keyboard.Key.enter:
        main_field.open()
    elif key == keyboard.Key.alt:
        main_field.accord()
    main_field.draw()

if __name__ == '__main__':
    choice = -1
    while choice not in ["1", "2", "3", "4", "5"]:
        print("Выберите уровень сложности:")
        print("1) Новичок 10 мин поле 9х9")
        print("2) Любитель 40 мин поле 16х16")
        print("3) Профессионал 99 мин поле 16х30")
        print("4) Настроить поле")
        print("5) Выход")
        choice = input("Введите номер пункта:")
    rows = cols = 9
    bombs = 10
    if choice == "1":
        rows, cols, bombs = 9, 9, 10
    elif choice == "2":
        rows, cols, bombs = 16, 16, 40
    elif choice == "3":
        rows, cols, bombs = 16, 30, 99
    elif choice == "4":
        while rows not in range(2, 41) or cols not in range(2, 41) or bombs not in range(rows * cols):
            try:
                rows = int(input("Количество строк (2..40):"))
                cols = int(input("Количество столбцов (2..40):"))
                bombs = int(input(f"Количество мин (1..{rows * cols - 1}):"))
            except:
                rows = cols = bombs = -1
    elif choice == "5":
        exit(0)
    main_field = Field(cols, rows, bombs)
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()



