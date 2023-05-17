from math import floor,log10
import math
import time
import numpy as np
class LU:      
  #this function is used to round a value to certaion significant figures
  def round_sig(x, sig): 

      if(x==0):
          return 0
      return round(x, sig-int(floor(log10(abs(x))))-1)
  #this function is used to extract the L matrix from compressed A matrix during the doolittle form of LU decomposition
  def getL(A): 
    n = len(A)
    L = np.identity(n) #identity --> diagonals = 1
    for i in range(1,n):
      for j in range(0,i):
        L[i,j] = float(A[i,j])
    return L
  #this function is used to extract U matrix from compressed matrix containing both L and U during the doolittke form of LU decomposition
  def getU(A): 
    n = len(A)
    U = np.zeros((n, n)) #setting upper triangular matrix of size n*n to zeros
    for i in range(0,n-1):
      for j in range(i+1,n):
        U[i,j] = A[i,j]
    for i in range(0,n): #setting elements of the diagonal
      U[i,i] = A[i,i]
    return U
  #this function to apply the process of forward substitution 
  def for_subs(self,L, b, sigFigures): 
    x = np.zeros(len(L))
    for i in range(len(L)):
      temp = b[i]
      for j in range(i):
        temp = temp - (L[i,j] * x[j])
      x[i] = self.round_sig(temp / L[i,i], sigFigures)
    return x 
  #this function is used to apply the process of backward substitution
  def back_subs(self,U, d, sigFigures): 
    x = np.zeros(len(U))
    for i in range(len(U)-1,-1,-1):
      temp = d[i]
      for j in range(i+1,len(U)):
        temp = temp - (U[i,j] * x[j])
      x[i] = self.round_sig(temp / U[i,i], sigFigures)
    return x 
  #this function is used to solve system of linear equations using the doolittle form of LU decomposition. it takes the coefficient matrix,the values of equations and the significant figures as arguments
  def doolittle(self,A,b,sigfigures):

      start=time.time() #start calculating the runtime
      data={}
      data['L']=[]
      data['U']=[]
      #the augmented matrix containing both coefficent (A) and the equations' results (b)
      aug=np.append(A,b.reshape(-1,1),axis=1) 
      #if the rank of the coefficient matrix not equal to that of augmented, the system has no solution
      if(np.linalg.matrix_rank(A)!=np.linalg.matrix_rank(aug)): 
          end=time.time()
          runtime=end-start #end runtime calculation
          return "The system of Equations has no solution.",runtime
      #if the ranks of bth coefficient and augmented matrices are equal but less than number of unknowns, the system has infinte number of solutions
      elif(np.linalg.matrix_rank(A)==np.linalg.matrix_rank(aug)<len(A)): 
          end=time.time()
          runtime=end-start #end runtime calculation
          return '',"The system has infinite number of Solutions",runtime
      else:
          n=len(A)
          for i in range(n-1):
              maxelement=max(A[:,i],key=abs) 
              if (A[i,i])!=maxelement: #max element of col #i is not the one in the diagonal,pivoting is needed
                  for k in range(i+1,n):
                      if np.abs(A[k,i])>np.abs(A[i,i]):
                          A[[i,k]]=A[[k,i]]  # Swap ith and kth rows  
                          b[[i,k]]=b[[k,i]] 
              # computing compessed matrix A containing both L and U
              for k in range(i+1,n):          
                  A[k,i] = self.round_sig(float(A[k,i]/A[i,i]),5)  
                  for j in range(i+1,n):    
                      A[k,j] -= self.round_sig(float(A[k,i]*A[i,j]),5) 
      # seperate A to L,U and solve by forward then backward substition
          L = self.getL(A)
          U = self.getU(A)
          data["L"].append(L)
          data["U"].append(U)
          d=self.for_subs(L,b,sigfigures)
          x=self.back_subs(U,d,sigfigures)
          end=time.time() #end runtime calculation
          runtime=end-start
          return data, x,runtime
  #this function is used to solve system of linear equations using the crout form of LU decomposition. it takes the coefficient matrix,the values of equations and the significant figures as arguments
  def crout(self,A,b,sigfigures):
    start=time.time() #start calculating the runtime
    data={}
    data['L']=[]
    data['U']=[]
    n=len(A)
    #setting U matrix to n*n identity matrix
    U=np.identity(n)
    #setting L matrix to zero matrix of length n*n
    L=np.zeros((n,n))
    #create augmented matrix of A and b
    aug=np.append(A,b.reshape(-1,1),axis=1)
    #if rank of A not equal rank of augmnted matrix, system has no solution
    if(np.linalg.matrix_rank(A)!=np.linalg.matrix_rank(aug)):
      end=time.time() #end runtime calculation
      runtime=end-start
      return "System has no solution", runtime
    # if both Matrices A and augmented have equal ranks but less than the number of unknowns, the system has infinte number of solutions
    elif(np.linalg.matrix_rank(A)==np.linalg.matrix_rank(aug)<len(A)):
      end=time.time() #end runtime calculation
      runtime=end-start
      return '',"system has infinte number of solutions", runtime
    else:
      for i in range (n):
        #setting the elements of L matrix
        for j in range(i,n):
          sum=0
          for k in range(i):
            sum+= L[j,k]*U[k,i]
          L[j,i]=self.round_sig(A[j,i]-sum,sigfigures)
        #setting the elements of U matrix
        for j in range(i+1,n):
          sum=0
          for k in range(i):
            sum=+ L[i,k]*U[k,j]
          U[i,j]=(A[i,j]-sum)/L[i,i]
          U[i,j]=self.round_sig(U[i,j],sigfigures)
      #calculating the results by applying forwward and backward substitution
      d=self.for_subs(L,b,sigfigures)
      x=self.back_subs(U,d,sigfigures)
      data["L"].append(L)
      data["U"].append(U)
      end=time.time() #end runtime calculation
      runtime=end-start
      return data, x, runtime
  #this function is used to xheck if a given matrix is symmetric or not
  def issymmetric(A):
    return np.all(np.abs(A-A.T) < 1e-8)
  #this function is used to solve system of linear equations using the cholesky form of LU decomposition if and only if the coefficient matrix is symmetric. it takes the coefficient matrix,the values of equations and the significant figures as arguments
  def cholesky(self,A,b,sigfigures):
    start=time.time() #start runtime calculation
    data={}
    data['L']=[]
    data['U']=[]
    n=len(A)
    #creating an augmented matrix containing both A and b
    aug=np.append(A,b.reshape(-1,1),axis=1)
    #setting Lower triangular matrix of length n*n initially to zero
    L=np.zeros((n,n))
    #if the rank of the coefficient matrix not equal to that of augmented, the system has no solution
    if(np.linalg.matrix_rank(A)!=np.linalg.matrix_rank(aug)):
      end=time.time() #end runtime calculation
      runtime=end-start
      return '',"System has no solution",runtime 
    #if the ranks of bth coefficient and augmented matrices are equal but less than number of unknowns, the system has infinte number of solutions
    elif(np.linalg.matrix_rank(A)==np.linalg.matrix_rank(aug)<n):
      end=time.time() #end runtime calculation
      runtime=end-start
      return '',"System has infinte number of solutions",runtime
    #check if the given coefficient matrix is symmetric
    elif(self.issymmetric(A)):
    #computing the Lower traingular matrix of cholesky decomposition
      for i in range (n):
        for j in range (i+1):
          sum=0
          if(j==i):
            for k in range(j):
              sum+=pow(L[i,k],2)
            L[j,j]=self.round_sig(math.sqrt(A[j,j]-sum),sigfigures)
          else:
            for k in range (j):
              sum+=L[i,k]*L[j,k]
            L[i,j]=self.round_sig((A[i,j]-sum)/L[j,j],sigfigures) 
      #creating the upper triangular matrix of cholesky decomposition which is the transpose of the lower triangular matrix
      U=L.T
      #calculating the final answer through forward and backward substitutions 
      d=self.for_subs(L,b,sigfigures)
      x=self.back_subs(U,d,sigfigures)
      data["L"].append(L)
      data["U"].append(U)
      end =time.time() #end runtime calculation
      runtime=end-start
      return data,x,runtime
    # if the matrix is not symmetric, cholesky cannot be applied
    else:
      end=time.time()

      runtime=end-start
    return '',"the system is not symmetric, try another method",runtime
