"""FE python サンプル問題"""
import math
import matplotlib.pyplot as plt

def parse(s):
    return [(x[0], int(x[1:])) for x in s.split(';')] #['R4','F100','T90','E0']

class Marker():
    """マーカー"""
    def __init__(self) -> None:
        self.x , self.y, self.angle = 0, 0, 0;
        plt.xlim(-320, 320);  #x軸の表示範囲を設定
        plt.ylim(-240,240);   #y軸の表示範囲を設定

    def forward(self, val: int):
        rad = math.radians(self.angle);
        dx = val * math.cos(rad) #x軸方向の増分
        dy = val * math.sin(rad) #y軸方向の増分
        x1, y1, x2, y2 = self.x, self.y, self.x + dx, self.y + dy;
        plt.plot([x1, x2], [y1, y2], color = 'black', linewidth =2)
        self.x, self.y = x2, y2
    
    def turn(self, val: int):
        self.angle = (self.angle + val) % 360

    def show(self):
        plt.show()

def draw(s):
    insts = parse(s)
    marker = Marker()
    stack = []
    opno = 0
    while opno < len(insts):
        print(stack)
        code, val = insts[opno]
        if code == 'F':
            marker.forward()
        elif code == 'T':
            marker.turn()
        elif code == 'R':
            stack.append({'opno':opno, 'rest':c})
        elif code == 'E':
            if stack[-1]['rest']:
                pass
            else:
             pass
        opno += 1
    marker.show()



