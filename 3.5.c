#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
        int a=1;
        int isprime=0;
        int p[2];
        pipe(p);

        int pid = fork();
        if(pid < 0)
                exit(1);
        if(pid == 0)
        {
                close(p[1]);
                read(p[0],&a,sizeof(int));
                isprime = 1;
                for(int i=2;i*i<=a;i++)
                        if(a%i==0)
                                isprime = 0;
                if(isprime == 1)
                        printf("%d is prime",a);
                close(p[0]);
        }
        else
        {
                close(p[0]);
                while(a!=0){
                        printf("a=");
                        scanf("%d",&a);
                        write(p[1],&a,sizeof(int));
                }
                wait(0);
                close(p[1]);

        }

        return 0;
}
