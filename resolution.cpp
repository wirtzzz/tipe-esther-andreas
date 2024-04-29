#include <iostream>
#include <list>
#include "headers/retour_sur_trace_recurrence.hpp"
#include "headers/lecture.hpp"

std::string entree;
bool keep_going=true;
char choix;



int main()
{
  while (keep_going){
    printf("Entrez la liste de kataminos que vous voulez tester :\n");
    std::cin >> entree;
    std::list<Katamino> L = str_to_list(entree);
    int form[2]={5,calcul_format(L)};
    Plateau plateau = Plateau(form);

    Plateau sol = premiereSolution(L, plateau,form[0]*form[1],0);
    sol.affiche();

    printf("Continuer ? [o/n]\n");
    std::cin >> choix;
    if (choix!='o')
        keep_going = false;
  }
    return 0;
}
