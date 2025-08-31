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
        coor = input("Enter your coordinates : ")
        coor = coor.split(",")
        x = int(coor[0])
        y = int(coor[1])
        return x,y  
    
    def print_grid(self):
        l=[[" "," "," "],[" "," "," "],[" "," "," "]]
        first_person = self.choose_player()
        for i in range(9):
            if i%2 == 0:
                print(f"it's your turn {first_person}")
                coor = self.coordinates()
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
                print("2nd player's turn")
                coor = self.coordinates()
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
ttt = TicTacToe()
ttt.print_grid()






                




    

    
    

    




