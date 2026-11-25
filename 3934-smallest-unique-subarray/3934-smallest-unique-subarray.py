class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        l = 1 
        n = len( nums ) 
        
        h = n 
        b = 12334456789
        mod1 = 10**9 + 7 
        mod2 = 10**9+9 
        def helper( k ) : 
            fre = defaultdict ( int ) 
            pow1 = pow( b , k-1  , mod1 ) 
            pow2 = pow ( b , k-1 , mod2 )
            h1 = 0 
            h2 = 0 
            for i in range( k ) : 
                h1 = ( h1* b + nums[i] ) % mod1 
                h2 = ( h2* b + nums[i] ) % mod2 
            fre[( h1, h2 ) ] = 1 
            for i in range( k , n ) : 
                left = nums[i-k] 
                h1 = ( h1- left * pow1 ) % mod1 
                h1 = ( h1* b + nums[i] )%mod1

                h2 = ( h2-left * pow2 ) % mod2 
                h2 = ( h2*b + nums[i] ) %mod2 
                fre[( h1, h2)]+=1 
            for val ,f in fre.items() : 
                if f == 1: 
                    return True 
            return False 
            
        
        ans = n 
        while l <= h : 
            mid = ( l+ h ) //2 
            if helper( mid ) : 
                ans = mid 
                h = mid-1 
            else : 
                l = mid+1 
        return ans