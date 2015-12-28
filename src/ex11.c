#include <stdio.h>
#include <string.h>

int is_ok(char const *s) {
    // 2nd requirement (fastest to check)
    if (strstr(s, "i") || strstr(s, "o") || strstr(s, "l"))
        return 0;

    // 3rd requirement
    int nb = 0;
    char double_letters[3];
    double_letters[2] = '\0';
    for(double_letters[0] = 'a',double_letters[1] = 'a'; double_letters[0] <= 'z' && nb < 2; double_letters[0]++, double_letters[1]++) {
        if (strstr(s, double_letters)) {
            nb++;
        }
    }

    if (nb < 2)
        return 0;

    // 1st requirement (longest to check)
    char alphabet['z' - 'a' + 1];
    char a;
    for (a = 'a'; a <= 'z'; a++) {
        alphabet[a - 'a'] = a;
    }

    char subbuff[4];
    int start, b = 0;
    for (start = 0; start <= 'z' - 'a' - 2 && !b; start++) {
        memcpy(subbuff, &alphabet[start], 3);
        subbuff[3] = '\0';
        if (strstr(s, subbuff))
            b = 1;
    }

    if (!b)
        return 0;

    return 1;
}

void incr(char* s) {
    s[strlen(s) - 1]++;

    int b = 0;
    size_t i;
    for (i = strlen(s) - 1; i > 0; i--) {
        if (b) {
            s[i]++;
            b = 0;
        }

        if (s[i] > 'z') {
            s[i] = 'a';
            b = 1;
        }
    }
}

int main(int argc, char const *argv[]) {
    char input[80];

    if (argc == 2)
        strcpy(input, argv[1]);
    else
        strcpy(input, "vzbxkghb");
    printf("Initial input : %s\n", input);

    do {
        incr(input);
    } while (!is_ok(input));
    printf("Final input : %s\n", input);

    return 0;
}
