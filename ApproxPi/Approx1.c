#include <stdio.h>
#include <stdlib.h>
#include <time.h>

clock_t begin, end;
int sum;
int MAX_steps = 1000000;
int main()
{
   begin = clock();
   for(int n=0; n<1000;n++){
        for(int i=0;i<MAX_steps;i++)
        {
            double x = drand48();
            double y = drand48();
            if (x*x + y*y < 1.0)
            {
                sum += 1;
            }
        }
        double estimate = 4.0 * sum / MAX_steps;
        printf("Approximierung: %f \n", estimate);
        sum = 0;

    }
end = clock();
//printf("Ticks fuer 100 Zyklen:	 %d \n", end-begin);
//printf("Bzw in Sekunden:         %f\n", ((end-begin)/CLOCKS_PER_SEC));
return 0;

}
