//Write C++ program using stack to check whether given expression is well parenthesized or not.

#include <iostream>
#include <stack>
using namespace std;

void balance_parentheses(string s)
{
    stack<char> a;
    int flag = 1;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '{' || s[i] == '[' || s[i] == '(') {
            a.push(s[i]);
        }
        if (!a.empty()) 
            {
            if (s[i] == '}') 
            {
                if (a.top() == '{')
                    {
                        a.pop();
                        continue;
                    }
                else
                    flag=0;
            }
            if (s[i] == ']') 
            {
                if (a.top() == '[') 
                    {
                        a.pop();
                        continue;
                    }
                else
                    flag=0;
            }
            if (s[i] == ')') {
                if (a.top() == '(') 
                {
                    a.pop();
                    continue;
                }
                else
                    flag=0;
            }
        }
        else {
            flag=0;
        }
    }

    if ((a.empty()) && (flag !=0))
        cout << "\nBalanced" << endl;
    else
        cout << "\nNot balanced" << endl;
}

int main()
{
    int t;
    string s;
    cout << "Enter string of parentheses:";
    cin >> s;
    balance_parentheses(s);
    return 0;
}
