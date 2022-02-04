import turtle

captain = turtle.Turtle()
print("\n--------------------------")
print("Ad ve Soyad : Emre MERT\nOkul No : 203305028")
print("----------------------------")

kenar = float(input("Kenar Uzunluklarini Gir : "))
yariCap = float(input("Dairenin Yaricapini Gir : "))
x = 0
y = 0
count = 0
kenar += yariCap
captain.shape("circle")

for i in range(4):
    
    captain.up()
    captain.goto(x,y)
    captain.down()
    
    captain.circle(yariCap)
    count += 1
    
    if(count == 1):
        x = kenar + yariCap
    
    elif(count == 2):
        x = 0
        y = (-kenar) - yariCap
    
    elif(count == 3):
        x = kenar + yariCap
        
captain.up()
captain.goto(0,yariCap)
captain.down()

 
for i in range(4):
    captain.shape("arrow")
    captain.dot()
    captain.forward(x)
    captain.right(90)
    
        