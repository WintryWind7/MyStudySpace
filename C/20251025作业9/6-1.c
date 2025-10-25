#include<stdio.h>

double m_tax(double salary,int month);

int main()
{
    double money,tax;
    int i;
    for(i=1;i<=12;i++)
    {
        scanf("%lf",&money);
        tax=m_tax(money,i);
        printf("the sum of %d months tax is %.2f\n",i,tax);
    }
    return 0;
}

double m_tax(double salary, int month) {
    static double total_salary = 0;
    total_salary += salary;
    
    double tax_free = 5000.0 * month;
    
    double taxable_income = total_salary - tax_free;
    
    if (taxable_income <= 0) {
        return 0.0;
    }
    
    double tax = 0.0;
    
    if (taxable_income <= 36000) {
        tax = taxable_income * 0.03;
    } else if (taxable_income <= 144000) {
        tax = 36000 * 0.03 + (taxable_income - 36000) * 0.10;
    } else if (taxable_income <= 300000) {
        tax = 36000 * 0.03 + 108000 * 0.10 + (taxable_income - 144000) * 0.20;
    } else if (taxable_income <= 420000) {
        tax = 36000 * 0.03 + 108000 * 0.10 + 156000 * 0.20 + (taxable_income - 300000) * 0.25;
    } else if (taxable_income <= 660000) {
        tax = 36000 * 0.03 + 108000 * 0.10 + 156000 * 0.20 + 120000 * 0.25 + (taxable_income - 420000) * 0.30;
    } else if (taxable_income <= 960000) {
        tax = 36000 * 0.03 + 108000 * 0.10 + 156000 * 0.20 + 120000 * 0.25 + 240000 * 0.30 + (taxable_income - 660000) * 0.35;
    } else {
        tax = 36000 * 0.03 + 108000 * 0.10 + 156000 * 0.20 + 120000 * 0.25 + 240000 * 0.30 + 300000 * 0.35 + (taxable_income - 960000) * 0.45;
    }
    
    return tax;
}

