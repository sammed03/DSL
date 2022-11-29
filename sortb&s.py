# selection and bubble sort
a=[]
n=int(input("enter number of elements you want in 1st list:"))
b=[]
m=int(input("enter number of elements you wantin 2nd list:"))

def accept(m,b):
	for i in range(m):
		y=int(input("enter an element:"))
		b.append(y)
	print("Your list is = ",b)

	
def bub_sort():
	for i in range(n-1):
		for j in range(n-1):
			if a[j] > a[j+1]:
				temp=a[j]
				a[j]=a[j+1]
				a[j+1]=temp
			j=j+1
		i=i+1
	print("The Bubblely sorted list is = ",a)
	

def sel_sort():
	for i in range(m-1):
		for j in range(i,m-1):
			if b[i] > b[j+1]:
				temp=b[i]
				b[i]=b[j+1]
				b[j+1]=temp
			
			
	
	print("the selectionaly sorted list is = ",b)
	

def main():