#oop exercise. will be creating pet
#define a dictionary that holds our pet's attributes.
puppy = {
    "name": "Cujo",
    "fullness": 50,
    "happiness": 20,
}

#Define functions that increase a pets sttribute levels
def feed_pet (pet):
    pet["fullness"] += 10

def play_with_pet(pet):
    pet ["happiness"] +=10

#Define functions that decrease pets attributes
def get_hungry_and_mopey(pet):
    pet["fullness"] -=5
    pet["happiness"] -=5

#user interaction
while True:

    print("""
%s's stats:
Fullness: %d
Happiness: %d
""" % (puppy["name"], puppy["fullness"], puppy["happiness"]))
    
#added  prompt to ask user to pick a number.    
    choice = int(input("""
Please pick a number:
1. Feed puppy
2. Play with puppy
3. Do nothing
"""))
    if choice == 1:
        feed_pet(puppy)
    elif choice == 2:
        play_with_pet(puppy)
    else:
        pass

    # Each time the loop runs, the pet
    # will need some attention!
    get_hungry_and_mopey(puppy)    
    