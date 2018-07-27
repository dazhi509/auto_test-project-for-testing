import socket


class Client(object):
    def __init__(self):
        self.host = ''
        self.port = 0

    def send_msg_to_tcpserver(self):
        tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket---{}'.format(tcpClientSocket))

        tcpClientSocket.connect((self.host, self.port))
        print('connect success!')

        while True:
            # 发送数据
            sendData = b'sdsdsdsd'

            if len(sendData)>0:
                tcpClientSocket.send(sendData)
            else:
                break
            print('the receive message is:{}'.format(recvData))

        # tcpClientSocket.close()
        # print('close socket!')



tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket---{}'.format(tcpClientSocket))

tcpClientSocket.connect(('127.0.0.1', 8000))
print('connect success!')

while True:
    # 发送数据
    sendData = b'sdsdsdsd'
    #
    # if len(sendData)>0:
    #     tcpClientSocket.send(sendData)
    # else:
    #     break

    recvData = tcpClientSocket.recv(1024)

    print('the receive message is:{}'.format(recvData))

# tcpClientSocket.close()
# print('close socket!')
