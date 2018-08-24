alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 5
newMessage = ''
message = input('please enter ur message:')
for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position+key)%26
    newCharacter = alphabet[newPosition]
    newMessage+=newCharacter
  else:
    newmessage+=character
print('your new message is:',newMessage)
    
