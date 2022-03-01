import tkinter as tk
import math
from tp1 import multiplication, projection

# constantes nommees
# ecran virtuel
LA, HA = 1000, 800

def point(px, py, pcoul):
    """
    affichage dans le repère écran d'un point (px, py) défini dans le repère euclidien
    pcoul couleur du pixel correspondant
    canva canvas unique, HA hauteur du canvas
    """
    canva.create_line(px, HA-py, px+1, HA-py, fill=pcoul)

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
        point(x, y, "pink")
        if dec < 0 :
            dec = dec + (dx << 1)
            y = y + 1
        dec = dec - (dy <<1)
        x = x + 1

def Octant2(xa , ya , xb , yb ):
    print('Octant2', xa, ya, xb, yb)
    dx = xb - xa
    dy = yb - ya
    dec = dy - (dx << 1)
    x = xa
    y = ya
    print("2",y,yb,dy)
    while y <= yb :
        point(x, y, "pink")
        if dec < 0 :
            dec = dec + (dy << 1)
            x = x + 1
        dec = dec - (dx << 1)
        y = y + 1

def Octant3(xa , ya , xb , yb ):
    print('Octant3', xa, ya, xb, yb)
    # on connait les signes de dx et dy
    dx, dy = abs(xb - xa), abs(yb - ya)
    dec = dy - (dx << 1)
    x, y = xa, ya
    print("3",y,yb)
    while abs(y) <= abs(yb) :
        point(x, y, 'pink')
        if dec < 0 :
            dec = dec + (dy << 1)
            x = x - 1
        dec = dec - (dx << 1)
        y = y + 1

def Octant4(xa , ya , xb , yb):
    print('Octant4', xa, ya, xb, yb)
    dx, dy = abs(xb - xa), abs(yb - ya)
    dec = dx - (dy << 1)
    x, y = xb, yb
    while abs(x) <= abs(xa) :
        point(x, y, "pink")
        if dec < 0 :
            dec = dec + (dx << 1)
            y = y - 1
        dec = dec - (dy <<1)
        x = x + 1

def Octant5(xa , ya , xb , yb):
    print('Octant5', xa, ya, xb, yb)
    dx, dy = abs(xb - xa), abs(yb - ya)
    dec = dx - (dy << 1)
    x, y = xb, yb
    while abs(x) <= abs(xa) :
        point(x, y, "pink")
        if dec < 0 :
            dec = dec + (dx << 1)
            y = y + 1
        dec = dec - (dy <<1)
        x = x + 1

def Octant6(xa , ya , xb , yb ):
    print('Octant6', xa, ya, xb, yb)
    dx, dy = abs(xb - xa), abs(yb - ya)
    dec = dy - (dx << 1)
    x = xb
    y = yb
    while abs(y) <= abs(ya) :
        point(x, y, "pink")
        if dec < 0 :
            dec = dec + (dy << 1)
            x = x + 1
        dec = dec - (dx << 1)
        y = y + 1

def Octant7(xa , ya , xb , yb ):
    print('Octant7', xa, ya, xb, yb)
    dx, dy = abs(xb - xa), abs(yb - ya)
    dec = dy - (dx << 1)
    x = xb
    y = yb
    while abs(y) <= abs(ya) :
        point(x, y, "pink")
        if dec < 0 :
            dec = dec + (dy << 1)
            x = x - 1
        dec = dec - (dx << 1)
        y = y + 1

def Octant8(xa , ya , xb , yb):
    print('Octant8', xa, ya, xb, yb)
    dx, dy = abs(xb - xa), abs(yb - ya)
    dec = dx - (dy << 1)
    x = xa
    y = ya
    while x <= xb :
        point(x, y, "pink")
        if dec < 0 :
            dec = dec + (dx << 1)
            y = y - 1
        dec = dec - (dy <<1)
        x = x + 1



def Bresenham (pxa , pya , pxb , pyb ,canva) :
    # ATTENTION a l'ordre des parametres (x, y, dimx, dimy) !
    xa, ya = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, pxa, pya)
    xb, yb = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, pxb, pyb)

    # DEBUG
    print('projection', xa, ya, xb, yb)
    canva.create_oval(xa-3, HA-(ya-3), xa+3, HA-(ya+3), fill = "green" )
    canva.create_oval(xb-3, HA-(yb-3), xb+3, HA-(yb+3), fill = "green" )

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
                Octant2(xa, ya, xb, yb)
        elif dy < 0 :
            if dx < abs(dy):
                #octant 7
                print("octant 7 ")
                Octant7(xa, ya, xb, yb)

            elif dx >= abs(dy) :
                print("octant 8 ")
                Octant8(xa, ya, xb, yb)

                #octant 8
    elif dx < 0 :
        if dy >= 0 :
            #octant 3
            if abs(dx) < dy :
                print("octant 3 ")
                Octant3(xa, ya, xb, yb)
            elif abs(dx) >= dy:
                #octant4
                print("octant 4 ")
                Octant4(xa, ya, xb, yb)
                # return Octant1(xa, ya, xb, yb)
        else :
            #octant5
            if abs(dx) > abs(dy):
                print("octant 5 ")
                Octant5(xa, ya, xb, yb)
                # return Octant1(xa, ya, xb, yb)
                #octant6
            else :
                print("octant 6 ")
                Octant6(xa, ya, xb, yb)

                # return Octant2(xa, ya, xb, yb)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("TP02_Infographie")
    canva= tk.Canvas(root,width=LA, height=HA, bd=1)
    canva.pack(padx=10,pady=10)

    # dim puis pos de la viewport
    DimxV, DimyV = 350, 350
    #  /!\ repere local haut gauche => FAUX pour la projection choisie (cf. tp1.py)
    # xviewport, yviewport = 150, 350
    # repere local bas gauche (euclidien)
    xviewport, yviewport = 150, 100

    #dimension puis position de la window
    dimxw = 1000
    dimyw = 1000
    xwindow = 0
    ywindow = 0


    # rect = canva.create_rectangle(xviewport, yviewport, DimxV+xviewport,DimyV+yviewport, fill="white", outline="blue", width=5)#viewport
    rect = canva.create_rectangle(xviewport, HA-yviewport, DimxV+xviewport,HA-(DimyV+yviewport), fill="white", outline="blue", width=5)#viewport

    #l_naif = segment_naif(0,0,20,20,0,0.5)
    # Bresenham(0,0,300,100,canva) #octant1
    # Bresenham(0,0,100,300,canva) #octant2
    # Bresenham(50,0,0,100,canva)  #octant3
    # Bresenham(300,0,0,100,canva) #octant4
    # Bresenham(400,200,200,100,canva) #octant5
    # Bresenham(200,400,100,200,canva) #octant6
    # Bresenham(100,500,200,300,canva) #octant7
    Bresenham(100,100,200,50,canva) #octant8






    root.mainloop()

    exit(0)
