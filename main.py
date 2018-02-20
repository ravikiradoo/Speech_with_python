import pyaudio
import wave
import speech_recognition as sr
import subprocess
import os
from commands import Commander

def play_audio(filename):
    chunk=1024
    wv=wave.open(filename,"rb")
    pa=pyaudio.PyAudio()

    stream=pa.open(format=pa.get_format_from_width(wv.getsampwidth()),channels=wv.getnchannels(),rate=wv.getframerate(),output=True)

    data_stream=wv.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream=wv.readframes(chunk)

    stream.close()
    pa.terminate()

r=sr.Recognizer()
cmd=Commander()
running=True

def initSpeech():
    play_audio("Audio/sms-alert-5-daniel_simon.wav")

    with sr.Microphone() as source:
        print("Listening.......")
        audio=r.listen(source)

        play_audio("Audio/sms-alert-5-daniel_simon.wav")

    command=""
    try:
        command=r.recognize_google(audio)
    except:
        print("Error")
    if command in ["quit","good bye" , "ok bye", "exit"]:
        global running
        running=False
    else:
        cmd.Discover(command)












