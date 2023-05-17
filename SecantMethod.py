from sympy import *
from sympy.abc import x
import time
import numpy as np
import matplotlib.pyplot as plt

class Secant:
    
    def solve(self, prevX, currentX, fi, MaxNoOfIterations, error, sf):
        start=time.time()
        self.arr=[]
        data={}
        data['steps']=[]
        data['number']=''
        data['time']=''
        data['steps'].append("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} ".format('Xi-1','Xi','Xi+1','F(Xi)','F(Xi+1)','E','Ea'))
        fx = lambdify(x, fi, "math")
        flag=False
        NoOfIterations = 0
        while NoOfIterations < MaxNoOfIterations:
            prevX = float('%.*g' % (sf, prevX))
            currentX = float('%.*g' % (sf, currentX))
            # print(fx(prevX),fx(currentX))
            nextX = float(currentX - ((fx(currentX) * (prevX - currentX)) / (fx(prevX) - fx(currentX))))
            nextX = float('%.*g' % (sf, nextX))
            error1 = abs(nextX - currentX)
            error1 = float('%.*g' % (sf, error1))
            if nextX != 0 and flag==True:
                relativeError = error1 / nextX * 100
                relativeError = float('%.*g' % (sf, relativeError))
                if relativeError < error:
                    break
            NoOfIterations += 1
            if(flag==False):
                data['steps'].append("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} ".format(prevX, currentX, nextX, float('%.*g' % (sf, fx(prevX))),
                      float('%.*g' % (sf, fx(currentX))), float('%.*g' % (sf, error1)),
                      "------"))
            else:
                data['steps'].append("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} ".format(prevX, currentX, nextX, float('%.*g' % (sf, fx(prevX))),
                      float('%.*g' % (sf, fx(currentX))), float('%.*g' % (sf, error1)),
                      float('%.*g' % (sf, relativeError))))
            prevX = currentX
            currentX = nextX
            self.arr.append(nextX)
            flag=True
        data['number']=str(NoOfIterations)
        data['time']=str(time.time()-start)
        plot=self.plot_secant(name=fi,root=nextX)
        if(NoOfIterations>MaxNoOfIterations):
            return data,plot,"reached maximum number of iterations", nextX
        else:
            return data,plot,"answer reached", nextX

    def plot_secant(self,name,root): 
        ylist = []
        xlist = np.linspace(-2*abs(root), 2*abs(root), 100)
        f=lambdify('x',name,"math")
        for i in range(0, 100):
            x = xlist[i]
            ylist.append(f(x))
        plt.clf()
        fig = plt.figure("Secant")
        fig.set_dpi(100)
        ax = fig.add_subplot(1,1,1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.title('Derivetive of f(x)')
        plt.plot(xlist, ylist)
        print(self.arr)
        plt.plot(self.arr, [0]*len(self.arr), 'ro')
        # plt.imsave(fname='NewtonRaphson.png')
        return plt