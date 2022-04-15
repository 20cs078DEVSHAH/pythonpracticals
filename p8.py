#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int ts;
    cout<<"Enter table size: ";
    cin>>ts;
    int a[ts]={0};
    for(int i=0;i<15;i++){
        int ele;
        cout<<"Enter Element: ";
        cin>>ele;
        int h=(ele%18)+2;
        if(a[h]==0){
            a[h]=ele;
        }
        else{
            int j;
            for(j=h+1;j<ts;j++){
                if(a[j]==0){
                    a[j]=ele;
                    break;
                }
                else if(j==ts-1){
                    if(a[j]!=0){
                        j=0;
                    }
                }
            }
        }
    }


for(int k=0;k<ts;k++){
    cout<<k<<"  "<<a[k]<<endl;
}

    cout<<"Created by -20CS078 DEV SHAH "<<endl;
    return 0;
}
