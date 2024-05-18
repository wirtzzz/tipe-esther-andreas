#ifndef RESOLUTION_ALEATOIRE_H
#define RESOLUTION_ALEATOIRE_H
#include <stdlib.h>
#include <thread>
#include <list>
#include <time.h>
#include "retour_sur_trace_recurrence.hpp"

std::list<Plateau> calcul_solutions_stoppable(std::list<Katamino> LK, Plateau p, int N, bool *quit_flag){
    i++;
    if (*quit_flag)
	return {};
    if (empty(LK))
    {
        return {};
    }
    Katamino k=LK.back();
    LK.pop_back();
    if(empty(LK) && N==k.aire){
        std::pair<std::list<Plateau>, int> coups = coups_possibles(k, p, N);
        i=i+size(std::get<0>(coups));
        return std::get<0>(coups);
    }
    else{
        std::pair<std::list<Plateau>, int> C = coups_possibles(k, p, N);
        std::list<Plateau> coups = std::get<0>(C);
        N = std::get<1>(C);
        std::list<Plateau> LS = {}; //liste des solutions
        for (Plateau coup: coups){
            std::list<Plateau> solutions_rec = calcul_solutions_stoppable(LK, coup, N, quit_flag);
            for (Plateau NC: solutions_rec){ //NC est un des nouveaux coups
                LS.push_front(NC);
            }
        }
        return LS;
    }

}

std::list<Katamino> melange(std::list<Katamino> LK){ // problème avec mélange
  srand(time(NULL));
  std::list<Katamino> unpile={}, l={};
  int n=size(LK), i=0, ind;
  while(n>0) {
      ind=rand()%n;
      while (i<ind){
	unpile.push_front(LK.back());
	LK.pop_back();
      	i++;
      }
      while (i>ind){
	LK.push_back(unpile.front());
	unpile.pop_front();
      	i--;
      }
      l.push_back(LK.back());
      LK.pop_back();
      n--;
  }
  return l;
}

void calcul(std::list<Plateau> *solutions,std::list<Katamino> LK, Plateau p, int N, bool *quit_flag){
  std::list<Plateau> temp=calcul_solutions_stoppable(LK, p, N, quit_flag);
  if (!*quit_flag)
    {
    	*quit_flag = true;
    	*solutions = temp;
    }
}

//fonction qui teste différentes listes avec des ordres aléatoires en utilisant le multi thread
std::list<Plateau> resolution_aleatoire (std::list<Katamino> LK, Plateau p, int N){
  std::list<Plateau> plateaux;
  std::list<Katamino> lk1 = melange(LK), lk2 = melange(LK), lk3 = melange(LK), lk4 = melange(LK);
  bool status=false;

  std::thread t1(calcul, &plateaux, lk1, p, N, &status);
  std::thread t2(calcul, &plateaux, lk2, p, N, &status);
  std::thread t3(calcul, &plateaux, lk3, p, N, &status);
  std::thread t4(calcul, &plateaux, lk4, p, N, &status);

  t1.join(); t2.join(); t3.join(); t4.join();	// arrêter les autres threads quand le premier se termine

  return plateaux;
}


#endif /* RESOLUTION_ALEATOIRE_H */