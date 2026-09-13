class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let existingNums = [];
        for(let i = 0; i < nums.length; i++ ) {
            if (existingNums.includes(nums[i])) {
                return true;
            }
            else {
                existingNums.push(nums[i])
            }
        }
        return false;
    }
}
