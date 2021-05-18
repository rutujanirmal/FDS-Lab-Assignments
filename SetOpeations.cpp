/*Second year Computer Engineering class, set A of students like Vanilla Ice-cream
and set B of students like butterscotch ice-cream. Write C/C++ program to store two sets using linked list.
compute and display-
i. Set of students who like either vanilla or butterscotch or both
ii. Set of students who like both vanilla and butterscotch
iii. Set of students who like only vanilla not butterscotch
iv. Set of students who like only butterscotch not vanilla
v. Number of students who like neither vanilla nor butterscotch*/
#include<iostream>
using namespace std;
struct node{
int data;
struct node *link;
};
class Icecream
{
public:
    struct node *root=NULL;
    struct node *rootv=NULL;
    struct node *rootb=NULL;
    struct node *rootn=NULL;
    struct node *rootu=NULL;
    struct node *roote=NULL;

    void ButterS()
    {
        struct node *temp;
        int b;
        cout<<"\nEnter the no.of std like butterscotch: \n";
        cin>>b;
        for(int i=0;i<b;i++)
        {
            temp=new node;
            cout<<"\nEnter the roll no. of std "<<i+1<<" : ";
            cin>>temp->data;
            temp->link=NULL;
            if(rootb==NULL)
            {
                rootb=temp;
            }
            else
            {
                struct node *p;
                p=rootb;
                while(p->link!=NULL)
                {
                    p=p->link;
                }
                p->link=temp;
            }
        }
    }

    void Vanilla()
    {
        struct node *temp;
        int v;
        cout<<"\nEnter the no.of std like vanilla: \n";
        cin>>v;
        for(int i=0;i<v;i++)
        {
            temp=new node;
            cout<<"\nEnter the roll no. of std "<<i+1<<" : ";
            cin>>temp->data;
            temp->link=NULL;
            if(rootv==NULL)
            {
                rootv=temp;
            }
            else
            {
                struct node *p;
                p=rootv;
                while(p->link!=NULL)
                {
                    p=p->link;
                }
                p->link=temp;
            }
        }
    }

    void Total()
    {
        struct node *temp;
        int t;
        cout<<"\nEnter the total no.of stds: \n";
        cin>>t;
        for(int i=0;i<t;i++)
        {
            temp=new node;
            cout<<"\nEnter the roll no. of std "<<i+1<<" : ";
            cin>>temp->data;
            temp->link=NULL;
            if(root==NULL)
            {
                root=temp;
            }
            else
            {
                struct node *p;
                p=root;
                while(p->link!=NULL)
                {
                    p=p->link;
                }
                p->link=temp;
            }
        }
    }
    void DisplayButterS()
    {
        struct node *temp;
        temp=rootb;
        if(rootb==NULL)
        {
            cout<<"List is empty";
        }
        else
        {
            cout<<"\nStd liking butterscotch icecream are: ";
            while(temp!=NULL)
            {
                cout<<temp->data<<" ";
                temp=temp->link;
            }
        }
        cout<<endl;
    }

    void DisplayVanilla()
    {
        struct node *temp;
        temp=rootv;
        if(rootv==NULL)
        {
            cout<<"List is empty";
        }
        else
        {
            cout<<"\nStd liking vanilla icecream are: ";
            while(temp!=NULL)
            {
                cout<<temp->data<<" ";
                temp=temp->link;
            }
        }
        cout<<endl;
    }

    void DisplayTotal()
    {
        struct node *temp;
        temp=root;
        if(root==NULL)
        {
            cout<<"List is empty";
        }
        else
        {
            cout<<"\nTotal stds are: ";
            while(temp!=NULL)
            {
                cout<<temp->data<<" ";
                temp=temp->link;
            }
        }
        cout<<endl;
    }

    void Either()
    {
        struct node *temp,*temp1,*temp2,*temp3;;
        int flag;
        for(temp=root ; temp!=NULL ; temp=temp->link)
        {
            flag=0;
            for(temp1=rootv ; temp1!=NULL ; temp1=temp1->link)
            {
                for(temp2=rootb ; temp2!=NULL ; temp2=temp2->link)
                {
                    if(temp->data==temp1->data || temp->data==temp2->data)
                    {
                        flag=1;
                    }
                }
            }
            if(flag==1)
            {
                temp3=new node;
                if(roote==NULL)
                {
                    roote=temp3;
                    temp3->data =temp->data;
                    temp3->link=NULL;
                }
                else
                {
                    struct node *p;
                    p=roote;
                    while(p->link!=NULL)
                    {
                        p=p->link;
                    }
                    p->link=temp3;
                    temp3->data = temp->data;
                    temp3->link=NULL;
                }
            }
        }
    }

