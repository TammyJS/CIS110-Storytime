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