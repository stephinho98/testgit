import pyautogui as pa
from python_imagesearch.imagesearch import imagesearcharea
import time

pos = imagesearcharea("x2.PNG", 0, 0, 200, 1080)
if pos[0] != -1:
    print("nasao")
else:
    print("nije nasao")
