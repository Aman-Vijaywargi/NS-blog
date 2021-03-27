#                                                                 1D ARRAYS

# Array Rotation

# Given an array of N elements and an integer D. Your task is to rotate the array D times in a circular manner from the right to left direction. Consider the examples for better understanding:-
# Try to do without creating another array
# Input
# User task:
# Since this will be a functional problem, you don't have to take input. You just have to complete the functions rotate() that takes the array, size of the array, and the integer d as a parameter.

# Constraints:
# 1 <= T <= 25
# 2 <= N <= 10^4
# 1<=D<=10^5
# 1 <= A[i] <= 10^5
# Output
# For each test case, you just need to rotate the array by D times. The driver code will prin the rotated array in a new line.

#Hint:
# Try to do this with substrings

#Code: Java

# public static void rotate(int arr[], int n, int d){

#     if (d == 0) 
#             return; 
  
#         int j = arr.length; 
#         d = d % n; 
        
#         reverseArray(arr, 0, d - 1); 
#         reverseArray(arr, d, n - 1); 
#         reverseArray(arr, 0, n - 1); 
#     } 
  
    
#     static void reverseArray(int arr[], int start, int end) 
#     { 
#         int temp; 
#         while (start < end) { 
#             temp = arr[start]; 
#             arr[start] = arr[end]; 
#             arr[end] = temp; 
#             start++; 
#             end--; 
#         } 
#     } 
  
 
#     static void printArray(int arr[]) 
#     { 
#         for (int i = 0; i < arr.length; i++) 
#             System.out.print(arr[i] + " "); 
#     }

# Find unique

# standard input/output: 2s/128000 kB

# Given an array of N elements. In the array, each element is present twice except for 1 element whose frequency in the array is 1. Hence the length of the array will always be odd.
# Find the unique number.
# Input
# An integer, N, representing the size of the array. In the next line, N space-separated integers follow.

# Constraints:
# 1 <= N <=105
# 1 <= A[i] <=108
# Output
# Output the element with frequency 1.

#Hint: Try it with XOR or you could also use a hashmap/dictionary to have counts 
#code:
n = int(input())

inp = list(map(int,input().split()))

res = inp[0] 
for i in range(1,n): 
    res = res ^ inp[i] 
    
print(res)


# Is palindrome?

# standard input/output: 2s/128000 kB

# Check if the given string is a palindrome or not?
# Palindromes are a numbers, phrases or words that reads same both the ways, backward as well as forward. For example, 1331 is a palindrome because on reversing the digits the number remains the same. But 123 is not a palindrome, as on reversing the digits it becomes 321. So given a number n you have to output whether the number is a palindrome or not.
# Print 1 if True and 0 if false.
# Input
# input contains a single string s.

# Constraints:-
# 1<=|s|<=100000

# Note:- String will only contains characters from '0' to '9'.
# Output
# 1 or 0. where 1 means the number is palindrome and zero indicates it's not.

#Hint: if original_string=reverse_string then it's a palindrome. numbers can be converted to strings. 
#Code:
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

# Pattern making (debugging)

# standard input/output: 2s/128000 kB

# Given an integer n, your task is to print the pattern as shown in example:-
# For n=5, the pattern is:
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 2 1
# 1 2 1
# 1
# Input
# User Task:
# Since this will be a functional problem, you don't have to take input. You just have to complete the function pattern_making() that takes the integer n as parameter.

# Constraints:-
# 1 <= n <= 100
# Output
# Print the pattern as shown.

#Code:
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
# Mohit and array

# standard input/output: 2s/128000 kB

# Mohit has an array of N integers containing all elements from 1 to N, somehow he lost one element from the array.
# Given N-1 elements your task is to find the missing one.
# Input
# First line of input contains a single integer N, the next line contains N-1 space separated integers.

# Constraints:-
# 1 < = N < = 1000
# 1 < = elements < = N
# Output
# Print the missing element

#Hint: sum of n natural numbers and 1 number is missing, how would u find it?
#Code:
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

# Buildings

# standard input/output: 1s/128000 kB

# There are N buildings in a row with different heights(H[i]).
# You are viewing the buildings from the left and can see the roof of a building, if no building to the left of that building has height greater than equal to height of that building.
# You are asked the number of buildings whose roofs you can see.
# Input
# The first line contains N denoting number of buildings.
# The next line contains N space seperated integers denoting heights of the buildings from left to right.


