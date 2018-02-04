// creditcard validation using Luhns algorithm
#include <stdio.h>
#include <stdlib.h>

int luhnAlgorithm(char creditNumb[]){
    int sum = 0;
    for(int i=0; creditNumb[i]!='\0'; i++){
        int digit = (creditNumb[i] - '0');
        if(i % 2 != 0){
            digit = digit * 2;
            if(digit > 9){
                digit = digit - 9;
            }
        }
        sum+=digit;
    }
    return (sum % 10 == 0);
}

int getSizeOfCharArray(char input[]){
    int length = 0;
    for(int i=0; input[i]!='\0'; i++){
        length++;
    }
    return length;
}

int main(){
    printf("Enter credit card number:\n");
    char input[256];
    int length;
    do{
        scanf("%s", &input);
        length = getSizeOfCharArray(input);
        if(length < 13){
            printf("%s", "length must be at least 13\n");
        }
    }while(length < 13);

    char firstTwoDigit[2];
    firstTwoDigit[0] = input[0];
    firstTwoDigit[1] = input[1];
    char *ptr;
    long res = strtol(firstTwoDigit, &ptr, 10);

    int valid = luhnAlgorithm(input);
    if(valid && length == 15 && (res == 37 || res == 34)){
        printf("AMEX\n");
    }
    else if(valid && length == 16 && (res >= 50 || res <= 55)){
        printf("MASTERCARD\n");
    }
    else if(valid && (length == 16 || length == 13) && (firstTwoDigit[0]-'\0') == 4){
        printf("VISA\n");
    }
    else{
        printf("INVALID\n");
    }

    return 0;
}