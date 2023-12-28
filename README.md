# 🤖 StickHelper

🤖 StickHelper is a Telegram bot designed to assist in resizing images and managing them as stickers for @Stickers on Telegram. It simplifies the process of creating custom Telegram stickers by allowing users to upload images, which are then converted into usable stickers or covers for sticker packs.

<div id="badges" align="center">
  <a href="https://t.me/CodQu">
    <img src="https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Badge"/>
  </a>
  <a href="https://t.me/Cisamu">
    <img src="https://img.shields.io/badge/Join%20My%20Telegram%20Channel-blue?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Channel Badge"/>
  </a>
</div>

## Requirements

To run StickHelper, you'll need:

- Python 3.7 or higher
- pillow==8.4.0
- pyTelegramBotAPI==4.0.0

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/cisamu123/StickHelper.git
    cd StickHelper
    ```

2. Set up Python and a Virtual Environment (optional but recommended):
    - Install Python (version 3.7 or higher): [Python Downloads](https://www.python.org/downloads/)
    - Create a virtual environment:
        ```bash
        python -m venv venv
        # For Windows: python -m venv venv
        ```

3. Activate the Virtual Environment (if used):
    - For Windows:
        ```bash
        venv\Scripts\activate
        ```
    - For macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set Up the Telegram Token:
    - Replace `'YOUR_BOT_TOKEN'` in the bot's code with your actual Telegram token.

6. Run the Bot:
    ```bash
    python main.py
    ```

## Usage

To use StickHelper, start the bot and interact with it via Telegram. Send an image and follow the prompts to convert it into a sticker or cover for sticker packs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
