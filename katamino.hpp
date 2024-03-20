#ifndef KATAMINO_H
#define KATAMINO_H
#include <array>
#include <iostream>

//classes
//=================================== KATAMINO =========================================
class Katamino{
  public:
    int shape[4][4];
    int x,y;
    bool sym;
    int max_rot;
    int aire;
    int format[2]; //format correspond au format du katamino, par exemple 2×4 pour L5
    int color;
    Katamino(int s[4][4],bool symmetric, int max, int f[2], int a, int c, int x_coord=0, int y_coord=0){
      for (int i = 0; i<4; i++){
        for (int j=0; j<4; j++){
          shape[i][j]=s[i][j];
        }
      }
      format[0]=f[0];
      format[1]=f[1];
      sym=symmetric;
      max_rot=max;
      aire=a;
      color=c;
      x=x_coord;
      y=y_coord;
    }
    //méthodes
    void affiche(){
      for (int i=0; i<4; i++){
          for (int j=0; j<4; j++){
              if (shape[i][j]==0)
              	printf("  ");
              else
		printf("\033[%dm  \033[0m", color); //affiche la couleur du katamino
              }
          std::cout<<std::endl;
      }
    }
    void rotation(){
      int ns[4][4];
      for (int i = 0; i<4; i++){
      for(int j=0; j<4; j++){
        if (i<format[1] && j<format[0])
          ns[i][j]=shape[format[0]-j-1][i];
        else
          ns[i][j]=0;
        }
      }
      for (int i=0; i<4; i++){
        for(int j=0; j<4; j++){
          shape[i][j]=ns[i][j];
        }
      }
      int temp=format[0];
      format[0]=format[1];
      format[1]=temp;
    }

    void retourne(){
      int ns[4][4];
      for (int i=0; i<4; i++){
        for(int j=0; j<4; j++){
          if (i<format[0] && j<format[1])
            ns[i][j]=shape[format[0]-i-1][j];
          else
            ns[i][j]=0;
          }
        }
        for (int i=0; i < 4; i++)
        {
          for (int j=0; j < 4; j++)
           {
            shape[i][j]=ns[i][j];
           }
        }
      }
};

//================================== PLATEAU ==================================
class Plateau{
  public:
    int format[2]; // 1<=format[0]<<5 et 1<=format[1]<<13
    int shape[5][13];
    Plateau(int f[2]){
      for(int i=0; i<f[0]; i++){
        for (int j=0; j < f[1]; j++)
          {
            shape[i][j]=0;
          }
      }
      format[0]=f[0];
      format[1]=f[1];
    }
    void affiche(){
      for (int i = 0; i < format[0]; i++)
        {
          for(int j=0; j< format[1]; j++)
            {
            	if(shape[i][j]==0)
            		printf("  ");
            	else
			printf("\033[%dm  \033[0m", shape[i][j]);
            }
          std::cout << std::endl;
        }
    }
    void ajouter(Katamino katamino){
      for (int i=katamino.x; i< katamino.x + katamino.format[0]; i++){
        for (int j = katamino.y; j<katamino.y+katamino.format[1]; j++)
          {
            if (katamino.shape[i-katamino.x][j-katamino.y]!=0){
             if (i<format[0] && j<format[1] && shape[i][j]==0)
		shape[i][j] = katamino.color;
              else
                {throw 0; return;}
            }
          }
     }
      throw 1;
    }
};

//objets

int L5s[4][4]={{1,1,0,0}, {1,0,0,0},{1,0,0,0},{1,0,0,0}};
int L5f[2]={4,2};
Katamino L5=Katamino(L5s, false, 4, L5f,5, 40);

int L4s[4][4]={{2,2,0,0}, {2,0,0,0},{2,0,0,0},{0,0,0,0}};
int L4f[2]={3,2};
Katamino L4=Katamino(L4s, false, 4, L4f,4, 41);

int V3s[4][4]={{3,3,0,0},{3,0,0,0},{0,0,0,0},{0,0,0,0}};
int V3f[2]={2,2};
Katamino V3=Katamino(V3s, true, 4, V3f,3, 42);

int V5s[4][4]={{4,4,4,0},{4,0,0,0},{4,0,0,0},{0,0,0,0}};
int V5f[2]={3,3};
Katamino V5=Katamino(V5s, true, 4, V5f,5,43);

int T5s[4][4]={{5,0,0,0},{5,5,0,0},{5,0,0,0},{5,0,0,0}};
int T5f[2]={4,2};
Katamino T5=Katamino(T5s, false, 4, T5f,5,44);

int T4s[4][4]={{6,0,0,0},{6,6,0,0},{6,0,0,0},{0,0,0,0}};
int T4f[2]={3,2};
Katamino T4=Katamino(T4s, true, 4, T4f,4,45);

int E5s[4][4]={{7,0,0,0},{7,7,0,0},{0,7,0,0},{0,7,0,0}};
int E5f[2]={4,2};
Katamino E5=Katamino(E5s, false, 4, E5f,5,46);

int E4s[4][4]={{8,0,0,0},{8,8,0,0},{0,8,0,0},{0,0,0,0}};
int E4f[2]={3,2};
Katamino E4=Katamino(E4s, false, 2, E4f,4,47);

int P5s[4][4]={{9,9,0,0},{9,9,0,0},{9,0,0,0},{0,0,0,0}};
int P5f[2]={3,2};
Katamino P5=Katamino(P5s,  false, 4, P5f,5,100);

int C5s[4][4]={{15,15,0,0},{15,0,0,0},{15,15,0,0},{0,0,0,0}};
int C5f[2]={3,2};
Katamino C5=Katamino(C5s, true, 4, C5f,5,101);

int Z5s[4][4]={{16,0,0,0},{16,16,16,0},{0,0,16,0},{0,0,0,0}};
int Z5f[2]={3,3};
Katamino Z5=Katamino(Z5s, false, 2, Z5f,5,102);

int C4s[4][4]={{10,10,0,0},{10,10,0,0},{0,0,0,0},{0,0,0,0}};
int C4f[2]={2,2};
Katamino C4=Katamino(C4s, true, 1, C4f,4,103);

int P1s[4][4]={{11,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
int P1f[2]={1,1};
Katamino P1=Katamino(P1s, true, 1, P1f,1,104);

int I2s[4][4]={{12,12,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
int I2f[2]={1,2};
Katamino I2= Katamino(I2s, true, 2, I2f,2,105);

int I3s[4][4]={{13,13,13,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
int I3f[2]={1,3};
Katamino I3=Katamino(I3s, true, 2, I3f,3,106);

int I4s[4][4]={{14,14,14,14},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
int I4f[2]={1,4};
Katamino I4=Katamino(I4s, true, 2, I4f,4,107);

#endif /* KATAMINO_HPP */
