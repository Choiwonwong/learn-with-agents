package main

import "testing"

func TestGreet(t *testing.T) {
	got := Greet("Go")
	want := "Hello, Go"

	if got != want {
		t.Fatalf("Greet() = %q, want %q", got, want)
	}
}

func TestUserLabel(t *testing.T) {
	user := User{Name: "Ada", Age: 37}

	got := user.Label()
	want := "Ada (37)"

	if got != want {
		t.Fatalf("User.Label() = %q, want %q", got, want)
	}
}
