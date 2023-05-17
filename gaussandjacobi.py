import time
import numpy as np
class Siedel_jacobi:
    # checks if jacobi or gauss-siedel is applicable on the matrix
    def check_if_possible(self,cols,Rows,A=[[]]):
        if(cols!=Rows):
            return False
        for i in range(cols):
            if(A[i][i]==0):
                return False
        return True
    #this copies array Ans into array Answer
    def copy_answer(self,cols,Answer=[],Ans=[]):
        for i in range(cols):
            Answer[i]=Ans[i]
        return Answer

    def jacobi(self,cols,Rows,maxnoOfIterations,relativeerror,accuary,Ans=[],A=[[]],B=[]):
        data = {}
        data['Steps'] = []
        start = time.time()
        if (self.check_if_possible(cols, Rows, A) == False):
            return '', 'error there is at least one element with value zero at the diagonal','',''
        error = [0 for i in range(cols)]
        Answer = [0 for i in range(cols)]
        Answer = self.copy_answer(cols, Answer, Ans)
        noOfIterations = 0
        flag2 = True
        firstTime = True
        # flag2 becomes false when all the relative errors smaller than the given error
        while ((noOfIterations < maxnoOfIterations) and (flag2 == True)):
            noOfIterations += 1
            # the few next lines implement the equations for gauss-siedel
            for i in range(cols):
                Ans[i] = float(B[i])
                for k in range(cols):
                    if (k != i):
                        Ans[i] -= A[i][k % cols] * Answer[k % cols]
                Ans[i] /= A[i][i]
                Ans[i] = float('%.*g' % (accuary, Ans[i]))
                if (abs(Ans[i]) <= 10**-accuary):
                    Ans[i] = 0
                if (firstTime == False):
                    if (Ans[i] != 0):
                        error[i] = abs((Ans[i] - Answer[i]) / Ans[i])
            if (firstTime == False):
                flag2 = False
                for i in range(cols):
                    if (abs(error[i]) > relativeerror):
                        flag2 = True
            else:
                firstTime = False
            self.copy_answer(cols, Answer, Ans)
            data['Steps'].append(np.array(Ans).copy())
            print(Ans)
        print(noOfIterations)
        end = time.time()-start
        return data,Ans,end,noOfIterations

    # Gauss siedel function    
    def gauss_siedel(self,cols,Rows,maxnoOfIterations,relativeerror,accuary,Ans=[],A=[[]],B=[]):
        data = {}
        data['Steps'] = []
        if (self.check_if_possible(cols, Rows, A) == False):
            return '','error there is at least one element with value zero at the diagonal','',''
        error = [0 for i in range(cols)]
        Answer = [0 for i in range(cols)]
        Answer = self.copy_answer(cols, Answer, Ans)
        noOfIterations=0
        flag2 = True
        firstTime = True
        # flag2 becomes false when all the relative errors smaller than the given error
        start = time.time()
        while((noOfIterations<maxnoOfIterations)and(flag2==True)):
            noOfIterations+=1
            # the few next lines implement the equations for gauss-siedel
            for i in range(cols):
                Ans[i] = float(B[i])
                for k in range(cols):
                    if (k != i):
                        if ((k % cols) < i):
                            Ans[i] -= A[i][k % cols] * Ans[k % cols]
                        else:
                            Ans[i] -= A[i][k % cols] * Answer[k % cols]
                Ans[i] /= A[i][i]
                Ans[i] = float('%.*g' % (accuary, Ans[i]))
                if (abs(Ans[i]) <= 10**-accuary):
                    Ans[i] = 0
                if (firstTime == False):
                    if (Ans[i] != 0):
                        error[i] = abs((Ans[i] - Answer[i]) / Ans[i])
            if (firstTime == False):
                flag2 = False
                for i in range(cols):
                    if (abs(error[i]) > relativeerror):
                        flag2 = True
            else:
                firstTime = False
            self.copy_answer(cols, Answer, Ans)
            data['Steps'].append(np.array(Ans).copy())
            print(Ans)
        print(noOfIterations)
        end = time.time()- start
        return data,Ans,end,noOfIterations
