import MyfuntionsOne as f

f.load_info()

print("学生信息已导入！")

while True:
    f.show_menu()  # 显示菜单
    action_str = input("请选择希望执行的操作: ")
    print("你选择的操作是 %s" % action_str)
    if action_str in ["1", "2", "3", "4", "5", "6"]:
        if action_str == "1":
            f.show_all()
        elif action_str == "2":
            f.new_student()
        elif action_str == "3":
            f.search_student()
        elif action_str == "4":
            f.update_student()
        elif action_str == "5":
            f.delete_student()
        elif action_str == "6":
            f.save_info()
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【学生信息管理系统】:")
        break
    else:
        print("输入错误，请重新输入:")
       

    
def show_menu():
    """显示菜单"""
    print()
    print('*' * 70)
    print('欢迎使用【学生信息管理系统】')
    print()
    print('1.浏览全部')
    print('2.新增学生')
    print('3.搜索学生')
    print('4.修改学生')
    print('5.删除学生')
    print('6.保存信息')
    print('0.退出系统')
    print('*' * 70)
    print()


def new_student():
    """新增学生"""
    print('-' * 70)
    print('新增学生')
    # 提示用户输入学生的详细信息
    num_str = input('请输入学号：')
    name_str = input('请输入姓名：')
    class_str = input('请输入班级：')
    sex_str = input('请输入性别：')
    age_str = input('请输入年龄：')
    phone_str = input('请输入电话：')
    qq_str = input('请输入 QQ：')
    addr_str = input('请输入地址：')
    # 使用用户输入的信息建立一个学生信息字典
    card_dict = {'num_str': num_str,
                 'name_str': name_str,
                 'class_str': class_str,
                 'sex_str': sex_str,
                 'age_str': age_str,
                 'phone_str': phone_str,
                 'qq_str': qq_str,
                 'addr_str': addr_str}
    # 将学生信息字典添加到列表中
    card_list.append(card_dict)  # 一个字典的键值对为列表中的一个元素
    # 提示用户添加成功
    print('添加%s 的信息成功' % name_str)


def show_all():
    """显示所有学生信息"""
    print('-' * 70)
    print('显示所有学生信息')
    # 判断是否存在学生信息记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print('当前没有任何学生记录，请使用新增功能添加学生信息')
        return
    # 打印表头
    for name in ["学号", "姓名", "班级", "性别", "年龄", "电话", "QQ", "地址"]:
        print(name, "\t", end="")
    print('')
    # 打印分隔线
    print('=' * 70)
    # 遍历学生信息列表依次输出字典信息
    for card_dict in card_list:
        print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (card_dict['num_str'],
                                                  card_dict['name_str'],
                                                  card_dict['class_str'],
                                                  card_dict['sex_str'],
                                                  card_dict['age_str'],
                                                  card_dict['phone_str'],
                                                  card_dict['qq_str'],
                                                  card_dict['addr_str']))


def search_student():
    """搜索学生信息"""
    print('-' * 70)
    print('搜索学生信息')
    # 1.提示用户输入要搜索的姓名
    find_name = input('请输入要搜索的姓名：')
    # 2.遍历学生信息列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for i in range(len(card_list)):
        if find_name == card_list[i]['name_str']:
            print("学号\t 姓名\t 班级\t 性别\t 年龄\t 电话\tQQ\t 地址")
            print('=' * 70)
            print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (card_list[i]['num_str'],
                                              card_list[i]['name_str'],
                                              card_list[i]['class_str'],
                                              card_list[i]['sex_str'],
                                              card_list[i]['age_str'],
                                              card_list[i]['phone_str'],
                                              card_list[i]['qq_str'],
                                              card_list[i]['addr_str']))
            break
        else:
            print('抱歉，没有找到%s' % find_name)
