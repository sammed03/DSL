# Shell Short and Insertion Sort 

def accept_array(a):
    n = int(input("Number of Students: "))
    for i in range(n):
        x = float(input("Enter the percentage of marks scored in second year by students : "))
        a.append(x)
    print("Array accepted successfully")


def display_array(a):
    n = len(a)
    if (n == 0):
        print("No records in the Database!")
    else:
        print("Array of Second year students marks = ", end=" ") 
        for i in range(n):
            print(a[i], end=" ")
        print(" \n ")


def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        element = a[i]
        j = i - 1
        while(j >= 0):
            if (a[j] <= element):
                break
            else:
                a[j+1] = a[j]
                j = j - 1
        a[j+1] = element


def shell_sort(a,n):
    gap = n // 2
    while (gap > 0):
        for i in range(gap,n):
            temp = a[i]
            j = i
            while((j >= gap) and ((a[j - gap]) > temp)):
                a[j] = a[j - gap]
                j = j - gap
            a[j] = temp 
        gap = gap // 2


def main():
    a = []
    while True:
        print("\t1 : Accept and Display Student Marks :")
        print("\t2 : Insertion Sort")
        print("\t3 : Shell Sort")
        print("\t4 : EXIT")
        ch = int(input("Enter your Choice : "))
        if(ch == 4):
            print("End of the program")
            break
        elif(ch == 1):
            print("Accept the Marks : ")
            accept_array(a)
            display_array(a)
        elif(ch == 2):
            insertion_sort(a)
            print("Sorted Array is :", end = " ")
            display_array(a)
        elif(ch == 3):
            n = len(a)
            shell_sort(a,n)
            print("Sorted Array is : ", end = " ")
            display_array(a)
            n = len(a)
            if(n >= 5):
                print("\t\t\tTOP 5 SCORERS : ")
                for i in range(n-1,n-6,-1):
                    print(a[i])
            else:
                print("\t\t\tTOP 5 SCORERS : ")
                for i in range(n-1,-1,-1):
                    print(a[i])
        else:
            print("wrong Choice!")

main()
quit()    
        

