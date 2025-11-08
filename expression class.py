class Emotion:

    def __init__(self,name,color):
        self.name = name
        self.color = color

Sadness = Emotion('Sadness', 'Blue')
Happy = Emotion('Happy', 'Yellow')
Angry = Emotion('Angry', 'Red')

print("I am",Sadness.name,"and my color is", Sadness.color)
print("I am",Happy.name,"and my color is", Happy.color)
print("I am",Angry.name, "and my color is", Angry.color)
