import turtle
import random

class Window:
    main_window = turtle.Screen()
    main_window.title("Greed")
    main_window.bgcolor("black")
    main_window.setup(width = 800, height = 600)

class Player:
    player = turtle.Turtle()
    player.color("green")
    hashtag = "turtle"
    player.shape(hashtag)
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    playerspeed = 15
    
class Movement(Player):
    def move_left(player,playerspeed):
        x = player.xcor()
        x -= playerspeed
        if x < -390:
            x = -390
        player.setx(x)

    def move_right(player,playerspeed):
        x = player.xcor()
        x += playerspeed
        if x > 380:
            x = 380
        player.setx(x)

    turtle.listen()
    turtle.onkeypress(move_left, "Left")
    turtle.onkeypress(move_right, "Right")


class Gem:
    gems = []

    for _ in range(10):
        gem = turtle.Turtle()
        colors = ['gold', 'orange', 'red', 'maroon', 
            'violet', 'magenta', 'purple', 'navy', 'blue', 
            'cyan', 'turquoise', 'darkgreen']
        gem.color(random.choice(colors))
        asterisk = "triangle"
        gem.shape(asterisk)
        gem.penup()
        gem.speed(0)
        gem.setposition(random.randint(-400, 400), random.randint(-300, 300))
        gem.speed = random.randint(10, 15)
        gems.append(gem)

class Rock:
    rocks = []

    for _ in range(10):
        rock = turtle.Turtle()
        rock.color("gray")
        zero = "circle"
        rock.shape(zero)
        rock.penup()
        rock.speed(0)
        rock.setposition(random.randint(-400, 400), random.randint(-300, 300))
        rock.speed = random.randint(10, 15)
        rocks.append(rock)

class Generate(Gem,Rock):
    
    while True:

        for gem in Gem.gems:
            y = gem.ycor()
            y -= gem.speed
            gem.sety(y)

            if y < -300:
                x = random.randint(-390, 380)
                y = random.randint(300, 350)
                gem.goto(x, y)

        for rock in Rock.rocks:
            y = rock.ycor()
            y -= rock.speed
            rock.sety(y)

            if y < -300:
                x = random.randint(-390, 380)
                y = random.randint(300, 350)
                rock.goto(x, y)



class Catch:
    pass

class Scoreboard:
    score = 0
    pass

def main(Window,Player,Movement):
    Window().runall()
    Player().runall()
    Movement().runall()
    Gem().runall()
    Rock().runall()
    Generate().runall()
    

if __name__ == "__main__":
    main()
    main_window.mainloop()
