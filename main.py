FILE_NAME=test.bin

def to_bin(var):
    print("Write var to disk in binary format")


    while var > 0:
        binVar = var % 2
        if binVar == 0 or binVar == 1:
            with open(FILE_NAME, 'w') as file:
                file.seek(0)
                file.write(binVar)
        var = var // 2



def from_bin():
    print("Reading binary file to memory")

if __name__ == "__main__":
    print("In the main file")
    packet1 = Packet("192.168.0.1")
    packet1.to_binary()
    to_bin(10)
    var = from_bin()
    print(var)


class Packet:
    def __init__(self, source_port, dest_port, seq_num, ack_num, payload):
        self.source_port=source_port
        self.dest_port=dest_port
        self.seq_num=seq_num
        self.ack_num=ack_num
        self.payload=payload
    def __str__(self):
        return f"Packet from {self.source_ip} to {self.dest_ip} with payload: {self.payload}"
    def to_binary(self):
        with open('output.bin', 'wb') as f:
            for p in self.source_ip.split('.'):
                f.write(int(p).to_bytes(1, byteorder='big'))
        print("Packet written to output.bin in binary format")