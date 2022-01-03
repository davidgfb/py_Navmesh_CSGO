from tkinter import Tk, Canvas, PhotoImage, Label      

def actualiza():
    global pol
    
    canvas.delete(pol) #"all" borra tmb la imagen
    pol = canvas.create_polygon(ptos, outline=cSeg, fill='')

def click(e):
    global ptos_Seg, seg

    ptos_Seg[:2] = e.x, e.y

    actualiza()
    
    seg = canvas.create_line(x, y, x, y, fill = cSeg)

def release(e): 
    canvas.delete(seg)

def drag(e): #poco eficiente
    global ptos_Seg

    x, y = ptos_Seg[:2]

    x1, y1 = e.x, e.y
    
    ptos_Seg[2:] = x1, y1

    #canvas.coords(seg, x, y, x1, y1)

    '''ulPto = ptos[len(ptos) - 1]
    print(ulPto)'''

seg, pol, ptos_Seg, imagen, ancho, ptos, cSeg, seVeSeg, root =\
     None, None, 4 * [0], "De_mirage_radar.png", 1000, [],\
     "white", True, Tk()
canvas = Canvas(root, width = ancho, height = ancho)

canvas.pack()

img = PhotoImage(file="De_mirage_radar.png")   
canvas.create_image(20,20, anchor="nw", image=img)    

canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag)
canvas.bind("<ButtonRelease-1>", release)

root.mainloop()

'''widget = Label(canvas, text='AAA', fg='white', bg='black')
widget.pack()'''
