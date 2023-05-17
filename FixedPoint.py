from sympy import *
from sympy.abc import x
import time
import numpy as np
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application
import matplotlib.pyplot as plt
from shapely.geometry import LineString


class Fixed:

    def solve(self, currentX, fi, MaxNoOfIterations, error, sf):
        start=time.time()
        data={}
        x0=currentX
        data['steps']=[]
        data['number']=''
        data['time']=''
        data['steps'].append("{:<10} {:<10} {:<10} {:<10} {:<10} ".format('Xi','Xi+1','F(Xi+1)','E','Ea'))
        flag=False
        g=Add(fi,symbols('x'))
        gx = lambdify(x, fi, "complex")
        fx=lambdify(x,fi,'math')
        NoOfIterations = 0
        while NoOfIterations < MaxNoOfIterations:
            currentX = float('%.*g' % (sf, currentX))
            nextX = float(gx(currentX))
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
            else:
                data['steps'].append("{:<10} {:<10} {:<10} {:<10} {:<10} ".format(currentX, nextX,
                        float('%.*g' % (sf, fx(currentX))), float('%.*g' % (sf, error1)),
                        float('%.*g' % (sf, relativeError))))
            currentX = nextX
            flag=True
        data['number']=str(NoOfIterations)
        data['time']=str(time.time()-start)
        if NoOfIterations>MaxNoOfIterations:
            pl=self.plot_fixed_point(g,x0,nextX)
            return data,pl,"reached maximum number of iterations", nextX
        else:
            pl=self.plot_fixed_point(g,x0,nextX)
            return data,pl,"answer reached", nextX

    def plot_fixed_point(self,g ,x0 ,root):
        x=np.linspace(x0-4,root+8, 100)
        y = []
        f=lambdify('x',g,"math")
        for i in range(0, 100):
            y.append(f(x[i]))
        plt.clf()
        fig = plt.figure("Fixed Point")
        fig.set_dpi(100)
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        plt.plot(x,x,label='y=x')
        plt.plot( x,y,'-',label='g(x)')
        idx = np.argwhere(np.diff(np.sign(x-y))).flatten()
        plt.plot(x[idx], x[idx], 'ro')
        plt.legend()
        plt.grid(True, linestyle =':')
        plt.xlim([-x0-5,x0+5])
        plt.ylim([-5,5])
        plt.text(root,0,'xr')
        plt.axvline(x=root, color = "green", linestyle ="--")
        return plt
