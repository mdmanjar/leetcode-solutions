class Solution {
  public int[] sortArray(int[] nums) {
    int mx = 0;
    for (var e : nums)
      mx = Math.max(mx, Math.abs(e)); // Use Math.max
      
    for (int i = 1; i <= mx; i *= 10)
      sort(nums, i);
      
    int neg = 0;
    for (var e : nums)
      if (e < 0)
        neg++;
        
    if (neg == 0)
      return nums;
      
    var ans = new int[nums.length];
    int left = 0;      // Negatives go from 0 to neg - 1
    int right = neg;   // Non-negatives go from neg to nums.length - 1
    
    // Iterate backwards so larger magnitudes (more negative) go to the front
    for (int i = nums.length - 1; i >= 0; i--) {
      if (nums[i] < 0) {
        ans[left++] = nums[i];
      }
    }
    
    // Iterate forwards for non-negative numbers to preserve their sorted order
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] >= 0) {
        ans[right++] = nums[i];
      }
    }

    return ans; // Return ans, not nums
  }

  void sort(int[] nums, int idx) {
    var count = new int[10];
    for (var e : nums)
      count[(Math.abs(e) / idx) % 10]++;

    for (int i = 1; i < 10; i++)
      count[i] += count[i - 1];

    var temp = new int[nums.length];
    for (int i = nums.length - 1; i >= 0; i--) {
      var e = nums[i];
      temp[count[(Math.abs(e) / idx) % 10] - 1] = e;
      count[(Math.abs(e) / idx) % 10]--;
    }
    System.arraycopy(temp, 0, nums, 0, nums.length);
  }
}