    int DisplayEither()
    {
        struct node *temp;
        temp=roote;
        if(roote==NULL)
        {
            cout<<"List is empty";
        }
        else
        {
            cout<<"\nStds who like either of the icecream are: ";
            while(temp!=NULL)
            {
                cout<<temp->data<<" ";
                temp=temp->link;
            }
        }
        cout<<endl;
    }

    void Neither()
    {
        struct node *temp;
        temp=root;
        struct node *temp1;
        int flag,s;
        s=0;
        while(temp!=NULL)
        {
            flag=0;
            temp1=roote;
            while(temp1!=NULL)
            {
                if(temp->data==temp1->data)
                {
                    flag=1;
                }
                temp1=temp1->link;
            }
            if(flag==0)
            {
                cout<<temp->data<<" ";
                s=s+1;
            }
            temp=temp->link;
        }
        cout<<endl;
        cout<<"The total number of std who don't like either of the icecream: "<<s<<endl;
    }

    void OnlyButterS()
    {
        struct node *temp;
        temp=rootb;
        struct node *temp1;
        int flag;
        while(temp!=NULL)
        {
            flag=0;
            temp1=rootv;
            while(temp1!=NULL)
            {
                if(temp->data==temp1->data)
                {
                    flag=1;
                }
                temp1=temp1->link;
            }
            if(flag==0)
            {
                cout<<temp->data<<" ";
            }
            temp=temp->link;
        }
        cout<<endl;
    }

    void OnlyVanilla()
    {
        struct node *temp;
        temp=rootv;
        struct node *temp1;
        int flag;
        while(temp!=NULL)
        {
            flag=0;
            temp1=rootb;
            while(temp1!=NULL)
            {
                if(temp->data==temp1->data)
                {
                    flag=1;
                }
                temp1=temp1->link;
            }
            if(flag==0)
            {
                cout<<temp->data<<" ";
            }
            temp=temp->link;
        }
        cout<<endl;
    }

    void Both()
    {
        struct node *p,*q,*r,*temp1;
        int flag=0;
        q=rootv;
        while(q!=NULL)
        {
            p=rootb;
            while(p!=NULL)
            {
                if(p->data == q->data)
                {
                    flag=1;
                    break;
                }
                p=p->link;
            }
            if(flag==1)
            {
                temp1=new node;
                temp1->data = q->data;
                temp1->link =NULL;
                if(rootu == NULL)
                {
                    rootu=temp1;
                }
                else
                {
                    r=rootu;
                    while(r->link!=NULL)
                    {
                        r=r->link;
                    }
                    r->link=temp1;
                }
                q=q->link;
                flag=0;
            }
            else
            {
                q=q->link;
            }
        }
    }

    void DisplayBoth()
    {
         struct node *temp;
        temp=rootu;
        if(rootu==NULL)
        {
            cout<<"Linked list is empty"<<endl;
        }
        else
        {
            cout<<"\nStudent eating both icecream are:";
            while(temp!=NULL)
            {
                cout<<temp->data<<" ";
                temp=temp->link;
            }
        }
        cout<<endl;
    }

};
int main()
{
    Icecream c;
    int ch;
    do
    {
        cout<<"1.Insert"<<endl<<"2.Insert vanilla"<<endl<<"3.Insert Butterscotch"<<endl<<"4.Display students who like vanilla"<<endl<<"5.Display students who like butterscotch"<<endl<<"6.Students like both"<<endl<<"7.Only vanilla"<<endl<<"8.Only butterscotch"<<endl<<"9.either or"<<endl<<"10.Neither nor"<<endl;
        cout<<"Enter choice";
        cin>>ch;
        switch(ch)
        {
            case 1:
            c.Total();
            c.DisplayTotal();
            break;

             case 2:
            c.Vanilla();
            break;

             case 3:
            c.ButterS();
            break;

             case 4:
            c.DisplayVanilla();
            break;

             case 5:
            c.DisplayButterS();
            break;

             case 6:
            c.Both();
            c.DisplayBoth();
            break;

             case 7:
            c.OnlyVanilla();
            break;

             case 8:
            c.OnlyButterS();
            break;

             case 10:
             c.Neither();
            break;

             case 9:
            c.Either();
            c.DisplayEither();
            break;

            default:
            cout<<"Enter correct choice"<<endl;
        }
    }while(ch!=0);
    return 0;
}


