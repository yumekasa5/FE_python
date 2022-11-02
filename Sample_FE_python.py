"""FE python サンプル問題"""
import math
import matplotlib.pyplot as plt

def parse(s):
    return [(x[0], int(x[1:])) for x in s.split(';')]

class Marker():
    """マーカー"""
    def __init__(self) -> None:
        self.x , self.y, self.angle = 0, 0, 0;
        plt.xlim(-320, 320);
        plt.ylim(-240,240)

    def forward(self, val: int):
        x += math.cos(val);
        y += math.sin(val);

    def turn(self, val: int):
        angle += val;


