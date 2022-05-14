print("Welcome to my The Hobbit quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
	quit()

print("So you're also a Tolkien fan. Okay, let's play! :)")
score = 0

anwser = input("What is the name of Bilbo’s hillside home? ")
if anwser.lower() == "bag end":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: Bag End")

anwser = input("What do trolls turn into when exposed to daylight? ")
if anwser.lower() == "stone":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: Stone")

anwser = input("What is Gollum’s name for his ring? ")
if anwser.lower() == "precious":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: Precious")

anwser = input("Who kills Smaug? ")
if anwser.lower() == "bard":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: Bard")
 
anwser = input("Who is the master of Rivendell? ")
if anwser.lower() == "elrond":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: Elrond")

anwser = input("What is the magic effect of the ring?  ")
if anwser.lower() == "invisibility":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: Invisibility")

anwser = input("What is the name of the evil wolflike creatures that support the goblins? ")
if anwser.lower() == "wargs":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: Wargs")

anwser = input("What does Bilbo name his sword? ")
if anwser.lower() == "sting":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: Sting")

anwser = input("What is the name of Gandalf’s sword? ")
if anwser.lower() == "glamdring":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: Glamdring")

anwser = input("Who saves the party from the Wargs? ")
if anwser.lower() == "the eagles":
	print("Correct!")
	score += 1
else:	
	print("Incorrect! The right anwser is: The eagles")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")
