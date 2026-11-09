import java.util.Arrays;
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int m= Arrays.stream(candies).max().getAsInt();
        ArrayList <Boolean> a=new ArrayList<>();
        for (int i=0;i<candies.length;i++){
            if (candies[i]+extraCandies>=m){
                a.add(true);
            }else{
                a.add(false);
            }
        }
        return a;
        
    }
}