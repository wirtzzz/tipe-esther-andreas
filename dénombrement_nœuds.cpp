#include <iostream>
#include <fstream>
#include "headers/katamino.hpp"
#include "headers/retour_sur_trace_recurrence.hpp"
#include "headers/lecture.hpp"

std::fstream nodes, sortie;
std::string path_in, path_out, ligne;
int f[2]={5,0};
Plateau p = Plateau(f);
std::list<Katamino> L;
int n_noeuds;
int last_f=0;

int line_num(std::string);
void loading_bar(int, int);

//dénombrer les nœuds d'un arbre de solutions
int main(){
  printf("Rentrez le chemin du fichier que vous voulez tester en entrée (ENTREE pour le chemin par défaut)\n");
  std::cin >> path_in;
  printf("Rentrez le chemin du fichier où écrire les résultats (ENTREE pour le chemin par défaut)\n");
  std::cin >> path_out;
  int n=line_num (path_in);
  if (path_in==" ")
    path_in="tests/entree.txt";
  if (path_out==" ")
    path_out="tests/nœuds.txt";
  nodes.open(path_in, std::ios::in);
  sortie.open(path_out, std::ios::out);
  int i = 0;

  while (!nodes.eof ()){
    i++;
    std::getline (nodes, ligne);
    system ("clear");
    std::cout << "Test de la liste : " << ligne << " [" << i << "/" << n << "]\n";
    loading_bar (i, n);
    L = str_to_list (ligne);
    f[1]=calcul_format (L);
    if(f[1] != last_f)
      p=Plateau(f);
    n_noeuds = nombre_noeuds (L, p, f[0]*f[1]);
    sortie << size(L) << std::endl;
    sortie << "Nombre de nœuds " << n_noeuds << std::endl; // pour éviter de compter les diverses rotations
    last_f=f[1];
  }

  sortie.close ();
  nodes.close();
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
