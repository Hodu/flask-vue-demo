
if __name__ == '__main__':
    # input = input("input:")  # 输入
    # print("input ", input)
    # print(input, "end")  # 不换行输出

    a = b = c = "哈哈"  # 多个变量赋值
    print(a, b, c)
    a = 3.14j
    print(a)
    print(a + 3)
    b = 2+1j
    c = 1+1j
    print(b, c, b*c)
    a = "hello"
    """
     h   e   l   l   o
     0   1   2   3   4  # 从左到右索引默认0开始的
     -5  -4  -3  -2  -1  # 从右到左索引默认-1开始的
    """
    print(a)
    print(a[1:])  # 从索引1开始到结尾: ello
    print(a[:3])  # 从索引0开始到索引3(不包含3): hel
    print(a[::4])  # 取值可以有三个参数，分别为起始索引、结束索引、步长: ho
    print(a[:-2])  # 从索引0开始到索引-2: hel
    print(a[-2:])  # 从索引-2开始: lo
    print(a[:])  # 从索引0到结尾 即：hello

    tuple2 = ('runoob', 786, 2.23, 'john', 70.2)
    list2 = ['runoob', 786, 2.23, 'john', 70.2]
    print("tuple : ", tuple2)
    print("list : ", list2)
    # tuple[2] = 1000  # 元组中是非法应用
    list2[2] = 1000  # 列表中是合法应用
    print("list : ", list2)
    dict2 = {'one': "hello world"}
    print(dict2)
    dict2['two'] = "hello python"
    print(dict2)

    print(int("1", 2))  # 将字符串转换成对应base(2)的整数
    print(float(2))  # 将字符串转换成对应base(2)的整数
    print(1/2)  # 将字符串转换成对应base(2)的整数
    print(1/3)  # 将字符串转换成对应float数
    print(7//3)
    print(7/3)
    print("="*20)
    a = 0b0011_1100  # 60
    b = 0b0000_1101  # 13
    print(a & b)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(~a)
    print(a and b)  # 如果a为False, 则结果为False, 否则为b的计算值
    print(a or b)  # 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值
    print(not a)  # 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True

    print(a >> 2)
    print(a >> 2 + 1)  # a >> 3





