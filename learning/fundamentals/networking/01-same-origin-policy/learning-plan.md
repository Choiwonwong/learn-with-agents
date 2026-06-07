# Same-Origin Policy Learning Plan

## 학습 판단

Same-Origin Policy(SOP)는 코드 구현 주제가 아니라 브라우저 보안 경계를 이해하는 이론 중심 주제입니다. 따라서 이 모듈은 기본 code-first 학습 루프를 유지하되, `theory-first` 보조 경로를 사용합니다.

```text
위협 모델
→ origin / site / cross-origin 경계
→ SOP가 막는 것과 막지 않는 것
→ CORS라는 통제된 예외
→ 브라우저 관찰 실험
→ 자기 말로 설명 리뷰
```

## 최종 성공 기준

아래를 자신의 말로 설명할 수 있으면 1차 학습 성공입니다.

1. origin은 왜 `scheme + host + port`로 정의되는가?
2. SOP는 왜 “요청 차단”보다 “다른 origin 응답/객체 읽기 제한”으로 이해해야 하는가?
3. 이미지, script, form, iframe, `fetch()`는 cross-origin에서 각각 왜 다르게 동작하는가?
4. CORS는 SOP를 끄는 기능인가, 아니면 서버가 특정 origin에 읽기 권한을 위임하는 장치인가?
5. SOP, CORS, CSRF, XSS, SameSite Cookie는 각각 어떤 문제를 담당하는가?

## Phase 1 — 위협 모델 먼저 잡기

### 핵심 질문

사용자가 `bank.example`에 로그인한 상태에서 공격자 페이지 `evil.example`을 열었다면, `evil.example`의 JavaScript가 `bank.example/api/me` 응답 본문을 읽을 수 있어야 할까?

### 학습 내용

- 브라우저는 여러 사이트의 문서와 스크립트를 동시에 실행한다.
- 사용자의 쿠키나 인증 상태는 요청에 자동으로 붙을 수 있다.
- 서버가 인증된 사용자에게 민감한 응답을 줄 때, 공격자 origin의 JavaScript가 그 응답을 읽을 수 있으면 정보 유출이 된다.
- SOP는 이 상황에서 문서/스크립트가 다른 origin의 리소스와 상호작용하는 방식을 제한하는 브라우저 보안 경계다.

### 산출물

`notes.md`에 아래 문장을 완성합니다.

```text
SOP가 없다면 evil.example은 ________ 할 수 있고, 그래서 ________ 가 위험해진다.
```

## Phase 2 — Origin 판정 훈련

### 핵심 개념

origin은 세 요소가 모두 같아야 같습니다.

```text
scheme + host + port
```

### 연습

아래 쌍을 same-origin / cross-origin으로 판정합니다.

| A | B | 판정 | 이유 |
|---|---|---|---|
| `http://localhost:8000` | `http://localhost:8000` |  |  |
| `http://localhost:8000` | `http://localhost:8001` |  |  |
| `http://localhost:8000` | `https://localhost:8000` |  |  |
| `http://127.0.0.1:8000` | `http://localhost:8000` |  |  |
| `https://app.example.com` | `https://api.example.com` |  |  |

### 주의

`same-origin`과 `same-site`는 다릅니다. SOP는 origin 경계를 중심으로 보고, SameSite Cookie는 site 경계를 중심으로 봅니다.

## Phase 3 — SOP가 막는 것 / 막지 않는 것

### 분류표

| 동작 | Cross-origin 가능? | JS가 응답/객체를 읽을 수 있나? | 설명 |
|---|---:|---:|---|
| `<img src="...">` | 대체로 가능 | 제한됨 | 로드는 되지만 픽셀/응답 본문 읽기는 제한됨 |
| `<script src="...">` | 가능 | 스크립트가 실행됨 | 역사적 예외이며 JSONP 같은 패턴의 배경 |
| `<form action="...">` | 가능 | 응답 읽기는 제한됨 | CSRF가 SOP만으로 막히지 않는 이유 |
| `<iframe src="...">` | 가능 | DOM 접근 제한 | embed와 DOM read를 구분해야 함 |
| `fetch()` | 요청은 나갈 수 있음 | CORS 없으면 제한 | 흔히 보는 CORS 에러의 배경 |
| `localStorage` | origin별 분리 | 다른 origin 접근 불가 | 저장소도 origin 경계로 나뉨 |

### 산출물

`notes.md`에 “SOP가 막은 것”과 “SOP가 막지 않은 것”을 분리해 씁니다.

## Phase 4 — CORS는 통제된 예외로 보기

### 핵심 질문

서버가 `Access-Control-Allow-Origin: http://localhost:8000`을 응답하면 브라우저는 무엇을 허용하는가?

### 학습 내용

- CORS는 서버가 특정 origin의 브라우저 JavaScript에게 cross-origin 응답 읽기를 허용하는 방식이다.
- 단순 요청(simple request)은 preflight 없이 실제 요청이 갈 수 있다.
- 특정 조건의 요청은 `OPTIONS` preflight로 서버 허용 여부를 먼저 확인한다.
- credentials를 포함하는 요청에서 wildcard `*`는 안전한 허용 방식이 아니다.

### 산출물

아래 문장을 완성합니다.

```text
CORS는 SOP를 제거하는 기능이 아니라 ________ 이다.
```

## Phase 5 — 로컬 브라우저 관찰 실험

### 실행

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python learning/fundamentals/networking/01-same-origin-policy/practice/sop_lab.py
```

브라우저에서 엽니다.

```text
http://localhost:8000
```

### 관찰

1. Same-origin fetch
2. Cross-origin fetch without CORS
3. Cross-origin fetch with CORS

각 버튼을 누르기 전에 결과를 예측하고, 누른 뒤 브라우저 콘솔과 Network 탭을 확인합니다.

### 산출물

`notes.md`의 실험 결과 표를 채웁니다.

## Phase 6 — 개념 경계 리뷰

아래 문장을 각각 한 문단으로 설명합니다.

- SOP는 서버 인증/인가를 대체하지 않는다.
- CORS는 공격을 막는 벽이라기보다 허용 정책이다.
- CSRF는 “요청이 가는 것”이 문제이고, SOP는 주로 “응답을 읽는 것”을 제한한다.
- XSS는 공격자 코드가 피해 origin 안에서 실행되는 문제이므로 SOP 경계 자체가 다른 방식으로 무력화된다.
- SameSite Cookie는 SOP가 아니라 cookie가 cross-site 요청에 포함되는 조건을 다룬다.

## Phase 7 — 다음 확장 후보

1. preflight가 필요한 요청 추가
   - custom header
   - `PUT` 또는 `DELETE`
   - `Content-Type: application/json`
2. credential 포함 요청 실험
   - `credentials: "include"`
   - `Access-Control-Allow-Credentials`
   - wildcard origin 실패 관찰
3. iframe DOM 접근 실험
4. CSRF 미니 실험
   - form submit은 가능하지만 응답 읽기는 제한되는 구조 확인
5. SameSite Cookie 별도 모듈로 분리

## 참고 자료

- MDN Same-origin policy: https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
- MDN CORS guide: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- web.dev Same-site and same-origin: https://web.dev/articles/same-site-same-origin
