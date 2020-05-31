package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
func nextIntArray() []int {
	sc.Scan()
	slice := strings.Fields(sc.Text())
	var ns []int
	for _, str := range slice {
		n, e := strconv.Atoi(str)
	    if e != nil {
        	panic(e)
	    }
		ns = append(ns, n)
	}
    return ns
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func manhattan2(toX int,toY int,fromX int,fromY int) int {
	return abs(toX - fromX) + abs(toY - fromY)
}

func f(N int, nums [][]int) bool {
	t,x,y := 0,0,0
	for i := 0; i<N; i++ {
		nextt := nums[i][0]
		nextx := nums[i][1]
		nexty := nums[i][2]
		d := manhattan2(nextx,nexty,x,y)
		if (nextt-t) < d {
			return false
		}
		if (nextt-t) % 2 != d % 2 {
			return false
		}
		t,x,y = nextt,nextx,nexty
	}
	return true
}

func scanNums(length int) (nums [][]int) {
	var s string
    for i := 0; i < length; i++ {
		fmt.Scan(&s)
		fmt.Println(s)
		fmt.Println(strings.Fields(s))
		slice := strings.Fields(s)
		fmt.Println(slice)
		fmt.Println(len(slice))
		var ns []int
		for _, str := range slice {
			n, _ := strconv.Atoi(str)
			ns = append(ns, n)
		}
		nums = append(nums, ns)
		fmt.Println(nums)
    }
    return
}

func main() {
	N := nextIntArray()[0]
	var nums [][]int
	for i:=0; i<N; i++ {
		nums = append(nums, nextIntArray())
	}
	if f(N, nums) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}