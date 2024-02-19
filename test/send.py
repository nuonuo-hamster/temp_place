# pipenv install pyserial
import serial
import time

def main(ser):
    
    data_to_send = 'OFX41\n' #'ONX41\n'
    print("send...",data_to_send)
    ser.write(data_to_send.encode('utf-8')) 

    # 关闭串口
    # ser.close()

if __name__ == '__main__':

    # 串口初始化
    ser = serial.Serial('/dev/ttyACM0', 9600)  # 请替换为你的 Arduino 串口号和波特率

    # 等待串口初始化完成
    time.sleep(1)

    main(ser)

    ser.close()