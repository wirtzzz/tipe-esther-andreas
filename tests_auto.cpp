#include <iostream>
#include <fstream>
#include "retour_sur_trace_recurrence.hpp"

//déclaration des variables
std::fstream entree, sortie;
std::string ligne;
std::string path_entree, path_sortie;
int f[2]={5,0};
Plateau p = Plateau(f);
std::list<Katamino> L;
std::list<Plateau> solutions;
int last_f=0;

//déclaration des fonctions
int line_num(std::string);
void loading_bar(int, int);

int main(){
  printf("Rentrez le chemin du fichier que vous voulez tester en entrée (ENTREE pour le chemin par défaut)\n");
  std::cin >> path_entree;
  printf("Rentrez le chemin du fichier où écrire les résultats (ENTREE pour le chemin par défaut)\n");
  std::cin >> path_sortie;
  int n=line_num (path_entree);
  if (path_entree==" ")
    path_entree="tests/entree.txt";
  if (path_sortie==" ")
    path_sortie="tests/sortie.txt";
  entree.open(path_entree,std::ios::in);
  sortie.open(path_sortie,std::ios::out);
  int i = 0;

  while (!entree.eof ()){
    i++;
    std::getline (entree, ligne);
    system ("clear");
    std::cout << "Test de la liste : " << ligne << " [" << i << "/" << n << "]\n";
    loading_bar (i, n);
    L = str_to_list (ligne);
    f[1]=calcul_format (L);
    if(f[1] != last_f)
      p=Plateau(f);
    solutions = calcul_solutions (L, p, f[0]*f[1]);
    sortie << ligne << std::endl;
    sortie << "Nombre de solutions " << size(solutions)/4 << std::endl; // pour éviter de compter les diverses rotations
    last_f=f[1];
  }

  sortie.close ();
  entree.close ();
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
