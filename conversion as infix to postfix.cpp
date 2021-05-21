// Group B-27.N
// Implement C++ program for expression conversion as infix to postfix and its evaluation
// using stack based on given conditions:
// 1. Operands and operator, both must be single character.
// 2. Input Postfix expression must be in a desired format.
// 3. Only '+', '-', '*' and '/'operators are expected.
#include<iostream>
#include<cstring>
#include<stack>
using namespace std;

int getWeight(char ch) {
	switch (ch) {
	case '/': return 2;
	case '*': return 2;
	case '+': return 1;
	case '-': return 1;
	default : return 0;
	}
}

// convert infix expression to postfix using a stack
void infix2postfix(char infix[], char postfix[], int size) {
	stack<char> s;
	int weight;
	int i = 0;
	int k = 0;
	char ch;
	while (i < size) {
		ch = infix[i];
		if (ch == '(') {
			s.push(ch);
			i++;
			continue;
		}
		if (ch == ')') {
			while (!s.empty() && s.top() != '(') {
				postfix[k++] = s.top();
				s.pop();

			}
			if (!s.empty()) {
				s.pop();
			}
			i++;
			continue;
		}
		weight = getWeight(ch);
		if (weight == 0) {
			postfix[k++] = ch;

		}
		else {
			if (s.empty()) {
				s.push(ch);
			}
			else {
				while (!s.empty() && s.top() != '(' &&
						weight <= getWeight(s.top())) {
					postfix[k++] = s.top();
					s.pop();

				}
				s.push(ch);
			}
		}
		i++;
	}

	while (!s.empty()) {
		postfix[k++] = s.top();
		s.pop();
	}
	postfix[k] = 0;
}

// main
int main() {
	char infix[100];//"A*(B+C)/D";
	cout<<"\nEnter Infix Operation:";
	cin>>infix;
	int size = strlen(infix);
	char postfix[size];
	infix2postfix(infix,postfix,size);
	cout<<"\nInfix Expression :: "<<infix;
	cout<<"\nPostfix Expression :: "<<postfix;
	cout<<endl;
	return 0;
}
