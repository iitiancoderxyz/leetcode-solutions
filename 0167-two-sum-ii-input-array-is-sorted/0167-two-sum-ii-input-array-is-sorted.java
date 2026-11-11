class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l=0,r=numbers.length-1;
        int[] x=new int[2];
        while (l<r){
            int s=numbers[l]+numbers[r];
            if(s>target){
                r--;
            }
            else if(s<target){
                l++;
            }
            else{
                break;
            }
        }
        x[0]=l+1;
        x[1]=r+1;
        return x;
    }
}