package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {

	hashTable := make(map[int]int)
	for idx, item := range nums {
		if value, ok := hashTable[target-item]; ok {
			return []int{idx, value}
		}
		hashTable[item] = idx
	}
	return nil
}

func main() {
	nums := []int{2, 11, 7, 15}
	target := 9
	res := twoSum(nums, target)
	fmt.Println(res)
}
