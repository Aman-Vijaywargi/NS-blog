#                                                                 1D ARRAYS

## Array Rotation


### Hint: Try to do this with substrings

```Java

public static void rotate(int arr[], int n, int d){

    if (d == 0) 
            return; 
  
        int j = arr.length; 
        d = d % n; 
        
        reverseArray(arr, 0, d - 1); 
        reverseArray(arr, d, n - 1); 
        reverseArray(arr, 0, n - 1); 
    } 
  
    
    static void reverseArray(int arr[], int start, int end) 
    { 
        int temp; 
        while (start < end) { 
            temp = arr[start]; 
            arr[start] = arr[end]; 
            arr[end] = temp; 
            start++; 
            end--; 
        } 
    } 
  
 
    static void printArray(int arr[]) 
    { 
        for (int i = 0; i < arr.length; i++) 
            System.out.print(arr[i] + " "); 
    }
```

## Find unique

### Hint: Try it with XOR or you could also use a hashmap/dictionary to have counts 

```python
n = int(input())

inp = list(map(int,input().split()))

res = inp[0] 
for i in range(1,n): 
    res = res ^ inp[i] 
    
print(res)
```


# Is palindrome?

### Hint: if original_string=reverse_string then it's a palindrome. numbers can be converted to strings. 
```python
n = str(input())
j = len(n)
boolean = 1
for i in range(int(len(n)/2)):
    if n[i]!=n[j-1]:
        boolean = 0
        break
    j=j-1
if boolean==0:
    print("0")
else:
    print("1")
```

## Pattern making (debugging)

```python
def pattern_making(n): 
    a_min=[]
    a_fin=[]
    a_rev=[]

    rows=n+1
    for i in range(1, rows + 1):

        for j in range(1, i - 1):
            a_min.append(str(j)+" ")

        for z in range(i -1, 0, -1):
            a_min.append(str(z)+" ")

        a_fin.append(a_min)
        a_min=[]
    for i in range(n):
        while n>1:
            a_rev.append(a_fin[n-1])
            n=n-1

    for i in range(1,len(a_fin)):
        for j in a_fin[i]:
            print(j,end='')
        print()

    for x in range(len(a_rev)):
        for y in a_rev[x]:
            print(y,end='')
        print() 
```   
## Mohit and array

### Hint: sum of n natural numbers and 1 number is missing, how would u find it?
```python
n = int(input())
inp = list(map(int,input().split()))
l = []
inp.sort()

j=1
for i in range(1,n+1):
	l.append(i)

for ele in range(1,len(l)+1):
	if ele not in inp:
		print(ele)
		break
```

## Buildings

```python
def countBuildings(arr, n): 
	count = 1
	curr_max = arr[0] 
	for i in range(1, n): 
		if (arr[i] > curr_max): 
			count += 1
			curr_max = arr[i] 
	return count 
a = int(input())
arr = list(map(int,input().split()))
n = len(arr) 
print(countBuildings(arr, n))
```

# 2D ARRAYS

## Good cells
```python

column,row=map(int,input().split())
a=[]
s=0
for z in range(column):
	a.append(list(map(int,input().split())))
for i in range(1,len(a)):
	for j in range(1,len(a[i])):
		#print(a[i][j])
		try:
			if a[i+1][j]==1 and a[i-1][j]==1 and a[i][j+1]==1 and a[i][j-1]==1:
				s+=1
		except:
			continue
print(s)
```

## Alternate Matrix Addition
```c++

include <bits/stdc++.h> // header file includes every Standard library
using namespace std;

int main() {
    	int n;
        cin>>n;
        long black = 0, white = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                long x;
                cin>>x;
                if ((i + j) % 2 == 0) {
                    black += x;
                } else {
                    white += x;
                }
            }
        }
        cout<<black<<"\n"<<white;
	return 0;

}
```

