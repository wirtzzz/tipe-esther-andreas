#ifndef KATAMINO_H
#define KATAMINO_H
#include <array>

class Katamino{
  public:
    int shape{};
    int x_coord,y_coord;
    bool sym;
    int max_rot;
    set_kata(int s[6][6],bool symmetric, int max, int x=0, int y=0){
      shapte=s
      sym=symmetric;
      max_rot=max;
      x_coord=x;
      y_coord=y;
    }
};


#endif /* KATAMINO_H */
