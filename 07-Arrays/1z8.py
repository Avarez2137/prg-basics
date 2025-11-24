computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

sorted = sorted(computer_games)
print(sorted)
i = 0
while i < len(sorted):
    print(i+1, sorted[i]) 
    i+=1