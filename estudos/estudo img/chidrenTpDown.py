
# importing only those functions
# which are needed
from tkinter import * 
from tkinter.ttk import *
from PIL import Image, ImageTk 
import os.path

# creating tkinter window

def telaBtn():
    #root = Tk()
    root = Toplevel()

    # Adding widgets to the root window
    Label(root, text = 'GeeksforGeeks', font =(
    'Verdana', 15)).pack(side = TOP, pady = 10)
    
    img = Image.open("imagens/img_cad_ferr.png")
    imgNw=img.resize((48, 48))
    my_img=ImageTk.PhotoImage(imgNw)
 
    #photo = PhotoImage(file = r"imagens/img_cad_ferr.png")
    
    # here, image option is used to
    # set image on button
    my=Button(root, text = 'Click Me !', image = my_img).pack(side = TOP)
    my.draw()
    
    #mainloop()