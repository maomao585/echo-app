import sys

def echo():
    shout = "\\~s" in sys.argv  # 修正了转义字符
    message = input("Type anything: ")
    print(message.upper() if shout else message)

if __name__ == "__main__":  # 修正了缩进
    echo()