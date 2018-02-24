import subprocess
import os
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm=["yes","confirm","sure","affirmative","do it","yeah"]
        self.cancel=["no" "negative","don't","wait","cancel"]

    def Discover(self,text):
        if "what" in text and "your name" in text:
            self.respond("Hi my name is Ravi. How Are You ?")
            if "How are you " in text:
                self.respond("I am fine and you ?")

        else:
            f=Fetcher("https://www.google.co.in/search?q="+text)



    def respond(self,text):
        os.chdir("C:\Program Files\Jampal")
        file = open(r"C:\Users\Student\PycharmProjects\Speech_with_python\Text.txt", "w+")
        file.write(text)
        os.popen("ptts -u " + r"C:\Users\Student\PycharmProjects\Speech_with_python\Text.txt")

