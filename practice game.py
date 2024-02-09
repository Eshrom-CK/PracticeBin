print("Get your booty up and going! The games have begun!")

playing = input("Do you want to play? ")
playing = playing.capitalize()

if playing.lower() != "yes":
    print("No? Well, those who say 'no' often find themselves in a pool of regret. ")
    quit()
    
print("Very good. I look forward to embarking in this journey with you! ")
time.sleep(2)

answer = input("What time have you committed to going to sleep? ")

if answer == "10:30":
    print("You son of a gun, that's correct")
