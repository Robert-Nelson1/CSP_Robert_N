// Robert Nelson, Time of Day - C
#include <stdio.h>
#include <time.h>

int main(void){
    // Time since Jan 1 1970
    time_t seconds;

    seconds = time(NULL);
    //printf("Seconds since Jan 1, 1970 = %d", seconds);
    // Current time
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    //printf("Current time and date is %s", asctime(timeinfo));

    //current hour
    time_t now = time(NULL);

    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("%d\n", hour);



    if(hour >=0 && hour <=12){
        printf("Good morning\n");
    }else if (hour >=12 && hour <=17){
        printf("Good evening");
    }else{
        printf("Good evening\n");
    }



    return 0;
}


// #< less than
// #> greater than
// #<= less than or equal to
// #>= greater than or equal to
// #== Equal to
// #=== *Doesn't exist in Python*
// #! Not