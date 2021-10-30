from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Скажите что-нибудь:')
        audio = r.listen(source)
    try:
        our_speech = r.recognize_google(audio, language='ru')
        print(our_speech)
        return our_speech
    except sr.UnknownValueError:
        return 'Google Speech Recognition could not undestand audio'
    except sr.RequestError as e:
        return 'Could not requests from Google Speech Recognition service {e}'


def do_this_command(message):
    message = message.lower()
    if 'привет' in message:
        say_message('Привет друг')
    elif 'пока' in message:
        say_message('Пока')
        exit()
    else:
        say_message('Команда не распознана')


def say_message(message):
    voice = gTTS(message, lang='ru')
    file_voice_name = f'_audio_{str(int(time.time()))}_{str(random.randint(0, 100000))}.mp3'
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print(f'Голосовой ассистент: {message}')


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
