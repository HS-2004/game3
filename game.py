from IPython.display import clear_output
boat_side='Right'
missionaries_on_right=3
cannibals_on_right=3
missionaries_on_left=0
cannibals_on_left=0
print('M=',missionaries_on_left,'C=',cannibals_on_left,'boat','M=',missionaries_on_right,'C=',cannibals_on_right)


while True :

    Missionaries=int(input('enter no of missionaries: '))
    Cannibals=int(input('enter no of cannibals  :'))

    if 0< Missionaries + Cannibals <=2:
        print("valid move 1")
    else:
        print('invalid move 1')
        continue

    if boat_side =='Right':
        print('...........b :')


        if Missionaries>missionaries_on_right or Cannibals>cannibals_on_right:
            print('invalid move 2')
            continue
        else:
            print('valid move')
        missionaries_on_right=missionaries_on_right-Missionaries
        cannibals_on_right=cannibals_on_right-Cannibals
        missionaries_on_left=missionaries_on_left+Missionaries
        cannibals_on_left=cannibals_on_left+Cannibals

        print('M=',missionaries_on_left,'c=',cannibals_on_left,'b......','M=',missionaries_on_right,'C=',cannibals_on_right)
        boat_side ="Left"


    else:
        print('b.........')

        if Missionaries>missionaries_on_left or Cannibals>cannibals_on_left:
            print('Invalid move2')
            continue
        else:
            print('valid move2')

        missionaries_on_left=missionaries_on_left-Missionaries
        cannibals_on_left=cannibals_on_left-Cannibals
        missionaries_on_right=missionaries_on_right+Missionaries
        cannibals_on_right=cannibals_on_right+Cannibals

        print('M=',missionaries_on_left,'C=',cannibals_on_left,'.......b','M=',missionaries_on_right,'C=',cannibals_on_right)
        boat_side='Right'

    if missionaries_on_right<cannibals_on_right and missionaries_on_right>0:
        print('YOU LOSE')
        break
    elif missionaries_on_left<cannibals_on_left and missionaries_on_left>0 :
        print('YOU LOSE')
        break

    if missionaries_on_left==3 and cannibals_on_left==3:
        print('YOU WIN')
        break
print('GAME OVER')