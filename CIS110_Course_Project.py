print(f"Hello and welcome to my exciting story about an enchanted car and the farmer! I hope you are just as excited as me! ")
print(f"Before we can start the story, I need you to answer a few questions first. ")
print(f"After typing your answer, please hit the enter key. ")


keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    #5 Questions Before the story begins
    car = input(f"\nWhat kind of car is enchanted?:  ")
    while len(car) == 0:
        car = input(f"Please enter the car:  ")
    #Second Question
    farmersName = input(f"What is the farmers name?  ")
    while len(farmersName) == 0:
        famersName = input(f"Please enter the farmers name:  ")
    #Third Question
    town = input(f"What is the name of the town he lives in?  ")
    while len(town) == 0:
        town = input(f"Please enter the name of the town:  ")
    #Fourth Question
    carName = input(f"What name would you give this enchanted car?  ")
    while len(carName) == 0:
        carName = input(f"Please enter the name of the enchanted car:  ")
    #Fifth Question
    foodItem = input(f"What is your favorite food?  ")
    while len(foodItem) == 0:
        foodItem = input(f"What is your favorite food item:  ")

    #Story Starts
    print(f"Let's get this story going!!")
    print(f"\nThe old farmer {farmersName} wants to drive his car again but knows he can't see well enough with his old eyes.  ")
    print(f"He named the old car, {carName} years ago.  ")
    print(f"The old car {carName} roars to life and opens the driver's door, bumpng farmer {farmersName}.  ")
    print(f"Surprised, {farmersName} makes his way into the driver's seat to turn off the car.  ")
    print(f"{farmersName} always knew the old {car} was particular.  ")
    print(f"When he couldn't find the keys in the ignition, the car door closed, locks, gave a little honk of it's horn and pulled out of the barn, and started driving to the end of the road.  ")
    
    #Decision 1
    iceCream = input(f"\nShould the enchanted {car} take farmer {farmersName} to {town} for ice cream? Please type yes or no:  ")  
    while iceCream.lower() != "yes" and iceCream.lower() != "no":
        iceCream = input("Please type yes or no:  ")

    if iceCream == "yes":
        print(f"\nThe enchanted {car} turns to the left and heads to town.  ")
        print(f"All the while, farmer {farmersName} was hooting and laughing with joy.  ")
        print(f"{farmersName} gently lays his hands on the steering wheel and enjoys being behind the wheel again.  ")
        print(f"As they go through town, the townspeople who know, stop and stare in shock and amazement as he drives by. ")
        print(f"They know faremer {farmersName} has not been able to drive in 5 years due to his eyesight being bad.  ")
        print(f"He says out loud, I sure would like an ice cream right now.  ")
        print(f"The enchanted car {carName} makes and left, then a right, and another left, slows down and stops in front of the ice cream parlor.  ")
        print(f"After farmer {farmersName} gets his ice cream, he sits on the bench outside, eating his ice cream cone and enjoying the beautiful day.  ")
    else:
        print(f"\nFarmer {farmersName} decides to stop and get his wife some flowers.  ")
        print(f"The enchanted {car} knew where to go and stopped at the florist.  ")
        print(f"Farmer {farmersName} got a dozen daisies from the florist.  ")
        print(f"In {carName} he placed them on the seat beside him. ")
        
    print(f"With no destination in mind {carName} drives up and down the town roads.  ")
    print(f"Not wanting to go home yet, he thinks about going to the grocery store to pick up a few items for his wife.  ")

    #Decision 2 
    goToStore = input(f"\nShould Farmer {farmersName} go to the store?:  ")
    while goToStore.lower() != "yes" and goToStore.lower() != "no":
        goToStore = input(f"Please type yes or no:  ")

    if goToStore == "yes":
        print(f"\nHe tells {carName} the enchanted {car}, let's go to the grocery store to shop!  ")
        print(f"After turning right, then left, then left again, they arivved at the grocery store.  ")
        print(f"{carName} drops off farmer {farmersName} in front of the store, gives a little honk then parks itself into a parking space.  ")
        print(f"Getting a cart, farmer {farmersName} starts his shopping.  ")
        print(f"Not being able to see the labels to clearly, he does his best to get what he thinks his wife needs.  ")
        print(f"When he comes out of the store, the enchanted {car} pulls up and pops open the back for farmer {farmersName} to put the groceries in.  ")
        print(f"Customers in the parking lot stare in amazement at the car driving itself.  ")
    else:
        print(f"\nFarmer {farmersName} decides that maybe it's best to leave the shopping to his wife because his eyes can't see the labels to good anymore.  ")
        print(f"The enchanted {car} and farmer {farmersName} continue to drive around town, waving at the townspeople as they drive by.  ")

    #Alternate Endings
    if iceCream == "yes" and goToStore == "yes":
        print(f"\nWith a quick wave to the people in the parking lot, the farmer tells the enchanted {car} it's time to go home.  ")
        print(f"With the groceries in the back, the farmer is happy and filled with life again.  ")
        print(f"He thanks the car as it parks in front of his farmhouse.  ")
        print(f"His wife comes running out of the door after watching through the window, her husband pulling in")
        print(f"She stood in the doorway, looking at her husband as he got out of {carName}.  ")
        print(f"Amazed, she stares at the {car}, thinking about the days they use to ride in it.  ")
        print(f"He grabs the bags of food, and inside the bags, the wife sees cans of dog and cat food for pets they do not have, chili powder, {foodItem}, and jalapenos.  ")
        print(f"The enchanted {car} gives a honk and drives back to the barn.  ")
    elif iceCream == "no" and goToStore == "no":
        print(f"\nWith the flowers on the seat beside him, he is excited to get home to give them to his wife.  ")
        print(f"He tells {carName}, it's time to go home  ")
        print(f" Driving out of town, he decides he is going to take his wife out for a drive tomorrow and the {car} gives a little honk in agreement.  ")
        print(f"Parked outside his farmhouse, his wife comes out and looks in amazement at the old {car} and her husband.  ")
        print(f"He gives the flowers to her and places a gentle kiss on her lips.  ")
        print(f"The enchanted {car} gives a little honk and drives back to the barn.  ")
    else:
        print(f"\nWith his fill of ice cream, farmer {farmersName} decides it would be best to go home after a little drive through town.  ")
        print(f"He rather not attract anymore attention to himself and {carName}.  ")
        print(f"Once home, he tells his wife about the enchanted {car}, and they decide to go for a ride tomorrow, with her sitting in the drivers seat of course.  ")
        print(f"She can see better than him!  ")

        print(f"\nThe End")
        
        keepPlaying = input(f"\nDo you want to play again? Please enter yes or no:  ") 
        while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
            keepPlaying = input(f"Please type yes or no:  ")