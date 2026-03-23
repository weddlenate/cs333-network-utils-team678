# cs333-network-utils-team678

This repository contains a collection of network utilities designed for educational purposes,
specifically for the use in the CS333 course. These tools are intended to help students understand and
analyze network traffic, identify vulnerabilities, and practice ethical hacking techniques in a 
controlled environment.

## Team Members
- Nate Weddle
- Chandler Black
- Hayden Nguyen

## Quick Start

To get started with the network utilities, follow these steps:

- Install UV

## Network Packet Structure

- TCP Packet
  - Source Port
    - Port number that the application sends data to
  - Destination Port
    - Port number that the application sends data from
  - Sequence Number
    - Position of the first byte of data in this segment
    - This assures that data is assembled in the correct order once it has been received
  - Acknowledgement Number
    - Confirms successful retrieval of data and indicates the next byte that the sender should transmit
  - Flags
    - Used to indicate the particular state of connection or to provide additional information used for troubleshooting
    - These flags include:
      - Synchronization (SYN)
      - Acknowledgement (ACK)
      - Finish (FIN)
      - Reset (RST)
      - Urgent (URG)
      - Push (PSH)
  - Data
    - Actual application data being sent
  - Checksum
    - Ensures integrity in the transmission
  - Urgent Pointer
    - Points to urgent data as specified by the Urgent flag

### Sources

- [GeeksforGeeks TCP Packet]https://www.geeksforgeeks.org/computer-networks/tcp-ip-packet-format/
- [GeeksforGeeks Control Flags]https://www.geeksforgeeks.org/computer-networks/tcp-flags/