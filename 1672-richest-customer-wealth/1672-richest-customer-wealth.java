class Solution {
    public int maximumWealth(int[][] accounts) {
        int count=-1;
        for(int i=0;i<accounts.length;i++){
            int p=0;
            for (int j=0;j<accounts[i].length;j++){
                p+=accounts[i][j];
            }
            if (p>count){
                count=p;
            }
        }
        return count;
    }
}