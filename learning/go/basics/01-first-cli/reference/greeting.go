package main

import "fmt"

func Greet(name string) string {
	return fmt.Sprintf("Hello, %s", name)
}

type User struct {
	Name string
	Age  int
}

func (u User) Label() string {
	return fmt.Sprintf("%s (%d)", u.Name, u.Age)
}
