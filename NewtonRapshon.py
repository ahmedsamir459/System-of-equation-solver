import math
from sympy import *
from sympy.abc import x
import math
from sympy import symbols
from sympy import *
from sympy.abc import x
from sympy.plotting import plot
import time
 
import matplotlib.pyplot as plt
import numpy as np
class Newton:

    def solve(self, currentX, fi, MaxNoOfIterations, error, sf):
        start=time.time()
        data={}
        data['steps']=[]
        data['number']=''
        data['time']=''
        data['steps'].append("{:<10} {:<10} {:<10} {:<10} {:<10} ".format('Xi','Xi+1','F(Xi+1)','E','Ea'))
        fx = lambdify(x, fi, "math")
        self.fdash=fi.diff('x')
        flag=False
        fdashx=lambdify(x,self.fdash,"math")
        NoOfIterations = 0
        while NoOfIterations < MaxNoOfIterations:
            currentX = float('%.*g' % (sf, currentX))
            nextX = float(currentX-fx(currentX)/fdashx(currentX))
            nextX = float('%.*g' % (sf, nextX))
            error1 = abs(nextX - currentX)
            error1 = float('%.*g' % (sf, error1))
            if nextX != 0 and flag==True:
                relativeError = error1 / nextX * 100
                relativeError = float('%.*g' % (sf, relativeError))
                if relativeError < error:
                    break
            NoOfIterations += 1
            if flag==False:
                data['steps'].append("{:<10} {:<10} {:<10} {:<10} {:<10} ".format(currentX, nextX,
                        float('%.*g' % (sf, fx(currentX))), float('%.*g' % (sf, error1)),
                        "------"))
                # print("{:<10} {:<10} {:<10} {:<10} {:<10} ".format(currentX, nextX,
                #       float('%.*g' % (sf, fx(currentX))), float('%.*g' % (sf, error1)),
                #       "------"))
            else:
                data['steps'].append("{:<10} {:<10} {:<10} {:<10} {:<10} ".format(currentX, nextX,
                        float('%.*g' % (sf, fx(currentX))), float('%.*g' % (sf, error1)),
                        float('%.*g' % (sf, relativeError))))
                # print("{:<10} {:<10} {:<10} {:<10} {:<10} ".format(currentX, nextX,
                #       float('%.*g' % (sf, fx(currentX))), float('%.*g' % (sf, error1)),
                #       float('%.*g' % (sf, relativeError))))
            currentX = nextX
            flag=True
        # print(NoOfIterations)
        data['number']=str(NoOfIterations)
        data['time']=str(time.time()-start)
        if NoOfIterations>MaxNoOfIterations:
            pl=self.plot_newton(self.fdash,nextX)
            return data,pl,"reached maximum number of iterations", nextX
        else:
            pl=self.plot_newton(self.fdash,nextX)
            return data,pl,"answer reached", nextX

    def plot_newton(self,name,root): 
        ylist = []
        xlist = np.linspace(-2*abs(root), 2*abs(root), 100)
        f=lambdify('x',name,"math")
        for i in range(0, 100):
            x = xlist[i]
            ylist.append(f(x))
        plt.clf()
        fig = plt.figure("Newton")
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
        return plt





