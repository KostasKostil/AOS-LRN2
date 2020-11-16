import socket			 
from random import*

s = socket.socket()		 
port = 12345			

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))	

# put the socket into listening mode 
s.listen(5)
c, addr = s.accept()	 

def send(msg):
    c.send(msg.encode())

def receive():
    return c.recv(1024).decode();

def values(right, guess):
    almost, exact = 0, 0
    for i in range(4):
        for j in range(4):
            if right[i]==guess[j]:
                almost+=1
        if right[i]==guess[i]:
            exact+=1
    return almost, exact

def game():
    number = randint(1000, 9999)
    numberstr = str(number)
    while True:
        guess=receive()
        if (guess == "/exit"):
            return False
        if (guess == "/concede"):
            send("Number was "+str(number)+". Next number was generated and you can try again.")
            return True
        elif ((len(guess) > 8) and (guess[0:8] == "/random ")):
            try:
                times = int(guess[8:len(guess)])
                assert(1 <= times <= 10)
                response = "Starting random queries "+str(times)+" times:"
                for i in range(times):
                    guess=str(randint(1000, 9999))
                    almost, exact = values(numberstr, guess)
                    response+="\nFor number "+guess+" there are "+str(almost)+" number matches and "+str(exact)+" exact matches."
                send(response)
            except:
                send("Error when applying /random command. Please, try again.")
        else:
            try:
                guess_number = int(guess)
                assert(1000 <= guess_number <= 9999)
                almost, exact = values(numberstr, guess)
                if (exact == 4):
                    send("Congratulations! Number "+guess+" is correct!\nNext number was generated and you can play again.")
                    return True
                send("For number "+guess+" there are "+str(almost)+" number matches and "+str(exact)+" exact matches.") 
            except:
                send("Incorrect input. Please, try again.")

send("Number from 1000 to 9999 was generated.")
while True:
    if not game():
        break

