import time
import keyboard
from PIL import ImageGrab


def screenshot():
    # 예) 2025년 5월 31일 16시 18분 40초 → _20250531_161840
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("imageP{}.png".format(curr_time))  # ex) image_20250531_161840.png


keyboard.add_hotkey("F9", screenshot)  # 사용자가 F9 키를 누르면 스크린 샷 저장
# keyboard.add_hotkey("a", screenshot)  # 사용자가 'a' 키를 누르면 스크린 샷 저장
# keyboard.add_hotkey(
#     "ctrl+shift+s", screenshot
# )  # 사용자가 'ctrl + shift + s' 키를 누르면 스크린 샷 저장

keyboard.wait("esc")  # 사용자가 esc 를 누를 때까지 프로그램 수행
