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
    
    def coordinates(self):
        while True:
            coor = input("Enter your coordinates (like 0,0): ")
            coor = coor.split(",")
            x = int(coor[0])
            y = int(coor[1])
            if x<3 and y<3:
                break
            print("coordinates out of range")
        return x,y  
    
    def print_grid(self):
        import time
        print("              WELCOME TO        ")
        time.sleep(0.8)
        print("         TIC")
        time.sleep(0.8)
        print("             TAC")
        time.sleep(0.8)
        print("                 TOE")
        time.sleep(1)
        print(""" Use the coordinate system to mark you sign

                    (0,0) | (0,1) | (0,2)
                    ------+-------+------
                    (1,0) | (1,1) | (1,2)
                    ------+-------+------
                    (2,0) | (2,1) | (2,2)

""")
        l=[[" "," "," "],[" "," "," "],[" "," "," "]]
        first_person = self.choose_player()
        for i in range(9):
            if i%2 == 0:
                time.sleep(0.5)
                print(f"it's your turn {first_person}")
                while True:
                    coor = self.coordinates()
                    if l[coor[0]][coor[1]] ==" ":
                        break
                    print("Box already marked")
                l[coor[0]][coor[1]] = "X"
                print(f"""
                         {l[0][0]} | {l[0][1]} | {l[0][2]}
                        ---+---+---
                         {l[1][0]} | {l[1][1]} | {l[1][2]}
                        ---+---+---
                         {l[2][0]} | {l[2][1]} | {l[2][2]}
""")
                if (l[0][0] == l[0][1] == l[0][2] != " ") or (l[1][0] == l[1][1] == l[1][2] != " ") or (l[2][0] == l[2][1] == l[2][2] != " ") or (l[0][0] == l[1][0] == l[2][0] != " ") or (l[0][1] == l[1][1] == l[2][1] != " ") or (l[0][2] == l[1][2] == l[2][2] != " ") or (l[0][0] == l[1][1] == l[2][2] != " ") or (l[0][2] == l[1][1] == l[2][0] != " "):
                    print(f"{first_person} WINS! ")
                    break
                else:
                    continue
            
            else:
                time.sleep(0.5)
                print("2nd player's turn")
                while True:
                    coor = self.coordinates()
                    if l[coor[0]][coor[1]] ==" ":
                        break
                    print("Box already marked")
                l[coor[0]][coor[1]] = "O"
                print(f"""
                         {l[0][0]} | {l[0][1]} | {l[0][2]}
                        ---+---+---
                         {l[1][0]} | {l[1][1]} | {l[1][2]}
                        ---+---+---
                         {l[2][0]} | {l[2][1]} | {l[2][2]}
""")
                if (l[0][0] == l[0][1] == l[0][2] != " ") or (l[1][0] == l[1][1] == l[1][2] != " ") or (l[2][0] == l[2][1] == l[2][2] != " ") or (l[0][0] == l[1][0] == l[2][0] != " ") or (l[0][1] == l[1][1] == l[2][1] != " ") or (l[0][2] == l[1][2] == l[2][2] != " ") or (l[0][0] == l[1][1] == l[2][2] != " ") or (l[0][2] == l[1][1] == l[2][0] != " "):
                    print("2nd WINS! ")
                    break
                else:
                    continue
        
        print("Draw")            
ttt = TicTacToe()
ttt.print_grid()






                




    

    
    

    




