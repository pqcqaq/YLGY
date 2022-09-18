import requests
import random
import time
import threading
from tkinter import *
from ttkthemes import *
from tkinter.ttk import *
import tkinter.messagebox

proxy_list=[
    'http://124.112.174.237:8080',  #添加代理服务器
    'http://49.88.148.249:8888',
    'http://113.241.137.248:8080',
    'http://218.7.116.103:9999',
    'http://122.140.5.115:9999',
    'http://58.55.252.58:8080',
    'http://218.1.201.136:8888',
    'http://113.101.96.66:8080',
    'http://175.4.184.220:9999',
    'http://114.104.185.239:8080',
    'http://140.255.202.124:9999',
    'http://117.28.134.240:8888',
    'http://61.135.208.184:80',
    'http://218.108.168.132:80',
    'http://218.108.168.144:82',
    'http://221.2.174.164:8082',
    'http://202.98.123.126:8080',
]

headers_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.1785.109 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2832.1 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.622.43 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.1263.10 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.341.42 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.1713.58 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.346.92 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2638.48 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.1698.79 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3187.76 Safari/537.36",
]
#https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=15&rank_role=1&skin=1',headers=headers)
#----------------------------------------------------------------------主循环------------------------------------------------------------
flag = False
class MyThread(threading.Thread):
    def run(self):
        global flags
        i = 1
        while (True):
            if flag:
                print("开始尝试通关......")
                try:
                    headers = {'User-Agent': random.choice(headers_list),
                                't': token.get()}
                    proxy = {
                        'http': random.choice(proxy_list)
                    }
                    print("使用代理服务器："+ str(proxy))
                    r = requests.get(
                        'https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=100&rank_state=1&rank_time=4026&rank_role=1&skin=1',
                        headers=headers, timeout=10, proxies=proxy)
                    print("               第" + str(i) + "次" + " Successed")
                    Rut(True,i)
                    i += 1
                except requests.exceptions.ConnectionError:
                    print("访问错误,暂停300秒.....")
                    Rut(False, i)
                    time.sleep(300)
        pass
thread = MyThread()
thread.daemon = True
#-------------------------------------------------------------------按钮函数-------------------------------------------------------------------
def Exit():
    global flag
    flag = False
    root.destroy()
def Switch():
    global flag
    if not flag:
        print("开始")
        try:
            thread.start()
            print("Start Running...")
        except RuntimeError:
            print("Back Running...")
        flag = True
        print(token.get());
        butauto.config(text="暂停")
    else:
        butauto.config(text="开始")
        print("程序已暂停")
        flag = False
def Rut(result,i):
    if result:
        lbRut2 = Label(root, text=("成功"+str(i)+"次"), font=("黑体", 16)).place(x=16, y=80)
    else:
        lbRut2 = Label(root, text=("等待重试"), font=("黑体", 18)).place(x=14, y=80)
        #lbRut2.config(fg = "red")
#-------------------------------------------------------------------窗口属性-------------------------------------------------------------------
root=ThemedTk(theme="adapta", toplevel=True, themebg=True)
root.title("羊了个羊刷分器 By QCQCQC")
root.geometry("260x160")
try:
    root.iconbitmap("./YLGY.ico")
except:
    tkinter.messagebox.showinfo("错误","图标文件丢失，程序将使用默认图标！")
root.attributes('-alpha',0.85)
root.minsize(260,160)
#-------------------------------------------------------------------按钮属性-------------------------------------------------------------------
butexit = Button(root, text=" 退出 ",command = Exit)
butexit.place(x = 135,y = 90)
butauto = Button(root, text=" 开始 ",command = Switch)
butauto.place(x = 135,y = 40)
#------------------------------------------------------------------token输入框-----------------------------------------------------------------
lbToken = Label(root, text='Token:', font=("黑体", 14)).grid()
tokenStr = StringVar(value='Token')
token = Entry(root,textvariable=tokenStr)
token.grid(row=0,column=1,sticky=E)
lbRut1 = Label(root, text="运行结果:", font=("黑体", 16)).place(x = 16,y = 40)

root.mainloop()