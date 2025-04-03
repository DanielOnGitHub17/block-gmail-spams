# Block Gmail Spams

A Python automation tool that helps you block multiple spam email senders in Gmail with minimal effort.

## Overview

This tool uses PyAutoGUI to automate the process of blocking spam email senders in Gmail. Instead of manually clicking through each email, you can run this script to automatically:

1. Open the menu for each spam email
2. Click the "Block" option
3. Confirm blocking the sender
4. Move to the next email

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/your-username/block-gmail-spams.git
    cd block-gmail-spams
    ```

2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

### Setup Button Coordinates

First, record the coordinates of the buttons:

```
python get_button_coords
```

Follow the on-screen instructions to position your cursor over each button when prompted:
- menu button
- block option
- block confirmation
- next email button

### Block Spam Emails

1. Open Gmail in your browser
2. Navigate to your spam folder
3. Run the script:
    ```
    python click_button_coords.py
    ```
4. Enter the number of spam emails you want to process when prompted

## How It Works

The tool works in three different ways:
1. **Recording Coordinates**: Uses `get_button_coords.py` to save the exact position of important buttons
2. **Using Images**: Alternatively, you can use `block_by_image.py` which recognizes buttons by matching screenshots
3. **Automation**: Uses `click_button_coords.py` or `block_by_image.py` to simulate mouse movements and clicks

### Note on Methods
- **Coordinates Method**: Generally more reliable as it doesn't depend on visual recognition
- **Image Method**: If you prefer using image recognition, take screenshots of the buttons and place them in the `assets` folder with appropriate naming (e.g., `menu_button.png`)

### Important 
The Gmail website must remain open and visible on your screen during the entire process for the automation to work properly. Don't minimize or switch to other windows during execution.

## Developer
Daniel Enesi - Developer and Prompt Engineer
1. **Recording Coordinates**: Uses `get_button_coords.py` to save the exact position of important buttons
2. **Automation**: Uses `click_button_coords.py` to simulate mouse movements and clicks based on the recorded positions

## Requirements

- Python 3.6+
- PyAutoGUI and other dependencies listed in requirements.txt
- A desktop environment (not compatible with headless systems)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

