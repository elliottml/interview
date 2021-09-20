/*The Parallel Hello World Program*/
/*Lori Pollock*/
/*eecis.udel.edu/~pollock/367/manual/node18.html*/

#include <stdio.h>
#include <mpi.h>

main(int argc, char **argv)
{
   int node;
   
   MPI_Init(&argc,&argv);
   MPI_Comm_rank(MPI_COMM_WORLD, &node);
     
   printf("Hello World from Node %d\n",node);
            
   MPI_Finalize();
}