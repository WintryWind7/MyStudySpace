int sumDigits(int a, int b){
    if ((a<0) || (b<0)){
        return -1;
    }else{
        int c = a+b, sum=0, num=c;
        while (num!=0){
            sum += num%10;
            num /= 10;
        }
    return sum;
    }
}