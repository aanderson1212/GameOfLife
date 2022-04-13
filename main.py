from board import Board
import pyautogui

def main():
    user_rows = int(input('how many rows? '))
    user_columns = int(input('how many columns? '))

    game_of_life_board = Board(user_rows,user_columns)

    game_of_life_board.draw_board()

    generation = 0
    user_action = ''
    print ('Press enter to begin')
    print ('')
    print ('To stop spam q, sorry about that')
    while user_action != 'q':
        for i in range(5):
            user_action = input()
            pyautogui.press("enter")
       
        if user_action == '':
            generation += 1
            game_of_life_board.update_board()
            game_of_life_board.draw_board()
            
            print ('Generation: ' + str(generation))
        
main()
