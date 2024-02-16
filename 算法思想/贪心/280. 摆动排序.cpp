/**
 给你一个的整数数组 nums, 将该数组重新排序后使 nums[0] <= nums[1] >= nums[2] <= nums[3]... 

输入数组总是有一个有效的答案。

 示例 1:

输入：nums = [3,5,2,1,6,4]
输出：[3,5,1,6,2,4]
解释：[1,6,2,5,3,4]也是有效的答案
示例 2:

输入：nums = [6,6,5,6,3,8]
输出：[6,6,5,6,3,8]
*/
#include <clang/stdc++.h>
using namespace std;

class Solution {
public:
    void swap(vector<int>& nums, int idx1, int idx2) {
        int tmp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = tmp;
    }

    void wiggleSort(vector<int>& nums) {
        /*
        
        贪心思想，若当前num和后续数据不满足wiggle结构，则交换
        */
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() -1; i++) {
            if ((i % 2 == 0 && nums[i] > nums[i+1])  
                    || (i % 2 == 1 && nums[i] < nums[i+1])) {
                swap(nums, i, i+1);
            }
        }
    }
};