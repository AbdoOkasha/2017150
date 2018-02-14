#include <iostream>
#include <windows.h>
using namespace std;

int main()
{
    bool again = 1;
    while (again){
        cout << "please choose 1 or 2 player : ";
        int NumOfPlayers,coins=21,player1,player2,comp;
        string PlayAgain;
        cin >> NumOfPlayers;
        while (NumOfPlayers>2 || NumOfPlayers<1){
            cout << "please enter 1 or 2 :";
            cin >> NumOfPlayers;
        }
        if (NumOfPlayers == 2){
            while (coins > 0){
                cout << "player 1 turn : ";
                cin >> player1;
                while (player1 <1 || player1 >3){
                    cout << "please choose a number between 1 to 3: \n";
                    cin >> player1;
                }
                coins=coins-player1;
                if (coins <1){
                    cout << "player 1 lost :v \n";
                }
                else cout << "coins = "<<coins << "\n";

                if (coins >=1){
                    cout << "player 2 turn : ";
                    cin >> player2;
                    while (player2 >3 || player2<1){
                        cout << "please enter a number between 1 to 3 \n";
                        cin >> player2;
                    }
                    coins = coins - player2;
                    if (coins <1){
                        cout << "player 2 lost :v\n";
                    }
                    else cout <<"coins = "<< coins << "\n";
                }
            }
        }
        else if (NumOfPlayers ==1){
            while (coins >0){
                cout << "player 1 turn : ";
                cin >> player1;
                while (player1 <1 || player1>3){
                    cout << " please enter a number between 1 to 3 :\n";
                    cin >> player1;
                }
                coins = coins - player1;
                if (coins <1 ) cout << "player 1 lost :v \n";
                else cout << "coins = "<< coins << "\n";
                if (coins >1){
                    comp = 4-player1;
                    coins = coins - comp;
                    cout << "computer turn : ";
                    Sleep (300);
                    cout << comp;
                    cout << "\n coins = "<< coins << "\n";
                }
            }
        }
        cout << "do you want play again ? yes / no  ";
        cin >> PlayAgain;
        while ( PlayAgain != "yes" && PlayAgain != "no"){
            cout << "enter yes or no  ";
            cin>> PlayAgain;

        }
        if (PlayAgain=="no") again=0;
    }
}
