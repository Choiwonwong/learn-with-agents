# Public Safety Gate

이 gate는 public learning lab에 커밋해도 되는 내용만 남았는지 확인합니다.

## 제거하거나 일반화할 것

- 개인 신상, 감정적/일기식 서술
- 회사, 고객, 계정, 인터뷰, 사내 프로젝트 맥락
- 토큰, 키, 비밀번호, 쿠키, private URL
- raw AI runtime state, local logs, IDE metadata, virtualenv
- 민감한 약점 서사

## 남겨도 되는 것

- 학습 목표
- 작성한 코드와 리뷰 포인트
- 검증 결과
- 다음 수정
- 공개 가능한 기술적 tradeoff

## 권장 표현

```text
Needs more practice with dependency boundaries in small OOP examples.
```

## 피할 표현

```text
I struggled because of <private/company/interview-specific context>.
```

## 최소 확인

1. `git diff` 기준으로 실제 커밋될 내용을 확인한다.
2. 민감 후보 키워드를 검색한다.
3. `.omx/`, `.venv/`, `.idea/`, raw logs, secrets가 커밋 대상이 아닌지 확인한다.
4. 공개 repo 문서가 NexusV1 같은 private system 접근을 독자 요구사항처럼 설명하지 않는지 확인한다.
