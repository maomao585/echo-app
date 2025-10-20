import sys

def echo():
    shout = "-s" in sys.argv  # 判断是否传入 -s 选项
    message = input("Say something: ")
    # 若有 -s 则输出大写，否则正常输出
    print(message.upper() if shout else message)

if __name__ == "__main__":
    echo()