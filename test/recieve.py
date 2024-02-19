# pipenv install pyserial
import serial
import time
import re
import tkinter as tk

def update_label(ser, window, label):

    # 从 Arduino 接收数据
    received_data = ser.readline().decode('utf-8')
    
    # 使用正则表达式提取数字
    numbers = re.findall(r'\d+', received_data)
    # 将提取的数字转换为整数
    numbers = [int(num) for num in numbers]

    if(len(numbers) == 4):
        new_info = "新的信息：" + str(list(numbers))
    else:
        new_info = "新的信息： error" 

    label.config(text=new_info)
    window.after(1000, update_label, ser, window, label)  # 每秒调用一次update_label函数


def main(ser):
    window = tk.Tk()
    window.title('GUI')
    window.geometry('380x400')
    window.resizable(False, False)

    # 创建一个IntVar，用于存储信息的计数
    # counter = tk.IntVar()

    # 创建Label控件，显示信息
    label = tk.Label(window, text="初始信息", font=('Arial', 14))
    label.pack(pady=20)

    # 初始调用一次update_label函数，之后会每秒自动调用一次
    update_label(ser, window, label)

    # 启动主循环
    window.mainloop()

if __name__ == '__main__':

    # 串口初始化
    ser = serial.Serial('/dev/ttyACM0', 9600)  # 请替换为你的 Arduino 串口号和波特率

    # 等待串口初始化完成
    time.sleep(1)

    main(ser)