class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        ArrayList<List<Integer>> triplets = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            int front = i + 1;
            int back = nums.length - 1;

            while (front < back) {
                if (nums[i] + nums[front] + nums[back] > 0) {
                    back--;
                    continue;
                }
                if (nums[i] + nums[front] + nums[back] < 0) {
                    front++;
                    continue;
                }
                if (nums[i] + nums[front] + nums[back] == 0) {
                    triplets.add(List.of(nums[front], nums[i], nums[back]));
                    front++;
                    back--;
                    while (front < back && nums[front] == nums[front-1]) {
                        front++;
                        continue;
                    }
                    while (front < back && nums[back] == nums[back+1]) {
                        back--;
                        continue;
                    }
                } 
            }
        }
        return triplets;
    }
}
