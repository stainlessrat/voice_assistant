from gtts import gTTS


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
    print(message)


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
