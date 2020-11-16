from tkinter import *
from classes.placeImage import PlaceImage
from classes.placeGif import PlaceGif
from classes.placeText import PlaceTxt
from classes.placeGraph import *
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
import pandas as pd
# from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

plt.rcParams['toolbar'] = 'None'
root = Tk()
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
fig.patch.set_facecolor('#2E3347')



def graph(i):
    data = pd.read_csv('dataFiles/data.csv')
    x = data['HOUR']
    y = data['MSG']
    holder = [i.split('/') for i in y]
    ynew = [i[0] for i in holder]
    ynew = [int(i) for i in ynew]
    print(ynew)

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax1.plot(x, ynew)
    ax1.set_title('windmolen')

    ax2.plot(x, ynew)
    ax2.set_title('batterij')

    ax3.plot(x, ynew)
    ax3.set_title('windmolen')
    
    ax4.plot(x, ynew)
    ax4.set_title('e3')


    plt.cla()
def test():
    global fig,ax1,ax2,ax3,ax4
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
    fig.patch.set_facecolor('#2E3347')
    ani = animation.FuncAnimation(fig,graph,interval=1000)
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()

    # ani = FuncAnimation(plt.gcf(), graph, interval=1000)
# ===== niet veranderen


root.geometry("1920x1080")
root.bind('<Escape>', quit)
SCREENWIDTH = root.winfo_screenwidth()
SCREENHEIGHT = root.winfo_screenheight()


def quit(event):
    root.quit()


root.attributes("-fullscreen", True)
canvas = Canvas(root, height=1080, width=1920,
                highlightthickness=0, background='#2E3347')
canvas.pack(fill="both", expand=True)
fig = Figure(figsize=(5, 5))

xpng = ImageTk.PhotoImage(Image.open('rsc/data.png'))
graphButton = Button(canvas,text='test...', anchor='center', command=test, borderwidth=0, bd=0, highlightthickness=0)
graphButton.place(x=SCREENWIDTH - 191.5, y=0)
