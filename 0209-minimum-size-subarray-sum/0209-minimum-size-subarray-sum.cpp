class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l=0;
        int sum=0;
        int ans=INT_MAX;
        int n=nums.size();
        for(int r=0;r<n;r++){
        sum+=nums[r];

        while(sum>=target){
            ans=min(ans,r-l+1);
            sum=sum-nums[l];
            l++;
            }
           
        
        }

       if(ans>target)
       return 0;
        return ans;
    }
};