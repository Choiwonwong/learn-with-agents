package main

import "fmt"

func main() {
	fmt.Println(Greet("GoLand"))

	user := User{
		Name: "Ada",
		Age:  37,
	}

	fmt.Println(user.Label())
}
