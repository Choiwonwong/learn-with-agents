# 01. First CLI

GoLand로 Go의 가장 작은 프로젝트 흐름을 1시간 동안 맛보는 실습 모듈입니다.

목표는 Go를 실무에 바로 쓰는 것이 아니라, Go가 `module`, `package`, `main`, `struct`, `method`, `test` 단위로 어떻게 움직이는지 관찰하는 것입니다.

## 파일

- `guide.md`: 1시간 진행 가이드
- `practice/`: 직접 수정하며 실행하는 실습 코드
- `reference/`: 비교용 완성 예시
- `notes.md`: 학습 회고와 질문 기록

## 준비

GoLand에서 이 폴더를 열거나, 프로젝트 루트에서 아래 경로를 Go project로 열어도 됩니다.

```bash
learning/go/basics/01-first-cli/practice
```

Go SDK가 아직 잡히지 않았다면 GoLand의 SDK 설정에서 설치 또는 선택합니다.

## 실행

직접 작성한 파일:

```bash
cd learning/go/basics/01-first-cli/practice
go run .
go test ./...
```

비교용 완성 파일:

```bash
cd learning/go/basics/01-first-cli/reference
go run .
go test ./...
```

## 완료 기준

- `go.mod`가 왜 필요한지 한 문장으로 설명할 수 있다.
- `package main`과 `func main()`의 역할을 말할 수 있다.
- `go run .`과 `go test ./...`를 직접 실행했다.
- `struct`와 method receiver를 사용해 작은 타입을 만들었다.
- GoLand에서 Run, Test, Debug 버튼이 Go CLI 흐름을 감싸는 것임을 확인했다.
