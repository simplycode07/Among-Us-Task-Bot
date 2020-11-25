from time import sleep
import pyautogui
import keyboard
import timeit


def main():
    pyautogui.PAUSE = 0
    print("""the program has started
1. press Shift + Q to quit the program
2. press Shift + C to do card swipe
3. press Shift + W to do wire task
4. press Shift + P to do prime shield task
5. press Shift + G to do grabage task""")
    while True:
        if(keyboard.is_pressed('w') and keyboard.is_pressed('shift')):
            wiring_task()
        if(keyboard.is_pressed('c') and keyboard.is_pressed('shift')):
            card_task()
        if(keyboard.is_pressed('p') and keyboard.is_pressed('shift')):
            prime_shields()
        if(keyboard.is_pressed('g') and keyboard.is_pressed('shift')):
            garbage()
        if(keyboard.is_pressed('q') and keyboard.is_pressed('shift')):
            break
        sleep(0.15) # reduces system load for low end pc (optional)
    print("Done")


def wiring_task():
    x_right = 930
    x_left = 402
    heights = [192, 324, 457, 590]
    rightcolordict = {"(255, 0, 0)": heights[0], "(38, 38, 255)": heights[1],
                          "(255, 235, 4)": heights[2], "(255, 0, 255)": heights[3]}
    print("Starting Wiring Task")
    start_time = timeit.default_timer()
    # colordict["location"] = pixel color
    # to print 272,462,647,833 could be faster probably not
    for x in range(4):
        # 1905
        pyautogui.moveTo(x_left, heights[x])
        try:
            pyautogui.dragTo(x_right, rightcolordict[str(
                pyautogui.pixel(x_left, heights[x]))], .50, button='left')
            sleep(.05)
        except IndexError:
            print("no index try again")
        except KeyError:
            print("invalid key try again")
    print("Time to complete Wiring Task: " +
          str(round(timeit.default_timer() - start_time, 2)) + " seconds")
def card_task():
    x_card = [545, 393, 1114]
    y_card = [592, 300, 300]
    
    # clicking on wallet to take out the card
    pyautogui.click(x=x_card[0], y=y_card[0])

    sleep(0.5) # waiting for animation to over
    # moving cursor to starting position
    pyautogui.moveTo(x_card[1], y_card[1])

    # draging cursor to end point of the card swipe
    pyautogui.dragTo(x_card[2], y_card[2], 1, button='left')

def prime_shields():
    
    print("starting shield task")
    
    x_button = [685,803,824,671,582,560,692]
    y_button = [233,319,447,522,463,323,336]
    
    for i in range(len(x_button)):
        #getting color value of each point
        color = pyautogui.pixel(x_button[i], y_button[i])
        print(color)
        #checking if the color is red and if it is the we will click on it
        if color == (202, 83, 100) or color == (202, 86, 105) or color == (202, 91, 109) or color == (202, 95, 112) or color == (202, 98, 117) or color == (202, 102, 120) or color == (202, 106, 124):
            print(f"unprimed shield detected at {x_button[i]}, {y_button[i]}")
            pyautogui.click(x=x_button[i], y=y_button[i])

def garbage():
    #(x=898, y=296) and (x=912, y=508)
    pyautogui.moveTo(898, 296)
    pyautogui.mouseDown(button="left")
    sleep(0.2)
    pyautogui.moveTo(912, 508)
    sleep(1.5)
    pyautogui.mouseUp(button="left")
    print("grabage done")
        
    
if __name__ == "__main__":
    main()
