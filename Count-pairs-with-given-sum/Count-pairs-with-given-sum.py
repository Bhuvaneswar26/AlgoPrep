#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        
        d1 = {}
        
        for i in range(n):
            
            try:
                
                d1[arr[i]].append(i)
                
            except:
                
                d1[arr[i]] = [i]
                
        count = 0
            
        for i in range(n):
            
            diff_sum = k-arr[i]
            
            if diff_sum in d1.keys():
                
                for j in d1[diff_sum]:
                    
                    if j>i:
                        
                        count+=1
                        
        return count
            
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends