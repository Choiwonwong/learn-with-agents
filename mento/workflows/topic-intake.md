# Topic Intake Workflow

새 학습 주제를 모듈로 만들기 전에 확인합니다.

## 확인 항목

- 이 주제는 어떤 트랙에 속하는가?
- 오늘 1-3시간 안에 끝낼 수 있는가?
- 실습 산출물은 무엇인가?
- 선행 개념은 무엇인가?
- 기존 로드맵이나 약점과 연결되는가?
- reference 코드는 언제 보여줄 것인가?

## 모듈 생성 기준

새 모듈은 아래 구조를 따릅니다.

```text
learning/<track>/<area>/<NN-name>/
├── README.md
├── guide.md
├── practice/
├── reference/
├── notes.md
└── requirements.txt
```

`requirements.txt`는 필요한 경우에만 둡니다.
