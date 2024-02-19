# pipenv install pyserial
import serial
import time

def main():
    # 串口初始化
    ser = serial.Serial('/dev/ttyACM0', 115200)  # 请替换为你的 Arduino 串口号和波特率

    # 等待串口初始化完成
    time.sleep(1)

    # 向 Arduino 发送数据
    data_to_send = f'1 80 90 90 70\n'
    print(data_to_send)
    ser.write(data_to_send.encode()) 

    # 等待一点时间以确保 Arduino 有足够的时间处理数据
    time.sleep(0.25)

    # 从 Arduino 接收数据
    received_data = ser.readline().decode().strip()
    print(received_data, type(received_data))

    received_data = ser.readline().decode().strip()
    print(received_data, type(received_data))

    received_data = ser.readline().decode().strip()
    print(received_data, type(received_data))

    received_data = ser.readline().decode().strip()
    print(received_data, type(received_data))

    received_data = ser.readline().decode().strip()
    print(received_data, type(received_data))
    
    time.sleep(5)
    data_to_send = f'2 80 90 90 70\n'
    print(data_to_send)
    ser.write(data_to_send.encode()) 

    time.sleep(5)
    data_to_send = f'0\n'
    ser.write(data_to_send.encode()) 

    # data = ser.read(20) #是讀20個字元
    # data = ser.readline() #是讀一行，以/n結束，要是沒有/n就一直讀，阻塞。

    # 关闭串口
    ser.close()

if __name__ == '__main__':

    main()