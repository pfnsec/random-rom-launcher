import tkinter as tk 
import subprocess
import os
import sys
import yaml
import random

with open("layout.yaml") as f:
    layout = yaml.load(f.read())

consoles = ["nes", "snes", "n64"]

buttons = {}
icons = {}


def myfunction(event):
    console = buttons[event.widget]
    rompath = console['rompath']
    cmd = console['cmd']
    rom = random.choice([x for x in os.listdir(rompath) if os.path.isfile(os.path.join(rompath, x))])
    print(rom)
    if(console['path'] == 'file'):
        subprocess.Popen(cmd.format(rom))
    elif(console['path'] == 'relative'):
        rom = os.path.join(rompath, rom)
        subprocess.Popen(cmd.format(rom))
        print(cmd.format(rom))


class App:
  def __init__(self, master):
    frame = tk.Frame(master)
    frame.pack()
    self.button = tk.Button(frame,
        text="QUIT", fg="red",
        height=100,
        width=100,
        command=sys.exit
    )

    #self.button.pack(side=tk.LEFT)

    for console in layout['consoles']:

        b = tk.Button(
            root, 
            text=console["name"],
            image = icons[console['name']],
            compound=tk.BOTTOM,
            height=100,
            width=100,
        )
        #b.image = img
        b.pack(side=tk.LEFT)
        buttons[b] = console
        b.bind("<Button-1>", myfunction)

        #b.place(x=10,y=(10+(25*i)))

  def write_slogan(self):
    subprocess.Popen(r"F:\Roms\N64\mupen64plus\mupen64plus-gui.exe")

if __name__ == "__main__":
    root = tk.Tk()

    for console in layout['consoles']:
        img = tk.PhotoImage(file=console['icon'])
        #img = tk.PhotoImage(file="garfield.png")
        icons[console['name']] = img

    root.iconbitmap(r"icons/atari 2600.ico")
    root.geometry("800x800")
    app = App(root)
    root.mainloop()