## Server

The server script (server.py) sets up a TCP/IP socket server that listens for incoming connections from clients. Upon connection, it sends a welcome message to the client and receives the username from the client. Then, it adds the client to the list of connected clients and starts a new thread to handle messages from that client. Messages received from one client are broadcasted to all other connected clients.
## Client

The client script (client.py) is a graphical user interface (GUI) application implemented using the tkinter library. It prompts the user to enter a username and connects to the server upon confirmation. Once connected, the client can send messages to the server, which are then broadcasted to all other connected clients. Messages received from other clients are displayed in a scrolled text box, with usernames colored green for better visibility.
## How to Run
- Clone the repository:
- git clone https://github.com/MehranTurk/ChatApp
- Navigate to the repository directory:
- cd ChatApp
- Start the server by running:
- python3 server.py
- Start the client by running:
- python3 client.py
- Enter a username in the client GUI and click "Confirm" to connect to the server.

Start chatting with other connected clients by typing messages in the entry field and clicking "Send".

## Dependencies
    - Python 3.x
    - tkinter (for GUI)
    - threading (for concurrent client handling)

## Notes

By default, the server listens on 127.0.0.1 (localhost) and port 5500. You can modify these values in both the server and client scripts if needed.
This application is for educational purposes and may not be suitable for production use without further enhancements, such as error handling and security measures.

## Author
MehranTurk (M.T)

## *Donate*

USDT: TSVd8USqUv1B1dz6Hw3bUCQhLkSz1cLE1v

TRX: TSVd8USqUv1B1dz6Hw3bUCQhLkSz1cLE1v

BTC: 32Sxd8UJav7pERtL9QbAStWuFJ4aMHaZ9g

ETH: 0xb2ba6B8CbB433Cb7120127474aEF3B1281C796a6


