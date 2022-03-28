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
                cell.grid(row = i, column = j) 
            self.data.append(line) 
  
        self.results = list() 
        for i in range(self.numberColumns): 
            cell = Entry(self) 
            cell.insert(0, 0) 
            cell.grid(row = self.numberLines, column = i) 
            self.results.append(cell) 
        self.buttonSum =  Button(self, text="somme des colonnes", fg="red", command=self.sumCol) 
        self.buttonSum.grid(row = self.numberLines, column = self.numberColumns) 
  
    def sumCol(self): 
        for j in range(self.numberColumns): 
            result = int(0) 
            for i in range(self.numberLines): 
                result += int(self.data[i][j].get()) 
            self.results[j].delete(0, END) 
            self.results[j].insert(0, result)

fenetre = Tk() 
interface = IHM(fenetre, 6, 7) 
interface.mainloop()