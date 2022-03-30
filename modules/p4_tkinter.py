from tkinter import * 
  
class IHM(Frame):
    def __init__(self, fenetre, height, width):
        Frame.__init__(self, fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.pack(fill=BOTH)
        self.data = list()
        for i in range(self.numberLines):
            line = list()
            for j in range(self.numberColumns):
                cell = Entry(self)
                cell.insert(0, 0)
                line.append(cell) 
  

fenetre = Tk() 
interface = IHM(fenetre, 6, 7) 
interface.mainloop()