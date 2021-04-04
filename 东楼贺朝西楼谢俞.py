import tkinter

import tkinter.messagebox

# 账户类
class Account():
    def __init__(self, name, password, balance, operation):
        self.name = name
        self.password = password
        self.balance = balance
        self.operation = operation
        print(self.name, "账户"+self.operation+'成功')

    # 查询余额
    def check(self):
        tkinter.messagebox.showinfo("提示", "介位小朋友有"+str(self.balance)+"元")

    # 存钱
    def save(self, money):
        self.balance += money
        self.operation = "存入" + str(money)

    # 取钱
    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            self.operation = "取出" + str(money)
        else:
            tkinter.messagebox.showinfo("提示", "小朋友你莫得钱啊")

    # 记录
    def record(self):
        f = open(self.name + ".txt", "a")
        text = self.name + "," + self.password + "," + str(self.balance) + "," + self.operation + "\n"
        f.write(text)
        f.close()

window = tkinter.Tk()

window.geometry("400x500")

window.title("清华双杰谋财害命")

label1 = tkinter.Label(window, text="朝俞银行", font=("楷体",20))

label1.pack(pady=25)

label2 = tkinter.Label(window, text="账户名", font=("楷体", 15))

label2.pack(pady=0)

entry1 = tkinter.Entry(window, font=("楷体", 15))

entry1.pack()

label3 = tkinter.Label(window, text="密码", font=("楷体", 15))

label3.pack(pady=0)

entry2 = tkinter.Entry(window, font=("楷体", 15))

entry2.pack()

def signin():

      name = entry1.get()

      pw = entry2.get()

      try:

            open(name + ".txt", "r")

      except:

            user = Account(name, pw, 0, "创建账户")
            
            user.record()

            tkinter.messagebox.showinfo("提示", "吃颗糖")
    
      else:

            tkinter.messagebox.showinfo("提示", "小朋友吃颗糖清醒一下")

def loginin():

      name = entry1.get()

      pw = entry2.get()

      try:

            f1 = open(name + ".txt", "r")

      except:

            tkinter.messagebox.showinfo("提示", "小朋友吃颗糖清醒一下")
    
      else:

            lines = f1.readlines()

            line = lines[len(lines) - 1]

            lineList = line.split(",")

            password1=lineList[1]

            if pw == password1:

                balance1 = int(lineList[2])

                user = Account(name, pw, balance1, "登录账户")

                user.record()

                tkinter.messagebox.showinfo("提示", "吃颗糖")

                def checkMoney():

                    user.check()
                    user.record()

                def savein():

                    def savein2():

                        money = entry10.get()

                        money1 = int(money)

                        user.save(money1)
                        user.record()

                        tkinter.messagebox.showinfo("提示", "存储完成")

                        windows3.destroy()

                    windows3 = tkinter.Tk()
                    
                    windows3.geometry("300x400")
                    
                    label10 = tkinter.Label(windows3, text="小朋友要存多少钱？", font=("楷体",20))

                    label10.pack(pady=20)

                    entry10 = tkinter.Entry(windows3, font=("楷体", 15))

                    entry10.pack(pady=40)

                    button10 = tkinter.Button(windows3, text="确定", font=("楷体", 15), command=savein2)

                    button10.pack(pady=20)


                def saveout():

                    def saveout2():

                        money2 = entry10.get()

                        money3 = int(money2)

                        user.withdraw(money3)

                        user.record()

                        tkinter.messagebox.showinfo("提示", "取出完成")

                        windows3.destroy()

                    windows3 = tkinter.Tk()
                    
                    windows3.geometry("300x400")
                    
                    label10 = tkinter.Label(windows3, text="小朋友要取多少钱？", font=("楷体",20))

                    label10.pack(pady=20)

                    entry10 = tkinter.Entry(windows3, font=("楷体", 15))

                    entry10.pack(pady=40)

                    button10 = tkinter.Button(windows3, text="确定", font=("楷体", 15), command=saveout2)

                    button10.pack(pady=20)

                window.destroy()

                windows1=tkinter.Tk()

                windows1.geometry("400x500")

                label4 = tkinter.Label(windows1, text="朝俞银行", font=("楷体",20))

                label4.pack(pady=25)

                button3 = tkinter.Button(windows1, text="查询金额", font=("楷体", 15), width=25, command=checkMoney)

                button3.pack(pady=12.5)

                button4 = tkinter.Button(windows1, text="存钱", font=("楷体", 15), width=25, command=savein)

                button4.pack(pady=12.5)

                button5 = tkinter.Button(windows1, text="取钱", font=("楷体", 15), width=25, command=saveout)

                button5.pack(pady=12.5)

            else:

                tkinter.messagebox.showinfo("提示", "小朋友吃颗糖清醒一下")

button1 = tkinter.Button(window, text="登录", font=("楷体", 15), width=25, command=loginin)

button1.pack(pady=12.5)

button2 = tkinter.Button(window, text="注册", font=("楷体", 15), width=25, command=signin)

button2.pack(pady=12.5)
