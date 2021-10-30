from gtts import gTTS
import random
import time


def listen_command():
    return input("Скажите вашу команду: ")


def do_this_command(message):
    message = message.lower()
    if 'привет' in message:
        say_message('Привет, друг.')
    elif 'пока' in message:
        say_message('Пока!')
        exit()
    else:
        say_message('Команда не распознана!')


def say_message(message):
    voice = gTTS(message, lang='ru')
    file_voice_name = f'_audio_{str(time.time())}_{str(random.randint(0, 100000))}.mp3'
    voice.save(file_voice_name)
    print(message)


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
