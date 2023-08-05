#include<iostream>

using namespace std;

int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i = 0; i<n; i++){
        int m;
        cin>>m;
        arr[i] = m;
    }

    for (int i = 0; i <n; i++)
    {
        cout<<"element "<<i<<" is : " <<arr[i]<<endl;

    }
    return 0;

}