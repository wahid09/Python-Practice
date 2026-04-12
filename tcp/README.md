# TCP Server

A **TCP server** is a program that listens for incoming connections from clients over the **Transmission Control Protocol (TCP)** — a reliable, connection-oriented protocol in the TCP/IP suite.

TCP ensures data is delivered **in order**, **without loss**, and **without duplication** using acknowledgments, sequence numbers, and retransmissions. TCP servers form the foundation of many networked applications, including web servers, databases, and Redis (which uses TCP on the default port **6379**).

## Key Characteristics of TCP

- **Reliable**: Guarantees delivery of data in the correct order using acknowledgments and automatic retransmission.
- **Connection-Oriented**: Establishes a persistent connection through a three-way handshake before any data is exchanged.
- **Stream-Based**: Data is treated as a continuous stream of bytes with **no built-in message boundaries**.

Redis, a popular in-memory data store, implements a high-performance TCP server to accept client connections and process commands in the **RESP** (Redis Serialization Protocol) format.

## TCP Connection Lifecycle

A typical TCP server follows this sequence:

1. **Socket Creation** — Create a new socket.
2. **Binding** — Bind the socket to a specific IP address and port.
3. **Listening** — Put the socket into listening mode with a backlog queue.
4. **Accepting Connections** — Accept incoming client connections, creating a new socket per client.
5. **Data Exchange** — Read requests, process them, and send responses.
6. **Connection Termination** — Gracefully close the connection when finished.

## Connection Establishment (Three-Way Handshake)

The TCP three-way handshake establishes a reliable connection:

1. **Client → Server**: Sends **SYN** (synchronize) packet.
2. **Server → Client**: Responds with **SYN + ACK** (synchronize + acknowledgment).  
   Server socket state changes from **LISTEN** to **SYN_RCVD**.
3. **Client → Server**: Sends **ACK**.  
   Both sides move to **ESTABLISHED** state.

Once both sides are in the **ESTABLISHED** state, bidirectional data communication can begin.

## Connection Termination (Four-Way Handshake)

Graceful connection closure typically follows these steps:

1. **Client → Server**: Sends **FIN** flag → enters **FIN-WAIT-1** state.
2. **Server → Client**: Sends **ACK** → enters **CLOSE_WAIT** state.
3. **Server → Client**: Sends **FIN** when ready to close → enters **LAST_ACK** state.
4. **Client → Server**: Sends **ACK** → enters **TIME_WAIT** state.
5. After waiting **2 × MSL** (Maximum Segment Lifetime), the client moves to **CLOSED** state.

## Socket Programming Concepts

### Socket Types
- `AF_INET`: Uses IPv4 addressing (most common).
- `SOCK_STREAM`: Specifies TCP (reliable, connection-oriented stream).

### Important Socket Methods

| Method              | Description |
|---------------------|-----------|
| `socket()`          | Creates a new socket |
| `bind((host, port))`| Binds socket to an IP address and port |
| `listen(backlog)`   | Enables the socket to accept connections |
| `accept()`          | Blocks until a client connects, returns new socket and client address |
| `recv(size)`        | Receives up to `size` bytes of data |
| `send(data)`        | Sends data to the connected client |
| `close()`           | Closes the socket |

## Client-Server Model

In the classic client-server architecture:
- The **server** passively listens for connections.
- The **client** actively initiates the connection using the three-way handshake.
- Once connected, both can send and receive data until one of them closes the connection.

---

This README is suitable for projects involving custom TCP servers, Redis clients, or any socket programming tutorials.