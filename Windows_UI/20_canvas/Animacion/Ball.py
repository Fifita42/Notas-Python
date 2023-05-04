class Ball:
    def __init__(self,canvas,x,y,diameter,xVELOCITY,yVELOCITY,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVELOCITY = xVELOCITY
        self.yVELOCITY = yVELOCITY
        
    def move(self):
        coordinates = self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVELOCITY = -self.xVELOCITY
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVELOCITY = -self.yVELOCITY
        self.canvas.move(self.image,self.xVELOCITY,self.yVELOCITY)