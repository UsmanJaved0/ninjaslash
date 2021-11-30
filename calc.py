import socket		 	 # Import socket module
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 	  		 # Create a socket object

host = socket.gethostname()                    # Get local machine name
port = 5050

s.bind((host, port)) 			 # Bind to the port
s.listen(1) 			         # Now wait for client connection.

print("Server is up and running")

while True:
     conn, addr = s.accept() 		# Establish connection with client.
     print('Got connection from', host)

     while True:
          try:
               equation=conn.recv(5050).decode()
               if equation == "Q" or equation == "q" or equation == "Quit" or equation == "quit" or equation == "QUIT":
                    conn.send("Quit".encode())
                    print("Connection has been cut off")
                    break
               else:
                    print(host," gave me the equation:", equation)
                    result = eval(equation)
                    conn.send(str(result).encode())

          except (ZeroDivisionError):
               conn.send("ZeroDiv".encode())
          except (ArithmeticError):
               conn.send("MathError".encode())
          except (SyntaxError):
               conn.send("SyntaxError".encode())
          except (NameError):
               conn.send("NameError".encode())