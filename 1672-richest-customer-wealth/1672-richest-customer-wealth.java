class Solution {
    public int maximumWealth(int[][] accounts) {
        int count=-1;
        int p=0;
        for(int i=0;i<accounts.length;i++){
            int[] x=accounts[i];
            for (int j=0;j<x.length;j++){
                p+=x[j];
            }
            if (p>count){
                count=p;
            }
            p=0;
        }
        return count;
    }
}