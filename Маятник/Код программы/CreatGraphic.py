import math
from random import random,randint

class Graph_for_plt():
    def __init__(self):
        self.Gen = False
        self.h = 1
        self.tim = 0
        self.t = [0]
        self.x0 = [2]
        self.y0 = [2]
        self.kx = [[],[],[],[]]
        self.ky = [[],[],[],[]]
        self.Fsh= [[],[],[],[]]
        self.FshP = []
        self.xP = []
        self.yP = []
        self.Fi = 0

        self.g = 10

        self.m = 30
        self.k = -2
        self.L = -5
        self.w = 0.08
        self.q = 0.5#  ro
        self.sig = 1000000
        self.T = 50

        #######`
        self.t1 = 1
        self.E0 = 0
        self.E1 = 500
        self.Random = 0.5
        self.Randomk = (random() * 2 - 1)*self.Random


    def reset(self):
        self.tim = 0
        self.t = [0]
        self.x0 = [2]
        self.y0 = [2]
        self.kx = [[], [], [], []]
        self.ky = [[], [], [], []]
        self.Fsh = [[], [], [], []]
        self.FshP = []
        self.xP = []
        self.yP = []

    def Ras1(self):
        k=0
        if(self.tim%100==0):
            self.Randomk = (random() * 2 - 1)*self.Random
        self.tim+=1


        if(self.Gen):
            k =self.E0/self.m +(self.E1 / self.m) *math.exp(-(self.t[-1]-1)*(self.t[-1]-1)/self.sig)* math.cos(math.pi * 2 * self.t[-1] * self.T + self.Fi) + self.E1 * self.Randomk / self.m
        else:
            k=0
        self.FshP.append(k)
        s = self.h*(self.L*self.x0[-1]/self.m+    self.k*self.y0[-1]/self.m   -self.g*(1-self.q*self.w/self.m)
                    - self.FshP[-1])
        self.kx[0].append(s)
        self.ky[0].append(self.x0[-1]*self.h)


        s = self.h * (self.L * (self.x0[-1]+self.kx[0][-1]/2) / self.m + self.k * (self.y0[-1]+self.ky[0][-1]/2  ) / self.m - self.g * (1 - self.q * self.w / self.m)
                      - k)
        self.kx[1].append(s)
        self.ky[1].append((self.x0[-1]+self.kx[0][-1]/2) * self.h)

        s = self.h/self.m * (self.L * (self.x0[-1] + self.kx[1][-1] / 2) / self.m + self.k * (self.y0[-1] + self.ky[1][-1] / 2) / self.m - self.g * (1 - self.q * self.w / self.m)-
                      k)
        self.kx[2].append(s)
        self.ky[2].append((self.x0[-1] + self.kx[1][-1]/2) * self.h)



        s = self.h * (self.L * (self.x0[-1] + self.kx[2][-1]) / self.m + self.k * (self.y0[-1] + self.ky[2][-1] ) / self.m - self.g * (1 - self.q * self.w / self.m) -
                      k)
        self.kx[3].append(s)
        self.ky[3].append((self.x0[-1] + self.kx[2][-1]) * self.h)
        self.xP.append(sum([self.kx[i][-1] if i==1 or i==2 else self.kx[i][-1]*2   for i in range(len(self.kx))]  ) / 6 )
        self.yP.append(sum([self.ky[i][-1] if i==1 or i==2 else self.ky[i][-1]*2 for i in range(len(self.ky))]) / 6)
        self.x0.append(self.xP[-1] + self.x0[-1])
        self.y0.append(self.yP[-1] + self.y0[-1])
        self.t.append(self.t[-1]+self.h)
    def set_data(self):
        return self.t,self.x0,self.y0,self.xP,self.FshP

