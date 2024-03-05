from var import *
from lib import *

def gui(tk):
    #window
    window = tk.Tk()
    window.title(f"Jarvis AI: {type}")
    window.geometry(f"{x}x{y}")
    #label
    hello = tk.Label(text="Hello world!")
    #text 
    log = tk.Text(window, height=10, width=10)
    #.pack()
    hello.pack()
    log.pack()
    tk.mainloop()
