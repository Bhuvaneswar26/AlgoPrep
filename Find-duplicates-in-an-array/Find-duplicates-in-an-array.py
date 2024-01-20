class Solution:
    def duplicates(self, arr, n): 
        # code here
        if n==1:
            return [-1]
        arr.sort()
        l1=[]
        i=0
        while(i<=n-2):
            status=False
            if arr[i]==arr[i+1]:
                status=True
                while(arr[i]==arr[i+1]):
                    i+=1
                    if i==n-1:
                        break
            if status:
                l1.append(arr[i])
            i+=1
        if len(l1)==0:
            return [-1]
        else:
            return l1
                
                
            





#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends