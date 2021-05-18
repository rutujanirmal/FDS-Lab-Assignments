//Pizza parlour- accepting 'M' orders are served in first come first served basic.
//Order once placed cannot be cancelled Wap in C++ to simulate the system 
//using circlar queue using array .
#include<iostream>

using namespace std;
const int MAX=5;

class PizzaParlour
{
	int front,rear;
	int orders[MAX];
	public:
		PizzaParlour()
		{
			front=rear=-1;
		}
		bool addOrder(int data);
		void serveOrder();
		void display();
};
bool PizzaParlour::addOrder(int id){
 	if(rear==-1)
 	{
 		front=rear=0;
 		orders[rear]=id;
 		return true;
	 }
	 else
	 {
	 	int pos=(rear+1)%MAX;
	 	if(pos==front)
	 	{
	 		cout<<"\nCafe is Full.Please wait.\n";
	 		return false;
		 }
		 else
		 {
		 	rear=pos;
		 	orders[rear]=id;
		 	return true;
		 }
	 }
 }
 
 void PizzaParlour::serveOrder()
 {
 	if(front==-1)
 	{
 		cout<<"\n No Orders in Cafe.[Cafe is Empty)\n";
 		return;
	 }
	 else
	 {
	 	cout<<"\n Order No. "<<orders[front]<<" is processed.\n";
	 	if(front==rear) //only one order
	 	{
	 		front=rear=-1;
		 }
		 else
		 {
		 	front=(front+1)%MAX;
		 }
	 }
 }
 
 void PizzaParlour::display()
 {
 	int i=0;
 	if(front==-1)
 	{
 		cout<<"\nCafe is Empty.No orders.\n";
 		return;
	 }
	 else
	 {
	 	cout<<"Order Id's: \n";
	 	for(i=front;i!=rear;i=((i+1)%MAX))
	 	{
	 		cout<<orders[i]<<"  ";
		 }
		 cout<<orders[rear];
	 }
 }
 void intro()
 {	char name[50]={"\n Pizza parlour \n"};
 		for(int i=0;name[i]!='\0';i++)
	{
		cout<<name[i];
		
	}
 }
 int main()
 {
 	int ch,id=0;
 
	PizzaParlour q;

	do
	{
		cout<<"\n-----------------";
	intro();
		cout<<"-----------------";
		cout<<"\n***Menu**\n";
		cout<<"1. Accept order\n";
		cout<<"2. Serve order\n";
		cout<<"3. Display orders\n";
		cout<<"4. Exit";

		cout<<"\nChoice: ";
		cin>>ch;

		switch(ch)
		{
		case 1: 
				id++;
				if(q.addOrder(id))
				{
					cout<<"Thank you for order.Order id is : "<<id;
				}
				else
				{
					id--;
				}
				break;

		case 2: q.serveOrder();
				break;

		case 3: q.display();
				break;
		}
	}while(ch!=4);
	cout<<"\nThank You.Keep Visiting.";

 }




