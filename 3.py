import time
#注册系统
flag=True
while flag==True:
    n=input("注册名：")
    m=input("密码：")
    x=1
    while x==1:
        if "0"<=n[0]<="9":
            print("注册名首字不能为数字")
            x=0
            break
        elif len(n)<5 or len(n)>10:
            print("注册名长度为5-10")
            x=0
            break
        for i in n[1:]:
            if not("1"<=i<="9" or "a"<=i<="z" or "A"<=i<="Z"):
                 print("注册名要求由字母或数字构成")
                 x=0
                 break
        if m.isdigit():
            print("密码不能是纯数字")
            x=0
            break
        elif len(m)<10 or len(m)>20:
            print("密码长度为10-20")
            x=0
            break
        else:
            a=0
            b=0
            for i in m:
                if "a"<=i<="z":
                     a+=1
                elif "A"<=i<="Z":
                     b+=1
            if a==0 or b==0:
                print("密码中字母必须包含大小写")
                x=0
                break
        print("{}注册成功，请返回首页进行账号验证".format(n))
        flag="FALSE"
        break







#账号验证系统
c=0
while True:
    yhm=input("用户名：")
    mi=input("密码：")
    if yhm==n and mi==m:
         print("欢迎{}".format(yhm))
         break
    else:
        c+=1
        print(c)
    if c>=5:
        print("错误次数太多，请稍后再试")
        c=0
        time.sleep(30)






#密码修改系统
print("{}已进入修改密码界面".format(yhm))
c=0
while True:
    o=0
    y=input("原用户名：")
    ym=input("原密码：")
    if y==n and ym==m:
         print("验证成功")
         o=1
         break
    else:
        c+=1
    if c>5:
         print("错误次数太多，为保护账户安全，账号已退出系统")
         break
if o==1:
    x=1
    while x==1:
        xmm=input("请输入新密码：")
        while True:
            if xmm.isdigit():
                print("密码不能是纯数字")
                break
            elif len(xmm)<10 or len(xmm)>20:
                print("密码长度为10-20")
                break
            else:
                a=0
                b=0
                for i in xmm:
                    if "a"<=i<="z":
                         a+=1
                    elif "A"<=i<="Z":
                         b+=1
                if a==0 or b==0:
                    print("密码中字母必须包含大小写")
                    break
            print("密码修改成功")
            x=0
            break
            

