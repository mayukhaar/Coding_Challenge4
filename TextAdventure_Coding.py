points = 0
print("Hello there.")
name = input("What's your name?~ ")
chr_inv = "Character Inventory: "
print("Hello " + str(name) + "!")
print(str(chr_inv) + str(name))
print(str("Points: ") + str(points + 1))
print("What type of colors do you like?")
cool = "a) I like cool colors!\n"
warm = "b) I like warm colors!"
print(str(cool) + str(warm))
question_1 = input("a or b: ")
if question_1 == "a" or question_1 == "A":
    print("That's great!")
    print("This is Bob: ◉_◉ . He likes cool colors too.")
    print(str("Points: ") + str(points + 2))
    print(str(chr_inv) + str(name) + str(", Bob"))
    print("Do you want to meet more characters like Bob?")
    no_thx = "a) No thanks. I don't really feel like meeting Bob's buddies.\n"
    character = "b) Sure, I would love to meet more characters!"
    print(str(no_thx) + str(character))
    question_2 = input("a or b:")
    if question_2 == "a" or question_2 == "A":
        print(question_2)
        print("Aw, maybe next time.")
        print(str("Points: ") + str(points + 3))
        print("Do you prefer the summer or winter months?")
        winter = "a) I like the winter months. \n"
        summer = "b) I like the summer months"
        print(str(winter) + str(summer))
        question_3 = input("a or b:")
        if question_3 == "a" or question_3 == "A":
             print("Cool. Happy winter!!")
             print(str("Points: ") + str(points + 4))
        elif question_3 == "b" or question_3 == "B":
             print("That's great, summer is amazing.")
             print(str("Points: ") + str(points) + 4)
        else:
            print("Invalid response.")
    elif question_2 == "b" or question_2 == "B":
        print("Yay!!")
        print("This is Bob's friend Freddie: (~˘▾˘)~")
        print("And this is Daisy: \ (•◡•) /")
        print(str(chr_inv) + str(name) + str(", Bob") + str(", Freddie") + str(", Daisy"))
        print(str("Points: ") + str(points + 4))
        winter = "a) I like the winter months. \n"
        summer = "b) I like the summer months."
        print("Do you prefer the summer or winter months?")
        print(str(winter) + str(summer))
        question_3 = input("a or b:")
        if question_3 == "a" or question_3 == "A":
            print("Cool. Happy winter!!")
            print(str("Points: ") + str(points + 5))
        elif question_3 == "b" or question_3 == "B":
            print("That's great, summer is amazing.")
            print(str("Points: ") + str(points + 5))
        else:
            print("Invalid response.")
    else:
        print("Invalid response.")
elif question_1 == "b" or question_1 == "B":
    no = "a) No thanks. I don't really feel like meeting Sally's buddies.\n"
    yes = "b) Sure, I would love to meet more people like Sally!"
    print("That's great!")
    print("This is Sally: (｡◕‿◕｡) .She likes warm colors too.")
    print(str(chr_inv) + str(name) + str(", Sally"))
    print(str("Points: ") + str(points + 2))
    print("Do you want to meet more characters like Sally?")
    print(str(no) + str(yes))
    question_2 = input("a or b:")
    if question_2 == "a" or question_2 == "A":
        print("Aww, maybe next time.")
        print(str("Points: ") + str(points + 3))
        print("Do you prefer the summer or winter months?")
        winter = "a) I like the winter months. \n"
        summer = "b) I like the summer months."
        print(str(winter) + str(summer))
        question_3 = input("a or b:")
        if question_3 == "a" or question_3 == "A":
            print("Cool. Happy winter!!")
            print(str("Points: ") + str(points + 4))
        elif question_3 == "b" or question_3 == "B":
            print("That's great, summer is amazing.")
            print(str("Points: ") + str(points + 4))
        else:
            print("Invalid response.")
    elif question_2 == "b" or question_2 == "B":
        print("Yay!!")
        print("This is Sally's sister Marcy: (◕‿◕✿) .")
        print("And this is Sally's best friend Tim: (─‿‿─) .")
        print(str(chr_inv) + str(name) + str(", Sally") + str(", Marcy") + str(", Tim"))
        print(str("Points: ") + str(points + 5))
        print("Do you prefer the summer or winter months?")
        winter = "a) I like the winter months. \n"
        summer = "b) I like the summer months"
        print(str(winter) + str(summer))
        question_3 = input("a or b:")
        if question_3 == "a" or question_3 == "A":
            print("Cool. Happy winter!!")
            print(str("Points: ") + str(points + 6))
        elif question_3 == "b" or question_3 == "B":
            print("That's great, summer is amazing.")
            print(str("Points: ") + str(points + 6))
        else:
            print("Invalid response.")
    else:
        print("Invalid response.")
else:
    print("Invalid response.")
