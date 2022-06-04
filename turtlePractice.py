import turtle

mode = 0

# star alternate color
for x in range(5):
    if mode == 0:
        turtle.color('red', 'yellow')
        mode = 1
    elif mode == 1:
        turtle.color('blue', 'green')
        mode = 0
                
    turtle.forward(100)
    turtle.right(144)


# circle
turtle.circle(55)

# triangle

# 
