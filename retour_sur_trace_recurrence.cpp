#include <iostream>
#include <list>
#include <exception>
#include "katamino.hpp"

struct Place{ //utilisé pour premiereSolutionIteratif()
    Katamino piece;
    int r;
    int s;
};


//mieux
std::pair<std::list<Plateau>,int> coups_possibles(Katamino,Plateau,int);
std::list<Plateau> solutions(std::list<Katamino>, Plateau, int);
Plateau premiereSolution(std::list<Katamino>, Plateau, int);
Plateau premiereSolutionIteratif(std::list<Katamino>, Plateau);
bool rempli(Plateau);

std::list<Katamino> L7={Z5,L4,V3,C4,C4,V3,P5,E5,V3};
std::list<Katamino> List5 = {P5,I3,L4,T4,I4};
int f[2]={5,7};
Plateau p=Plateau(f);

int main(){
  Plateau sol = premiereSolutionIteratif(L7, p);
  sol.affiche();
  return 0;
}

//fonction calculant les différents coups possibles à partir d'un plateau et katamino donnés
std::pair<std::list<Plateau>, int> coups_possibles(Katamino k, Plateau p, int n){
    Katamino katamino = k;
    katamino.x=0, katamino.y=0;
    int r=0, s=0, s_max=0;  //fonction
    Plateau np=Plateau(p.format);
    std::list<Plateau> coups={};
    if (n-katamino.aire<0)
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

//renvoie par récurrence sur une liste donnée de kataminos l'ensemble des solutions
std::list<Plateau> solutions(std::list<Katamino> LK, Plateau p, int N){
    if (empty(LK))
        return {};
    Katamino k=LK.back();
    LK.pop_back();
    if(empty(LK) && N==k.aire){
        std::pair<std::list<Plateau>, int> coups = coups_possibles(k, p, N);
        return std::get<0>(coups);
    }
    else{
        std::pair<std::list<Plateau>, int> C = coups_possibles(k, p, N);
        std::list<Plateau> coups = std::get<0>(C);
        N = std::get<1>(C);
        std::list<Plateau> LS = {}; //liste des solutions
        for (Plateau coup: coups){
            std::list<Plateau> solutions_rec = solutions(LK, coup, N);
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

Plateau premiereSolution(std::list<Katamino> LK, Plateau p, int N){
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
        for (Plateau coup : coups){
            Plateau solution = premiereSolution(LK, coup, N);
            if (rempli(solution))
                return solution;
        }
        return p;
    }
}

Plateau premiereSolutionIteratif(std::list<Katamino> LK, Plateau p){
    std::list<Katamino> List = {};
    std::list<struct Place> Places = {};
    int n = size(LK);
    int m = n;
    if (empty(LK))
        return p;
    List.splice(List.begin(),LK);
    int s=0, r=0, i=0, j=0;
    bool rate=true;
    while (!empty(List)){ //pb là dessous
        Katamino k = List.back();
        i=k.x, j=k.y;
        while (s<2 && rate){
            while (r<k.max_rot && rate){
                while (k.y<=p.format[1] - k.format[1] && rate){
                    while (k.x<=p.format[0] - k.format[0] && rate){
                        try {
                            p.ajouter(k);
                        }
                        catch (int e){
                            if (e==1){
                                rate=false;
                                Places.push_front({k, r, s});
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
            if (empty(Places))
                return p;
            s=Places.front().s, r=Places.front().r, j=Places.front().piece.x, i=Places.front().piece.y;
            // copy(List, LK, m-n-1, m); <- trouver un truc pour remplacer le slicing
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
            LK.pop_back();
    }
    return p;
}
