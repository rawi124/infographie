import tkinter as tk
import math
from tp1 import transformation, multiplication, projection

def segment_naif(x1,y1,x2,y2,coeff_directeur,pas):
    """
    renvoie les valeurs de y pour un x donné avec un coeff_directeur
    et un pas entre les differents points
    """
    liste_y = []
    pente = (y2-y1)/(x2-x1)
    x_dep = min(x1,x2)
    x_fin = max(x1,x2)
    while x_dep <= x_fin :
        y = pente*x_dep + coeff_directeur
        liste_y.append((x_dep,y))
        canva.create_oval(x_dep, y, x_dep, y, fill = "pink" )
        x_dep = x_dep + pas

    return liste_y

def Octant1(xa , ya , xb , yb):
    print('Octant1', xa, ya, xb, yb)
    dx = xb - xa
    dy = yb - ya
    dec = dx - (dy << 1)
    x = xa
    y = ya
    while x <= xb :
        # 2 x 350 + 350 = 1050 pour corriger la symetrie car l'orgine viewport est a 350 en y et de taille 350
        canva.create_line(x, 1050-y, x+1, 1050-y, fill = "pink")
        #canva.create_line(x, y, x+1, y, fill = "pink")
        #print(x, DimyV-y, x+1, DimyV-y)
        if dec < 0 :
            dec = dec + (dx << 1)
            y = y + 1
        dec = dec - (dy <<1)
        x = x +1

def Octant2(xa , ya , xb , yb ):
    print('Octant2', xa, ya, xb, yb)
    dx = xb - xa
    dy = yb -ya
    dec = dy - (dx << 1)
    x = xa
    y = ya
    liste = []
    while y <= yb :
        #tran = transformation(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow,x,y)
        canva.create_line(x, 1050-y, x+1, 1050-y, fill = "pink")
        if dec < 0 :
            dec = dec + (dy << 1)
            x = x + 1
        dec = dec - (dx << 1)
        y = y +1

def Octant3(xa , ya , xb , yb ):
    print('Octant3', xa, ya, xb, yb)
    dx = xb - xa
    dy = yb - ya
    dec = abs(dy) - (abs(dx) << 1)
    x = xa
    y = -ya
    print(abs(y), abs(yb))
    while abs(y) <= abs(yb) :
        canva.create_line(x, 1050-abs(y), x+1, 1050-abs(y), fill = "pink")
        print(x, 1050-y)
        if dec < 0 :
            dec = dec - (abs(dy) << 1)
            x = x + 1
        dec = dec - (abs(dx) << 1)
        y = y - 1

def Bresenham (pxa , pya , pxb , pyb ,canva) :
    xa, ya = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, pxa, pya)
    xb, yb = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, pxb, pyb)
    print('projection', xa, ya, xb, yb)
    dx = xb - xa
    dy = yb - ya
    if dx >= 0 :
        if dy >= 0:
            if dx > dy :
                #octant 1
                print("octant 1 ")
                Octant1(xa, ya, xb, yb)
            elif dx <= dy :
                #octant 2
                print("octant 2 ")
                return Octant2(xa, ya, xb, yb)
        elif dy < 0 :
            if dx < abs(dy):
                #octant 7
                print("octant 7 ")
                return Octant2(xa, ya, xb, yb)
            elif dx >= abs(dy) :
                print("octant 8 ")
                #octant 8
                return Octant1(xa, ya, xb, yb)
    elif dx < 0 :
        if dy >=0 :
            #octant 3
            if abs(dx) < dy :
                print("octant 3 ")
                return Octant3(xa, ya, xb, yb)
            else :
                #octant4
                print("octant 4 ")
                return Octant1(xa, ya, xb, yb)
        else :
            #octant5
            if abs(dx) > abs(dy):
                print("octant 5 ")
                return Octant1(xa, ya, xb, yb)
                #octant6
            else :
                print("octant 6 ")
                return Octant2(xa, ya, xb, yb)



if __name__ == '__main__':
    root = tk.Tk()
    root.title("TP02_Infographie")
    canva= tk.Canvas(root,width=1000, height=800, bd=1)
    canva.pack(padx=10,pady=10)

    #dim puis pos de la viewport
    DimxV = 350
    DimyV = 350
    xviewport, yviewport = 150, 350

    #dimension puis position de la window
    dimxw = 1000
    dimyw = 1000
    xwindow = 0
    ywindow = 0

    px = 0
    py = 0
    rect = canva.create_rectangle(xviewport, yviewport, DimxV+xviewport,DimyV+yviewport, fill="white", outline="blue", width=5)#viewport
    #l_naif = segment_naif(0,0,20,20,0,0.5)
    #Bresenham(0,0,300,100,canva)
    Bresenham(50,0,0,100,canva)



    #l_Octant2 = Octant2(25,40,50,50)
    #pour iterer deux listes en meme temps de meme taille utiliser zip
    #for el in l_Octant2   :
        #tran=transformation(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow,el[0],el[1])
        #canva.create_oval(tran[0], tran[1], tran[0], tran[1], fill = "pink" )
        #trans=transformation(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow,ell[0],ell[1])
        #canva.create_oval(trans[0], trans[1], trans[0], trans[1], fill = "pink" )
    root.mainloop()

    exit(0)
