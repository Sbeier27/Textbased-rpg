
inventory = []

def introScene():
  directions = ["east", "west", "north"]
  print("You are at a large cavern, you can go east or west")
  userInput = ""
  while userInput not in directions:
    print("Options: east/west/inventory/map")
    userInput = input()
    if userInput == "east":
      PuzzleA()
    elif userInput == "west":
      TScene1()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-------------------")
      print("--[  ]-[ x ]-[  ]--")
      print("-------------------")
      print("-------------------")
    else:
      print("Please enter a valid option")

def PuzzleA():
  directions = ["east", "south" , "west"]
  print("Before you sits a massive door, you are unable to move it's hinges. Resting at the handles of the door are two large gemstones")
  userInput = ""
  while userInput not in directions:
    print("Options: west/inventory/map")
    userInput = input()
    if userInput == "dr'gosh":
      print("The door's roar to life as the move, you've spoken the correct word")
      SecretWeapon()
    elif userInput == "west":
      introScene()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
    print("-------------------")
    print("------------{  }----")
    print("-------[  ]-[ x ]--")
    print("-------------------")
    print("-------------------")
  else:
    print("Please enter a valid option for the adventure game.")


def SecretWeapon():
  directions = ["south"]
  print("You step into a room of prisitne marble and at the center, in the arms of the statue is a beautiful shield with a clear center")
  userInput = ""
  while userInput not in directions:
    print("Options: south/pick up/inventory")
    userInput = input()
    if userInput == "south":
      PuzzleA()
    elif userInput == "pick up":
      if "Truth Shield" in inventory:
        print("You've already found the truth")
      else:
        inventory.append("Truth Shield")
        print("You look through the shield, out to the doors and see them too made of marble, this shield reveals the truth of the world around you")
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
    elif userInput == "map":
      print("-------------------")
      print("-------------{ x }-")
      print("-------------[  ]--")
      print("-------------------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def GenericRoom1():
  directions = ["west", "south"]
  print("a faint glow comes from the south, why do you venture forward?")
  userInput = ""
  while userInput not in directions:
    print("Options: west/south/inventory")
    userInput = input()
    if userInput == "west":
      print("the skeletons have not died...again")
      SkeletonA()
    elif userInput == "south":
      Torch()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-------------------")
      print("---[   ]-[ x ]-----")
      print("---------[   ]-----")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")



def WeaponGet():
  directions = ["north", "south"]
  print("Embedded into the long deceased skull of a monster is a dull rusty blade, it may come in handy")
  userInput = ""
  while userInput not in directions:
    print("Options: north/south/pick up/inventory")
    userInput = input()
    if userInput == "north":
      SkeletonA()
    elif userInput == "pick up":
      if "Rusty Sword" in inventory:
        print("The corpse of the beast has been picked clean")
      else:
        inventory.append("Rusty Sword")
    elif userInput == "south":
      TScene1()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
    elif userInput == "map":
      print("-------------------")
      print("---[   ]-----------")
      print("---[ x ]-----------")
      print("---[   ]------------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")


def TScene1():
  directions = ["north", "south" , "west"]
  global weapon
  print("you have entered a t shaped area of the cave, there's a faint glow to the south, to the north continues the cave")
  userInput = ""
  while userInput not in directions:
    print("Options: north/south/east/inventory")
    userInput = input()
    if userInput == "south":
      ClassicRoom()
    elif userInput == "east":
      introScene()
    elif userInput == "north":
      WeaponGet()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
    elif userInput == "map":
      print("-------------------")
      print("---[   ]-----------")
      print("---[ x ]-[  ]------")
      print("---[   ]-----------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def ClassicRoom():
  directions = ["north"]
  print("You move to the south and find a part of the cave covered in glowing moss, etched into the wall is a single word, 'Konami' ")
  userInput = ""
  while userInput not in directions:
    print("Options: north/inventory/map")
    userInput = input()
    if userInput == "up up down down left right left right b a select start":
      print("The ground shakes as the wall under the etching falls revealing a small room, you go inside")
      PuzzleAAnswer()
    elif userInput == "north":
      TScene1()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
    elif userInput == "map":
      print("-------------------")
      print("-------------------")
      print("-------[   ]-------")
      print("-{   }-[ x ]-------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def PuzzleAAnswer():
  directions = ["east"]
  print("inside the room there are crystals on the wall spelling out the word 'dr'gosh'")
  userInput = ""
  while userInput not in directions:
    print("Options: east/inventory/map")
    userInput = input()
    if userInput == "east":
      TScene1()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
    elif userInput == "map":
      print("-------------------")
      print("-------------------")
      print("-------[   ]-------")
      print("-{ x }-[   ]-------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")


def SkeletonA():
  actions = ["fight", "flee"]
  global weapon
  print("The ground rumbles as the bones of foolish souls begin to emerge, do you stand your ground? what do you have to loose?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight/inventory/map")
    userInput = input()
    if userInput == "fight":
      if "Rusty Sword" in inventory:
        print("Brandishing the rusty blade you narrowly avoid an extra early demise..you continue on for now...to the east")
        GenericRoom1()
      else:
        print("you join the skeletal army, guarding the depths of this lost dream.")
      quit()
    elif userInput == "flee":
      WeaponGet()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-------------------")
      print("---[ x ]-[   ]-----")
      print("---[   ]-----------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")


def SkeletonB():
  actions = ["fight", "flee"]
  global weapon
  print("The adventurers from the camp now stand before you as skeletons do you put them out of their misery?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight/inventory/map")
    userInput = input()
    if userInput == "fight":
      if "Rusty Sword" in inventory:
        print("Slicing the magic reanimating them you put the skeletons down once more as you move to the northeast")
        DarkRoomA()
      else:
        print("you join the skeletal army, guarding the depths of this lost dream.")
      quit()
    elif userInput == "flee":
      GenericRoom2()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("----------[   ]----")
      print("---[   ]-/---------")
      print("---[ x ]/----------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")


def DarkRoomA():
  actions = ["leave", "light"]
  global weapon
  print("Entering the room you are consumed by total and utter darkness, it takes you a moment to realize death hasn't graced you with it's presence but instead you are simply in the dark")
  userInput = ""
  while userInput not in actions:
    print("Options: leave/light/inventory/map")
    userInput = input()
    if userInput == "light":
      if "torch" in inventory:
        print("using the torch you light the room up illuminating a path to the south")
        PuzzleB()
      else:
        print("you reach for a light, having long lost it, you let your spark of hope get consumed by the darkness")
      quit()
    elif userInput == "leave":
      SkeletonB()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("----------[ x ]----")
      print("---------/[   ]----")
      print("---[   ]/----------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def PuzzleB():
  directions = ["north" , "northeast"]
  print("To the northeast a large door stands, carved into it seems to be a large beast with leathery wings and an armor of scales")
  userInput = ""
  while userInput not in directions:
    print("Options: north/inventory/map")
    userInput = input()
    if userInput == "dragon":
      GenericRoom3()
    elif userInput == "north":
      DarkRoomA()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("---[   ]-{   }-----")
      print("---[ x ]/----------")
      print("-------------------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def GenericRoom3():
  directions = ["southeast", "southwest"]
  print("Fate has not been kind those who've made it this far, the walls are lined with dried blood, thick and ancient. theres an exit to the southeast...is it safe?")
  userInput = ""
  while userInput not in directions:
    print("Options: southeast/southwest")
    userInput = input()
    if userInput == "southeast":
      GhoulA()
    elif userInput == "southwest":
      PuzzleB()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-----/{ x }\-------")
      print("[   ]-------[   ]--")
      print("-------------------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def GhoulA():
    actions = ["fight", "flee"]
    global weapon
    print("The beast responsible for the blood appears before you, a Ghoul with claws as long as sword, just die already.")
    userInput = ""
    while userInput not in actions:
      print("Options: flee/fight/inventory/map")
      userInput = input()
      if userInput == "fight":
        if "Rusty Sword" in inventory:
          print("You slash at the monster, your blade cuts it's skin but it still pounces at you prepared to rip you to shreds, just accept your fate")
          print("Options: Give up/torch")
          userInput = input()
          if userInput == "torch":
            print("resisting death's ever lasting call you use your torch to set alight the rags of the ghoul, causing it to burn to a crisp and die, you can continue to the west")
            DarkRoomB()
          elif userinput == "Give up":
            print("you've laid down and accepted your fate, like all others before you")
            quit()
        else:
          print("With nothing equipped to fight the monster, you're forced to use your fists, it doesn't take long for them to be removed from your body..you've died")
        quit()
      elif userInput == "flee":
        print("the ghoul is much to quick, before you can move your feet out the door its already sliced out your insides, die")
      elif userInput == "inventory":
        if inventory == []:
          print("Empty")
        else:
          print(inventory)
      elif userInput == "map":
        print("-------------------")
        print("------{   }\-------")
        print("------[   ]-[ x ]--")
        print("-------------------")
        print("-------------------")
      else:
        print("Please enter a valid option for the adventure game.")

def DarkRoomB():
  actions = ["leave", "light"]
  print("Once again shadow envelops your view, though perhaps that is for the best, still with no light no exit can appear")
  userInput = ""
  while userInput not in actions:
    print("Options: leave/light/inventory/map")
    userInput = input()
    if userInput == "light":
      if "torch" in inventory:
        print("Once again holding the torch out you can see the room, it's filled with corpses all sliced to bits and consumed, the ghoul's lair, filled with it's previous victims, you move past them to a room in the southwest")
        PuzzleDAnswer()
      else:
        print("the light, your only hope, now gone")
      quit()
    elif userInput == "leave":
      print("The cave, ever cursed as it is, causes the ghoul to remerge from the ash")
      GhoulA()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-------------------")
      print("------[ x ]-[   ]--")
      print("[   ]/-------------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")


def PuzzleDAnswer():
  directions = ["northeast", "east"]
  print("Carved into the walls of the room stands the image of a mighty bird, covered in flames, the majestic Phoenix, across from it stands the exit to the east with groans erupting from it")
  userInput = ""
  while userInput not in directions:
    print("Options: northeast/east/inventory/map")
    userInput = input()
    if userInput == "northeast":
      DarkRoomB()
    elif userInput == "east":
      GhoulB()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-------------------")
      print("------[   ]--------")
      print("[ x ]/-------------")
      print("----\[    ]--------")
    else:
      print("Please enter a valid option for the adventure game.")

def GhoulB():
  actions = ["fight", "flee"]
  print("Yet another Ghoul blocks the path to the southeast, it wears effeminate clothing, perhaps once a beautiful woman, a depraved man, or someone else entirely, what now?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight/inventory/map")
    userInput = input()
    if userInput == "fight":
      if "torch" in inventory:
        print("Remembering your trick from last time you prepare to burn the ghoul, this one is clever though and dashes away before throwing a rock at you, it's less focused on you though and more on the shadow your torch makes")
        print("Options: die, die, die, die ,die ,die")
        userInput = input()
        if userInput == "shadow puppet":
          print("realizing it's clothing you make a shadowpuppet on the wall of a woman dancing, you lure it closer to you, before slashing it's heels and torching it once more, making your way to the southeast")
          PuzzleC()
      else:
        print("you've laid down and accepted your fate, like all others before you")
        quit()
    elif userInput == "flee":
      print("the ghoul is much to quick, before you can move your feet out the door its already sliced out your insides, die")
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("[   ]--------------")
      print("----\[ x ]---------")
      print("---------\[   ]----")
      print("-------------------")
  else:
    print("Please enter a valid option for the adventure game.")

def PuzzleC():
  directions = ["west" , "southwest"]
  print("You stand in this room another door locked, an inscription on it's solid stone self is all you have")
  userInput = ""
  while userInput not in directions:
    print("Options: west/inspect/inventory/map")
    userInput = input()
    if userInput == "inspect":
      print ("the inscription reads as follows 'to suck away at diseases deep one may wish to use a'?")
    elif userInput == "west":
      print("Nothing dies here...not for long...")
      GhoulB()
    elif userInput == "leech":
      print("the stone door opens slowly into the furthering depths of this hell, you continue to the southwest")
      GenericRoom4()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-----[   ]---------")
      print("---------\[ x ]----")
      print("----------/--------")
      print("-----{   }---------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def GenericRoom4():
  directions = ["northeast", "east"]
  print("Stalactites hang from the ceiling, like the maws of a hungry beast, it appears that from now on your in the belly of the beast...you can continue to the east ")
  userInput = ""
  while userInput not in directions:
    print("Options: northeast/east/inventory/map")
    userInput = input()
    if userInput == "east":
      PuzzleD()
    elif userInput == "northeast":
      GenericRoom4()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("----------[   ]----")
      print("----------/--------")
      print("-----{ x }-[   ]---")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def PuzzleD():
  directions = ["west" , "south"]
  print("once more a door, this time chared and made of what appears to be lava rock blocks your path an inscription amongst its surface")
  userInput = ""
  while userInput not in directions:
    print("Options: west/inspect/inventory/map")
    userInput = input()
    if userInput == "inspect":
      print ("the inscription reads as follows 'Ashes to ashes, dust to dust, flight requires a gust, never dead, always alive, what am I?'?")
    elif userInput == "west":
      print("Nothing dies here...not for long...")
      GhoulB()
    elif userInput == "phoenix":
      print("recalling from earlier the images of the phoenix on the wall, you recite the beast's name as the door opens, heat rushing out from it, you continue to the south")
      Corpses()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-----{   }-[ x ]---")
      print("-----------{   }---")
      print("-------------------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def Corpses():
  directions = ["north", "west"]
  print("stench fills the room, as you see before you a mountain of corpses, burnt to a crisp, flesh eaten off, all of them pile around a large door to the west")
  userInput = ""
  while userInput not in directions:
    print("Options: west/north/inventory/map")
    userInput = input()
    if userInput == "west":
      GrandHall()
    elif userInput == "north":
      PuzzleD()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-----------[   ]---")
      print("-----[   ]-{ x }---")
      print("-------------------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def GrandHall():
  directions = ["east", "west"]
  print("You've entered a massive hallway, carved into the stone and absolutely torched, hollow armor lines the walls but has been melted and is unable to be entered. Ahead of you is a grand door to the west")
  userInput = ""
  while userInput not in directions:
    print("Options: east/west/inventory/map")
    userInput = input()
    if userInput == "east":
      Corpses()
    elif userInput == "west":
        if "Rusty Sword" in inventory and "Truth Shield" not in inventory:
            Throne1()
        elif "Rusty Sword" in inventory and "Truth Shield" in inventory:
            Throne2()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-------------------")
      print("-[   ]-[ x ]-{   }-")
      print("-------------------")
      print("-------------------")
    else:
      print("Please enter a valid option for the adventure game.")

def Throne1():
  actions = ["fight", "giveup"]
  print("You enter into a massive Throne room, carpets torn and torched, tapestries long fallen, and on the throne a massive Phoenix towers above you")
  print("The Phoenix instead of being it's beautiful sunny self is instead a mix of greys and purples, but nonetheless molten,")
  print("The beast eyes you, prepared to eat once more, there is no going back now...what would be the purpose?")
  userInput = ""
  while userInput not in actions:
    print("Options: fight/giveup/inventory/map")
    userInput = input()
    if userInput == "fight":
      if "Rusty Sword" in inventory:
        print("The large bird fires a shot of burning skulls at you, your soon to be fate")
        print("Options: dodge/run/block/parry")
        userInput = input()
        if userInput == "parry":
          print("quickly thinking you draw your rusty blade and launch the skulls back at the beast, it screeches in pain as it soars into the air")
          print("Options: hide/taunt/attack")
          userInput = input()
        if userInput == "hide":
            print("Quick you leap under a tapestry on the floor hiding from the bird's sight")
            print("The phoenix caws in anger as it lands on a ceiling beam")
            print("Options: Cut rope/distract/hide")
            userInput = input()
            if userInput == "Cut rope":
                print("You slash at a rope pulled down by rubble, it quickly flies through the air to drop a large chandelier on the bird")
                print("In a blast of pain and rage the phoenix ignites the arena, burning the hiding places you could dare go")
                print("It is now soaring high above you launching down a rain of flaming feathers")
                print("Options: catch/run/hide/fan")
                userInput = input()
                if userInput == "fan":
                    print("your brain, ever in panic, you slash with your sword quickly creating just enough force int the air to blow the feathers back")
                    print("Once more the phoenix screams in pain, landing on the floor and laying down")
                    print("Now is the time, time to slash, maim, and induce havoc will you?")
                    print("Options: behead/leave/curse")
                    userInput = input()
                    if userInput == "Leave":
                        Ending1()
                    elif userInput == "behead":
                        Ending2()
                    elif userInput == "curse":
                        Ending3()
                else:
                    print("In your hubris and panic you end up catching fire with the rest of the throne room, you have died")
        else:
                print("The sheer trauma of seeing the skulls of previously engulfed adventurers is too much for you, so in your panic you die")
                quit()
      else:
        print("you fail to deal with the attack and end up eaten by the bird joining the next batch of flaming skulls")
        quit()
    elif "giveup" == userInput:
      print("Too cowardly to stand your ground you lay down and die")
      quit()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-------[   ]-------")
      print("{EXIT}-[ x ]-[  ]--")
      print("-------[   ]-------")
      print("-------------------")
  else:
    print("Please enter a valid option for the adventure game.")

def Throne2():
  actions = ["fight",]
  print("You enter into a massive Throne room, carpets torn and torched, tapestries long fallen, and on the throne a massive Phoenix towers above you")
  print("The Phoenix instead of being it's beautiful sunny self is instead a mix of greys and purples, but nonetheless molten,")
  print("You eye the beast through the shield, seeing the phoenix being tormented by a curse")
  userInput = ""
  while userInput not in actions:
    print("Options: fight")
    userInput = input()
    if userInput == "fight":
      if "Rusty Sword" in inventory:
        print("The large bird fires a shot of burning skulls at you, you can triumph your fate")
        print("Options: dodge/run/block/parry")
        userInput = input()
        if userInput == "parry":
          print("quickly thinking you use the shield and launch the attack back at the bird, it howls in pain before flying higher and raining down hellfire")
          print("Options: shield/taunt/attack")
          userInput = input()
        if userInput == "shield":
            print("You hold your shield above your head protecting you from the hellfire")
            print("The phoenix caws in anger as it swoops down and picks you up")
            print("Options: climb/distract/slash")
            userInput = input()
            if userInput == "climb":
                print("You worm your way out of it's grasp and begin climbing it, the fire of the bird burning at you")
                print("Climbing up to the neck you know you have your opportunity ")
                print("Options: slash/hit/yell")
                userInput = input()
                if userInput == "hit":
                    print("You throw all your might into hitting the beast with the shield ")
                    print("Once more the phoenix screams in pain, landing on the floor and laying down")
                    print("What do you do now?")
                    print("Options: leave/imbue")
                    userInput = input()
                    if userInput == "leave":
                        SecretEnd1()
                    elif userInput == "imbue":
                        SecretEnd2()
                else:
                  print("The flames are far too much, it melts your rusty blade and burns you up")
            else:
              print("The talons of the Phoenix are far too much, you end up crushed in it's grasp")
              quit()
      else:
        print("You perish to the flames")
        quit()
    elif userInput == "inventory":
      if inventory == []:
        print("Empty")
      else:
        print(inventory)
    elif userInput == "map":
      print("-------------------")
      print("-------[   ]-------")
      print("{EXIT}-[ x ]-[  ]--")
      print("-------[   ]-------")
      print("-------------------")
  else:
    print("Please enter a valid option for the adventure game.")

def End1():
  print("With the beast no longer in a frenzy you take the chance to simply walk away returning to your village")
  print("You failed to find the weapon of legends, and the cavern is still unsafe for those who fall in")
  print("but atleast you're alive right? survival is a game of the fittest...does that really describe you?")
  print("You may never truly know...")
  print("The end of your tale " + name)
  quit()


def End2():
  print("You glare at the beast, it was the straw that broke your back, the last piece of pain in this awful hell")
  print("You take the rusty blade and cleave off the monster's head, as it fades into ash, bound to return some other time")
  print("The rage, the bloodlust, it's all far too much for you to resist, and so you go on a killing spree")
  print("The friend's and family in your village you did this all for...they mean nothing now, the only thing that matters is the smell of freshly spilt blood")
  print("The end of your tale " + name)
  quit()


def End3():
  print("In your time you've learned only of only one spell, but you decide now is the time worth using it")
  print("You still your breath and concentrate, repeating the words, before finally looking at the beast and saying the final word")
  print("The Phoenix's feathers turn onyx black as it caws in pain, you've cursed it to be unable to stay alight for more than a minute")
  print("With the phoenix now eternally dying over and over, you now leave, but the cost of the curse was too much for you,")
  print("as you cross the threshold..you die then and there")
  print("The end of your tale " + name)
  quit()

def SecretEnd1():
  print("You sigh in relief, satisfied with owning the shield you leave")
  print("You return to your village a hero, able to help with the monster's attacks by defending against them")
  print("Only you know the truth of the cavern, the undying curse of the phoenix laying in there, and something feels wrong")
  print("Still you continue on triyng your best...but something feels incomplete")
  print("The end of your tale " + name)
  quit()

def SecretEnd2():
  print("You aren't the highest capacity magician, so you don't know how to decurse it, but you have an idea")
  print("Gently you lay the blade on the phoenix's chest and slowly bring the shield closer, and closer, as the phoenix and the sword glow")
  print("The phoenix and the sword become one, a mightly blade of flames, as the curse over this cavern is sealed inside the sword")
  print("You've freed the souls of the dead here, have come back with two legendary weapons, yet are now cursed to never die")
  print("The end of your tale " + name + "Congratulations, you've left me proud")
  quit()

def Torch():
  directions = ["northeast", "north"]
  print("To the northeast the familiar clanking of bones of all the basic rooms, this is the only one with a torch")
  userInput = ""
  while userInput not in directions:
    print("Options: northeast/north/pick up")
    userInput = input()
    if userInput == "northeast":
      GenericRoom2()
    elif userInput == "north":
      GenericRoom1()
    elif userInput == "pick up":
      if "torch" in inventory:
        print("the only source of light in the room, now gone")
      else:
        inventory.append("torch")
        print("you've stolen the only light in this darkened hell")
    else:
      print("Please enter a valid option for the adventure game.")

def GenericRoom2():
  directions = ["southeast", "south"]
  print("the remains of a camp sit, seemingly another group's best bet at venturing through this cavern")
  userInput = ""
  while userInput not in directions:
    print("Options: southeast/south/inspect")
    userInput = input()
    if userInput == "southeast":
      Torch()
    elif userInput == "south":
      SkeletonB()
    elif userInput == "inspect":
      print("you find a journal, the only page remaining in it is a simple statement 'remember not all paths are given to you' an odd statement in the least")
    else:
      print("Please enter a valid option for the adventure game.")

  # Simple pygame program

  # Import and initialize the pygame library





if __name__ == "__main__":
  while True:
    print("Before the game begins please read this")
    print("There are puzzles in this game that will require you to type out the answer")
    print("The answer will not be one of the options")
    print("Also for the map: x is you, [] is a room, {} is a locked room, if you can see a room you can get into it")
    print("Now let's begin...")
    print("Welcome to the Caverns...")
    print("legends tell of a grand weapon awaiting in the depths of this cavern")
    print("With your town under constant attack from monsters you've decided to look for it")
    print("You have fallen into the cavern with no way of escaping")
    print("what name will they put on your tombstone?: ")
    name = input()
    print("may you rest in peace, " +name+ ".")
    introScene()



