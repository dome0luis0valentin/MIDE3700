#Crea 12 puntos en linea recta desde (0.15784, -10.0049) hasta (0.16848, -9.541)
p1 = (0.15784, -10.0049)
for i in range(0, 10):
    print(p1[0],"    ",p1[1])
    p1 = (p1[0]+0.0015, p1[1]+0.046)