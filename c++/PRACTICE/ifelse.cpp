#include<iostream>

using namespace std;

void ifElse(){
    cout<<"Enter the first number : ";
    int n1;
    int n2;
    int sum = 0;


    cin>>n1;
    cout<<"Enter the second Number: ";

    cin>>n2;

    sum = n1+n2;

    if(sum>100){
        cout<<"Sum of the number i greater than 100 : sum is "<<sum;
    }
    else if (sum <0){
        cout<<"Sum of the numbers is negative: sum is "<<sum;
    }
    else{
        cout<<"Sum of the number is less than 100: sum is "<<sum;
    }

}
int main(){

    cout<<"Simple if else \n";
    ifElse();
    return 0;
}