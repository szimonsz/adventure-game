import time
import random


house_items = ["tennis ball", "bone next to the bin",
                "leftover steak in the kitchen", "squeeky old dog toy"]

enemylist = ["neighbour", "dog", "neighbour's wife"]

youritem = []

random_house_item = random.choice(house_items)
random_enemy = random.choice(enemylist)


def print_pause(text):
    print(text, flush=True)
    time.sleep(2)

def print_bigpause(text):
    print(text, flush=True)
    time.sleep(4)

def intro():
    print_pause("You notice you're a cat in your sunny spot.")
    print_pause("It's early afternoon, your kittens are around you.")
    print_bigpause("You feel a bit tired. YAWN.")
    print_bigpause("Shouldn't have been meowing till late.")
    print_pause("You realise, your cat-family won't have any for supper.")
    print_pause("Jumping down from the attic you find yourself thinking:")
    print_pause("'How am I going to provide?' You stop in the back yard.")
    print_pause("You yawn, drop and roll, stretch and take a look around.")
    print_pause("You can see the cat flap to the house is open.")
    print_pause("You know the neighbour keeps cows but the milk "
                "might be hard to get.")
    print_pause("They have a dog, the neighbour himself could be around..")

def firstchoice():
    first_choice = input("Press 1 to take a look inside the house.\n"
                         "Press 2 to check out the neighbour.\n")

    if first_choice == '1':
        gointhehouse()
    elif first_choice == '2':
        print_pause("You jump over onto the neighbour's garage roof.")
        print_pause("To get to the milk you first have to get through the "\
                    + random_enemy + ".")
        print_pause("You could still give it a go, "
                    "but you're tired and you will "
                    "have to get back somehow.. This could be risky.")

        secondchoice()
    else:
        print_pause("Please enter 1 or 2.")
        firstchoice()
        print_pause("What you want to do?")

def secondchoice():
    print_pause("What you want to do next?")
    second_choice = input("Press 1 to try to get past the "\
                            + random_enemy + ".\n"
                            "Press 2 to go back and check what's the house.\n")
    if second_choice == '1':
        if random_enemy == 'dog':
            if len(youritem) > 0:
                print_pause("You creep close to the dog on the roof\
                            and drop the " + random_house_item + \
                            " close to it.")
                print_pause("This does the trick! The dog gets distracted.")
                print_bigpause("...silly puppies. You go for it fast.")
                winprint()
            else:
                badfight()
        elif random_enemy == 'neighbour':
            if len(youritem) > 0:
                print_pause("You climb up to the ridge of the roof")
                print_pause("You drop the " + random_house_item +
                            " on the other side.")
                print_pause("It works! It makes a loud noise rolling down.")
                print_pause("The neighbour goes to check it out.")
                winprint()
            else:
                badfight()
        elif random_enemy == "neighbour's wife":
            wifewinprint()
    elif secondchoice == '2':
        if len(youritem) > 0:
            emptyhouse()
        else:
            gointhehouse()

def badfight():
    your_roll = random.randint(1,6)
    their_roll = random.randint(1,6) + random.randint(1,6)
    print_bigpause("To get past the " + random_enemy +
                " AND to make it back too"
                ", you need to roll at least"
                " that much with one die than they roll with two dice."
                " Hard to do but you are"
                " so tired from the meowing all night.")
    print("You roll: " + str(your_roll))
    print("They roll: " + str(their_roll))
    if your_roll <= their_roll:
        print_pause("Oh! They almost catch you!")
        print_bigpause("You hardly make it out from their yard.")
        print_bigpause("You climb back to the attic. Your cat-wife takes a"
                    " disappointed look at you and without a meow goes to try"
                    " to catch some bugs.")
        print_bigpause("GAME OVER. You lost.")
        again()
    else:
        winprint()

def gointhehouse():
        print_pause("You're inside the house. Lucky. The flap's rarely open.")
        print_pause("As you take a look around, you can see a "\
                    + random_house_item + ".")
        print_pause("How fortunate, I might be able to distract "
                    "the " + random_enemy + " with this!")
        print_pause("You head back, out to your back yard.")
        youritem.append(random_house_item)
        secondchoice()

def emptyhouse():
    print_pause("You already have a " + random_house_item + " for distraction")
    print_pause("You head back, out to your back yard.")
    secondchoice()

def winprint():
    print_pause("WOAH! It was close!")
    print_pause("You manage to steal a bottle of delicious milk!")
    print_pause("You run back to the attic where the hungry kittens"
                " are waiting for you with loud meows!")
    print_pause("Congratulations! You won!")
    again()

def wifewinprint():
    print_pause("But hey!")
    print_pause("You purringly acknowledge it's the neighbour's wife!")
    print_pause("Splendid! You know she loves cats and she keeps the dog in"
                " the kennel")
    print_pause("She thinks it jumps up too much..")
    print_pause("She can see you're hungry so she gives you a bottle"
                " of milk.")
    print_pause("You run back to the attic where the hungry kittens"
                " are waiting for you with loud meows!")
    print_pause("Congratulations! You won!")
    again()

def again():
    again = input("Do you want to play the game again? Please type y/n.")
    if again == 'y':
        playgame()
    elif again == 'n':
        print_pause("Thanks for playing! See you!")
    else:
        print_pause("Please enter y/n.")
        again()

def playgame():
    youritem = []
    #intro()
    firstchoice()

playgame()
