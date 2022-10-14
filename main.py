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
    elif key == keyboard.Key.end:
        main_field.accord()
    main_field.draw()


if __name__ == '__main__':
    main_field = Field()
    main_field.new_game()
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()
