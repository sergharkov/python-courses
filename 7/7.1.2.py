class Ball:
    def __init__(self, color):
        self.color = color
#        self.str = str
    
    def __str__(self):
        return f"<Ball: {self.color}>"

    def __repr__(self):
        return sefl.__str__()
  
b = Ball("black")   
 