## Simple-Transpose
```Java

import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
	public static void main (String[] args) {
                      Scanner sc = new Scanner(System.in);
					  int[][] arr = new int[1000][1000];
					  int n = sc.nextInt();
					  for(int i=0;i<n;i++){
						  for(int j=0;j<n;j++){
							  arr[i][j] = sc.nextInt();
						  }
					}
					int temp = 0;
					for(int i=0;i<n;i++){
						for(int j=0;j<n;j++){
							if (i<j){
								temp= arr[i][j]; // 8
								arr[i][j] = arr[j][i]; // 7
								arr[j][i] = temp; // 8
							}
						}
					}
					 for(int i=0;i<n;i++){
						  for(int j=0;j<n;j++){
							  System.out.print(arr[i][j] + " ");
						  }
						  System.out.println();
					 }
						  

	}
}
```
## A Boolean Matrix Problem

```java
	import java.io.*; // for handling input/output
	import java.util.*; // contains Collections framework

	// don't change the name of this class
	// you can add inner classes if needed
	class Main {
		public static void main (String[] args) throws IOException {
						// Your code here
		
			BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
			int test = Integer.parseInt(rd.readLine());

			while(test-- > 0){
				String[] rowcol = rd.readLine().split(" ");
				int rows = Integer.parseInt(rowcol[0]);
				int cols = Integer.parseInt(rowcol[1]);

				int[][]arr = new int[rows][cols];
				for(int r=0; r<rows; r++){
					String[] rowStr = rd.readLine().split(" ");
					for(int c=0; c<cols; c++){
						arr[r][c] = Integer.parseInt(rowStr[c]);
					}
				}

				for(int r=0; r<rows; r++){
					for(int c=0; c<cols; c++){
						if(arr[r][c] == 1){
							arr[r][0] = 1;
							break;
						}
					}
				}

				for(int r=0; r<rows; r++){
					if(arr[r][0] == 1){
						for(int c=0; c<cols; c++){
							arr[r][c] = 1;
						}
					}
				}

				for(int r=0; r<rows; r++){
					for(int c=0; c<cols; c++){
						System.out.print(arr[r][c] +" ");
					}
					System.out.println();
				}

			}
		}
	}
```

## Transpose of a matrix
```java
 import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
	public static void main (String[] args) {
                      Scanner sc = new Scanner(System.in);
					  
					  int n = sc.nextInt();
					  int [][]arr = new int[n][n];
					  for(int i=0;i<n;i++){
						  for(int j=0;j<n;j++){
							arr[i][j] = i+j;
						  }
					  }
					  for(int i=0;i<n;i++){
						  for(int j=0;j<n;j++){
							System.out.print(arr[i][j]+ " ");
						  }
						  System.out.println();
					  }

	}
}
```

## Boundary Traversal of Matrix
```Java
import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static void main(String[] args)throws IOException {
        
        // Your code here
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int k = 0; k < t; k++) {
            int m = in.nextInt();
            int n = in.nextInt();
            int[][] arr = new int[m][n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    arr[i][j] = in.nextInt();
                }
            }
            if (m == 1) {
                for (int i = 0; i < n; i++) {
                    System.out.print(arr[0][i] + " ");
                }
            } else if (n == 1) {
                for (int j = 0; j < m; j++) {
                    System.out.print(arr[j][0] + " ");
                }
            } else {
                for (int j = 0; j < n; j++) {
                    System.out.print(arr[0][j] + " ");
                }
                for (int i = 1; i < m - 1; i++) {
                    System.out.print(arr[i][n - 1] + " ");
                }
                for (int j = n; j > 0; j--) {
                    System.out.print(arr[m - 1][j - 1] + " ");
                }
                for (int i = m - 1; i > 1; i--) {
                    System.out.print(arr[i - 1][0] + " ");
                }
            }
            System.out.println();
        }
    }
}
```
## Print the Matrix
```python
n=int(input())
a=[]
for i in range(n):
	x=str(input())
	a.append(x)
for j in a:
	print(j)
```
## Diagonal Sum
```python
MAX = 100

def printDiagonalSums(mat, n): 

	principal = 0
	secondary = 0
	for i in range(0, n): 
		for j in range(0, n): 
			if (i == j): 
				principal += mat[i][j] 
			if ((i + j) == (n - 1)): 
				secondary += mat[i][j] 
		
	print(principal,secondary) 

n=int(input())	
a=[]
for i in range(n):
	a.append(list(map(int,input().split())))

printDiagonalSums(a, n)
```

