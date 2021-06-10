import pyautogui as pa
from python_imagesearch.imagesearch import imagesearch
import time

def restartGame():
    print("restartGame...")
    time.sleep(1)
    pa.moveTo(840, 80, 0.1)
    pa.click(button = 'left')
    time.sleep(1)
    pa.click(button = 'left')
    time.sleep(1)
    pa.moveTo(925, 300, 0.1)
    pa.click(button = 'left')
    while(1):
        play = imagesearch("./play.png")
        if play[0] != -1:
            pa.moveTo(1515, 665, 0.1)
            pa.click(button = 'left')
            break
        time.sleep(5)
    giftPack()

def giftPack():
    print("giftpack...")
    time.sleep(2)
    redx = imagesearch("./redx.png")
    if redx[0] != -1:
        pa.moveTo(1505, 195, 0.1)
        pa.click(button = 'left')
    time.sleep(1)

def failAd():
    print("failAd...")
    time.sleep(1)
    fa = imagesearch("./go.png")
    if fa[0] != -1:
        return True
    return False

ssbr = 0
while(1):
    giftPack()
    print("trazi wheel...")
    wheel = imagesearch("./wheel.png")
    if wheel[0] == -1:        
        restartGame()
    pa.moveTo(1620, 275, 0.1)
    pa.click(button = 'left')
    time.sleep(1)
    pa.moveTo(950, 660, 0.1)
    pa.click(button = 'left')
    print("cekam X...")
    br = 0
    nadjen = True
    while(1):
        if br == 15:
            print("error...")
            ss = pa.screenshot()
            path = 'C:/Users/Nikola/Desktop/Xs/ss/' + str(ssbr) + '.png'
            ss.save(path)
            ssbr += 1
            restartGame()
            nadjen = False
            break
        go = imagesearch("./go.png")
        if go[0] != -1:
            pa.moveTo(go[0], go[1], 0.1)
            pa.click(button = 'left')
        
        pos = imagesearch("./x1.png")
        if pos[0] != -1:
            time.sleep(1)
            pa.moveTo(pos[0], pos[1], 0.1)
            pa.click(button = 'left')
            break
        pos2 = imagesearch("./x2.png")
        if pos2[0] != -1:
            time.sleep(1)
            pa.moveTo(pos2[0], pos2[1], 0.1)
            pa.click(button = 'left')
            break
        pos3 = imagesearch("./x3.png")
        if pos3[0] != -1:
            time.sleep(1)
            pa.moveTo(pos3[0], pos3[1], 0.1)
            pa.click(button = 'left')
            break
        pos4 = imagesearch("./x4.png")
        if pos4[0] != -1:
            time.sleep(1)
            pa.moveTo(pos4[0], pos4[1], 0.1)
            pa.click(button = 'left')
            break
        pos5 = imagesearch("./x5.png")
        if pos5[0] != -1:
            time.sleep(1)
            pa.moveTo(pos5[0], pos5[1], 0.1)
            pa.click(button = 'left')
            break
        pos6 = imagesearch("./x6.png")
        if pos6[0] != -1:
            time.sleep(1)
            pa.moveTo(pos6[0], pos6[1], 0.1)
            pa.click(button = 'left')
            break
        pos7 = imagesearch("./x7.png")
        if pos7[0] != -1:
            time.sleep(1)
            pa.moveTo(1655, 170, 0.1)
            pa.click(button = 'left')
            break
        pos8 = imagesearch("./x8.png")
        if pos8[0] != -1:
            time.sleep(1)
            pa.moveTo(pos8[0], pos8[1], 0.1)
            pa.click(button = 'left')
            break
        pos9 = imagesearch("./x9.png")
        if pos9[0] != -1:
            time.sleep(1)
            pa.moveTo(pos9[0], pos9[1], 0.1)
            pa.click(button = 'left')
            break
        time.sleep(6)
        br += 1
    if nadjen:
        print("cekam reward...")
        time.sleep(12)
        if failAd():
            pa.moveTo(1330, 300, 0.1)
            pa.click(button = 'left')
        else:
            pa.moveTo(950, 550, 0.1)
            pa.click(button = 'left')

