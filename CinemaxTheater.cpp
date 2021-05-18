/*The ticket booking system of Cinemax theater has to be implemented using C++ program.
There are 10 rows and 7 seats in each row.
Doubly circular linked list has to be maintained to keep track of free seats at rows.
Assume some random booking to start with.
Use array to store pointers (Head pointer) to each row. On demand
a) The list of available seats is to be displayed
b) The seats are to be booked
c) The booking can be canceled.*/
#include<iostream>
using namespace std;
struct node
{
    char data;
    struct node *pre,*next;
};
struct node *root[10];

class Cinema
{
public:
    void seats()
    {
        for(int i=0;i<10;i++)
        {
            root[i]=NULL;
        }
        for(int k=0;k<10;k++)
        {
            struct node *temp;
            struct node *q;
            for(int j=0;j<8;j++)
            {
                temp=new node;
                temp->data='E';
                temp->next=NULL;
                if(root[k]==NULL)
                {
                    root[k]=temp;
                }
                else{
                    struct node *p;
                    p=root[k];
                    while(p->next!=NULL)
                    {
                        p=p->next;
                    }
                    p->next=temp;
                    temp->pre=p;
                }
            }
            temp->next=root[k];
            q=root[k];
            q->pre=temp;
        }
    }

    void displaySeats()
    {   int t=1;
        struct node *temp;
        struct node *p;
        cout<<"\nFor the following: E=Empty seats B=Booked seats"<<endl;
        for(int i=0;i<10;i++)
        {
            cout<<endl;
            int r=1;
            temp=root[i];
            p=root[i];
            cout<<"ROW:"<<t<<"  ";
            while(temp->next!=p)
            {
                cout<<r<<"."<<temp->data<<" ";
                temp=temp->next;
                r++;
            }
            t++;
        }
    }

    void BookSeats()
    {
        int row,col,r;
        int arr[10]={1,2,3,4,5,6,7,8,9,10};
        cout<<endl;
        cout<<"Enter the seat to be booked \nin the form : row_number column_number \nfor instance : 1 6\nEnter :: ";
        cin>>row>>col;
        for(int k=0;k<10;k++)
        {
            if(arr[k]==row)
            {
                r=k;
            }
        }
        struct node *temp;
        temp=root[r];
        for(int i=0;i<col-1;i++)
        {
            temp=temp->next;
        }
        if(temp->data=='B')
        {
            cout<<"Seat is already booked"<<endl;
        }
        else{
            temp->data='B';
            cout<<"Your seat is now booked"<<endl;
            displaySeats();
        }
    }

        void CancelSeats()
    {
        int row,col,r;
        int arr[10]={1,2,3,4,5,6,7,8,9,10};
        cout<<endl;
        cout<<"Enter the seat to cancel \nin the form : row_number column_number \nfor instance : 1 6\nEnter :: ";
        cin>>row>>col;
        for(int k=0;k<10;k++)
        {
            if(arr[k]==row)
            {
                r=k;
            }
        }
        struct node *temp;
        temp=root[r];
        for(int i=0;i<col-1;i++)
        {
            temp=temp->next;
        }
        if(temp->data=='E')
        {
            cout<<"Seat is already empty"<<endl;
        }
        else{
            temp->data='E';
            cout<<"Your seat is now canceled"<<endl;
            displaySeats();
        }
    }
};

int main()
{
    int ch;
    Cinema c;
    do
    {
        cout<<"\n1.Display seats \n2.Book your seat \n3.Cancel your booking\n4.Quit\nEnter the choice :: ";
        cin>>ch;
        switch(ch)
        {
        case 1:
            c.seats();
            c.displaySeats();
            break;
        case 2:
            c.BookSeats();
            break;
        case 3:
            c.CancelSeats();
            break;
        case 4:
            exit(1);
        default:
            cout<<"Enter the correct choice"<<endl;
        }
    }while(ch!=0);
    return 0;
}

