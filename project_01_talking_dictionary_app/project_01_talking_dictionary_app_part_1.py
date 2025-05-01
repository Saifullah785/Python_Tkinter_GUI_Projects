# import libraries

from tkinter import *
from PIL import ImageTk, Image

# creating a Tk object class
root = Tk()
root.geometry("626x626")
root.title("Talking Dictionary created by saif")
root.resizable(0,0)

# Load the image using Pillow
image = Image.open("E:/python projects/talking_dictionay_project/images/bg2.jpg")
bgimage = ImageTk.PhotoImage(image)

bglabel=Label(root,image=bgimage)
bglabel.place(x=0,y=0)

enterwordlabel = Label(root,text="Enter Word",font=("casteller",29,"bold"),fg="red3",bg="whitesmoke")
enterwordlabel.place(x=180, y=20)

enterwordentry=Entry(root,font=('arial',23,'bold'),justify=CENTER,bd=8,relief=GROOVE)
enterwordentry.place(x=110,y=80)

# Load the search icon image
search_image = Image.open("E:/python projects/talking_dictionay_project/images/iconsearch.png")
searchButton_image = ImageTk.PhotoImage(search_image)


searchButton = Button(root, image=searchButton_image,bd=0,bg='whitesmoke',cursor="hand2",activebackground="whitesmoke")
searchButton.image = searchButton_image  # Keep a reference!
searchButton.place(x=140, y=150)

mic_image = Image.open("E:/python projects/talking_dictionay_project/images/mic.png")
micButton_image = ImageTk.PhotoImage(mic_image)


micButton = Button(root, image=micButton_image,bd=0,bg='whitesmoke',cursor="hand2",activebackground="whitesmoke")
micButton.image = micButton_image  # Keep a reference!
micButton.place(x=240, y=150)

meaninglabel = Label(root,text="Meaning",font=("casteller",29,"bold"),foreground="red3",background="whitesmoke")
meaninglabel.place(x=200, y=240)

textarea=Text(root,width=34,height=8,font=('arial',18,"bold"),bd=8,relief=GROOVE)
textarea.place(x=100, y=300)

audio_image = Image.open("E:/python projects/talking_dictionay_project/images/mic.png")
audio_image = ImageTk.PhotoImage(audio_image)


audio_Button = Button(root, image=audio_image,bd=0,bg='whitesmoke',cursor="hand2",activebackground="whitesmoke")
audio_Button.image = audio_image  # Keep a reference!
audio_Button.place(x=130, y=558)

clear_image = Image.open("E:/python projects/talking_dictionay_project/images/clear.png")
clear_image = ImageTk.PhotoImage(clear_image)


clear_Button = Button(root, image=clear_image,bd=0,bg='whitesmoke',cursor="hand2",activebackground="whitesmoke")
clear_Button.image = clear_image # Keep a reference!
clear_Button.place(x=250, y=558)

exit_image = Image.open("E:/python projects/talking_dictionay_project/images/exit.png")
exit_image = ImageTk.PhotoImage(exit_image)


exit_Button = Button(root, image=exit_image,bd=0,bg='whitesmoke',cursor="hand2",activebackground="whitesmoke")
exit_Button.image = exit_image  # Keep a reference!
exit_Button.place(x=360, y=558)
root.mainloop()