class Solution {
    public boolean isPalindrome(String s) {
        
        int front = 0;
        int back = s.length()-1;
        while (front < back) {
            char front_char = Character.toLowerCase(s.charAt(front));
            char back_char = Character.toLowerCase(s.charAt(back));
            if (!Character.isLetterOrDigit(front_char)) {
                front++;
                continue;
            }
            if (!Character.isLetterOrDigit(back_char)) {
                back--;
                continue;
            }

            if (front_char != back_char) {
                return false;
            }
            front++;
            back--;
        }

        return true;
    }
}
