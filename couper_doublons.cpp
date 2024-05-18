#include <iostream>
#include <fstream>
#include <map>
#include "headers/lecture.hpp"

std::string list_to_str (std::list<Katamino>);

std::map <std::string , bool > dico={};
std::string path;
std::fstream file;
std::string ligne;
std::list<Katamino> liste = {};

int main(){
  printf ("entrez le fichier que vous voulez modifier\n");
  std::cin >> path;
  file.open(path, std::ios::in);

  while(!file.eof ()){
    getline (file,ligne);
    liste = str_to_list (ligne);
    ligne = list_to_str (liste);
    dico[ligne] = true;
  }
  file.close ();
  file.open (path, std::ios::out);

  for (auto elt : dico){
    ligne = elt.first;
    file << ligne;
  }

  file.close ();
  return 0;
}

std::string list_to_str(std::list<Katamino> L){
  std::string phrase="[";
  for (Katamino k: L){
    phrase=phrase+name(k)+", ";
  }
  phrase=phrase+"]\n";
  return phrase;
}
