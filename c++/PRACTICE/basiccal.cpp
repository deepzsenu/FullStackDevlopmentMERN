#include<iostream>

using namespace std;
class Cal{
    // private:
    public:
    int num1;
    int num2;

    public:
    // Cal(int num1, int num2){
    //     this->num1 = num1;
    //     this->num2 = num2;
    // }

    int sum(){
        return num1+num2;
    }
    int sub(){
        return num2-num1;
    }

};

int main(){
    // Cal cal1(2,3);
    Cal cal2;
    cal2.num1 = 8;
    cal2.num2= 4;
    cout<<cal2.sum()<<endl;
    cout<<cal2.sub()<<endl;

    return 0;
}   