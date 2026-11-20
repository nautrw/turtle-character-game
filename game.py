from turtle import *

screen = Screen()
screen.tracer(0, 0) # turns off turtle animation and delay

t = Turtle()
t.hideturtle()

class SpecialMove:
    def __init__(self, color: str, ):
        pass

class Character:
    def __init__(self, name: str, health: int, hair_color: str, skin_tone: str, shirt_color: str, pants_color: str, shoes_color: str):
        self.name = name
        self.health = health

        self.hair_color = hair_color
        self.skin_tone = skin_tone
        self.shirt_color = shirt_color
        self.pants_color = pants_color
        self.shoes_color = shoes_color
    
    def draw(self):
        color(self.hair_color)
        circle(50, 50)
        

character = Character("John", 100, "red", "brown", "red", "blue", "black")
character.draw()

update()
exitonclick()