import pyautogui
from PIL import ImageGrab

def get_mouse_color():
    try:
        while True:
            x, y = pyautogui.position()
            screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))
            color = screenshot.getpixel((0, 0))
            print(f"鼠标位置 ({x}, {y}) 处的颜色为 {color}")
    except KeyboardInterrupt:
        print("程序结束")

if __name__ == "__main__":
    get_mouse_color()
