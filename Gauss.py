import numpy as np
from scipy.linalg import lu
import time
class Gauss:
    def GaussMethod(self,n,sf,coeff=[[]],b=[],AUG=[[]]):
        m=n
        start = time.time()
        x=0
        sz=1
        data = {}
        data['Forward Elimination'] = []
        rankA=np.linalg.matrix_rank(coeff)
        rankAUG=np.linalg.matrix_rank(AUG)
        if(rankA<rankAUG):  
            return data,"inconsistent solution",start-time.time()
        elif(rankA==rankAUG!=n):
            return data,"infinite solutions",start-time.time()
        else:   
        #forward elimination
         for k in range(n-1):
            max=coeff[x][x]
            max_index=x
            switch=[0 for i in range(m)]
            for i in range(x,n):
                if(abs(max)<abs(coeff[i][x])):
                    max=coeff[i][x]
                    max_index=i   
            switch=coeff[x]
            coeff[x]=coeff[max_index]
            coeff[max_index]=switch
            temp=b[x]
            b[x]=b[max_index]
            b[max_index]=temp
            for i in range (sz,n):
                mult=coeff[i][x]/coeff[x][x]
                for j in range(m):
                    coeff[i][j]=float('%.*g' % (sf,coeff[i][j]-(coeff[x][j]*mult)))
                    if(abs(coeff[i][j])<1e-10):
                        coeff[i][j]=0.0
                
                b[i]= float('%.*g' % (sf,b[i]-(b[x]*mult)))
                if(abs(b[i])<1e-10):
                    b[i]=0.0      
                data['Forward Elimination'].append(np.c_[coeff,b])
            x=x+1
            sz=sz+1              
        # back subst   
        result=[0 for i in range(n)] 
        result[n-1]=float('%.*g' % (sf, b[n-1]/coeff[n-1][m-1]))         
        for i in range(n-2,-1,-1):
            sum=0
            for j in range(i+1,n):
                sum+=float('%.*g' % (sf,coeff[i][j]*result[j]))      
            result[i]=float('%.*g' % (sf, (b[i]-sum)/coeff[i][i]))
        end = time.time()-start
        return data,result,end

    def Gauss_Jordan(n,sf,coeff=[[]],b=[],AUG=[[]]):
        m=n
        x=0
        sz=1
        data = {}
        data['Forward Elimination'] = []
        data['Backward Elimination'] = []
        start = time.time()
        rankA=np.linalg.matrix_rank(coeff)
        rankAUG=np.linalg.matrix_rank(AUG)
        if(rankA<rankAUG):  
            return data,"inconsistent solution",start-time.time()
        elif(rankA==rankAUG!=n):
            return data,"infinite solutions",start-time.time()
        else:   
        #foward elimination
         for k in range(n-1):
            temp=coeff[x][x]
            for i in range(m):
                coeff[x][i]=float('%.*g' % (sf,coeff[x][i]/temp))
            b[x]=float('%.*g' % (sf,b[x]/temp))
            for i in range (sz,n):
                mult=float(coeff[i][x]/coeff[x][x])
                for j in range(m):
                    coeff[i][j]=float('%.*g' % (sf,coeff[i][j]-(coeff[x][j]*mult)))
                b[i]=float('%.*g' % (sf,b[i]-(b[x]*mult)))
            x=x+1
            sz=sz+1
            data['Forward Elimination'].append(np.c_[coeff,b])
        temp=coeff[x][x]    
        for i in range(m):
                coeff[x][i]=float('%.*g' % (sf,coeff[x][i]/temp))
        b[x]=float('%.*g' % (sf,b[x]/temp))
        #back elimination
        x=n-1
        sz=n-2
        for k in range(n-1):
            for i in range (sz,-1,-1):
                mult=float(coeff[i][x]/coeff[x][x])
                for j in range(m):
                    coeff[i][j]=float('%.*g' % (sf,coeff[i][j]-(coeff[x][j]*mult)))
                b[i]=float('%.*g' % (sf,b[i]-(b[x]*mult)))    
            data['Backward Elimination'].append(np.c_[coeff,b])
            x=x-1
            sz=sz-1   
        end = time.time()-start
        return data,b,end      
