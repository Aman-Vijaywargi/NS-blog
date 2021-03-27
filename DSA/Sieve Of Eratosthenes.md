## Kth Prime Factor of N
```java
static int kth_PrimeFactor(int N, int K)
{  int count=1; 
   while(N%2==0){
        if(count++ == K){
            return 2;
        }
         N = N/2;
   }
   
   for(int i=3; i<=Math.sqrt(N); i+=2){
       while(N%i==0){
            if(count++ == K){
                return i;
            }
            N/=i; 
       }
   }
   if(N>2){
       if(count++ == K){
           return N;
       }
   }
   return -1;
}
