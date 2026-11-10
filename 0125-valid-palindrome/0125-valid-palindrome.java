class Solution {
    public boolean isPalindrome(String s) {
        String s1="";
        for (int i=0;i<s.length();i++){
            if (Character.isLetterOrDigit(s.charAt(i))){
                s1+=s.charAt(i);
            }
        }
        s1=s1.toLowerCase();
        String s2="";
        for (int i=s1.length()-1;i>=0;i--){
            s2+=s1.charAt(i);
        }
        if(s1.equals(s2)){
            return true;
        }
        return false;
        

    }
}