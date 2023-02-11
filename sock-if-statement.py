question = "Sam has 3 pairs of socks: 1 green, 1 pink, and 1 blue. He wants to wear matching socks. Sam has already picked a sock and chose green. Write an if statement showing what he will do if he gets a pink or blue sock and what he should do if he gets a green sock."

sams_pick = input("Sam picks a sock from the drawer... ")

if sams_pick == "pink":
 print("Sam puts the sock aside and keeps looking.")

elif sams_pick == "blue":
 print("Sam puts the sock aside and keeps looking.")

elif sams_pick == "green":
 print("Sam puts his socks and shoes on and heads to the store.")

else:
  print("That color is not in the drawer.")

