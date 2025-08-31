class TicTacToe:
    def player_name(self):
        player1 = input("Enter the name of player 1 :")
        player2 = input("Enter the name of player 2 :")
        return player1,player2
    
    def choose_player(self):
        import random
        idx = random.randint(0,1)
        player = self.player_name()
        return player[idx]
    
    def coordinates():
        coor = input("Enter your coordinates : ")
        coor = coor.split(",")
        x = int(coor[0])
        y = int(coor[1])
        return x,y    
    

    
    

    




