import java.util.Arrays;
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int [] a=nums.clone();
        Arrays.sort(a);
        HashMap<Integer, Integer> d= new HashMap<>();
        for (int i=0;i<nums.length;i++){
            if(!d.containsKey(a[i])){
                d.put(a[i],i);
            }
        }
        int [] x=new int[a.length];
        for(int i=0;i<nums.length;i++){
            x[i]=d.get(nums[i]);
        }
        return x;

    }
}