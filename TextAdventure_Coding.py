print("Hello there.")
name = input("What's your name?~ ")
print("Hello " + str(name) + "!")
print("What type of colors do you like?")
cool = "a) I like cool colors!\n"
warm = "b) I like warm colors!"
print(str(cool) + str(warm))
question_1 = input("a or b: ")
#print(str(cool) + str(warm))

if question_1 == "a":
    no = "a) No thanks."
    yes = "b) Sure, I would love to meet more people like Bob!"
    print("That's great!")
    print("This is Bob: ◉_◉ . He likes cool colors too.")
    print("Do you want to meet more characters like Bob?")
    no_thx = "a) No thanks. I don't really feel like meeting Bob's buddies.\n"
    character = "b) Sure, I would love to meet more characters!"
    print(str(no_thx) + str(character))
    question_2 = input ("a or b:")
    if question_2 == "a":
        print("Aw, maybe next time.")
        print("Do you prefer the summer or winter months?")
        winter = "a) I like the winter months. \n"
        summer = "b) I like the summer months"
        print(str(winter) + str(summer))
        question_3 = input("a or b:")
        if question_3 == "a":
             print("Cool. Happy winter!!")
        elif question_3 == "b":
             print("That's great, summer is amazing.")
    elif question_2 == "b":
        print("Yay!!")
        print("")
elif question_2 == "b":
    print("something")

winter = "a) I like the winter months."
summer = "b) I like the summer months"
#print("Do you prefer winter months or summer months?")


#print("MEET BOB ◉_◉")
