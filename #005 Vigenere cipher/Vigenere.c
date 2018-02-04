#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
    char str[256];
    char key[256];
    printf("Plaintext: ");
    fgets(str, 256, stdin);
    printf("Key: ");
    scanf("%s", &key);
    int size = 0;
    for(int i=0; key[i] != '\0';i++){
        size++;
    }

    for(int i=0; str[i] != '\0'; i++){
        char shiftByKey;
        if(isalpha(str[i])){
            shiftByKey = key[i%size];
            if(isupper(shiftByKey)){
            shiftByKey = shiftByKey-65;
            }
            else if(islower(shiftByKey)){
                shiftByKey = shiftByKey-97;
            }
        }

        if(isupper(str[i])){
            str[i] = (char) ((((int) (str[i] - 65 + shiftByKey)) % 26) + 65);
        }
        else if(islower(str[i])){
            str[i] = (char) ((((int) (str[i] - 97 + shiftByKey)) % 26) + 97);
        }
    }

    printf("%s", str);
    return 0;
}