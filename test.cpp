#include <iostream>
#include <list>
#include "katamino.hpp"

void copy(std::list<Katamino> L1, std::list<Katamino> &L2){
    while(!empty(L1)){
            L2.push_front(L1.back());
            L1.pop_back();
    }

}
std::list<Katamino> L1={V5,V5};
std::list<Katamino> L2={};
int main()
{
    copy(L1, L2);
    for (Katamino k : L2){
        k.affiche();
    }
        for (Katamino k : L1){
        k.affiche();
    }
    return 0;
}


