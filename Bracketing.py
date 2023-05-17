import math
from sympy import *
import math
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import time
from validate import Valid
class Bracket:

    def bisection(self, x0,x1, fi, MaxNoOfIterations, error, sf):
        start=time.time()
        data={}
        data['steps']=[]
        data['number']=''
        data['Best']=''
        data['time']=''
        fx=lambdify("x",fi,'math')
        xl=float(x0)
        xu=float(x1)
        f0 = fx(x0)
        f1 = fx(x1)
        if f0 * f1 > 0.0:
            return "Incorrect Initial Guesses."
        
        k = math.ceil(abs((math.log((x1 - x0), 10)) - (math.log(error, 10))) / (math.log(2, 10)))
        data['Best']=str("\nNumber of iteration calclated from equation :"+str(k))
        data['steps'].append("{0:>10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>10}".format("Iteration", "xl", "Xu", "Xr", "f(Xr)", "error"))
        flag=False
        NoOfIterations = 0
        xp=0
        while NoOfIterations < MaxNoOfIterations:
            x = (x0 + x1) / 2.0
            x = float('%.*g' % (sf, x))
            f = fx(x)
            f = float('%.*g' % (sf, f))
            if  flag==True:
                err = abs((x - xp) / x) * 100
                err = float('%.*g' % (sf, err))
                if err < error:
                    break
            xp=x
            NoOfIterations += 1
            if flag==False:
                data['steps'].append("{0:>10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>10}".format(NoOfIterations, x0, x1, x, f, "----"))
            else:
                data['steps'].append("{0:>10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>10}".format(NoOfIterations, x0, x1, x, f, err))
            if f0 * f < 0:
                x1 = x
            elif f0 * f > 0:
                x0 = x
            else:
                break
            flag=True
        data['number']=str(NoOfIterations)+data['Best']
        data['time']=str(time.time()-start)
        if NoOfIterations>MaxNoOfIterations:
            pl=self.bracket_plot(xl,xu,x,fx)
            return data,pl,"reached maximum number of iterations", x
        else:
            pl=self.bracket_plot(xl,xu,x,fx)
            return data,pl,"answer reached",x

    def false_postion(self, x0,x1, fi, MaxNoOfIterations, error, sf):
        start=time.time()
        data={}
        data['steps']=[]
        data['number']=''
        data['Best']=''
        data['time']=''
        fx=lambdify("x",fi,'math')
        xl=float(x0)
        xu=float(x1)
        f0 = fx(x0)
        f1 = fx(x1)
        f0 = float('%.*g' % (sf, f0))
        f1 = float('%.*g' % (sf, f1))
        if f0 * f1 > 0.0:
            return "Incorrect Initial Guesses."
        k = math.ceil(abs((math.log((x1 - x0), 10)) - (math.log(error, 10))) / (math.log(2, 10)))
        print(k)
        data['Best']=str("Number of iteration calculated from equation :"+str(k))
        data['steps'].append("{0:>10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>10}".format("Iteration", "xl", "Xu", "Xr", "f(Xr)", "error"))
        flag=False
        NoOfIterations = 0
        xp=0
        while NoOfIterations < MaxNoOfIterations:
            x = (x0*f1-x1*f0)/(f1-f0)
            x = float('%.*g' % (sf, x))
            f = fx(x)
            f = float('%.*g' % (sf, f))
            if  flag==True:
                err = abs((x - xp) / x) * 100
                err = float('%.*g' % (sf, err))
                if err < error:
                    break
            xp=x
            NoOfIterations += 1
            if flag==False:
                data['steps'].append("{0:>10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>10}".format(NoOfIterations, x0, x1, x, f, "----"))
            else:
                data['steps'].append("{0:>10} {1:>10} {2:>10} {3:>10} {4:>10} {5:>10}".format(NoOfIterations, x0, x1, x, f, err))
            if f0 * f < 0:
                x1 = x
                f1=f
            elif f0 * f > 0:
                x0 = x
                f0=f
            else:
                break
            flag=True
        data['number']=str(NoOfIterations)+data['Best']
        data['time']=str(time.time()-start)
        if NoOfIterations>MaxNoOfIterations:
            pl=self.bracket_plot(xl,xu,x,fx)
            return data,pl,"reached maximum number of iterations", x
        else:
            pl=self.bracket_plot(xl,xu,x,fx)
            return data,pl,"answer reached",x

    def bracket_plot(self,xl, xu, xr, function):
        rng = (xl+ xu)/2.0
        points = []
        y = list()
        xl_range = abs(xl-rng*2) 
        xu_range = abs(xu+rng*2)
        if xl_range > xu_range:
            points = np.linspace(-xl_range,xl_range  ,100)
        else:
            points = np.linspace(-xu_range,xu_range  ,100)
        for i in range(0, 100):
            x = points[i]
            y.append(function(x))
        plt.clf()
        fig = plt.figure("Bracketing Methods")
        fig.set_dpi(100)
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.grid(True, linestyle =':')
        plt.plot(points ,y,'r')
        plt.text(xr,3,'xr')
        plt.text(xl,3,'xl')
        plt.text(xu,3,'xu' )
        plt.axvline(x=xr, color = "green", linestyle ="--")
        plt.axvline(x=xl, color = "#2C4ACF", linestyle ="solid")
        plt.axvline(x=xu, color = "#5B0202", linestyle ="solid")
        # plt.legend()
        plt.legend(["Fx","Xr","Xl",'Xu'], loc=0, frameon=True)
        xabs_max = abs(max(ax.get_xlim(), key=abs)) 
        ax.set_xlim(xmin=-xabs_max, xmax=xabs_max)
        yabs_max = abs(max(ax.get_ylim(), key=abs)) 
        ax.set_ylim(ymin=-yabs_max, ymax=yabs_max)
        return plt
