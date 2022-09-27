import random

class pickoption:
    def __init__(self):
        self.awnser=[
            "i must do it",
            "it's up to you",
            "you shouldn't do it"
            
        ]
    def begin(self):
        input('make a questions? ')
        print(random.choice(self.awnser))

decide=pickoption()
decide.begin()