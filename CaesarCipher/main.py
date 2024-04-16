alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# caesar function that takes the arguments (start_text,shift_amount,cipher_direction) 
def caesar(start_text, shift_amount, cipher_direction):
  # empty string that will contain the value of the final text
  end_text = ""
  #if the user chooses to decode the direction of the shift amount will be changed
  if cipher_direction == "decode":
    shift_amount *= -1
    #use a for loop to check if the char is in the alphabet list , if not add it as it is in the end_text
  for char in start_text:
    # if the char is in the alphabet 
    if char in alphabet:
      #get the index of the char and store it in the position variable
      position = alphabet.index(char)
      #create a new variable that will store the new position after the shift for encoding
      new_position = position + shift_amount
      #find the char at the new index in the alphabet and store in the end_text
      end_text += alphabet[new_position]
    else:
      end_text += char
      #print the final text
  print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo
print(logo)

#create a bool value that will triggered when the game is over
should_end = False
#as long as the bool is false the game should continue
while not should_end:
#get input from the user
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
 #check if the user inputs a big shift number is should be divided by 26 until the reminder is 19
  shift = shift % 26
#call the caesar function
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#ask the user if the game is over
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  #if the user chooses no then trigger the bool variable and end the game
  if restart == "no":
    should_end = True
    print("Goodbye")



