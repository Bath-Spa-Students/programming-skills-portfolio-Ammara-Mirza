''' Exercise 2: Alien Colors #2 :ballot_box_with_check:

Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 10 points.
•Write one version of this program that runs the if block and another that runs the else block.'''

alien_color="green"
if "green" in alien_color:
     print("the player just earned 5 points for shooting the alien.")
else:
     print("the player just earned 10 points.")

alien_color="red"
if "red" in alien_color:
     print("the player just earned 30 points for shooting the alien.")
else:
     print("the player just earned 50 points.")