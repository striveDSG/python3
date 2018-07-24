import math
x = input('请输入序号：1:现有三角形  2：等边三角形  3：椭圆形  4：正方形  5：菱形  6：圆形  7：梯形  8：长方形\n')
class Area(object):
    def __init__(self):
        self.pay = 3.14

    # 现有三角形  菱形
    def strugle(self,bottom,high):
        return bottom*high/2

    #等边三角形
    def deStrugle(self,side):
        return math.sqrt(3)*math.pow(side,2)/4

    #椭圆形
    def tuoyuan(self,semia,semim):
        return self.pay*self.semia*self.semime

    #正方形
    def zhengfang(self,side):
        return math.pow(side,2)

    #圆形
    def cicle(self,r):
        return self.pay*math.pow(r,2)

    #梯形
    def tixing(self,sd,xd,h):
        return (sd+xd)*h/2

    #长方形
    def changfang(self,c,k):
        return c*k


w = Area()
# 现有三角形
if x == '1':
    b = int(input('底：'))
    h = int(input('高：'))
    print('面积为：%.2f' %w.strugle(b,h))

#等边三角形
elif x == '2':
    side = int(input('边长：'))
    print('面积为：%.2f' %w.deStrugle(side))

#椭圆形
elif x == '3':
    c = int(input('长半轴：'))
    d = int(input('短半轴：'))
    print('面积为：%.2f' %w.tuoyuan(c,d))

#正方形
elif x == '4':
    side = int(input('边长：'))
    print('面积为：%.2f' %w.zhengfang(side))

#菱形
elif x == '5':
    c = int(input('长交叉线：'))
    d = int(input('短交叉线：'))
    print('面积为：%.2f' %w.strugle(c,d))

#圆形
elif x == '6':
    r = int(input('请输入圆半径：'))
    print('面积为：%.2f' %w.cicle(r))

#梯形
elif x == '7':
    sd = int(input('梯形上底：'))
    xd = int(input('梯形下底：'))
    print('面积为：%.2f' %w.tixing(sd,xd))

#长方形
elif x == '8':
    c = int(input('长：'))
    k = int(input('宽：'))
    print('面积为：%.2f' %w.tixing(c,k))





        