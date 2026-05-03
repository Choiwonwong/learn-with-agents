package main

import "fmt"

func Greet(name string) string {
	// TODO: Return "Hello, <name>".
	return fmt.Sprintf("Hello, %s", name)
}

type User struct {
	Name string
	Age  int
}

func (u User) Label() string {
	// TODO: Return "<Name> (<Age>)".
	return fmt.Sprintf("%s (%d)", u.Name, u.Age)
}
