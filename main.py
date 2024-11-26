"""Script to loop all button clicks"""
import pyautogui


def main():
    """If function ran as script. Will start/error when the user hits enter"""
    print("Please open the spam gmails window/tab for the app to work")
    n_spams = int(input("How many spam emails do you want deleted? "))
    delete_spams(n_spams)


def delete_spams(n):
    """Code starts running from here"""
    for _ in range(n):
        click_menu()
        click_block()
        click_block_confirm()
        click_next()  # Might not work the last time.
        pyautogui.moveTo(10, 10, duration=0.5)



def click_next():
    """Function to click next button"""
    click_button("next")


def click_menu():
    """Function to click menu button"""
    click_button("menu")


def click_block():
    """Function to click block button"""
    click_button("block")


def click_block_confirm():
    """Function to click block confirm button"""
    click_button("block_confirm")


def click_button(button_name, ext="png", duration=0.5):
    while True:
        try:
            pyautogui.moveTo(f"assets/{button_name}_button.{ext}", duration=duration)
            pyautogui.click(interval=0.1)
            break
        except pyautogui.ImageNotFoundException:
            print(f"Failing due to minor error {button_name}...")


if __name__ == "__main__":
    main()
