from socket import *
# 1.创建套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 2.准备连接服务器，建立连接
serve_ip = "192.168.8.178"#服务器端（主机B）的IP
serve_port = 8001  #端口，比如8000
tcp_socket.connect((serve_ip,serve_port))  # 连接服务器，建立连接,参数是元组形式
while(1):
    send_data = input("请输入内容：")
    if send_data=='end':
        print('========end========')
        break
    #send_data = "给服务器端发送数据了"
    tcp_socket.send(send_data.encode("gbk"))
    if send_data == "exit":
         break
    #从服务器接收数据
    #注意这个1024byte，大小根据需求自己设置
    from_server_msg = tcp_socket.recv(1024)
    #加上.decode("gbk")可以解决乱码
    print(from_server_msg.decode("gbk"))
#关闭连接
tcp_socket.close()
# #准备需要传送的数据
# send_data = "今天是2023年07月12日，给服务器端发送数据了"
# tcp_socket.send(send_data.encode("gbk")) 
# #从服务器接收数据
# #注意这个1024byte，大小根据需求自己设置
# from_server_msg = tcp_socket.recv(1024)
# #加上.decode("gbk")可以解决乱码
# print(from_server_msg.decode("gbk"))  
# #关闭连接
# tcp_socket.close()