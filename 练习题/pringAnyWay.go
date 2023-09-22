package main

import "fmt"

func main() {
	m, n := 7, 5
	myVec := make([][]int, m)
	for i := 0; i < m; i++ {
		lis := []int{}
		for j := 0; j < n; j++ {
			lis = append(lis, i*j)
		}
		// myVec[i] = []int{i * 1, i * 2, i * 3, i * 4, i * 5}
		myVec[i] = lis
	}
	fmt.Println(myVec)

	// 打印上三角，延斜边打印
	s := "hello"
	for length := 1; length <= len(s)-1; length++ {
		for start := 0; start < len(s)-length; start++ {
			end := start + length
			fmt.Print(start, end)
		}
	}

}
