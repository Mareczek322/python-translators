from pynput.keyboard import Key, Controller
import time
keyboard = Controller()


def encode(message):
    for i in message:
        if i == 'A':
            keyboard.type(':regional_indicator_a:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'B':
            keyboard.type(':regional_indicator_b:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'C':
            keyboard.type(':regional_indicator_c:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'D':
            keyboard.type(':regional_indicator_d:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'E':
            keyboard.type(':regional_indicator_e:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'F':
            keyboard.type(':regional_indicator_f:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'G':
            keyboard.type(':regional_indicator_g:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'H':
            keyboard.type(':regional_indicator_h:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'I':
            keyboard.type(':regional_indicator_i:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'J':
            keyboard.type(':regional_indicator_j:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'K':
            keyboard.type(':regional_indicator_k:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'L':
            keyboard.type(':regional_indicator_l:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'M':
            keyboard.type(':regional_indicator_m:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'N':
            keyboard.type(':regional_indicator_n:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'O':
            keyboard.type(':regional_indicator_o:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'P':
            keyboard.type(':regional_indicator_p:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'Q':
            keyboard.type(':regional_indicator_q:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'R':
            keyboard.type(':regional_indicator_r:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'S':
            keyboard.type(':regional_indicator_s:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'T':
            keyboard.type(':regional_indicator_t:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'U':
            keyboard.type(':regional_indicator_u:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'V':
            keyboard.type(':regional_indicator_v:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'W':
            keyboard.type(':regional_indicator_w:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'X':
            keyboard.type(':regional_indicator_x:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'Y':
            keyboard.type(':regional_indicator_y:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif i == 'Z':
            keyboard.type(':regional_indicator_z:')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        else:
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
    keyboard.press(Key.enter)


def begin_emoji():
    inputs = input("What message would you like to encode? ").upper()
    message = list(inputs)
    time.sleep(5)
    encode(message)


if __name__ == "__main__":
    begin_emoji()
