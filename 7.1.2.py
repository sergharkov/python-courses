class Ball:
    def __init__(self, color):
        self.color = color  
    def __str__(self):
        return f"<Ball: {self.color}>"

    def __repr__(self):
        return f"<ball: {self.color}>"
    
