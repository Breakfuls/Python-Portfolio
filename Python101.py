print("You are about to choose your own adventure. \n You will be given two choices in each scenario, simply type A or B to make a choice when prompted. \n Ready to play? ")

step_1 = "You have been tasked with finding a powerful artifact in Mexico. \n How will you get there? \n A: By plane B: By boat"
plane_1 = "While on your flight you get into a discussion with the man next to you about archaeology and they are very interested in joining your journey. \n What is your answer? \n A:yes B:no"
boat_1 = "Your journey is smooth and quite relaxing, upon arrival at the remote dock, the boat's captain informs you he will be back in exactly 1 week to pick you up. \n How do you proceed? C: Set up camp D: begin searching for the temple you beleive holds the artifact"
plane_2 = "The man introduces himself as Aldritch, and offers his personal mansion as a base of operations for the search, you politely accept.\n In the morning you and Aldritch make your way to the temple, once there he reveals he knows how to get the door open.\n Once the door opens you are met with two hallways, do you A: Take the left hallway B: Take the right hallway C: Split up"
plane_3 = "The man simply nods his head and goes back to reading a magazine,\n upon arrival you make your way to the site of the temple you think holds the artifact and set up camp.\n Once you have set up camp you make your way to the temple to see that the man from the plane has already beat you there.\n He is surrounded by armed gaurds and appears to be trying to open the door to the temple do you?\nA: Approach the man B: wait to see if he gets the door open "
camp_1 = "You work tirelessly to get your tent up, make a fire, and make dinner from your supplies.\n when all is said and done you retire to you sleeping bag.\n When you wake up in the morning you are surrounded by Natives brandishing spears.\n they tie you up and take you to their village, there they interrogate you to learn why you are here.\n Do you A: Tell them you seek the artifact B: keep quiet"
temple_1 = "You decide to go straight to the temple you think holds the artifact.\nYou stumble around the jungle for a bit but it seems your coordinates were wrong.\nYou wander aimlessley and eventually sucumb to dehydration.\nYou have died."
intro_var = input()
if intro_var == "yes":
    print(step_1)
else:
    print("Come back when you are ready")

step_1a = input()

if step_1a == "A":
    print(plane_1)
else:
    print(boat_1)

travel_1a = input()

if travel_1a == "A":
    print(plane_2)
    branch_1 = input()
    if branch_1 == "A":
        print("You decide to take the left hallway, it's very dark, you use your hand to guide you along the temple wall.\n suddenly your hand presses against some sort of pressure plate and you feel a sharp pain in your neck. \n You have died")
    if branch_1 == "B":
        print("You decide on the right hallway, it is narrow but well lit.\n after walking for what seemed like an hour you reach the end of the tunnel and enter what appears to be a throne room.\n Sitting on the massive stone throne in the center of the room you spot the artifact.\n You rush to grab it but when you turn around Aldritch's gaurd's have their weapons pointed at you.\n Aldritch demands you give him the artifact, what do you do? A: Hand the artifact over. B: make a run for it")
        branch_2 = input()
        if branch_2 == "A":
            print("You reluctanly hand Aldritch the artifact, and without skipping a beat he snaps his fingers and one of his guards shoots you in the chest.\n You have died")
        if branch_2 == "B":
            print("You dive behind the throne and stop another tunnel at the back of the throne room.\n you sprint at the exit and Aldritch's guard begins firing at you.\n you are struck in the shoulder by a bullet but make it to the tunnel.\n After crawling through miles of tunnel in agony you make it out of the temple to a clearing, the artifact is yours.\n The End")
    if branch_1 == "C":
        print("You decide to split up Aldritch taking the left hallway with one of his guards and you taking the right alone.\n The rest of the guards stay behind.\n You walk for what seems like and hour, but eventually get to the throne room at the end of the tunnel.\n You spot Aldritch already in front of the throne with the artifact in his hands.\n You demand he give it to you and he refuses he starts toward one of the tunnels.\n Do you A: let him leave B: try to stop him")
        branch_2 = input()
        if branch_2 == "A":
            print("You decide to let Aldritch leave with the artifact.\nYou escape with your life but your mission is failed.\nThe End")
        if branch_2 == "B":
            print("You confront Aldritch and a fight breaks out instantly, he appears to have suffered and injuring from a trap in his hallway.\n you exploit this by targeting the injury until he concedes, giving you the artifact.\nYou look for a back entrance so you don't run into Aldritch's guards and find one behind the throne.\n You escape with the artifact intact\nThe End")
if travel_1a == "B":
    print(plane_3)
    branch_1 = input()
    if branch_1 == "A":
        print("The man turns and recognizes you, He says you made it clear on the flight that you and him were not friends.\nHe snaps his fingers and one of his guards shoots you in the chest.\nYou have died.")
    if branch_1 == "B":
        print("You wait for a few minutes and suddenly the stone door creaks open.\nYou follow the man inside and tail him to the throne room where you spot the artifact sitting on the stone throne.\nDo you A: rush for the artifact B: cause a distraction then try to swipe the artifact.")
        branch_2 = input()
        if branch_2 == "A":
            print("You run straight for the artifact but are gunned down before you can get close.\nYou have died.")
        if branch_2 == "B":
            print("You grab a large piece of stone and throw it at a weak stone pillar in the throne room.\nThe pillar crashes to the ground and as everyone investigateds you sneak behind the throne and swipe the artifact.\nYou rush back down the hall you came, and escape with the artifact.\nMission complete.")
if travel_1a == "C":
    print(camp_1)
    branch_1 = input()
    if branch_1 == "A":
        print("They seem to understand what you've said and carry you to the temple.\nThe door to the temple is already open, the Natives seem surprised.\n They bring you to the throne room still tied up.\nThere you find a man in a cream white suit flanked by a pair of armed gaurds.\n The Natives untie you and charge the man, do you A: help the Natives fight the guards B: Try to sneak away with the artifact during the chaos")
        branch_2 = input()
        if branch_2 == "A":
            print("You charge the guards with the group of 10 or so Natives and are swiftly gunned down by M4s.\nYou have died.")
        if branch_2 == "B":
            print("As the fighting starts you run around to the back of the throne and swipe the artifact.\nYou escape the same way you got in and your mission is complete.\nThe End")
    if branch_1 == "B":
        print("You remain quiet as the Natives yell at you in their language.\nEventually they grow frustrated with you and sacrifice you on a stone table.\nYou have died.")
if travel_1a == "D":
    print(temple_1)



