#include <iostream>
#include "headers/lecture.hpp"
#include "headers/resolution_aleatoire.hpp"
#include "headers/retour_sur_trace_recurrence.hpp"
#include "headers/katamino.hpp"
#include <fstream>
#include <chrono>

//déclaration des variables
std::fstream entree, sortie;
std::string ligne;
std::string path_entree, path_sortie;
int f[2]={5,0};
Plateau p = Plateau(f);
std::list<Katamino> L1,L2;
int last_f=0;
std::list<Plateau> junk;

//déclaration des fonctions
int line_num(std::string);
void loading_bar(int, int);

//comparaison de la longueur des calculs avec calcul_solutions() et resolution_aleatoire() en secondes
int main(){
  printf("Rentrez le chemin du fichier que vous voulez tester en entrée (ENTREE pour le chemin par défaut)\n");
  std::cin >> path_entree;
  printf("Rentrez le chemin du fichier où écrire les résultats (ENTREE pour le chemin par défaut)\n");
  std::cin >> path_sortie;
  int n=line_num (path_entree);
  if (path_entree=="")
    path_entree="tests/entree.txt";
  if (path_sortie=="")
    path_sortie="tests/nœuds.txt";
  entree.open(path_entree, std::ios::in);
  sortie.open(path_sortie, std::ios::out);
  int i = 0;
  auto start = std::chrono::high_resolution_clock::now();
  auto duree = std::chrono::duration_cast<std::chrono::microseconds>(start - std::chrono::high_resolution_clock::now());
  while (!entree.eof ()){
    i++;
    std::getline (entree, ligne);
    system ("clear");
    std::cout << "Test de la liste : " << ligne << " [" << i << "/" << n << "]\n";
    loading_bar (i, n);
    L1 = str_to_list (ligne);
    L2=L1;
    f[1]=calcul_format (L1);
    if(f[1] != last_f)
      p=Plateau(f);


    sortie << size(L1) << std::endl;
    //calcul du temps mis par calcul_solutions()
    start = std::chrono::high_resolution_clock::now();
    junk = calcul_solutions(L1, p, f[0]*f[1]);
    duree = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - start);
    sortie << "D " << duree.count() << std::endl;

    //calcul du temps mis par
    start = std::chrono::high_resolution_clock::now();
    junk = resolution_aleatoire(L2, p, f[0]*f[1]);
    duree = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - start);
    sortie << "A " << duree.count() << std::endl; // A pour aléatoire
    last_f=f[1];
  }

  sortie.close ();
  entree.close();
  return 0;
}

int line_num(std::string path){
    std::fstream file;
    int i=0;
    std::string a;
    file.open(path, std::ios::in);
    while (!file.eof()){
        std::getline(file,a);
        ++i;
    }
    file.close();
    return i;
}

void loading_bar(int cur, int total){
  int state= (200*cur)/total;
  printf ("[");
  for (int i=0; i<200; i++){
    if (i<state)
      printf ("=");
    else
      printf (" ");
  }
  printf ("]\n");
}
