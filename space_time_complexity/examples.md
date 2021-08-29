# Space Time Complexity Analysis By Example

##Example 1:

for(int i=0; i <= n-1; i++){
    for(int j = i+!; j <= n -1;j++){
        // Constant work K
    }
}

Time Complexity:
= (n-1)*(n-1)*k 
= n^2k - 2nk + 1k
~= O(n^2)

##Example 2:

for(int i=0; i <= n-1; i++){
    for(int j = i+!; j <= K;j++){
        // Constant work C
    }
}

Time Complexity:
= (n-1)*K*C
= NKC - KC
~= O(n)

##Example 3:

Bubble Sort:

Best Case : O(n) if already sorted 
(make one flag to check if there are any swapped or not, 
if no swapped occur in inner loop then array is already sorted & 
no need to do more steps)
Average Case : O(n^2)
Worst Case: O(n^2)

##Example 4:

Binary Search

recursive function call will like:

1. func(N) = func(M/2^0)
2. func(N/2) = func(N/2^1)
3. func(N/4) = func(N/2^2)
4. func(N/2^K) = 1 // will terminate recursion with array size of 1

=> N/2^k = 1
=> N = 2^k
=> LogN = K
=> K = LogN

Best Case: O(1)
Average Case : O(logN)
Worst Case: O(logN)

##Example 5:

void mergesort(vector<int> &arr, int s, int e){
    if(s>=e){
        return;
    }
    int mid = (s+e)/2;
    mergesort(arr, s, mid); // T(N/2)
    mergesort(arr, mid+1, e); // T(N/2)
    return merge(arr,s,e); // KN
}

T(N) = K + T(N/2) + T(N/2) + KN
= K + 2T(N/2) + KN

T(N/2) = KN/2 + 2T(N/4)

Using Substitution method,

T(N) = (summation from i=1 to LogN) kN 
= KNlogN
= O(NlogN)

##Example 6:

int power(int a, int b){
    if (n == 0){
        return 1;
    }
    return a*power(a, n-1);
}

Explanation:
a^n = a*(a^(n-1))

T(N) = K + T(N-1)
T(N-1) = K + T(N-2)
T(N-2) = K + T(N-3)

T(N) = (summation from i=1 to N) kN
= O(N)

Space Complexity = O(N)// recursion will use stack space

##Example 7:

int power(int a, int n){
    if (n==0){
        return 1;
    }
    int halfPower = power(a, n/2); // T(N/2)
    int halfPowerSquare = halfPower*halfPower; // Constant time K
    
    if(n%2 !=0){
        return a * halfPowerSquare;
    }
    
    return halfPowerSquare;
}

T(N) = T(N/2) + k
T(N/2) = T(N/4) + k
...

Using Substitution method,

T(N) = (summation from i=1 to LogN) k 
= KlogN
= O(logN)

##Example 8:

// Simple recursion
int fib(int n){
    if(n==0 or n==1){
        return n;
    }
    return fib(n-1) + fib(n-2);
}

Time Complexity :
T(N) = calls * each call
= 2^N * K
= O(2^N)

// Simple DP based Optimisation

// Top Down Approach
int fib(int n, vector<int> &dp){
    if(n==0 or n==1){
        return n;
    }
    
    if(dp[n]!=0){
        return dp[n];
    }
    
    return dp[n] = fib(n-1,dp) + fb(n-2,dp);
}

Time complexity :
T(N) = 2N - 1 = O(N)

// Bottom Up Approach
int fib2(int n){
    int dp[n+1] = {0};
    // base case assignment
    dp[0] = 0;
    dp[1] = 1;
    
    // bottom up dp
    for(int i = 2; i <=n ;i++){
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}

Time Complexity:
T(N) = O(N)

## Points:

1. For recursive problem the total time is
   = Number of Calls * work done in each call
2. Space Complexity 
   = max depth of call stack  * extra memory used in each stack frame