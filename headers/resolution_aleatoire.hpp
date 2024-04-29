#ifndef RESOLUTION_ALEATOIRE_H
#define RESOLUTION_ALEATOIRE_H
#include <stdlib.h>
#include <thread>
#include <list>
#include "retour_sur_trace_recurrence.hpp"

std::list<Katamino> melange(std::list<Katamino> LK){
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
      l.push_back(LK.front());
      n--;
  }
  return l;
}

void calcul(std::list<Plateau> *solutions,std::list<Katamino> LK, Plateau p, int N){
  *solutions=calcul_solutions(LK, p, N);
}

//fonction qui teste différentes listes avec des ordres aléatoires en utilisant le multi thread
std::list<Plateau> resolution_aleatoire (std::list<Katamino> LK, Plateau p, int N){
  std::list<Plateau> plateaux;
  std::list<Katamino> lk1 = melange(LK), lk2 = melange(LK), lk3 = melange(LK), lk4 = melange(LK);
  std::thread t1(calcul, &plateaux, lk1, p, N);
  std::thread t2(calcul, &plateaux, lk2, p, N);
  std::thread t3(calcul, &plateaux, lk3, p, N);
  std::thread t4(calcul, &plateaux, lk4, p, N);

  t1.join(); t2.join(); t3.join(); t4.join();

  return plateaux;
}

#endif /* RESOLUTION_ALEATOIRE_H */