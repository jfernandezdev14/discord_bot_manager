import tkinter as tk
from tkinter import filedialog

from discord.ext import commands
from threading import Thread

from app.constants import DISCORD_BOT_TOKEN


def start_discord_bot():
    bot = commands.Bot(command_prefix='_', description="I am DevBot")
    bot.load_extension('app.controllers.discord_bot_controller')
    bot.run(DISCORD_BOT_TOKEN)


def onOpen():
    print(filedialog.askopenfilename(initialdir="/", title="Open file",
                                     filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))


def onSave():
    print(filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                       filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))


def start_frame_thread():

    app = tk.Tk()
    app.geometry('300x200')
    app.title("Menu Bar Command")

    menubar = tk.Menu(app)

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=onOpen)
    filemenu.add_command(label="Save", command=onSave)
    filemenu.add_command(label="Exit", command=app.quit)

    menubar.add_cascade(label="File", menu=filemenu)

    app.config(menu=menubar)

    app.mainloop()


def main():

    tk_thread = Thread(
        target=start_frame_thread, args=[]
    )
    tk_thread.start()
    # start_discord_bot()


main()
