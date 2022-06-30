from gtts import gTTS
import base64
import os


def text2Speech(data):
    my_text = data
    print(my_text)
    tts = gTTS(text=my_text, lang='en', slow=False)
    tts.save('converted-file.mp3')  # save file as ... (here saving as mp3)
    with open("converted-file.mp3", "rb") as file:
        my_string = base64.b64encode(file.read())
    # print(my_string)
    return my_string


