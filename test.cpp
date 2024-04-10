#include <iostream>
#include <list>
#include "katamino.hpp"
#include "lecture.hpp"

int main()
{
    std::string entree;
    std::cin >> entree;
    std::cout << entree << std::endl;
    std::cout << std::endl;
    std::list<Katamino> l = str_to_list(entree);
    for (Katamino k: l)
        k.affiche();
    return 0;
}


