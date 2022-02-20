import tkinter as tk
import math
from tp1 import transformation ,multiplication

def segment_naif(x1,y1,x2,y2,coeff_directeur,pas):
    """
    renvoie les valeurs de y pour un x donné avec un coeff_directeur 
    et un pas entre les differents points
    """
    liste_y = []
    pente = (y2-y1)/(x2-x1)
    x = x1
    while x <= x2 :
        y = pente*x + coeff_directeur
        liste_y.append((x,y))
        canva.create_oval(x, y, x, y, fill = "pink" )
        x = x + pas

    return liste_y


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
    dimxw = 200
    dimyw = 200
    xwindow = -100
    ywindow = -100

    px = 0
    py = 0
    rect = canva.create_rectangle(xviewport, yviewport, DimxV+xviewport,DimyV+yviewport, fill="white", outline="blue", width=5)#viewport

    l = segment_naif(0,0,20,20,0,0.5)
    for el in l :
        tran=transformation(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow,el[0],el[1])
        canva.create_oval(tran[0], tran[1], tran[0], tran[1], fill = "pink" )


    root.mainloop()

    exit(0)