# Constraints
# 1 <= N <= 100000
# 1 <= H[i] <= 1000000000000000
# Output
# The output should contain one integer which is the number of buildings whose roofs you can see.

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

# 2D ARRAYS

# Good cells

# standard input/output: 2s/128000 kB

# Given a boolean Matrix of size N*M, A cell of the matrix is called "Good" if it is completely surrounded by the cells containing '1' i.e. each adjacent cell (which shares a common edge) contains '1'. Your task is to find the number of such cells.

# See the below example for a better understanding
# Input
# First line of input contains two space- separated integers N and M. Next N lines of input contain M space- separated integers depicting the values of the matrix.

# Constraints:-
# 3 <= N, M <= 500
# 0 <= Matrix[][] <= 1
# Output
# Print the number of good cells.

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

# Alternate Matrix Addition

# standard input/output: 2s/128000 kB

# You are given a chessboard of size N x N, where the top left square is black. Each square contains a value. Find the sum of values of all black square and all white squares.

# Remember that in a chessboard black and white squares alternate.
# Input
# The first line of input will be the N size of the matrix. Then next N lines will consist of elements of the matrix. Each row will contain N elements since it is a square matrix.

# Constraints:-
# 1 <= N <= 800
# 1 <= Matrix[i][j] <= 100000
# Output
# Print two lines, first line containing the sum of black squares and second line containing the sum of white squares.

#code: c++

#include <bits/stdc++.h> // header file includes every Standard library
# using namespace std;

# int main() {
#     	int n;
#         cin>>n;
#         long black = 0, white = 0;
#         for (int i = 0; i < n; i++) {
#             for (int j = 0; j < n; j++) {
#                 long x;
#                 cin>>x;
#                 if ((i + j) % 2 == 0) {
#                     black += x;
#                 } else {
#                     white += x;
#                 }
#             }
#         }
#         cout<<black<<"\n"<<white;
# 	return 0;

# }

# Simple-Transpose

# standard input/output: 2s/128000 kB

# You are given a NXN matrix. You need to find the transpose of the matrix.
# The matrix is of form:
# a b c ...
# d e f ...
# g h i ...
# ...........
# There are N elements in each row.
# Input
# The first line of the input contains an integer N denoting the size of the square matrix.
# The next N lines contain N single-spaced integers.

# Constraints
# 1 <= N <= 100
# 1 <=Ai <= 100000
# Output
# Output the transpose of the matrix in similar format as that of the input.

#Code: Java

# import java.io.*; // for handling input/output
# import java.util.*; // contains Collections framework

# // don't change the name of this class
# // you can add inner classes if needed
# class Main {
# 	public static void main (String[] args) {
#                       Scanner sc = new Scanner(System.in);
# 					  int[][] arr = new int[1000][1000];
# 					  int n = sc.nextInt();
# 					  for(int i=0;i<n;i++){
# 						  for(int j=0;j<n;j++){
# 							  arr[i][j] = sc.nextInt();
# 						  }
# 					}
# 					int temp = 0;
# 					for(int i=0;i<n;i++){
# 						for(int j=0;j<n;j++){
# 							if (i<j){
# 								temp= arr[i][j]; // 8
# 								arr[i][j] = arr[j][i]; // 7
# 								arr[j][i] = temp; // 8
# 							}
# 						}
# 					}
# 					 for(int i=0;i<n;i++){
# 						  for(int j=0;j<n;j++){
# 							  System.out.print(arr[i][j] + " ");
# 						  }
# 						  System.out.println();
# 					 }
						  

# 	}
# }

# A Boolean Matrix Problem

# standard input/output: 2s/128000 kB

# You are given a matrix Mat of m rows and n columns. The matrix is boolean so the elements of the matrix can only be either 0 or 1.
# Now, if any row of the matrix contains a 1, then you need to fill that whole row with 1. After doing the mentioned operation, you need to print the modified matrix.
# Input
# The first line of input contains T denoting the number of testcases. T testcases follow.
# The first line of each testcase contains m and n denoting number of rows and number of columns.
# Then next m lines contain n elements denoting the elements of the matrix.

