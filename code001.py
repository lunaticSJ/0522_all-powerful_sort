"""
    练习：入学后第一次上体育课，体育老师要求大家按照身高从低到高排成一排，
    使用python程序模拟过程。获取10名同学的身高，单位厘米
"""
#list =[145,154,163,134,176,166,165,188,144,133,147]

def get_max(value):
    for i in range(len(value)-1):
        for j in range(len(value)- 1 -i):
            if value[j] > value[j+1]:
                value[j],value[j+1] = value[j+1],value[j]


if __name__ == "__main__":
    #原始数据
    value = [145,154,163,134,176,166,165,188,144,133,147]
    get_max(value)
    print(value)





def get_max(value):
    for i in range(len(value)-1):
        for r in range(len(value) -1 -i):
            if value[r] > value[r+1]:
                value[r],value[r+1] = value[r+1],value[r]

















