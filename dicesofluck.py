import random #everything starts with a journey
print("rolling the great die")
dice=random.randint(1,6)
print(f"you rolled {dice} !")
if dice==1:
    print("you suck")
elif dice==6:
    print("good")
else:
    print("loser")