# A  player starts with 3 lives. Each round, ask "Did you survive this level? (yes/no)". If "no",
# lose a life. Keep playing rounds until lives reach 0, then print "Game Over".
player_lives = 3
while player_lives > 0:
    answer = input("Did you survive this level (yes/no): ")
    if answer == "no":
        player_lives -= 1
    print(f"Remaining lives of player are: {player_lives}")
print("Game Over!")

    
        
