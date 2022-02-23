from http import client
from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket.socket()
    clientSocket.connect(mailserver, port)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    clientSocket.write(mailFromCommand)
    recv2 = clientSocket.read(1024)
    print(recv2)
    if recv2[:3] != '250':
	    print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    clientSocket.write(rcptToCommand)
    recv3 = clientSocket.read(1024)
    print(recv3)
    if recv3[:3] != '250':
	    print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.write(dataCommand)
    recv4 = clientSocket.read(1024)
    print(recv4)
    if recv4[:3] != '354':
	    print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.write(msg)
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.write(endmsg)
    recv5 = clientSocket.read(1024)
    print(recv5)
    if recv5[:3] != '250':
	    print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.write(quitCommand)
    recv6 = clientSocket.read(1024)
    print(recv6)
    if recv6[:3] != '221':
	    print('221 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')