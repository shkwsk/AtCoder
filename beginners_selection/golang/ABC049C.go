package main

import "fmt"
import "strings"

func f(S string) bool {
	if S == "dreamer" || S == "eraser" || S == "dream" || S == "erase" {
		return true
	}
	if len(S) > 7 {
		if strings.HasSuffix(S,"dreamer") {
			// fmt.Println(S[:len(S)-7])
			return f(S[:len(S)-7])
		}
	}
	if len(S) > 6 {
		if strings.HasSuffix(S,"eraser") {
			// fmt.Println(S[:len(S)-6])
			return f(S[:len(S)-6])
		}
	}
	if len(S) > 5 {
		if strings.HasSuffix(S,"dream") || strings.HasSuffix(S,"erase") {
			// fmt.Println(S[:len(S)-5])
			return f(S[:len(S)-5])
		}
	}
	return false
}

func main() {
	var S string
	fmt.Scan(&S) 
	if f(S) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}