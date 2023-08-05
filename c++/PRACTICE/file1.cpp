#include<cstdio>
#include <iostream>

using  namespace std;

void stringFun(){
    string s;
    cout<<"Enter a String \n";

    getline(cin,s);

    cout<<"You have Entered : "<< s<<endl;

    s.push_back('Y');

    cout<<"After Using Pushback Function : "<<s<<endl;

    s.pop_back();
    cout<<"After Using PopBack Function : "<<s<<endl;

}

int  main()
{
    puts("click on button  ");
    cout<<"Hello Boss  ";
    stringFun();
    return 0;
} // namespaces std;
