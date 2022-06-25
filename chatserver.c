#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <linux/if.h>
#include <time.h>
#include <stdlib.h>


#define MAX 1000

void func(int sockfd)
{
    char buff[MAX];
    int n;

    for (;;)
    {
        bzero(buff, MAX);
        bzero(buff, sizeof(buff));
        printf("\n==Welcome to BorakRoom. You may start chat==");
        read(sockfd, buff, sizeof(buff));
        printf("Client Name                     : %s\n", getlogin());
        printf("Message from client             : %s", buff);
        printf("Enter message to client         : ");
        n = 0;
        bzero(buff, MAX);
        while ((buff[n++] = getchar()) != '\n');
        if (strncmp("exit", buff, 4) == 0)
        {
             printf("\nServer Exit...\n\n");
             break;
        }
        write(sockfd, buff, sizeof(buff));
    }
    n = 0;
}

int main()
{
    int sockfd, connfd, len;
    struct ifreq ifr;
    struct sockaddr_in server, client;
    char array[] = "enp0s8";

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        puts("Socket creation failed...\n");
        exit(0);
    }
    else{
        printf("\nSocket successfully created...\n");
        bzero(&server, sizeof(server));
    }

    server.sin_family = AF_INET;
    server.sin_addr.s_addr = htonl(INADDR_ANY);
	server.sin_port = htons(123);

    if ((bind(sockfd, (struct sockaddr*)&server, sizeof(server))) != 0) {
        puts("Socket bind failed...\n");
        exit(0);
    }
    else
        printf("Socket successfully binded...\n");


    if ((listen(sockfd, 5)) != 0) {
        puts("Listen failed...\n");
        exit(0);
    }
    else{
        printf("Server is listening...\n");
        len = sizeof(client);
    }

    connfd = accept(sockfd, (struct sockaddr*)&client, &len);
    if (connfd < 0) {
        puts("Server accept failed...\n");
        exit(0);
    }
    else{
        printf("Server accept the client...\n");
        printf("\nThis is BorakRoom server...\n");
        printf("Waiting message from client...\n");
    }
	func(connfd);
    close(sockfd);
}

