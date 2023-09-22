package main

import (
	"fmt"
	"strconv"
)

func selfDividingNumbers(left int, right int) []int {
	var resArr []int
	for i := left; i <= right; i++ {
		itemStr := strconv.Itoa(i)
		flag := true
		for _, seg := range itemStr {
			segDigit, _ := strconv.Atoi(string(seg))
			if segDigit == 0 {
				flag = false
				break
			}
			if (i % segDigit) != 0 {
				flag = false
				break
			}
		}
		if flag {
			resArr = append(resArr, i)
		}
	}
	return resArr
}

func main() {
	left := 1
	right := 22
	res := selfDividingNumbers(left, right)
	fmt.Println(res)
}
