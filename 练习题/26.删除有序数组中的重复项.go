package main

import "fmt"

func removeDuplicates(nums []int) int {
	left, right := 0, 0
	for right <= len(nums)-1 {
		if nums[right] == nums[left] {
			right += 1
		} else {
			left += 1
			nums[left] = nums[right]
			right += 1
		}
	}
	return left + 1
}

func main() {
	nums := []int{1, 1, 2}
	res := removeDuplicates(nums)
	fmt.Println(res)
}
