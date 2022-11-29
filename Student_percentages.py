# students percentage 
a=[]
f=[]
n=int(input("enter number of students:"))
for i in range(n):
    marks=int(input("enter marks:"))
    a.append(marks)
print(a)

def average():
    av=0
    for i in a:
        if i>0:
              av=av+i
    
    avg=av/n
    print("average marks are:",avg)
    
def highest_marks():
    hm=0
    for i in a:
         if i>hm:
               hm=i
         else:
             hm=hm
    print("highest score is:",hm)
    
def lowest_marks():
    lm=max(a)
    for i in a:
        if i<lm and i>0:
              lm=i
    print("lowest score is:",lm) 
    
def freq():
    global a
    f = []
    for i in range(101):
    	f.append(0)
    	
    for i in a:
    	if i>0:
        	f[i] = f[i]+1
      
    print("highest frequency score is:",f.index(max(f)))
       
    
def absent():
	p = 0
	for i in a:
		if i<0:
			p=p+1
	print("number of absent students are:",p)	     
		
    
def main():
    average()
    highest_marks()
    lowest_marks()   
    freq() 
    absent()  
    
main()                        