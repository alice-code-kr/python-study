from car import Car
import keyboard

Car()

def keyboard_down(evt):
    print('Keyboard down {}'.format(evt.name)) #입력된 키를 출력합니다.

keyboard.on_press(keyboard_down) #키보드 버튼을 누르면 keyboard_down 함수를 호출합니다.
keyboard.wait('esc') #esc 키를 누를때 까지 대기합니다.