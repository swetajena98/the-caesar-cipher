alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 5
newMessage = ''
secret code = 2048
code = input('enter the code')
if secret_code==code:
   message = input('please enter ur message:')
   for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position+key)%26
      newCharacter = alphabet[newPosition]
      newMessage+=newCharacter
    else:
      newMessage+=character
   print('your new message is:',newMessage)
else:
   print('you are not allowed to message')
