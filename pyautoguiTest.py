import pyautogui
import time

message = "hello world!";

time.sleep(1);
pyautogui.typewrite(message,interval=0.15);
pyautogui.press("enter");

