import pyautogui

def delete_spams(n):
    """Loops and blocks by calling necessary functions"""
    for i in range(n):
        if i:
            click_next()
        click_menu()
        click_block()
        click_block_confirm()
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
    """Function to click a button given image name"""
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        try:
            pyautogui.moveTo(f"assets/{button_name}_button.{ext}", duration=duration)
            pyautogui.click(interval=0.1)
            return True
        except pyautogui.ImageNotFoundException:
            print(f"Attempt {attempts+1}: Could not find {button_name} button image")
            attempts += 1
    
    # If we get here, all attempts failed
    raise Exception(f"Could not find {button_name} button after {max_attempts} attempts")
