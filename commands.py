import subprocess
import os

class Commander:
    def __init__(self):
        self.confirm=["yes","confirm","sure","affirmative","do it","yeah"]
        self.cancel=["no" "negative","don't","wait","cancel"]

    def Discover(self,text):
        if "what" in text and "your name" in text:
            self.respond("Hi my name is Ravi. How Are You ?")
        if "hello" in text:
            self.respond("Hi my name is Ravi. How Are You ?")

    def respond(self,text):
        os.chdir("C:\Program Files\Jampal")
        file = open(r"C:\Users\cubastion\PycharmProjects\Speech_with_python\Text.txt", "w+")
        file.write(text)
        os.popen("ptts -u " + r"C:\Users\cubastion\PycharmProjects\Speech_with_python\Text.txt")

