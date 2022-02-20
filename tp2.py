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
    x_dep = min(x1,x2)
    x_fin = max(x1,x2)
    while x_dep <= x_fin :
        y = pente*x_dep + coeff_directeur
        liste_y.append((x_dep,y))
        canva.create_oval(x_dep, y, x_dep, y, fill = "pink" )
        x_dep = x_dep + pas

    return liste_y
    
def Octant1(xa , ya , xb , yb ):
	dx = xb - xa
	dy = yb -ya
	dec = dx - (dy << 1)
	x = xa 
	y = ya
	liste = []
	while x <= xb :
		print("octant 1 ")
		liste.append((x,y))
		if dec < 0 :
			dec = dec + (dx << 1)
			y = y + 1
		dec = dec - (dy <<1)
		x = x +1
	return liste

def Octant2(xa , ya , xb , yb ):
	dx = xb - xa
	dy = yb -ya
	dec = dy - (dx << 1)
	x = xa 
	y = ya
	liste = []
	while y <= yb :
		print("octant 2")
		liste.append((x,y))
		if dec < 0 :
			dec = dec + (dy << 1)
			x = x + 1
		dec = dec - (dx <<1)
		y = y +1
	return liste

	




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

    #l_naif = segment_naif(0,0,20,20,0,0.5)
    l_Octant1 = Octant2(25,40,50,50)
    l_Octant2 = Octant1(25,40,50,50)
    #pour iterer deux listes en meme temps de meme taille utiliser zip
    for el in l_Octant1   :
        tran=transformation(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow,el[0],el[1])
        canva.create_oval(tran[0], tran[1], tran[0], tran[1], fill = "pink" )
    #for el in l_Octant2   :
        #tran=transformation(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow,el[0],el[1])
        #canva.create_oval(tran[0], tran[1], tran[0], tran[1], fill = "pink" )
        #trans=transformation(xviewport,yviewport,DimxV,DimyV,dimxw,dimyw,xwindow,ywindow,ell[0],ell[1])
        #canva.create_oval(trans[0], trans[1], trans[0], trans[1], fill = "pink" )
    root.mainloop()

    exit(0)
