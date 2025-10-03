class Board:
    board_positions = {}
    def __init__(self):
        for x in range(8):
            for y in range(8):
                self.board_positions[f"{x+1}{y+1}"] =  None
                
    def getboard(self):
        print(self.board_positions)
        
    def change_position(self,destination, piece):
        self.board_positions[f"{destination[0]}{destination[1]}"] = piece
        
    def get_piece_at_position(self,destination):
        return self.board_positions[f"{destination[0]}{destination[1]}"]

# ♜, ♞, ♝, ♛, ♚, ♟ for black and ♖, ♘, ♗, ♕, ♔, ♙
class Piece:
    color = ""
    position = [0,0]
    representation = ''
    def __init__(self, position:list[int],color:str, representation, board):
        if (type(position) == list and len(position) == 2):
            for each in position:
                if each > 8 or each < 1 or color not in ["white","black"]:
                    raise "Invalid position or color values"
                    return
                else:
                    self.color = color
                    self.position = position
                    self.representation = representation
                    # board[f'{position[0]}{position[1]}'] = self
                    board.change_position(position,self)
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
    def __init__(self, position, color,board):
        super().__init__(position, color,"♟",board)
    def move(self,destination, board):
        if not super().check_destination_value(destination):
            return 
        if self.position[0] + 1 == destination[0] and destination[1] in [self.position[1], self.position[1] + 1 , self.position[1] -1]:
             # call the game and check for obstruction and update
             
             if not self.is_obstructed(destination,board):
                 "not obstructed"
                 
                #  move the piece to new position
                 board.change_position(destination,self)
                 
                 #Empty the previous position
                 board.change_position(self.position, None)
             else:
                 print('wrong move')
                 return None
        else:
            print("wrong move",self.color,self.representation)
            
    def is_obstructed(self,destination,board):
        
        piece_at_destination = board[f"{destination[0]}{destination[1]}"]
        
        if not piece_at_destination:
            'not obstructed'
            return False
        
        if piece_at_destination.color == self.color:
            return True
        
        

class Rook(Piece):
    def __init__(self, position, color,board):
        super().__init__(position, color,"♜",board)
    def move(self,destination, board):
        if not super().check_destination_value(destination):
            return 
        if self.position[0] == destination[0] or self.position[1] == destination[1]:
             # call the game and check for obstruction and update
             
            if not self.is_obstructed(destination,board):
                 "not obstructed"
                 
                #  move the piece to new position
                 board.change_position(destination,self)
                 
                 #Empty the previous position
                 board.change_position(self.position, None)
                 
          
            print("right move")
        else:
            print("wrong move",self.color, self.representation)
            
    def is_obstructed(self,destination,board):
        is_move_direction_in_row = destination[0] == self.position[0]
        
        if is_move_direction_in_row:
            is_current_position_less =   self.position[1] < destination[1]
            if is_current_position_less:
                
                piece_in_between = False
                for each in range(self.position[1],destination[1]):
                    # check piece between the position and destination
                    if board.get_piece_at_position([self.position[0],each]):
                        piece_in_between = True
                return piece_in_between
            else:
                piece_in_between = False
                for each in range(destination[1],self.position[1]):
                    # check piece between the position and destination
                    # board[f'{self.position[0]}{each}'] 
                    if board.get_piece_at_position([self.position[0],each]):
                        piece_in_between = True
                return piece_in_between
        else:
            # move is in y-direction
            is_current_position_less = self.position[0] < destination[0]
            if is_current_position_less:
                piece_in_between = False
                for each in range(self.position[0],destination[0]):
                    # check piece between the position and destination
                    if board.get_piece_at_position([each,self.position[0]]):
                        piece_in_between = True
                return piece_in_between
            else:
                piece_in_between = False
                for each in range(destination[1],self.position[1]):
                    # check piece between the position and destination
                    if board.get_piece_at_position([each,self.position[0]]):
                        piece_in_between = True
                return piece_in_between
            
                 
                    
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




        
b = Board()
b.getboard()

pawn1_black = Pawn([1,3],"black", b)
rook1_black = Rook([1,1],"black",b)
rook1_black.move([1,4],b)

