#include <iostream>
#include <string>
using namespace std;


int main(){
    int value = 7;
    int *ptr = &value;
    cout << "value : "<<value << endl;
    cout << "&value : "<<&value << endl;
    cout << "*ptr : "<<*ptr << endl;
    cout << "ptr : "<<ptr << endl;
    return 0;
}