import sys
import signal
import pyautogui
import pytesseract
import keyboard
import easyocr
import time
import cv2

stop_macro = False
stop_macro_real = False

xy=[[390,530], [390,570],[390,605],[390,645], [390,680], [390,725], [390,755], [390,795], [390,830], [390,870]]
ocr=[605, 540, 145, 60]
e_learning=["501269","501320","501343","501347"]
sub = "001"
search=[400, 580]
number=[480,580]

second = 1
minute = second*60
hour = minute*60
def check_interrupt():
    global stop_macro
    while not stop_macro:
        if keyboard.is_pressed("ctrl+c"):
            print("Macro interrupted.")
            stop_macro = True
        elif keyboard.is_pressed("ctrl+z"):
            print("Macro interrupted.")
            stop_macro_real = True
            sys.exit(1)
def ocr_screen_region(left, top, width, height):
    screenshot = pyautogui.screenshot('test.png', region=(left, top, width, height))
    file = r"E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Resources\Temp\test.png"
    reader = easyocr.Reader(['en'], gpu=True)
    img = cv2.imread(file)
    text = reader.readtext(img, detail=0)
    results = reader.readtext(screenshot)

def ocr_screen_region2(left, top, width, height):
    screenshot = pyautogui.screenshot('test.png', region=(left, top, width, height))
    result = pytesseract.image_to_string(screenshot, config="--psm 6 -c tessedit_char_whitelist=0123456789")

    return result

def KMOOC_macro():
    # pyautogui.moveTo(480, 400, duration=0.05)
    # pyautogui.click()
    #
    # pyautogui.moveTo(480, 610, duration=0.05)
    # pyautogui.click()
    #
    # pyautogui.moveTo(830, 400, duration=0.05)
    # pyautogui.click()
    # k_mooc="K-MOOC"
    # keyboard.write(k_mooc)
    #
    # pyautogui.moveTo(1640, 400, duration=0.05)
    # pyautogui.click()
    #
    # time.sleep(0.1)
    #
    # pyautogui.moveTo(1520, 495, duration=0.05)
    # pyautogui.click()
    #
    # pyautogui.moveTo(1410, 575, duration=0.05)
    # pyautogui.click()

    # Perform the macro steps

    for elem in xy:
        pyautogui.moveTo(elem[0], elem[1], duration=0.05)
        pyautogui.click()

        pyautogui.moveTo(950, 550, duration=0.05)
        pyautogui.click()

        text = ocr_screen_region2(ocr[0], ocr[1], ocr[2], ocr[3])
        keyboard.write(text)

        pyautogui.moveTo(960, 730, duration=0.05)
        pyautogui.click()

        pyautogui.moveTo(1020, 750, duration=0.05)
        pyautogui.click()



        pyautogui.moveTo(1010, 720, duration=0.05)
        pyautogui.click()
        time.sleep(0.2)

def e_learning_macro():
    pyautogui.moveTo(480, 400, duration=0.05)
    pyautogui.click()

    pyautogui.moveTo(500, 580, duration=0.05)
    pyautogui.click()
    for str in e_learning:
        if str != "501269":
            pyautogui.moveTo(820, 400, duration=0.05)
            pyautogui.click()

            keyboard.press_and_release('ctrl+a')
            keyboard.press_and_release('backspace')

            keyboard.write(str)

        else:
            pyautogui.moveTo(820, 400, duration=0.05)
            pyautogui.click()
            keyboard.write(str)

            pyautogui.moveTo(1100, 400, duration=0.05)
            pyautogui.click()
            keyboard.write(sub)

        pyautogui.moveTo(1640, 400, duration=0.05)
        pyautogui.click()

        click=[400,530]
        pyautogui.moveTo(click[0], click[1], duration=0.05)
        pyautogui.click()

        pyautogui.moveTo(950, 550, duration=0.05)
        pyautogui.click()

        text = ocr_screen_region2(ocr[0], ocr[1], ocr[2], ocr[3])
        print(text)
        keyboard.write(text)

        pyautogui.moveTo(960, 730, duration=0.05)
        pyautogui.click()

        pyautogui.moveTo(1020, 750, duration=0.05)
        pyautogui.click()

        pyautogui.moveTo(1010, 720, duration=0.05)
        pyautogui.click()

def main(h, m, s):
    global stop_macro
    print("Starting Mouse Macro...")
    stop_macro = False

    def check_interrupt(signum, frame):
        print("\nCtrl+C received. Stopping macro...")
        sys.exit(0)

    signal.signal(signal.SIGINT, check_interrupt)

    time.sleep(1)

    timestamp_now = time.time()
    target_timestamp = timestamp_now + (h*hour + m*minute + s*second)

    try:
        while timestamp_now <= target_timestamp:
            start_time = time.time()

            KMOOC_macro()
            #e_learning_macro()

            end_time = time.time()
            time_difference = end_time - start_time
            print(f"Time difference: {time_difference:.3f} seconds")

            timestamp_now = time.time()

        stop_macro = True  # Stop macro even if loop completes
        print("Mouse Macro completed.")

    except KeyboardInterrupt:
        print("\nCtrl+C received. Stopping macro...")



if __name__ == "__main__":
    main(0, 30, 0)