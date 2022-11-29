# Matrix operations


def main():
    r1=int(input("enter number of rows of 1st matrix:"))
    c1=int(input("enter number of columns of 1st matrix:"))
    r2=int(input("enter number of rows of 2st matrix:"))
    c2=int(input("enter number of columns of 2st matrix:"))
    
    mat1=[]
    mat2=[]
    mat1t=[]
    mat2t=[]
    
    read(r1,c1,mat1)    
    dis(r1,c1,mat1)
    
    read(r2,c2,mat2)
    dis(r2,c2,mat2)
    
    add(r1,c1,mat1,mat2)
    sub(r1,c1,mat1,mat2)
    transpose(r1,c1,mat1,mat2,r2,c2,mat1t,mat2t)
    mul(r1,c1,mat1,r2,c2,mat2)
    
def read(r1,c1,mat1):
    print("")
    for i in range(r1):
         a=[]
         for j in range(c1):
             a.append(int(input("enter element:")))
         mat1.append(a)
           
def dis(r1,c1,mat1):
    print("")
    for i in range(r1):
        for j in range(c1):
            
            print(mat1[i][j],end=" ")
        print("")
                



def add(r1,c1,mat1,mat2):
    print("")
    print("addition matrix is")
    for i in range(r1):
        for j in range(c1):
            print(mat1[i][j]+mat2[i][j],end=" ")
    print("")
        

def sub(r1,c1,mat1,mat2):
     print("")
     print("subtraction matrix is")
     for i in range(r1):
        for j in range(c1):
            print(mat1[i][j]-mat2[i][j],end=" ")
     print("")
        
def transpose(r1,c1,mat1,mat2,r2,c2,mat1t,mat2t):
     print("")
     print("transpose of 1st matrix is")
     for i in range(r1):
        for j in range(c1):
            mat1t.append(mat1[j][i])
        
     print(mat1t,end=" ")
     print("")

    # for _ in mat1t:
        #   for i in _:
        #       print(i,end=" ")
        #   print(" ")
        
     print("")
     print("transpose of 2nd matrix is")
     for i in range(r2):
        for j in range(c2):
            mat2t.append(mat2[j][i])
     print(mat2t,end=" ")
     print("")
        



def mul(r1,c1,mat1,r2,c2,mat2):
    print("")
    print("multiplication these matxis is")
    res = []
    for i in range(r1):
         a=[]
         for j in range(c2):
             a.append(0)
         res.append(a)
             
    a=[]        
    if c1==r2:    
       for i in range(r1):
           for j in range(c2):
               for k in range(c1):
                   res[i][j]+=mat1[i][k]*mat2[k][j]  
                   
       dis(r1,c2,res)  
                 
                  
    else:
              print("matrix multiplication is not possible")



        
main()