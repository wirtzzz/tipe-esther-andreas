#ifndef RETOUR_SUR_TRACE_RECURRENCE_H
#define RETOUR_SUR_TRACE_RECURRENCE_H
#include <iostream>
#include <list>
#include <exception>
#include "lecture.hpp"
#include "katamino.hpp"

//STRUCTURE
struct Place{ //utilisé pour premiereSolutionIteratif()
    Katamino piece;
    int r;
    int s;
};

//FONCTIONS

void afficher_solutions(std::list<Plateau> Solu){
    for (Plateau p : Solu){
        p.affiche();
    }
}

// fonction déterminant la plus grande longueur vide dans le plateau
// complexité en O(format[0]*format[1]), là où la recherche de tous les coups dans coups possible est en O(format[1]*format[2]*k.aire)
int l_max(Plateau plateau){
    int max=0;
    int ch;
    for (int i=0; i<plateau.format[0]; i++){
    	ch=0;
    	for (int j=0; j<plateau.format[1]; j++){
	    if (plateau.shape[i][j] == 0){
	    	ch++;
	    	if (ch>max)
	    	   max=ch;
	    }
	    else
		ch=0;
    	}
    }
    for (int i=0; i<plateau.format[1]; i++){
    	ch=0;
    	for (int j=0; j<plateau.format[0]; j++){
	    if (plateau.shape[j][i] == 0){
		ch++;
		if (ch>max)
		   max=ch;
	    }
	    else
	        ch=0;
    	}
    }
    return max;
}

//fonction calculant les différents coups possibles à partir d'un plateau et katamino donnés
std::pair<std::list<Plateau>, int> coups_possibles(Katamino k, Plateau p, int n){
    Katamino katamino = k;
    katamino.x=0, katamino.y=0;
    int r=0, s=0, s_max=0;  //fonction
    Plateau np=Plateau(p.format);
    std::list<Plateau> coups={};
    if (n-katamino.aire<0 || l_max(p)<katamino.max_length) //critère permettant d'éliminer rapidement certains calculs
        {
        return std::make_pair(coups,0);
        }
    if (!katamino.sym)
        s_max++;
    while (s<=s_max){
        while (r<katamino.max_rot){
            while (katamino.x <= p.format[0]-katamino.format[0]){
                while (katamino.y <= p.format[1]-katamino.format[1]){
                    np=p;
                    try{
                        np.ajouter(katamino);
                    }
                    catch(int e){
                        if (e==1){
                            coups.push_front(np);
                        }

                    }
                    katamino.y++;
                }
                katamino.y=0;
                katamino.x++;
            }
            katamino.x=0;
            katamino.rotation();
            r++;
        }
        r=0;
        katamino.retourne();
        s++;
    }
    return std::make_pair(coups, n-katamino.aire);
};

int i;
//renvoie par récurrence sur une liste donnée de kataminos l'ensemble des solutions
std::list<Plateau> calcul_solutions(std::list<Katamino> LK, Plateau p, int N){
    i++;
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
            std::list<Plateau> solutions_rec = calcul_solutions(LK, coup, N);
            for (Plateau NC: solutions_rec){ //NC est un des nouveaux coups
                LS.push_front(NC);
            }
        }
        return LS;
    }
};

bool rempli(Plateau p){
    for (int i = 0; i<p.format[0] ; i++){
        for (int j=0; j<p.format[1]; j++){
            if (p.shape[i][j]==0)
                return false;
        }
    }
    return true;
}

Plateau premiereSolution(std::list<Katamino> LK, Plateau p, int N, int niveau){
    if (empty(LK))
        return p;
    Katamino k = LK.back();
    LK.pop_back();
    if (empty(LK) && N==k.aire){
        std::pair<std::list<Plateau>, int> C=coups_possibles(k, p, N);
        Plateau solution = std::get<0>(C).back();
        return solution;
    }
    else{
        std::pair<std::list<Plateau>, int> C = coups_possibles(k, p, N);
        std::list<Plateau> coups = std::get<0>(C);
        printf("%li \n %d \n",size(coups),niveau);
        afficher_solutions(coups);
        for (Plateau coup : coups){
            Plateau solution = premiereSolution(LK, coup, N,niveau+1);
            if (rempli(solution))
                return solution;
        }
        return p;
    }
}

int nombre_noeuds(std::list<Katamino> LK, Plateau p, int N){
    i=0;
    calcul_solutions(LK, p, N);
    return i;
};

//mise en standby pour l'instant parce que trop chiant pour pas grand chose
Plateau premiereSolutionIteratif(std::list<Katamino> LK, Plateau p){
    std::list<Katamino> List = {};
    std::list<struct Place> Places = {};
    int n = size(LK);
    int m = n;
    if (empty(LK))
        return p;
    List.insert(List.end(),LK.begin(),LK.end());
    int s=0, r=0, i=0, j=0;
    bool rate=true;
    Plateau np=Plateau(p.format);
    while (!empty(List)){
        rate=true;
        Katamino k = List.back();
        i=k.x, j=k.y;
        while (s<2 && rate){
            while (r<k.max_rot && rate){
                while (k.y<=p.format[1] - k.format[1] && rate){
                    while (k.x<=p.format[0] - k.format[0] && rate){
                        np=p;
                        try {
                            p.ajouter(k);
                        }
                        catch (int e){
                            if (e==1){
                                rate=false;
                                Places.push_front({k, r, s});
                                p=np;
                                break;
                            }
                        }
                        k.x++;
                    }
                    k.x=0;
                    k.y++;
                }
                k.y=0;
                r++;
                if (rate)
                    k.rotation();
            }
            r=0;
            if (rate)
                k.retourne();
            s++;
        }
        s=0;
        if (rate){
            printf("ah");
            if (empty(Places))
                return p;
            s=Places.front().s, r=Places.front().r, j=Places.front().piece.y, i=Places.front().piece.x;
            Places.pop_front();
            auto it = LK.begin();
            std::advance(it, m-n-1);
            List={};
            List.insert(List.end(),it,LK.end());
            printf("%li",size(List));
            LK.back()=Places.front().piece;
            i=LK.back().x, j=LK.back().y;
            if (i>p.format[0]-Places.back().piece.format[0]){
                i=0;
                if (j>p.format[1]-Places.back().piece.format[1]){
                    j=0;
                    if (r>3){
                        r=0;
                        if (s==0)
                            s++;
                    }
                    else
                        r++;
                }
                else
                    j++;
            }
            else
                i++;

        }
        else
            {
                List.pop_back();
                m--;
            }
    }
    return p;
}

#endif /*RETOUR_SUR_TRACE_RECURRENCE_H*/
