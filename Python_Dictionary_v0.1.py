import csv
def cn_or_en(cn,en):
    flag_cn = flag_en= 0
    for char_cn in cn:
        if not '\u4e00' <= char_cn <= '\u9fa5':
            flag_cn=0
        else:
            flag_cn=1
    for char_en in en:
        if 97 <= ord(char_en) <= 122 or 65 <= ord(char_en) <= 90:
            flag_en=1
        else:
            flag_en=0
    return flag_cn,flag_en
def dict_input():
    while True:
        dict_file = open('dicts.csv', mode='a', encoding='utf-8-sig', newline='')
        csv_writer = csv.DictWriter(dict_file, fieldnames=["中文", "英文", ])
        flag=()
        flag_if_in_dict = 0
        cn = input("请输入中文(输入#返回主菜单)：")
        en = input('请输入英文(输入#返回主菜单)：')
        if cn==en=='#':
            break
        flag=cn_or_en(cn,en)
        if flag[0]==0:
            print("中文输入有误，请重新输入")
            continue
        elif flag[1]==0:
            print("英文输入有误，请重新输入")
            continue
        else:
            with open('dicts.csv', 'a+', encoding='utf-8-sig', newline='') as f:
                csv_reader = csv.reader(f)
                data = list(csv_reader)
                for row in data:
                    if data.index(row)==0:
                        continue
                    if row[0]==cn and row[1]==en:
                        flag_if_in_dict=1
                if flag_if_in_dict==1:
                    print('对应词条已存在，请重试！')
                    continue
                else:
                    dict_true={"中文":cn,"英文":en}
                    csv_writer.writerow(dict_true)
                    print("已保存!")
                    dict_file.close()
                    break

def dict_show():
    print("—————————————")
    with open('dicts.csv', 'r',encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            if data.index(row)==0:
                print("语言|{} {} ".format(row[0], row[1]), end="")
            else:
                print("词组|{} {} ".format(row[0],row[1]),end="")
            print()
    print("——————————————")
    dict_file.close()

def dict_change():
    flag_if_change=0
    while True:
        change_char=input("请输入要修改的内容(按什么内容查找)(输入#返回主菜单)：")
        if change_char=='#':
            break
        change_cn=input("请输入要修改的中文：")
        change_en=input("请输入要修改的英文：")
        flag=cn_or_en(change_cn,change_en)
        flag_change=cn_or_en(change_char,change_char)
        if flag[0] == 0:
            print("中文输入有误，请重新输入")
            continue
        elif flag[1] == 0:
            print("英文输入有误，请重新输入")
            continue
        else:
            with open('dicts.csv', 'r', encoding='utf-8-sig', newline='') as f:
                csv_reader = csv.reader(f)
                data = list(csv_reader)
                for row in data:
                    if data.index(row)==0:
                        continue
                    if flag_change[0]==1:
                        if row[0]==change_char:
                            print("已修改'{}'对应词组为 '{}'和'{}'".format(change_char,change_cn,change_en))
                            row[0]=change_cn
                            row[1]=change_en
                            flag_if_change=1
                    elif flag_change[1]==1:
                        if row[1]==change_char:
                            print("已修改'{}'对应词组为 '{}'和'{}'".format(change_char,change_cn,change_en))
                            row[0]=change_cn
                            row[1]=change_en
                            flag_if_change=1
            if flag_if_change==0:
                print("未找到对应的单词，请检查")
                continue
            with open('dicts.csv', 'w', encoding='utf-8-sig', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
                dict_file.close()
                break
def dict_del():
    while True:
        flag_if_change = 0
        char_del = input('请输入你要删除的单词(中文或者英文)(输入#返回主菜单)：')
        if char_del=='#':
            break
        flag = cn_or_en(char_del, char_del)
        with open('dicts.csv', 'r', encoding='utf-8-sig', newline='') as f:
            csv_reader = csv.reader(f)
            data = list(csv_reader)
            for row in data:
                if data.index(row) == 0:
                    continue
                if flag[0] == 1:
                    if row[0] == char_del:
                        data.remove(row)
                        flag_if_change = 1
                elif flag[1] == 1:
                    if row[1] == char_del:
                        data.remove(row)
                        flag_if_change = 1
        if flag_if_change == 1:
            with open('dicts.csv', 'w', encoding='utf-8-sig', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
                dict_file.close()
                print("已删除 '{}'！".format(char_del))
                break
        else:
            print("没有找到对应的单词，请检查！")
            continue

def dict_find():
    while True:
        find=0
        char_find = input('请输入你要查找的单词的中文(输入#返回主菜单)：')
        if char_find=='#':
            break
        flag = cn_or_en(char_find, char_find)
        if not flag[0]==1:
            print("输入错误，请输入中文！")
            continue
        with open('dicts.csv', 'r', encoding='utf-8-sig', newline='') as f:
            csv_reader = csv.reader(f)
            data = list(csv_reader)
            for row in data:
                if data.index(row) == 0:
                    continue
                if row[0] == char_find:
                    find=row[1]
                    break
        if find==0:
            print("没有找到 '{}' ，请重新输入！".format(char_find))
            continue
        else:
            print("'{}' 对应的英文是 '{}'".format(char_find, find))
            break


if __name__=='__main__':
    dict_file = open('dicts.csv', mode='a', encoding='utf-8-sig', newline='')
    with open('dicts.csv','r',encoding='utf-8-sig',newline="")as f:
        reader = csv.reader(f)
        csv_writer = csv.DictWriter(dict_file, fieldnames=["中文","英文",])
        if not [row for row in reader]:
            csv_writer.writeheader()


    passwd_book={'yuan':"123456",'user':'user','admin':'admin'}
    admin_book=['yuan','admin']

    while True:
        print("——————欢迎使用电子英汉词典——————")
        user_id=input("请输入用户名(输入q退出系统)：")
        if user_id=='q':
            print("程序退出")
            break
        passwd=input("请输入密码：")
        if user_id in passwd_book.keys():
            if passwd==passwd_book[user_id]:
                if user_id in admin_book:
                    while True:
                        print("欢迎您，{}！您有词典的完全控制权限，请按提示选择".format((user_id)))
                        print('1.词条录入')
                        print('2.信息显示')
                        print('3.词条修改')
                        print('4.词条删除')
                        print('5.单词查询')
                        print('6.退出登录')
                        num_x = input('请按提示输入数字:')
                        try:
                            num_x = int(num_x)
                        except:
                            print("输入应为整数")
                        if num_x == 6:
                            print("已登出！")
                            break
                        elif num_x == 1:
                            dict_input()
                        elif num_x == 2:
                            dict_show()
                        elif num_x == 3:
                            dict_change()
                        elif num_x == 4:
                            dict_del()
                        elif num_x == 5:
                            dict_find()
                        else:
                            print("输入错误，请重新输入！")
                            continue

                else:
                    while True:
                        print("{},您好！您只有访客权限，请按键选择！".format(user_id))
                        print('1.信息显示')
                        print('2.单词查询')
                        print('3.退出登录')
                        num_x = input('请按提示输入数字:')
                        try:
                            num_x = int(num_x)
                        except:
                            print("输入应为整数")
                        if num_x == 3:
                            print("已登出！")
                            break
                        elif num_x == 1:
                            dict_show()
                        elif num_x == 2:
                            dict_find()
                        else:
                            print("输入错误，请重新输入！")
                            continue

            else:
                print('密码错误，请重新输入！')
        else:
            print("用户不存在！请重试！")

    dict_file.close()