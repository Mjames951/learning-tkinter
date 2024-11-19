from tkinter import *
from tkinter import ttk
from PIL import ImageTk as itk, Image as img
import tools

root = Tk()
rootwidth = root.winfo_screenwidth()
rootheight = root.winfo_screenheight()

wunit = rootwidth / 100
hunit = rootheight / 100

root.title("pingas")
root.attributes("-fullscreen", True)
#root.option_add('*tearOff', FALSE)

def stop():
    exit()

exitButton = ttk.Button(root, command=stop, text="exit")
exitButton.place(x=rootwidth - exitButton.winfo_reqwidth(),y=0)

test_image = img.open('test-image.png')
test_image = test_image.resize((10,10))

text_label = ttk.Label(root, text="yo wuddup").place()
feet = ttk.Label(root, text="FEET")
feet.place(x=10, y=10)

button = ttk.Button(root)
button['image'] = itk.PhotoImage(test_image)

tools.check_options(root)
print(button.configure())

button.place(x=50, y=50)

root.mainloop()