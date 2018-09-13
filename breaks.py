while True:
  print('Who are you?')
  name = input()
  if name != 'Pat':    #the continue statement causes the program execution to jump back to the start of the loop   
    continue              
  print('Hello, pat. What is the password? (It is an animal.)') 
  password = input()      
  if password == 'bobcat':
    break
print('Access granted.')  