# Constraints:
# 1 <= T <= 20
# 1 <= m, n <= 700
# Mat[I][j] ∈ {0,1}
# Output
# For each testcase, in a new line, print the modified matrix.

#code: java
	# import java.io.*; // for handling input/output
	# import java.util.*; // contains Collections framework

	# // don't change the name of this class
	# // you can add inner classes if needed
	# class Main {
	# 	public static void main (String[] args) throws IOException {
	# 					// Your code here
		
	# 		BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
	# 		int test = Integer.parseInt(rd.readLine());

	# 		while(test-- > 0){
	# 			String[] rowcol = rd.readLine().split(" ");
	# 			int rows = Integer.parseInt(rowcol[0]);
	# 			int cols = Integer.parseInt(rowcol[1]);

	# 			int[][]arr = new int[rows][cols];
	# 			for(int r=0; r<rows; r++){
	# 				String[] rowStr = rd.readLine().split(" ");
	# 				for(int c=0; c<cols; c++){
	# 					arr[r][c] = Integer.parseInt(rowStr[c]);
	# 				}
	# 			}

	# 			for(int r=0; r<rows; r++){
	# 				for(int c=0; c<cols; c++){
	# 					if(arr[r][c] == 1){
	# 						arr[r][0] = 1;
	# 						break;
	# 					}
	# 				}
	# 			}

	# 			for(int r=0; r<rows; r++){
	# 				if(arr[r][0] == 1){
	# 					for(int c=0; c<cols; c++){
	# 						arr[r][c] = 1;
	# 					}
	# 				}
	# 			}

	# 			for(int r=0; r<rows; r++){
	# 				for(int c=0; c<cols; c++){
	# 					System.out.print(arr[r][c] +" ");
	# 				}
	# 				System.out.println();
	# 			}

	# 		}
	# 	}
	# }

# Transpose of a matrix
#code : java
#  import java.io.*; // for handling input/output
# import java.util.*; // contains Collections framework

# // don't change the name of this class
# // you can add inner classes if needed
# class Main {
# 	public static void main (String[] args) {
#                       Scanner sc = new Scanner(System.in);
					  
# 					  int n = sc.nextInt();
# 					  int [][]arr = new int[n][n];
# 					  for(int i=0;i<n;i++){
# 						  for(int j=0;j<n;j++){
# 							arr[i][j] = i+j;
# 						  }
# 					  }
# 					  for(int i=0;i<n;i++){
# 						  for(int j=0;j<n;j++){
# 							System.out.print(arr[i][j]+ " ");
# 						  }
# 						  System.out.println();
# 					  }

# 	}
# }

# Boundary Traversal of Matrix
#code: Java
# import java.io.*; // for handling input/output
# import java.util.*; // contains Collections framework

# // don't change the name of this class
# // you can add inner classes if needed
# class Main {
#     public static void main(String[] args)throws IOException {
        
#         // Your code here
#         Scanner in = new Scanner(System.in);
#         int t = in.nextInt();
#         for (int k = 0; k < t; k++) {
#             int m = in.nextInt();
#             int n = in.nextInt();
#             int[][] arr = new int[m][n];
#             for (int i = 0; i < m; i++) {
#                 for (int j = 0; j < n; j++) {
#                     arr[i][j] = in.nextInt();
#                 }
#             }
#             if (m == 1) {
#                 for (int i = 0; i < n; i++) {
#                     System.out.print(arr[0][i] + " ");
#                 }
#             } else if (n == 1) {
#                 for (int j = 0; j < m; j++) {
#                     System.out.print(arr[j][0] + " ");
#                 }
#             } else {
#                 for (int j = 0; j < n; j++) {
#                     System.out.print(arr[0][j] + " ");
#                 }
#                 for (int i = 1; i < m - 1; i++) {
#                     System.out.print(arr[i][n - 1] + " ");
#                 }
#                 for (int j = n; j > 0; j--) {
#                     System.out.print(arr[m - 1][j - 1] + " ");
#                 }
#                 for (int i = m - 1; i > 1; i--) {
#                     System.out.print(arr[i - 1][0] + " ");
#                 }
#             }
#             System.out.println();
#         }
#     }
# }
# Print the Matrix
n=int(input())
a=[]
for i in range(n):
	x=str(input())
	a.append(x)
for j in a:
	print(j)
#Diagonal Sum
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

