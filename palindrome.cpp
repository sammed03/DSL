#include <iostream>
#include <stdlib.h>
#define SIZE 100
using namespace std;

class mystack
{
private:
    char st[SIZE];
    int top;

public:
    mystack();
    void push(char x);
    char pop();
    int isEmpty();
    int isFull();
};

mystack ::mystack()
{
    top = -1;
}

mystack ::isEmpty()
{
    if (top == -1)
        return 1;
    else
        return 0;
}

mystack ::isFull()
{
    if (top == SIZE - 1)
        return 1;
    else
        return 0;
}

void mystack ::push(char x)
{
    if (!isFull())
    {
        top++;
        st[top] = x;
    }
    else
    {
        cout << "\n Stack Overflow!! ERROR";
    }
}

char mystack ::pop()
{
    char x = '\0';
    x = st[top];
    top--;
    return x;
}

void convert_string(char str[], char str1[])
{
    int i, j = 0;
    for (i = 0; str[i] != '\0'; i++)
    {
        if (str[i] >= 'a' && str[i] <= 'z')
            str1[j++] = str[i];
        if (str[i] >= 'A' && str[i] <= 'z')
            str1[j++] = str[i] + 32;
    }
    str1[j] = '\0';
}

int main()
{
    int ch, flag, i;
    char str[100];
    char str1[100];
    mystack s;
    system("clear");
    do
    {
        cout << "\n\t\t\t1 : Check for Palindrome";
        cout << "\n\t\t\t2 : Find Reverse";
        cout << "\n\t\t\t3 : Exit";
        cout << "\n\n Enter Your CHoice: ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            cout << "Enter the string to check for Palindrome";
            cin.ignore();
            cin.getline(str, 100);
            cout << "Entered String is " << str;
            convert_string(str, str1);
            cout << "Converted string is : " << str1;
            for (i = 0; str1[i] != '\0'; i++)
            {
                s.push(str1[i]);
            }
            i = 0;
            flag = 1;
            while (!s.isEmpty())
            {
                if (str1[i++] != s.pop())
                {
                    flag = 0;
                    break;
                }
            }
            if (flag == 1)
            {
                cout << "\nGiven string is palindrome!";
            }
            else
            {
                cout << "\n Given string is not Palindrome!";
            }
            break;

        case 2:
            cout << "Enter the string to be reversed";
            cin.ignore();
            cin.getline(str, 100);
            cout << "Entered string is : " << str;
            for (i = 0; str[i] != '\0'; i++)
            {
                s.push(str[i]);
            }
            cout << "\nReverse string is :";
            while (!s.isEmpty())
            {
                cout << s.pop();
            }
            break;

        case 3:
            cout << "ENd of Program\n";
            break;

        default:
            cout << "Invalid CHoice";
        }
    } while (ch != 3);

    return 0;
}