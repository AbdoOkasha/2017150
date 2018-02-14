import time

again=True
while (again):
    again1=False
    NumberOfPlayers= int (input("plase choose 1 or 2 players : "))
    while(NumberOfPlayers>2 or NumberOfPlayers<1):
        NumberOfPlayers = int(input("please enter 1 or 2 :"))
    coins=21
    if (NumberOfPlayers==2):
        while (coins>0):
            player1 = int (input("player 1 trun :\n"))
            while (player1 >3 or player1 <1):
                player1 = int (input("please enter a number between 1 to 3 :\n"))
            coins = coins -player1
            if (coins < 1 ):
                print ("player 1 lost :P ")
            else :
                print ("coins = ",coins)
            if (coins >=1):
                time.sleep(.2)
                player2 = int (input("player 2 trun :\n"))
                while (player2 >3 or player2 <1):
                    player2 = int (input("please enter a number between 1 to 3 :\n"))
                coins = coins -player2
                if (coins < 1 ):
                    print ("player 2 lost :P ")
                else :
                    print ("coins = ",coins)
                    time.sleep(.2)
            
    elif (NumberOfPlayers==1):
        while ( coins >0):
            player1 = int (input("player 1 trun :\n"))
            while (player1 >3 or player1 <1):
                player1 = int (input("please enter a number between 1 to 3 :\n"))
            coins = coins -player1
            if (coins < 1 ):
                print ("player 1 lost :P ")
            else :
                print ("coins = ",coins)

            if ( coins >1 ) :
                comp=4-player1
                coins=coins-comp
                print ("computer turn :")
                time.sleep(.3)
                print (comp)
                print("coins = ",coins)
                time.sleep(.2)
    while again1==False:    
        playagain=input("do you want to play again ? yes / no  ")
        if (playagain == "no"):
            again=False
            again1=True
        elif (playagain == "yes"):
            again1=True
        else :
            print("enter yes or no ")
quit()
                
