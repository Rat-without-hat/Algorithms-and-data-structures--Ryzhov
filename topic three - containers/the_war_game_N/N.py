from collections import deque

deck_first_player = deque(list(map(int, input().split())))
deck_second_player = deque(list(map(int, input().split())))

for cnt_step in range(10**6):
    if(not(deck_first_player)):
        print(f"second {cnt_step}")
        break
    elif(not(deck_second_player)):
        print(f"first {cnt_step}")
        break

    if((deck_first_player[0] == 0) and (deck_second_player[0] == 9)):
        deck_first_player.append(deck_first_player.popleft())
        deck_first_player.append(deck_second_player.popleft())
    elif((deck_second_player[0] == 0) and (deck_first_player[0] == 9)):
        deck_second_player.append(deck_first_player.popleft())
        deck_second_player.append(deck_second_player.popleft())
    elif(deck_first_player[0] > deck_second_player[0]):
        deck_first_player.append(deck_first_player.popleft())
        deck_first_player.append(deck_second_player.popleft())
    else:
        deck_second_player.append(deck_first_player.popleft())
        deck_second_player.append(deck_second_player.popleft())
else:
    print("botva")
    