def accept_matrix(mat):
    print("Enter the number of Rows and Columns: ")
    r = int(input("\tNumber of Rows : "))
    c = int(input("\tNumber of Rows : "))
    print("Enter the matrix Elements :  \n")
    for i in range(r):
        a = []
        for j in range(c):
            b = []
            a.append(int(input()))
        mat.append(a)
    print("Matrix accepted successfully")

def display_matrix(mat,r,c):
    print("Matrix = ")
    for i in range(r):
        for j in range(c):
            print(mat[i][j],end=" ")
        print()

def check_saddlepoint(mat,r,c):
    count = 0
    for i in range(r):
        min = mat[i][0]
        c = 0
        for j in range(c):
            if (min > mat[i][j]) :
                min = mat[i][j]
                c = j
        flag = 1
        for i in range(r):
            if(min < mat[i][c]):
                flag = 0
                break
        if(flag == 1):
            count += 1
    if (count == 0):
        print("No Saddle Point")
    else :
        print("Saddle point is : ", min)


def main():
    while True:
        print("\t\t\t1: Accept Matrix")
        print("\t\t\t2: Display Matrix")
        print("\t\t\t3: Find the Saddle Point")
        print("\t\t\t4: Exit")
        ch = int(input("Enter your Choice : "))
        if (ch == 4):
            print("End of the Program")
            break
        elif (ch == 1):
            Mat = []
            print("Input the Matrix")
            accept_matrix(Mat)
            r = len(Mat)
            c = len(Mat[0])
        elif (ch == 2):
            display_matrix(Mat,r,c)
        elif(ch == 3):
            display_matrix(Mat,r,c)
            check_saddlepoint(Mat,r,c)
        else :
            print("Wrong Choice!")
            

main()
quit()