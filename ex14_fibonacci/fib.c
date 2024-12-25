#include <stdio.h>

static int fibonacci_calls;

int fibonacci_number(int n) {
   fibonacci_calls++;
   if (n == 0)
      return 0;
   if (n == 1)
      return 1;
    
    return fibonacci_number(n - 1) + fibonacci_number(n - 2);
}

int main()
{
    printf("%d\n", fibonacci_number(6));
    printf("%d\n", fibonacci_calls);
}

