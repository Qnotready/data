# 定义打印函数
def displayMenu():
    "无参数，无返回，打印"
    print("-" * 30)
    print("      学生管理系统    V8.88   ")
    print("1.添加学生的信息")
    print("2.删除学生的信息")
    print("3.修改学生的信息")
    print("4.查询学生的信息")
    print("5.遍历所有的学生的信息")
    print("6.退出系统")
    print("-" * 30)

# 定义选择函数


def getChoice():
    selectedKey = input("请输入序列号：")
    return selectedKey


def addNewstu(studentsTemp):
    "完成添加学生信息的功能"
    name = input("请输入学生姓名：")
    stuId = input("请输入学生的学号：")
    age = input("请输入学生的年龄：")
    stuClass = input("请输入学生的年级和班级：")

    stuInfo = {}
    stuInfo['name'] = name
    stuInfo['stuId'] = stuId
    stuInfo['age'] = age
    stuInfo['stuClass'] = stuClass

    studentsTemp.append(stuInfo)


def printAllinfo():
    "遍历所有的学生的信息"
    print("*" * 30)
    print("遍历所有的学生的信息中。。。。。。。")
    print("姓名   学号   年龄   班级")
    for temp in students:
        print("%-4s   %-4s   %-4s   %-4s   " %
              (temp.get('name'), temp.get('stuId'), temp.get('age'), temp.get('stuClass')))
    print("*" * 30)


def delStu():
    "删除学生相关信息"
    num = int(input("请输入需要删除的学生序号："))
    del students[num - 1]


def changeStu():
    "更改学生相关信息"
    num = int(input("请输入你想要更改学生的序号："))

    name = input("请输入学生姓名：")
    stuId = input("请输入学生的学号：")
    age = input("请输入学生的年龄：")
    stuClass = input("请输入学生的年级和班级：")

    studentsChange = {}
    studentsChange['name'] = name
    studentsChange['stuId'] = stuId
    studentsChange['age'] = age
    studentsChange['stuClass'] = stuClass
    students[num - 1] = studentsChange


def findStu():
    "查询学生的相关信息"
    num = int(input("请输入你想要查询学生的序号："))
    print("遍历所有的学生的信息中。。。。。。。")
    print("姓名   学号   年龄   班级")

    '''for temp in students[num - 1].items():
        print(temp)
        #(temp['name'], temp['stuId'], temp['age'], temp['stuClass']))'''

    for temp in students[num - 1].values():
        print(temp, end="     ")

students = []


def main():

    while True:
        displayMenu()
        keyId = getChoice()
        juge = keyId.isdigit()  # 判断输入的字符串是否为数字 isalpha判断是否为字母
        if juge == True:
            key = int(keyId)
            if key == 1:
                print("你选择了添加名片功能:")
                addNewstu(students)
            elif key == 2:
                delStu()
            elif key == 3:
                changeStu()
            elif key == 4:
                findStu()
            elif key == 5:
                printAllinfo()
            elif key == 6:
                break
            else:
                print("输入错误，请重新输入：")
        else:
            print("不能输入字母，请输入数字：")


if __name__ == "__main__":
    main()
