#include <iostream>

using namespace std;

class HanoiTower{
public:
    void hanoi(int disk, string source, string dest, string spare){
        if(disk == 1){
            cout << "Move disk from "  << source  << " to "  << dest << "\n";
        }
        else{
            hanoi(disk-1, source, spare, dest);
            hanoi(1, source, dest, spare);
            hanoi(disk-1, spare, dest, source);
        }
    }

    int main(){
        hanoi(3,"A","B","C");
        return 0;
    }
};