class Solution {
    public int findNumbers(int[] nums) {
        int count=0;
        for (int i=0;i<nums.length;i++){
            int k=0;
            while(nums[i]!=0){
                nums[i]=nums[i]/10;
                k+=1;
            }
            if (k%2==0){
                count+=1;
            }
        }
        return count;
    }
}