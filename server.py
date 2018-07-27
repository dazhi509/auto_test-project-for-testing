import socket
import urllib.parse
import _thread
import pymysql


# class 用于保存数据
class Request(object):
    def __init__(self):
        self.server_ID = ''
        self.server_num = ''
        self.board = ''
        self.cpu = ''
        self.memory_bank = ''
        self.hard_disk = ''
        self.raid = ''
        self.vga = ''
        self.gpu = ''
        self.hba = ''
        self.net_card = ''
        self.fc_card = ''
        self.inspect_time = ''
        self.status = ''

    def form(self):
        body = urllib.parse.unquote(self.body)
        args = body.split('&')
        f = {}
        log('form debug', args, len(args))
        for arg in args:
            k, v = arg.split('=')
            f[k] = v
        return f

    def json(self):
        import json
        return json.loads(self.body)


def process_data(data):
    """
    用于处理数据
    :param data:
    :return:
    """
    pass


# def save(data):
#     """
#     用于保存数据
#     :param data:
#     :return:
#     """
#     mysql_host = '192.168.1.210'
#     mysql_db = 'dataOA'
#     mysql_user = 'root'
#     mysql_password = 'wuzhou666'
#     mysql_port = 3306
#     db = pymysql.connect(host=mysql_host, port=mysql_port,
#                          user=mysql_user, charset='utf8',
#                          password=mysql_password, db=mysql_db, )
#     cur = db.cursor()


def process_request(connection):
    """
    用于接收数据并处理、存储数据。
    :param connection:
    :return:
    """
    data = b''
    buf_size = 1024
    while True:
        r = connection.recv(buf_size)
        print(r, "receive datas")
        if len(r) == 0:
            break
        data += r
    data = data.decode('utf-8')
    print(data)
    log('完整请求,数据接收完毕')

    # # 将数据处理成标准格式
    # process_data(data)
    #
    # path = r.split()[1]
    # # 创建一个新的 request 并设置
    # request = Request()
    # request.method = r.split()[0]
    # request.add_headers(r.split('\r\n\r\n', 1)[0].split('\r\n')[1:])
    # # 把 body 放入 request 中
    # request.body = r.split('\r\n\r\n', 1)[1]
    #
    #
    # # 用 response_for_path 函数来得到 path 对应的响应内容
    # response = response_for_path(path, request)
    # # 把响应发送给客户端
    # connection.sendall(response)
    # print('完整响应')
    # try:
    #     log(response.decode('utf-8').replace('\r\n', '\n'))
    # except Exception as e:
    #     log('异常', e)
    # # 处理完请求, 关闭连接
    # connection.close()
    # print('关闭')


def run(host='', port=3000):
    """
    启动服务器
    """
    print('start at', '{}:{}'.format(host, port))
    with socket.socket() as s:
        s.bind((host, port))
        s.listen(3)
        while True:
            connection, address = s.accept()
            connection.sendall(b'test')
            print('连接成功, 使用多线程处理请求', address)
            _thread.start_new_thread(process_request, (connection,))


if __name__ == '__main__':
    config = dict(
        host='127.0.0.1',
        port=3000,
    )
    run(**config)
