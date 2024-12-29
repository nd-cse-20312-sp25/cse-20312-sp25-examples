#include <stdio.h>

int main()
{
    char s[] = "abcde";

    // Keep going while s[i] != 0 (false)
    for (int i = 0;  s[i];  i++) {
        printf("%c", s[i]);
    }
    printf("\n");

    // Keep going while *(s + i) != 0 (false)
    for (int i = 0;  *(s + i);  i++) {
        printf("%c", *(s + i));
    }
    printf("\n");
}