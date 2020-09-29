def attack01():
    '''
    第一种攻击方式
    :return:
    '''
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("肘击")

def attack02(count):
    '''
    急眼了，胡打一通
    :param count:
    :return:
    '''
    for _ in  range(count):
        attack01()
        print()

attack02(3)