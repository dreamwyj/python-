import socket


def main():
    # 1.创建套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    # 2.获取服务器的ip,port
    dest_ip=input("输入下载服务器的ip:")
    dest_port=input("输入下载服务器的port:")

    # 3.连接服务器
    tcp_socket.connect((dest_ip,int(dest_port)))

    # 4.获取下载的文件名字
    download_file_name=input("请输入要下载的文件名字：")

    # 5.将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode("utf-8"))

    # 6.接受文件中的数据
    recv_data=tcp_socket.recv(1024)
    
    if recv_data:
        # 7.保存接受到的数据到一个文件中
        with open("[新]"+download_file_name,"wb")as f:
            f.write(recv_data)

    # 8.关闭套接字
    tcp_socket.close()

if __name__=="__main__":
    main()


