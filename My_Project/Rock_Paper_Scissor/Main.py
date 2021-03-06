import sys
import random

#   Define RPS_list 
RPS_list = {"Rock": 0, "Paper": 1, "Scissor": 2}
random_list = ["Rock", "Paper", "Scissor"]

class Player:
    def __init__(self, name):
        self.name = name
        self.live = 3
        self.point = 0

    def lose_life(self):
        #   Take away life point from user
        self.live -= 1

    def gain_point(self):
        #   Add point to user
        self.point += 1

class RPS(Player):
    def __init__(self, name):
        #   Use super to Initialize the parent class
        super(RPS,self).__init__(name)

        self.player_input = None
        self.computer_input = None

    def clear_up(self):
        self.computer_input = None
        self.plaer_input = None

    def computer_choice(self):
        #   Random choice from the computer
        self.computer_input = random.choice(random_list)

    def user_choice(self):
        #   Check and get the input form the user
        while (self.player_input not in RPS_list):
            self.player_input = input("Please choose Rock, Paper or Scissor : ")
            
            if(self.player_input == ""):
                print("You didn't choose anything")
            
            if(self.player_input not in RPS_list):
                print("Please choose another")
    
    def verify_winner(self):
        #   verify the winner
        player_math = RPS_list.get(self.player_input)
        computer_math = RPS_list.get(self.computer_input)

        #   Lost
        if((player_math + 1) % 3 == computer_math):
            
            #   Make the user lose 1 life 
            self.lose_life()
            print("You lost")

        #   Tie
        elif(player_math == computer_math):
            print("Tie")
        
        #   Win
        else:
            self.gain_point()
            print("You win this move")
        
        self.clear_up()

def exit():
    print("Bye, see you again")
    sys.exit(0)

if __name__ == '__main__':
    
    game = None
    
    while True:
        try:
            if not isinstance(game, RPS):

                temp_name = input("Please enter your name : ")
                game = RPS(temp_name)
                del temp_name
            
            elif (game.live == 0):
                print("Out of move")
                exit()

            elif isinstance(game, RPS):
                game.user_choice()
                game.computer_choice()
                game.verify_winner()
                
                if(input("Would you like to try again ? ").lower() == "no"):
                    break

        except KeyboardInterrupt:
            exit()
