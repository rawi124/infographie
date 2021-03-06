#!/usr/bin/python
import tkinter as tk
import math

mat = None  # matrice de transformation

def multiplication(m1,m2):
	"""
	multiplication de deux matrices
	"""
	n = len(m1)
	m = len(m1[0])
	w = len(m2[0])
	j = 0
	l=[]
	k = []
	while j < n:
		i = 0
		while i < w :
			y = 0
			s = 0
			while y < m :
				s = s +m1[j][y]*m2[y][i]
				y = y + 1
			i = i + 1
			k = k+[s]
		l = l + [k]
		k=[]
		j = j + 1
	return l

def transformation_old(o2x , o2y , vx , vy , wx , wy , o1x ,o1y , a , b) :
	"""
	renvoie les coordonnées du point en parametre de parmetre a , b apres transformation matricielle
	ma viewport est d origine le coin superieur gauche

	les deux premiers parametres coordonnées de l origine de la viewport : coin sup gauche
	vx vy dimension de la viewport
	o1x o1y origine de la window
	dimension de la window : wx wy

	"""
	t1 =  [[1,0,-o1x],[0,1,-o1y],[0,0,1]]
	d1 =  [[1/wx,0,0],[0,1/wy,0],[0,0,1]]
	d2 =  [[vx,0,0],[0,vy,0],[0,0,1]]
	s  =  [[1,0,0],[0,-1,0],[0,0,1]]
	t3 =  [[1,0,0],[0,1,vy],[0,0,1]]
	t4 =  [[1,0,o2x],[0,1,o2y],[0,0,1]]
	l =  multiplication(t4,t3)
	l1 = multiplication(l,s)
	l2 = multiplication(l1,d2)
	l3 = multiplication(l2,d1)
	l4 = multiplication(l3,t1)
	point = [[a],[b],[1]]
	l5 = multiplication(l4,point)
	return l5[0],l5[1]

def projection(o2x , o2y , vx , vy , wx , wy , o1x ,o1y , a , b) :
	"""
	renvoie les coordonnées du point en parametre de parmetre a , b apres transformation matricielle
	ma viewport est d origine le coin superieur gauche

	les deux premiers parametres coordonnées de l origine de la viewport : coin sup gauche
	vx vy dimension de la viewport
	o1x o1y origine de la window
	dimension de la window : wx wy

	"""
	global mat
	t1 =  [[1,0,-o1x],[0,1,-o1y],[0,0,1]]
	d1 =  [[1/wx,0,0],[0,1/wy,0],[0,0,1]]
	d2 =  [[vx,0,0],[0,vy,0],[0,0,1]]
	t2 =  [[1,0,o2x],[0,1,o2y],[0,0,1]]

	l1 = multiplication(t2,d2)
	l2 = multiplication(l1,d1)
	mat = multiplication(l2,t1)
	point = [[a],[b],[1]]
	l4 = multiplication(mat,point)
	print(l4)
	return int(l4[0][0]), int(l4[1][0])

def transformation(o2x , o2y , vx , vy , wx , wy , o1x ,o1y , a , b):
	x, y = projection(o2x , o2y , vx , vy , wx , wy , o1x ,o1y , a , b)

	s  =  [[1,0,0],[0,-1,0],[0,0,1]]
	t3 =  [[1,0,0],[0,1,vy],[0,0,1]]

	l =  multiplication(mat, s)
	l1 = multiplication(l, t3)
	point = [[x],[y],[1]]
	l2 = multiplication(l1,point)
	return l2[0],l2[1]

def OpenFichier(fichier,o2x , o2y , vx , vy , wx , wy , o1x ,o1y):
	"""
	permet d ouvrir un fichier , lire ces lignes et recuperer les coordonées ainsi
	 que de les transformer en une séquence de points de la fenêtre écran
	"""
	try:
		files = open(fichier,"r")
		lignes = files.readlines()
		l = []
		for ligne in lignes :
			if ligne[0].isdigit() :
				f = 0
				tupl =()
				while f < 3 :
					if ligne[f].isdigit() :
						tupl = tupl + (int(ligne[f]),)
					f = f + 1
				l = l + [tupl]
		liste = ()
		for el in l :
			liste = liste +  transformation(o2x , o2y , vx , vy , wx , wy , o1x ,o1y,el[0],el[1])
		return liste
		files.close()
	except IOError:
		print("fichier inexistant ")
def dessiner_ensemble_point(tran,canva):
    """
    dessine un ensemble de point
    """
    i = 0
    lis = []
    while i < len(tran) :
        lis.append(canva.create_oval(tran[i][0], tran[i+1], tran[i][0], tran[i+1], fill = "pink" ))
        i = i + 2
    return lis


if __name__ == '__main__':
 root = tk.Tk()
 root.title("TP01_Infographie")
 global canv
 global rect
 global x,y,X,Y

 #dim puis pos de la viewport
 dimxV = 350
 dimyV = 350
 xViewport, yViewport = 150, 350

 #dimension puis position de la window
 dimxW = 20
 dimyW = 20
 xWindow = -10
 yWindow = -10

 Px = 0
 Py = 0
 canv= tk.Canvas(root,width=1000, height=800, bd=1)
 canv.pack(padx=10,pady=10)

 #On cree un rectangle qui est la viewPort
 rect = canv.create_rectangle(xViewport, yViewport, dimxV+xViewport,dimyV+yViewport, fill="white", outline="blue", width=5)#viewport

 l = transformation(xViewport,yViewport,dimxV,dimyV,dimxW,dimyW,xWindow,yWindow,Px,Py)
 #Point = canv.create_oval( l[0] , l[1] , l[0] , l[1] , fill = "pink" )
 trans = OpenFichier("fichier.txt",xViewport,yViewport,dimxV,dimyV,dimxW,dimyW,xWindow,yWindow)
 print(trans)


 lis_id_point = dessiner_ensemble_point(trans)
 def right(event):
    for el in lis_id_point :
        canv.move(el,10,0)
    canv.move(rect,10,0)

 def left(event):
    for el in lis_id_point :
        canv.move(el,-10,0)
    canv.move(rect,-10,0)

 def down(event):
    for el in lis_id_point :
        canv.move(el,0,10)
    canv.move(rect,0,10)

 def up(event):
    for el in lis_id_point :
        canv.move(el,0,-10)
    canv.move(rect,0,-10)


 #On associe les touche du clavier aux fonction:
 canv.bind_all('<Right>',right)
 canv.bind_all('<Left>',left)
 canv.bind_all('<Up>',up)
 canv.bind_all('<Down>',down)

 root.mainloop()

 exit(0)
