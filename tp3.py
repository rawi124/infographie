#!/usr/bin/python
import tkinter as tk
import math
from tp1 import projection
from tp2 import projection

LA, HA = 1000, 800


def point(px, py, pcoul,canva):
    """
    affichage dans le repère écran d'un point (px, py) défini dans le repère euclidien
    pcoul couleur du pixel correspondant
    canva canvas unique, HA hauteur du canvas
    """
    canva.create_line(px, HA-py, px+1, HA-py, fill=pcoul)

def equation_X_Y(xa, ya, xb, yb, xc, yc, xd, yd, t):
    """
    prend en entree une liste contenant les coordonées des 4 points de la courbe de bezier
    et t qui est entre 0 et 1 , et renvoie x(t),y(t) sous forme de tuple
    """
    B3_0 = (1-t)**3
    B3_1 = 3*t -6*t**2 + 3*t**3
    B3_2 = 3*t**2 - 3*t**3
    B3_3 = t**3
    return B3_0 *xa + B3_1 *xb + B3_2*xc + B3_3*xd, B3_0 *ya + B3_1 *yb + B3_2*yc + B3_3*yd

def courbe_Bezier_Bernstein(xA, yA, xB, yB, xC, yC, xD, yD , N, canva):
    """
    prend en entree une liste contenant les coordonées des 4 points de la courbe de bezier
    et N ( nombre de points d’interpolation) et dessine la courbe correspondante avec la methode
    de Bernstein
    """
    pas = 1 / N # 1 / N pour savoir on fait varier t de combien ( selon le nombre N saisie par l utilisateur )
    t = 0
    xa, ya = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, xA, yA)
    xb, yb = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, xB, yB)
    xc, yc = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, xC, yC)
    xd, yd = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, xD, yD)

    canva.create_oval(xa-3, HA-(ya-3), xa+3, HA-(ya+3), fill = "green" )
    canva.create_oval(xb-3, HA-(yb-3), xb+3, HA-(yb+3), fill = "green" )
    canva.create_oval(xc-3, HA-(yc-3), xc+3, HA-(yc+3), fill = "green" )
    canva.create_oval(xd-3, HA-(yd-3), xd+3, HA-(yd+3), fill = "green" )

    while (t < 1):
        pt = equation_X_Y(xa, ya, xb, yb, xc, yc, xd, yd, t)
        point(pt[0], pt[1], "black", canva)
        t = t + pas

def combinaison_lineaire(A,B,t):
    """renvoie le point tA + (1-t)B
    avec A un point du plan
    """
    u = t
    v = 1-t
    return [A[0]*u+B[0]*v,A[1]*u+B[1]*v]

def barycentre(xa, ya, xb, yb, xc, yc, xd, yd, t):
    """
    calcule le barycentre des deux points a(xa, xb) et b(xb, yb)
    """
    l = []
    l.append([(1-t)*xa + t*xb, (1-t)*ya + t*yb])
    l.append([(1-t)*xb + t*xc, (1-t)*yb + t*yc])
    l.append([(1-t)*xc + t*xd, (1-t)*yc + t*yd])
    l.append([(1-t)*l[0][0] + t*l[1][0], (1-t)*l[0][1] + t*l[1][1]])
    l.append([(1-t)*l[1][0] + t*l[2][0], (1-t)*l[1][1] + t*l[2][1]])
    l.append([(1-t)*l[2][0] + t*l[3][0], (1-t)*l[2][1] + t*l[3][1]])
    l.append([(1-t)*l[3][0] + t*l[4][0], (1-t)*l[3][1] + t*l[4][1]])
    return l[6][0], l[6][1]

def bezier_Algo(xA, yA, xB, yB, xC, yC, xD, yD , N, canva):
    pas = 1 / N # 1 / N pour savoir on fait varier t de combien ( selon le nombre N saisie par l utilisateur )
    t = 0

    xa, ya = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, xA, yA)
    xb, yb = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, xB, yB)
    xc, yc = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, xC, yC)
    xd, yd = projection(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow, xD, yD)

    canva.create_oval(xa-3, HA-(ya-3), xa+3, HA-(ya+3), fill = "green" )
    canva.create_oval(xb-3, HA-(yb-3), xb+3, HA-(yb+3), fill = "green" )
    canva.create_oval(xc-3, HA-(yc-3), xc+3, HA-(yc+3), fill = "green" )
    canva.create_oval(xd-3, HA-(yd-3), xd+3, HA-(yd+3), fill = "green" )
    while (t < 1):
        pt = barycentre(xa, ya, xb, yb, xc, yc, xd, yd, t)
        point(pt[0], pt[1], "black", canva)
        t = t + pas
cli = 0
liste = []

def clic(event):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    global cli
    cli = cli + 1
    global liste
    liste.append(X)
    liste.append(Y)

    if (cli % 4) == 0 :
        pas = 1 / 100 # 1 / N pour savoir on fait varier t de combien ( selon le nombre N saisie par l utilisateur )
        t = 0
        xa, ya, xb, yb, xc, yc, xd, yd = liste[0],liste[1], liste[2], liste[3], liste[4], liste[5], liste[6], liste[7]
        liste = []
        canva.create_oval(xa+3, ya, xa+3, ya, fill = "green" )
        canva.create_oval(xb+3, yb, xb+3, yb, fill = "green" )
        canva.create_oval(xc+3, yc, xc+3, yc, fill = "green" )
        canva.create_oval(xd+3, yd, xd+3, yd, fill = "green" )

        while (t < 1):
            pt = barycentre(xa, ya, xb, yb, xc, yc, xd, yd, t)
            canva.create_line(pt[0], pt[1], pt[0]+1, pt[1], fill="black")
            t = t + pas



if __name__ == '__main__':
    root = tk.Tk()
    root.title("TP03_Infographie")
    canva = tk.Canvas(root,width=LA, height=HA, bd=1)
    canva.pack(padx=10,pady=10)

    # dim puis pos de la viewport
    DimxV, DimyV = 350, 350

    # repere local bas gauche (euclidien)
    xviewport, yviewport = 150, 100

    #dimension puis position de la window
    dimxw = 1000
    dimyw = 1000
    xwindow = 0
    ywindow = 0

    # rect = canva.create_rectangle(xviewport, yviewport, DimxV+xviewport,DimyV+yviewport, fill="white", outline="blue", width=5)#viewport
    rect = canva.create_rectangle(xviewport, HA-yviewport, DimxV+xviewport,HA-(DimyV+yviewport), fill="white", outline="blue", width=5)#viewport
    courbe_Bezier_Bernstein(0, 100, 200, 500, 500, 400, 600, 0, 100, canva)
    bezier_Algo(0, 0, 0, 100, 100, 100, 100, 0, 100, canva)
    canva.bind('<Button-1>', clic)
    root.mainloop()
    exit(0)
