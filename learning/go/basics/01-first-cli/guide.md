# Go 1시간 맛보기: 첫 CLI와 테스트

먼저 생각할 질문: Go는 Python처럼 파일 하나를 바로 실행하는 언어일까, 아니면 module/package 단위로 생각해야 하는 언어일까?

이번 실습의 답은 후자에 가깝다. Go는 파일보다 package와 module의 경계를 먼저 의식하게 만든다.

## 오늘의 성공 기준

1시간 뒤에 다음 질문에 답할 수 있으면 성공입니다.

- `go.mod`는 무엇을 기록하는가?
- `package main`은 왜 특별한가?
- `go run .`은 현재 디렉터리를 어떻게 실행 대상으로 해석하는가?
- Go의 함수 선언은 Python/Java와 무엇이 다른가?
- Go에서 class 없이 `struct`와 method로 행동을 붙이는 방식은 어떤 느낌인가?
- `_test.go` 파일과 `TestXxx(t *testing.T)` 함수는 어떻게 테스트로 인식되는가?

## 60분 진행표

| 시간 | 목표 | 산출물 |
|---:|---|---|
| 0-10분 | GoLand와 Go SDK 확인 | `go version` 확인 |
| 10-20분 | 첫 실행 구조 이해 | `main.go`, `go run .` |
| 20-35분 | 함수와 struct 맛보기 | `Greet`, `User`, `Label()` |
| 35-50분 | 테스트 맛보기 | `greeting_test.go`, `go test ./...` |
| 50-60분 | 디버깅과 회고 | breakpoint, `notes.md` |

## 1단계: GoLand와 Go SDK 확인

GoLand에서 `practice/` 폴더를 프로젝트로 열고 Terminal을 엽니다.

```bash
go version
```

안 되면 GoLand 설정에서 Go SDK를 추가합니다. GoLand가 SDK를 직접 다운로드할 수도 있습니다.

관찰 포인트:

- IDE가 Go SDK를 알지 못하면 실행/테스트/자동완성이 약해진다.
- GoLand의 Run/Test 버튼도 결국 `go` 명령을 감싸는 UI다.

## 2단계: 첫 실행 구조 이해

`practice/main.go`를 열고 실행합니다.

```bash
go run .
```

핵심 구조:

```go
package main

func main() {
    // program entry point
}
```

생각할 점:

- 실행 가능한 프로그램은 `package main`에 있어야 한다.
- `func main()`은 프로그램의 시작점이다.
- `go run .`은 현재 디렉터리의 package를 빌드하고 실행한다.

## 3단계: 함수와 struct 맛보기

`practice/greeting.go`에서 `Greet`와 `User.Label`을 직접 수정해봅니다.

목표 동작:

```text
Hello, GoLand
Ada (37)
```

Go 함수 선언의 기본 모양:

```go
func name(parameter Type) ReturnType {
    return value
}
```

Go method의 기본 모양:

```go
func (u User) Label() string {
    return ...
}
```

여기서 `(u User)`를 receiver라고 부릅니다. Python의 `self`처럼 "이 method가 어느 값에 붙는가"를 보여주지만, 문법적으로는 함수 이름 앞에 따로 적습니다.

## 4단계: 테스트 맛보기

`practice/greeting_test.go`를 열고 테스트를 실행합니다.

```bash
go test ./...
```

Go 테스트의 기본 규칙:

- 파일명은 `_test.go`로 끝난다.
- 테스트 함수는 `TestXxx`로 시작한다.
- 인자는 `t *testing.T`를 받는다.
- 실패는 `t.Fatalf`, `t.Errorf` 등으로 보고한다.

GoLand에서는 테스트 함수 옆 gutter 버튼으로도 실행할 수 있습니다. 단, CLI에서도 같은 결과가 나와야 합니다.

## 5단계: 디버깅

`main.go`의 `fmt.Println(Greet("GoLand"))` 줄에 breakpoint를 걸고 Debug를 실행합니다.

확인할 것:

- `name` 값이 어디에서 들어오는가?
- `Greet` 함수 안으로 Step Into가 되는가?
- `user.Label()` 호출 때 receiver `u`의 값이 보이는가?

## 작은 검산

아래 명령이 모두 동작하면 이번 모듈의 기본 실행은 성공입니다.

```bash
cd learning/go/basics/01-first-cli/practice
go run .
go test ./...
```

예상 출력:

```text
Hello, GoLand
Ada (37)
```

## 비목표

- goroutine과 channel은 하지 않습니다.
- interface는 깊게 하지 않습니다.
- HTTP 서버는 다음 모듈로 미룹니다.
- 실무 프로젝트 구조나 배포 세팅으로 확장하지 않습니다.

## 다음 확장

다음 세션은 아래 순서가 좋습니다.

1. slice/map으로 작은 in-memory 목록 다루기
2. error handling으로 실패를 값처럼 다루기
3. interface로 필요한 행동만 계약하기
4. HTTP handler로 요청/응답 맛보기
5. goroutine/channel로 동시성 모델 보기
