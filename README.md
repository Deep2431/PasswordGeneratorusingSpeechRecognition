# PasswordGeneratorusingSpeechRecognition

![This is an image](https://i.pcmag.com/imagery/articles/06r3O9TGIbCXQhR7C69f1vE-10..v1617039239.jpg)

## About:
It generates a random password for a user.

## Libraries and modules used:
- SpeechRecognition
- pyttsx3
- string
- random

## Working:
Two functions are created speak(using pyttsx3) - coverts text to speech and gives output in form of speech, micro_input(using SpeechRecogntion) - takes input as speech(voice) and performs tasks based on it. String is a built-in module which consists of constants such as: **string.ascii_lowercase** - returns all lowercase letters, **string.ascii_uppercase** - returns all uppercase letters, **string.digits** - returns digits from 0 to 9, **string.punctuation** - characters that are considered punctuation (!"#$%&'()*+,-./:;) and more. Here all these methods of strings are combined and a random password is generated with the help of these constants
