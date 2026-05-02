# Code Review Rubric

코드 리뷰는 아래 순서로 봅니다.

## 1. Correctness

- 실행했을 때 의도한 결과가 나오는가?
- 예외나 빈 입력에서 깨지는 지점은 없는가?
- 외부 입력을 신뢰하고 있지 않은가?

## 2. Lesson Fit

- 지금 학습 목표와 코드가 연결되는가?
- 연습해야 할 개념이 코드에 드러나는가?
- 불필요하게 앞선 주제를 끌어오지 않았는가?

## 3. Responsibility

- 함수나 클래스의 책임이 한 문장으로 설명되는가?
- HTTP, parsing, validation, orchestration 같은 경계가 섞이지 않았는가?
- 이름이 책임을 정확히 드러내는가?

## 4. Simplicity

- 지금 단계에서 가장 단순한 구조인가?
- 추상화가 실제 중복이나 변경 가능성을 줄이는가?
- 상속보다 composition이 더 자연스럽지 않은가?

## 5. Verification

- 최소 실행 확인을 했는가?
- 작은 assert나 fake object로 검산할 수 있는가?
- 실패했을 때 원인을 좁힐 수 있는가?

## 6. Pythonic Style

- 타입 힌트가 읽기와 검증에 도움을 주는가?
- 표준 라이브러리 기능을 적절히 쓰는가?
- mutable 기본값, 과도한 전역 상태, 숨은 side effect를 피했는가?
