import pyautogui
import time

  # 给你5秒切换到目标窗口
for i in range(1,6):
    print(f'要来了 {6-i}')
    time.sleep(1)

k = 0
while k <= 280:
    pyautogui.press('enter')
    time.sleep(1)  # 每0.1秒按一次
