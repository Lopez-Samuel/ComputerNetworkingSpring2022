from socket import *
import base64

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    #clientSocket.connect(("smtp.aol.com", 25))
    clientSocket.connect(("smtp.gmail.com",587))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    tlsCommand = 'STARTTLS \r\n'
    clientSocket.send(tlsCommand.encode())
    recv8 = clientSocket.recv(1024).decode()
    print("Message after STARTTLS command:" + recv8)
    if recv8[:3] != '220':
        print('220 reply not received from server.')
        
    # Send AUTH command and print server response.
    print("Sending AUTH Command")
    authMsg = "AUTH PLAIN\r\n"
    clientSocket.send(authMsg.encode())
    recv_auth = clientSocket.recv(1024)
    print(recv_auth.decode())
    if recv_auth[:3] != '250':
        print('250 reply not received from server.')

    #Info for username and password
    username = "sl4506@nyu.edu"
    password = " aVn9tiquity"

    # AUTH with base64 encoded user name password
    auth = username+"\0"+password
    base64_str = ('%s\0%s' % (username, password)).encode()
    auth = base64.b64encode(base64_str)
    clientSocket.send(auth)
    recv_user = clientSocket.recv(1024)
    print(recv_user.decode())
    if recv_user[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFromCommand = "MAIL FROM:<tester@test.com>\r\n"
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != '250':
	    #print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptToCommand = "RCPT TO:<test@test.com>\r\n"
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
	    #print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '354':
	    #print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)
    #if recv5[:3] != '250':
	    #print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)
    #if recv6[:3] != '221':
	    #print('221 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')