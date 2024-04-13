#ifndef LECTURE_H
#define LECTURE_H
#include <iostream>
#include <list>
#include "katamino.hpp"

Katamino str_to_kata(char str[2]){
	switch (str[1]){
		case '1':
			return P1;
		case '2':
			return I2;
		case '3':
			if (str[0]=='V')
				return V3;
			else
				return I3;
		case '4':
			switch (str[0]){
				case 'I':
					return I4;
				case 'L':
					return L4;
				case 'T':
					return T4;
				case 'C':
					return C4;
				default:
					return E4;
			}
		case '5':
			switch (str[0]){
				case 'L':
					return L5;
				case 'E':
					return E5;
				case 'V':
					return V5;
				case 'P':
					return P5;
				case 'C':
					return C5;
				default:
					return Z5;
			}
		default: return P1;
	}
}

std::string name(Katamino katamino){
	switch (katamino.color){
		case 40:
			return "L5";
		case 41:
			return "L4";
		case 42:
			return "V3";
		case 43:
			return "V5";
		case 44:
			return "T5";
		case 45:
			return "T4";
		case 46:
			return "E5";
		case 47:
			return "E4";
		case 100:
			return "P5";
		case 101:
			return "C5";
		case 102:
			return "Z5";
		case 103:
			return "C4";
		case 104:
			return "P1";
		case 105:
			return "I2";
		case 106:
			return "I3";
		default:
			return "I4";
	}
}

std::list<Katamino> str_to_list(std::string entree){
	int i=0;
	std::list<Katamino> l = {};
	int n=entree.size();
	char k[2];
	while (i < n){
		if (entree[i]>=65 && entree[i]<=90)
			{
				k[0]=entree[i], k[1]=entree[i+1];
				Katamino kata=str_to_kata(k);
				l.push_back(kata);
				i++;
			}
		i++;
	}
	return l;
}

int calcul_format(std::list<Katamino> l){
	int s = 0;
	for (Katamino k : l)
		s=s+k.aire;
	return s/5;
}

//fonction pour transformer chaine de char en liste de kataminos

//éventuellement faire aussi une fonction pour écrire les résultats des expériences dans un fichier texte

#endif /* LECTURE_H */