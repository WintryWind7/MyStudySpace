#include <stdio.h>

double Distance(double velocity, double accelerate, double time);

int main()
{
    double v0, a, t, s;
    scanf("%lg%lg%lg", &v0, &a, &t);
    s = Distance(v0, a, t);
    printf("%.4f\n", s);
    return 0;
}

double Distance(double velocity, double accelerate, double time)
{
    double distance;
    distance = velocity*time+accelerate*time*time/2;
    return distance;
}