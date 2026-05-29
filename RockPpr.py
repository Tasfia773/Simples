import random
item_list=["Rock","Paper","Scissor"]
user_input=input("Choose One : ")
comp_input=random.choice(item_list)
print(f"You chose : {user_input}")
print(f"Computer chose : {comp_input}")
if(user_input==comp_input):
    print("It's a Tie")
elif(user_input=="Rock"):
    if(comp_input=="Paper"):
        print("Computer Won")
    else:
        print("You Won")
elif(user_input=="Paper"):
    if(comp_input=="Rock"):
        print("You Won")
    else:
        print("Computer Won")
elif(user_input=="Scissor"):
    if(comp_input=="Rock"):
        print("Computer Won")
    else:
        print("you Won")

