import telebot
from telebot import types
from PIL import Image
import os

TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

def convert_to_png(image_path):
    """
    Converts the image to PNG format and resizes it if necessary.
    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Path to the converted PNG image.
    """
    try:
        img = Image.open(image_path)

        _, ext = os.path.splitext(image_path)
        ext = ext.lower()

        if ext != '.png':
            new_image_path = os.path.splitext(image_path)[0] + '.png'

            if img.size != (100, 100):
                img = img.resize((100, 100), Image.LANCZOS)

            img.save(new_image_path, optimize=True, quality=80)

            while os.path.getsize(new_image_path) > 128 * 1024:
                img = img.resize((int(img.width * 0.9), int(img.height * 0.9)), Image.LANCZOS)
                img.save(new_image_path, optimize=True, quality=80)

            print(f"Converted {image_path} to {new_image_path}")
            return new_image_path
        else:
            new_image_path = os.path.splitext(image_path)[0] + '.png'
            if img.size != (100, 100):
                img = img.resize((100, 100), Image.LANCZOS)
            img.save(new_image_path, optimize=True, quality=80)
            print(f"{image_path} is already in PNG format")
            return new_image_path
    except Exception as e:
        print(f"Error converting image: {e}")
        return None

def process_cover(message):
    bot.send_message(message.chat.id, 'Please send the image for the cover:')
    bot.register_next_step_handler(message, process_cover_image)

def process_cover_image(message):
    if message.photo:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('cover.png', 'wb') as new_file:
            new_file.write(downloaded_file)
        
        image_path = convert_to_png('cover.png')
        if image_path:
            bot.send_photo(message.chat.id, open(image_path, 'rb'))
        else:
            bot.send_message(message.chat.id, 'Failed to process the image. Please try again.')
    else:
        bot.send_message(message.chat.id, 'Please send an image.')

def process_sticker(message):
    bot.send_message(message.chat.id, 'Please send the image for the sticker:')
    bot.register_next_step_handler(message, process_sticker_images)

def process_sticker_images(message):
    if message.photo:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('sticker.png', 'wb') as new_file:
            new_file.write(downloaded_file)
        converted_path = convert_to_png('sticker.png')
        if converted_path:
            bot.send_photo(message.chat.id, open('sticker.png', 'rb'))
        else:
            bot.send_message(message.chat.id, 'Failed to process the image. Please try again.')
    else:
        bot.send_message(message.chat.id, 'Please send an image.')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'This bot will help you change photo size and type to interact with @Stickers and create your own Telegram stickers. Here you can send a photo for your set of stickers and it will be edited and sent to you so that in the future you can use this photo as your sticker or cover for a sticker pack.')
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    Cover = types.KeyboardButton('Cover')
    Sticker = types.KeyboardButton('Sticker')
    keyboard.add(Cover, Sticker)
    bot.send_message(message.chat.id, 'Choose an option:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Cover':
        process_cover(message)
    elif message.text == 'Sticker':
        process_sticker(message)
    else:
        bot.send_message(message.chat.id, 'I do not understand that command.')

bot.polling()
