import turtle
tao = turtle.Pen() #Use pen function
tao.shape('turtle') #Change into turtle

def Rectangle():
    '''This function is for drawing a square'''
    for i in range(4):
        tao.forward(100)
        tao.left(90)

for i in range (60):
    Rectangle()
    tao.left(6)   
    
