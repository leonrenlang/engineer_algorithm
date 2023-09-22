package main

import "fmt"

func nextGreatestLetter(letters []byte, target byte) byte {

	// 遍历letters， 一一比较，寻找第一个unicode码大于target的
	// 若没有找到，则就是letters中的第一个
	for _, l := range letters {
		if target < l {
			return l
		}
	}
	return letters[0]
}

func main() {
	letters := []byte{'c', 'f', 'j'}
	var target byte = 'a'
	res := nextGreatestLetter(letters, target)
	fmt.Println(string(res))
}
