void root(int a, int b, int c){
    double delta,x1,x2;
    delta = b*b-4*a*c;
    if (delta > 0)printf("x1=%.6f,x2=%.6f",(-b+sqrt(delta))/2*a,(-b-sqrt(delta))/2*a);
    else if (delta == 0){
        printf("x1=%.6f,x2=%.6f",-b*1.0/(2*a),-b*1.0/(2*a));
    }else{
        printf("此方程无解");
    }

}