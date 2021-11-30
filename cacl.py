import socket		 	 # Import socket module
import ipaddress

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 	  		 # Create a socket object

try:
    host = socket.gethostbyname(socket.gethostname())  # Reading IP Address
    port = 5050                        # Reading port number

    s.connect((host, port))                # Connecting to server
    print("The IP address of the server is:", host)
    print("The port number of the server is:", port)

    while(True):
        equation=input("Please give me your equation (Ex: 2+2) or Q to quit: ")
        s.send(equation.encode())
        result = s.recv(5050).decode()
        if result == "Quit":
            print("Closing client connection, goodbye")
            break
        elif result == "ZeroDiv":
            print("You can't divide by 0,pls try again")
        elif result == "MathError":
            print("There is an error with your math,plz try again")
        elif result == "SyntaxError":
            print("There is a syntax error, pls try again")
        elif result == "NameError":
            print("You did not enter an equation,plz try again")
        else:
            print("The answer is:", result)
    s.close 				 # Close the socket when done
except (IndexError, ValueError):
    print("You did not specify an IP address and port number")