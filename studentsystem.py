# _*_ coding:utf-8   _*_
import re
import os

filename = "students.txt"


def menu():
    print('''
        ╔———————学生信息管理系统————————╗
    │                                              │
    │   =============== 功能菜单 ===============   │
    │                                              │
    │   1 录入学生信息                             │
    │   2 查找学生信息                             │
    │   3 删除学生信息                             │
    │   4 修改学生信息                             │
    │   5 排序                                     │
    │   6 统计学生总人数                           │
    │   7 显示所有学生信息                         │
    │   0 退出系统                                 │
    │  ==========================================  │
    │  说明：通过数字或↑↓方向键选择菜单          │
    ╚———————————————————————╝
    ''')


def main():
    flag = True
    while flag:
        menu()
        option = input("请选择：")
        option_str = re.sub("/D", "", option)  # 提取数字
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print("您已退出学生成绩管理系统！")
                flag = False
            elif option_int == 1:  # 录入学生成绩信息
                insert()
            elif option_int == 2:  # 查找学生成绩信息
                search()
            elif option_int == 3:  # 删除学生成绩信息
                delete()
            elif option_int == 4:  # 修改学生成绩信息
                modify()
            elif option_int == 5:  # 排序
                sort()
            elif option_int == 6:  # 统计学生总数
                total()
            elif option_int == 7:  # 显示所有学生信息
                show()


def insert():
    studentList = []  # 保存学生信息的列表
    # Variable in function should be lowercase
    # 函数变量应为小写
    flag = True
    while flag:
        id = input("请输入ID （如1001）：")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            c = int(input("请输入C语言成绩："))
        except:
            print("输入无效，非整数... 请重新输入！")
            continue
        stdent = {"id": id, "name": name, "english": english, "python": python
            , "c": c}
        studentList.append(stdent)  # 将学生字典添加到列表中
        inputMark = input("是否继续添加？ （y/n）:")
        if inputMark == "y":
            flag = True
        else:
            flag = False
    save(studentList)  # what`s wrong?
    print("学生信息录入完毕！！")


def save(student):
    try:
        students_txt = open(filename, "a")
    except Exception as e:
        students_txt = open(filename, "w")
    for info in student:
        students_txt.write(str(info) + "\n")
    students_txt.close()


def search():
    flag = True
    student_query = []  # 保存查询结果的学生列表
    while flag:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按照ID查询输入1；按照姓名查询输入2：")
            if mode == "1":
                id = input("请输入学生ID：")
            elif mode == "2":
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，清重新输入！")
                search()
        with open(filename, "r") as file:
            student = file.readlines()  # 读取全部内容
            for list in student:
                d = dict(eval(list))
                if id != "":  # 判断是否按照ID查
                    # 为啥3.8 is not  报错了？3.6却可以？
                    # is not 和 ！= 的区别？
                    # 语法警告：带有文字的“不是”。 你是说“！=”吗？如果id不是“”：＃判断是否按照ID查
                    if d['id'] == id:
                        student_query.append(d)  # 将找到的学生信息保存到列表中
                elif name != "":
                    if d['name'] == name:
                        student_query.append(d)
            show_student(student_query)
            student_query.clear()
            inputMark = input("是否继续查询？ （y/n）:")
            if inputMark == "y":
                flag = True
            else:
                flag = False
    print("暂未保存数据信息...")
    return


def show_student(studentList):  # 将保存在列表中的学生信息显示出来
    if not studentList:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("id"), info.get("name"), str(info.get("english")), str(info.get("python")),
                                 str(info.get("c")),
                                 str(info.get("english") + info.get("python") + info.get("c")).center(12)))


def delete():
    flag = True
    while flag:
        studentId = input("请输入要删除的学生ID：")
        if studentId != "":
            if os.path.exists(filename):
                with open(filename, "r") as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            ifdel = False  # 标记是否删除
            if student_old:
                with open(filename, "w") as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d['id'] != studentId:
                            wfile.write(str(d) + "\n")  # 将信息写入文件
                        ifdel = True  # 标记已经删除
                    if ifdel:
                        print("ID为 %s 的学生信息已经被删除..." % studentId)
                    else:
                        print("没有找到ID为 %s 的学生信息..." % studentId)
            else:
                print("无学生信息...")
                break
            show()
            inputMark = input("是否继续删除？（y/n）:")
            if inputMark == "y":
                flag = True
            else:
                flag = False


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input("请输入要修改的学生ID：")
    with open(filename, "w") as wfile:
        for student in student_old:
            d = dict(eval(student))  # 字符串转字典
            if d['id'] == student_id:
                print("已找到此学生，可以修改其信息！")
                while True:  # 输入要修改的信息
                    try:
                        d["name"] = input("请输入姓名：")
                        d["english"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入Python成绩："))
                        d["c"] = int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误,请重新输入...")
                    else:
                        break
                student = str(d)  # 将字典转换成字符串
                wfile.write(student + "\n")
                print("修改成功！")
            else:
                wfile.write(student)  # 将未修改的信息写入到文件
                print("老铁，没找到这个人阿，你是不是记错了？要不你先录入一下！")
    inputMark = input("是否继续修改？（y/n）:")
    if inputMark == "y":
        modify()


def sort():
    global ascBool
    show()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            student_old = file.readlines()
            student_new = []
        for list in student_old:
            d = dict(eval(list))
            student_new.append(d)
    else:
        return
    asc = input("请选择（0升序；1降序）：")
    if asc == "0":
        ascBool = False
    elif asc == "1":
        ascBool = True
    else:
        print("您的输入有误,请重新输入！")
        sort()
    mode = input("请选择排序方式（1按英语成绩排序；2按Python成绩排序；3按C语言成绩排序；0按总成绩排序）")
    if mode == "1":
        student_new.sort(key=lambda x: x["english"], reverse=ascBool)
    elif mode == "2":  # 按Python成绩排序
        student_new.sort(key=lambda x: x["python"], reverse=ascBool)
    elif mode == "3":  # 按C语言成绩排序
        student_new.sort(key=lambda x: x["c"], reverse=ascBool)
    elif mode == "0":  # 按总成绩排序
        student_new.sort(key=lambda x: x["english"] + x["python"] + x["c"], reverse=ascBool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(student_new)  # 显示排序结果


def total():
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
            if student_old:
                print("一共有 %d 名学生！" % len(student_old))
    else:
        print("还没有录入学生信息！")


def show():
    student_new = []
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息...")


if __name__ == "__main__":
    main()
