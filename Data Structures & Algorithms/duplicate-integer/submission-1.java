class Solution {
    public boolean hasDuplicate(int[] nums) {
        int[] visited = new int[nums.length];
        int visitedSize = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < visitedSize; j++) {
                if (nums[i] == visited[j]) {
                    return true;
                }
            }
            visited[i] = nums[i];
            visitedSize++;
        }
        return false;
    }
}