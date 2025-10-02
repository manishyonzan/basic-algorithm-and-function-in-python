class Board:
    _board_positions = []
    def __init__(self):
        for x in range(8):
            for y in range(8):
                self._board_positions.append((x+1,y+1,None))

# ♜, ♞, ♝, ♛, ♚, ♟ for black and ♖, ♘, ♗, ♕, ♔, ♙
class Piece:
    color = ""
    position = [0,0]
    representation = ''
    def __init__(self, position:list[int],color:str, representation):
        if (type(position) == list and len(position) == 2):
            for each in position:
                if each > 8 or each < 1 or color not in ["white","black"]:
                    raise "Invalid position or color values"
                    return
                else:
                    self.color = color
                    self.position = position
                    self.representation = representation
        else:
            raise f"Wrong position values{self.representation}"
    def check_destination_value(self,destination):
        if len(destination) != 2:
            print("Invalid value of destination")
            return
        row,col = destination
        if row > 0 and row < 9 and  col > 0 and col < 9:
            return True
        else:
            print("wrong move",self.color,self.representation, "out of matrix")
            return False
class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__(position, color,"♟")
    def move(self,destination):
        if not super().check_destination_value(destination):
            return 
        if self.position[0] + 1 == destination[0] and destination[1] in [self.position[1], self.position[1] + 1 , self.position[1] -1]:
             # call the game and check for obstruction and update
          
            print("right move")
            pass
        else:
            print("wrong move",self.color,self.representation)
        

class Rook(Piece):
    def __init__(self, position, color,):
        super().__init__(position, color,"♜")
    def move(self,destination):
        if not super().check_destination_value(destination):
            return 
        if self.position[0] == destination[0] or self.position[1] == destination[1]:
             # call the game and check for obstruction and update
          
            print("right move")
        else:
            print("wrong move",self.color, self.representation)
class Knight(Piece):
    def __init__(self, position, color):
        super().__init__(position, color,"♞")
    def move(self,destination):
        if not super().check_destination_value(destination):
            return 
        if (abs(destination[0] - self.position[0]), abs(destination[1] - self.position[1])) in [(2, 1), (1, 2)]:
            # call the game and check for obstruction and update
            print("right move")
        else:
            print("wrong move",self.color,self.representation)
class Bishop(Piece):
    def __init__(self, position, color):
        super().__init__(position, color, "♝")
    def move(self,destination):
        if not super().check_destination_value(destination):
            return 
        if abs(destination[0] - self.position[0]) == abs(destination[1] - self.position[1]):
            # call the game and check for obstruction and update
            print("right move")
        else:
            print("wrong move",self.color,self.representation)
            
class Queen(Piece):
    def __init__(self, position, color, representation):
        super().__init__(position, color, "♛")
    def move(self, destination):
        if not super().check_destination_value(destination):
            return 
        if (abs(destination[0] - self.position[0]) == abs(destination[1] - self.position[1])) or (self.position[0] == destination[0] or self.position[1] == destination[1]):
             # call the game and check for obstruction and update
          
            print("right move")
        else:
            print("wrong move",self.color,self.representation)
        
class King(Piece):
    def __init__(self, position, color):
        super().__init__(position, color, "♚")
    def move(self,destination):
        if not super().check_destination_value(destination):
            return
        if (abs(destination[0] - self.position[0]) <= 1) and (abs(destination[1] - self.position[1])<=1):
             # call the game and check for obstruction and update
           
            print("right move") 
        else:
            print("wrong move",self.color,self.representation)




        
        