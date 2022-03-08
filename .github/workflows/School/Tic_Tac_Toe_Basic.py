from random import choice, randrange

class Person:
    def __init__(self, name, Type, WinStatus):
        self.name = name
        self.Type = Type
        self.WinStatus = WinStatus

    def get_name(self):
        return self.name
    
    def get_Type(self):
        return self.Type
    
    def get_WinStatus(self):
        return self.WinStatus

    def set_WinStatus(self, WonStatus):
        if self.WinStatus == False:
            self.WinStatus = WonStatus
            return self.WinStatus

class Tic_Tac_Toe:
    def __init__(self, Person1, Person2):
        self.Person1 = Person1
        self.Person2 = Person2
    
    def player_first(self):
        first_player = choice([self.Person1.get_name(), self.Person2.get_name()])
        return first_player

    def turn(self, count, player_move, key, board):
        print(player_move.get_name())
        if player_move.get_name() == "Bot":
            move = str(randrange(1, 9))
            if board[move] == " ":
                board[move] = key
                return count
            else:
                while board[move] != " ":
                    move = str(randrange(1, 9))
                    if board[move] == " ":
                        board[move] = key
                        return count

        elif player_move.get_name() != "Bot":
            move = input()
            if board[move] == ' ':
                board[move] = key
                return count
            else:
                while board[move] != " ":
                    move = input()
                    if board[move] == " ":
                        board[move] = key
                        return count

    def Board(self, board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3']) 

    def win_check(self, player, theBoard):
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
            player.set_WinStatus(True)
            print(f'Congratulations {player.get_name()}')
            print("\nGame Over.\n")

            
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
            player.set_WinStatus(True)
            print(f'Congratulations {player.get_name()}')
            print("\nGame Over.\n")                
     
       
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
            player.set_WinStatus(True)
            print(f'Congratulations {player.get_name()}')
            print("\nGame Over.\n")                
     
         
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
            player.set_WinStatus(True)
            print(f'Congratulations {player.get_name()}')
            print("\nGame Over.\n")                
     
        
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
            player.set_WinStatus(True)
            print(f'Congratulations {player.get_name()}')
            print("\nGame Over.\n")                
      
         
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
            player.set_WinStatus(True)
            print(f'Congratulations {player.get_name()}')
            print("\nGame Over.\n")                
            
         
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
            player.set_WinStatus(True)
            print(f'Congratulations {player.get_name()}')  
            print("\nGame Over.\n")                
         
    
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
            player.set_WinStatus(True)
            print(f'Congratulations {player.get_name()}')
            print("\nGame Over.\n")


class Application:
    def main():
        print("Welcome to Tic Tac Toe get three in a row to win!")
        print("Use the numbers 1-9 to put your letter on the board!\nThe Top of the board is 7, 8, 9.\nThe midde of the board is 4, 5, 6.\nThe Bottom of the board is 1, 2, 3.")
        Person_One = Person("PersonOne", "X", False)
        Person_Two = Person("PersonTwo", "O", False)
        solo = input("Are you playing Solo?\ny/n\n")
        if solo == "y":
            Person_Two = Person("Bot", "O", False)            
        else:
            pass
        Showdown = Tic_Tac_Toe(Person_One, Person_Two)
        theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,'4': ' ' , '5': ' ' , '6': ' ' ,'1': ' ' , '2': ' ' , '3': ' ' }
        Showdown.Board(theBoard)
        first_player = Showdown.player_first()
        count = 0


        while Person_One.get_WinStatus() == False or Person_Two.get_WinStatus() == False:
            if first_player == "PersonOne":
                count += 1
                Showdown.turn(count, Person_Two, Person_Two.get_Type(), theBoard)
                Showdown.Board(theBoard)
                player = Person_One
                while player.get_WinStatus() == False or count == 9:
                    count += 1
                    Showdown.turn(count, player, player.get_Type(), theBoard)
                    Showdown.Board(theBoard)
                    Showdown.win_check(player, theBoard)
                    if player.get_WinStatus() == True:
                        return
                    elif count == 9:
                        print("Tie Game!")
                        return
                    elif player == Person_One:
                        player = Person_Two
                    else:
                        player = Person_One

            elif first_player == "PersonTwo" or first_player == "Bot":
                count += 1
                Showdown.turn(count, Person_One, Person_One.get_Type(), theBoard)
                Showdown.Board(theBoard)
                player = Person_Two
                while player.get_WinStatus() == False or count == 9:
                    count += 1
                    Showdown.turn(count, player, player.get_Type(), theBoard)
                    Showdown.Board(theBoard)
                    Showdown.win_check(player, theBoard)
                    if player.get_WinStatus() == True:
                        return
                    elif count == 9:
                        print("Tie Game!")
                        return
                    elif player == Person_Two:
                        player = Person_One
                    else:
                        player = Person_Two
         
if __name__ == "__main__":
    app = Application
    app.main()