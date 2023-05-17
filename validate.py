
import math
from sympy import *
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application

class Valid:

    def modify(self,equation):
            if not equation.__contains__('='):
                return equation
            equation = equation.replace("^","**")
            tempList = equation.split('=')
            mod = tempList[1]
            if mod[0]!='-':
                mod = '+'+mod
            new = list(mod)
            for i in range (0, len(mod)):
                
                if new[i] =='+' or new[i] == '-' :
                    if new[i] == '+':
                        new[i] = '-'
                    else:
                        new[i] = '+'
                        
            mod = ''.join(new)     
            tempList[1] = ''.join(mod)
            equation    = ''.join(tempList)         
            # print(equation)  
            return equation
    
    def validate(self,function):
        function=function.lower()
        function=self.modify(function)
        transformations = (standard_transformations + (implicit_multiplication_application,))

        symbols=['+','-','*','/']
        if (function.count('=') != 0):
            function = "error"
            return function
        function = function.replace("^","**").replace("+-", "-").replace("++", "+").replace("-+", "-").replace("--", "+")
        for i in range (len(function)):
            if(i<len(function)-2 and function[i] in symbols and function[i+1] in symbols):
                if(function[i]!='-' and function[i+1]!='-' and (function[i]!='*' and function[i+1]!='*')):
                    print("case 1")
                    function="error"
                    return function
                if(function[i]=='-' and function[i+1]!='-'):
                    print("case 2")
                    function = "error"
                    return function
        try:
            function=parse_expr(function, transformations=transformations)
        except:
            function="error"
            return function
        return function

