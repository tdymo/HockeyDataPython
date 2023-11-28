from hockeyGUI import *

def main():
    window = tkinter.Tk()
    window.geometry('450x400')
    window.title("Rangers Team-Player Stats")
    window.resizable(False, False)
    
    hockeyGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()