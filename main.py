from time import sleep
import pyautogui
import keyboard
import timeit


def main():
    # consts to make program marginally faster

    pyautogui.PAUSE = 0
    while True:
        if(keyboard.is_pressed('c') and keyboard.is_pressed('shift')):
            wiring_task()
        if(keyboard.is_pressed('q') and keyboard.is_pressed('shift')):
            break
    print("Done")


def wiring_task():
    x_right = 930
    x_left = 402
    heights = [192, 324, 457, 590]
    rightcolordict = {"(255, 0, 0)": heights[0], "(38, 38, 255)": heights[1],
                          "(255, 235, 4)": heights[2], "(255, 0, 255)": heights[3]}
    print("Starting Wiring Task")
    start_time = timeit.default_timer()
    # colordict[location"] = pixel color
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


if __name__ == "__main__":
    main()
