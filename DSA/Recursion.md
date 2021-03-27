# recursion!
## Fibonacci Numbers

```java 
static long  Fibonacci(long  n) 
    { 
      // 0 1 1 2 3 5 8 13
     if(n==1){
       return 1;
     }
     if(n==0){
       return 0;
     }
     else {
       return Fibonacci(n-1)+ Fibonacci(n-2);
     }
  }
```
## Sum of digits
```java
static long  Sum(long  n) 
    { 
    if(n==0){
      return n;
    }
    long remainder = n%10;
    n=n/10;
    return remainder + Sum(n);
    
  }
```
## Multiplication
``` java
static int  Multiply_by_recursion(int M, int N) 
    {
      int sum = 0;
      if(N == 1){
        return M;
      }else if(N == 0)
        return 0;
      else{
        sum = sum + M + Multiply_by_recursion(M, N-1);
        
        return sum;
      }
    }
```
## Print Pattern
```java
static void printPattern(int n,int curr, boolean flag)
{
    if(curr<=0){
    System.out.print(curr + " ");
    return;
    }
    System.out.print(curr+ " ");
    printPattern(n,curr-5,flag);
    System.out.print(curr +" ");
}
```
## Sum of Product of Digits of a given number
```java
public static int sumOfProductOfDigits(int n1, int n2)
{
     if(n1==0 || n2==0){
    return 0;
}          
        int remainder =  (n2%10)*(n1%10);
        return remainder + sumOfProductOfDigits(n1/10,n2/10);
        
}
```
## Tower of Hanoi
``` java
import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
public static void towerOfHanoi(int disks,String a ,String b ,String c){
	if(disks==0){
		return;
	}
	towerOfHanoi(disks-1,a,c,b);

	System.out.println(disks + ":" + a + "->" + c);

	towerOfHanoi(disks-1,b,a,c);


	

}
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		towerOfHanoi(n,"A","B","C");

	}
}
```
## Number of ways
```java
import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
	static int recur(int sum ,int start, int currSum){
		if (currSum==sum){
			return 1;
		}

		else if( currSum>sum){
			return 0;
		}
		int res = 0;
		for(int i = start ; i<=sum-currSum;i++){
			res += recur(sum, i+1,currSum+i);
		}
		return res;

		

	}
	public static void main (String[] args) {
                      Scanner sc = new Scanner(System.in);
					  int test = sc.nextInt();
					  for(int i=0;i<test;i++){
						  int N = sc.nextInt();
						  int res = recur(N,0,0)/2;
						  System.out.println(res);
						  
					  }
	}
}
```
