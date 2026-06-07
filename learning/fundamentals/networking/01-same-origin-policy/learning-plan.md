# Same-Origin Policy Final Study Plan

## 0. 기획 의도

Same-Origin Policy(SOP)는 코드를 많이 작성하는 주제가 아니라, 브라우저가 웹 문서와 스크립트 사이에 어떤 보안 경계를 세우는지 이해하는 이론 중심 주제입니다. 이 모듈은 기존 code-first 학습 방식을 대체하지 않고, `theory-first` 보조 경로를 사용합니다.

핵심 흐름은 아래와 같습니다.

```text
위협 모델
→ origin / site / cross-origin 경계
→ SOP가 막는 것과 막지 않는 것
→ CORS라는 통제된 예외
→ 브라우저 관찰 실험
→ renderer process / Site Isolation 관점
→ 자기 말로 설명 리뷰
```

## 1. 최종 성공 기준

학습 후 아래 질문에 자신의 말로 답할 수 있어야 합니다.

1. SOP가 필요한 위협 모델은 무엇인가?
2. origin은 왜 `scheme + host + port`로 정의되는가?
3. SOP는 왜 “요청 차단”보다 “다른 origin 응답/객체 읽기 제한”으로 이해해야 하는가?
4. 이미지, script, form, iframe, `fetch()`는 cross-origin에서 각각 왜 다르게 동작하는가?
5. CORS는 SOP를 끄는 기능인가, 아니면 서버가 특정 origin에 읽기 권한을 위임하는 장치인가?
6. SOP, CORS, CSRF, XSS, SameSite Cookie는 각각 어떤 문제를 담당하는가?
7. renderer process와 Site Isolation은 SOP와 같은 규칙인가, 아니면 SOP를 보강하는 구현/격리 전략인가?
8. origin 기준 접근 제어와 site 기준 process isolation은 어떻게 다른가?

## 2. 학습 산출물

이번 모듈의 결과물은 코드만이 아닙니다. 아래를 함께 남깁니다.

- `notes.md`에 작성한 위협 모델 문장
- origin 판정 표
- SOP가 막는 것 / 막지 않는 것 분류
- CORS 관찰 결과
- renderer process / Site Isolation 개념 정리
- 로컬 실험 결과
- 마지막 자기 설명 리뷰

## 3. 전체 진행안

권장 시간은 2회 세션입니다.

### Session A — SOP와 CORS의 논리적 보안 경계

목표: SOP를 “CORS 에러”가 아니라 브라우저의 cross-origin 읽기 제한으로 이해합니다.

범위:

1. 위협 모델
2. origin 판정
3. SOP가 막는 것 / 막지 않는 것
4. CORS 기본
5. 로컬 fetch 관찰 실험

완료 기준:

- `notes.md`의 위협 모델, origin 설명, 실험 결과 표를 채운다.
- “SOP는 요청 차단이 아니라 응답/객체 읽기 제한에 가깝다”를 설명한다.

### Session B — Renderer Process와 Site Isolation 레이어

목표: SOP가 웹 플랫폼 규칙이고, Site Isolation은 renderer compromise를 고려한 브라우저 내부 방어선임을 구분합니다.

범위:

1. renderer process가 하는 일
2. renderer process가 SOP enforcement에 관여한다는 의미
3. renderer가 compromise되면 SOP만으로 부족한 이유
4. Site Isolation의 목적
5. origin vs site vs SiteInstance vs process boundary 구분
6. iframe / cross-site data delivery 관점
7. process 배치가 SOP와 1:1로 대응하지 않는다는 점

완료 기준:

- `notes.md`의 renderer process / Site Isolation 리뷰 항목을 채운다.
- “SOP와 Site Isolation은 같은 계층이 아니다”를 예시로 설명한다.

## 4. Phase 1 — 위협 모델 먼저 잡기

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

## 5. Phase 2 — Origin 판정 훈련

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

### same-origin vs same-site

SOP는 origin 경계를 중심으로 봅니다. 반면 SameSite Cookie나 Chromium Site Isolation에서 말하는 site는 origin보다 넓은 단위일 수 있습니다. 또한 renderer process 배치는 SOP의 origin 판정과 1:1로 대응하지 않고, Chromium의 process model, SiteInstance, Site Isolation 정책, 브라우저 상태에 따라 달라질 수 있습니다.

예를 들어 아래 둘은 보통 same-site로 볼 수 있지만 same-origin은 아닙니다.

```text
https://app.example.com
https://api.example.com
```

이 차이는 renderer process / Site Isolation을 배울 때 다시 중요해집니다.

## 6. Phase 3 — SOP가 막는 것 / 막지 않는 것

### 분류표

| 동작 | Cross-origin 가능? | JS가 응답/객체를 읽을 수 있나? | 설명 |
|---|---:|---:|---|
| `<img src="...">` | 대체로 가능 | 제한됨 | 로드는 되지만 픽셀/응답 본문 읽기는 제한됨 |
| `<script src="...">` | 가능 | 응답 본문 읽기와 다름 | cross-origin script는 실행될 수 있지만, fetch처럼 임의로 본문을 읽는 것과 구분해야 함 |
| `<form action="...">` | 가능 | 응답 읽기는 제한됨 | CSRF가 SOP만으로 막히지 않는 이유 |
| `<iframe src="...">` | 가능 | DOM 접근 제한 | embed와 DOM read를 구분해야 함 |
| `fetch()` | 요청은 나갈 수 있음 | CORS 없으면 제한 | 흔히 보는 CORS 에러의 배경 |
| `localStorage` | origin별 분리 | 다른 origin 접근 불가 | 저장소도 origin 경계로 나뉨 |

### 산출물

`notes.md`에 “SOP가 막은 것”과 “SOP가 막지 않은 것”을 분리해 씁니다.

## 7. Phase 4 — CORS는 통제된 예외로 보기

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

## 8. Phase 5 — 로컬 브라우저 관찰 실험

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

## 9. Phase 6 — Renderer Process와 Site Isolation 관점

### 왜 이 Phase가 필요한가

SOP는 웹 플랫폼의 접근 규칙입니다. 하지만 실제 브라우저는 JavaScript, DOM, layout, rendering을 renderer process에서 처리합니다. 과거에는 renderer process 안의 코드가 SOP를 지키는 데 많이 의존했습니다. 그런데 renderer process 자체에 취약점이 있으면, 공격자가 같은 process 안에 들어온 다른 site의 민감 데이터를 읽으려 할 수 있습니다.

따라서 Chromium은 Site Isolation을 통해 서로 다른 site의 데이터를 가능한 한 다른 sandboxed renderer process에 배치하고, cross-site data가 공격자 page process로 전달되지 않도록 방어를 강화합니다. 다만 이것은 “same-origin이면 같은 renderer process, cross-origin이면 다른 renderer process”라는 단순 규칙이 아닙니다. renderer process 배치는 SiteInstance, browsing relationship, process reuse/limit, browser version/platform/configuration 같은 process model 요소의 영향을 받습니다.

### 핵심 구분

| 구분 | 중심 질문 | 단위 | 역할 |
|---|---|---|---|
| SOP | 이 JS가 다른 origin의 객체/응답을 읽을 수 있는가? | origin | 웹 플랫폼 접근 규칙 |
| CORS | 서버가 특정 origin에 응답 읽기를 허용했는가? | origin | SOP의 통제된 예외 |
| Site Isolation | 서로 다른 site의 데이터를 같은 renderer process에 둘 것인가? | 주로 site, 때로 origin | renderer compromise를 고려한 브라우저 내부 격리 |
| SiteInstance / process model | 어떤 문서/worker 그룹이 process를 공유해야 하거나 재사용할 수 있는가? | browsing relationship, site, agent cluster 등 | 실제 renderer process 선택 정책 |
| Renderer sandbox | renderer가 OS/user data에 직접 접근할 수 있는가? | process | OS 자원 접근 제한 |

### 핵심 질문

1. SOP가 있는데 왜 Chrome은 Site Isolation을 도입했을까?
2. renderer process가 compromise되면 SOP 체크는 충분할까?
3. cross-origin iframe은 DOM 접근만 막히는가, process도 분리될 수 있는가?
4. SOP의 origin 기준과 Site Isolation의 site 기준은 언제 달라지는가?
5. 왜 “same-origin이면 같은 renderer process”라고 일반화하면 안 되는가?

### 학습 포인트

- SOP와 Site Isolation은 같은 계층이 아니다.
- SOP는 “웹 API 접근 가능 여부”를 origin 기준으로 결정한다.
- renderer process 배치는 SOP의 origin 판정을 그대로 process 단위로 옮긴 것이 아니다.
- Site Isolation은 “민감한 cross-site data를 공격자 renderer process에 두지 않기” 위한 방어선이다.
- Chromium은 SiteInstance/process model을 통해 어떤 문서와 worker가 어떤 renderer process를 사용할지 결정한다.
- cross-origin iframe은 SOP 때문에 부모/자식 DOM 접근이 제한되고, 브라우저 구현에 따라 Out-of-Process iframe으로 분리될 수 있다.
- 모든 브라우저와 모든 상황에서 process 배치가 동일하다고 가정하면 안 된다.

### 관찰 후보

이 관찰은 브라우저/OS/버전에 따라 결과가 달라질 수 있으므로 “정답 맞히기”보다 “레이어 구분”이 목표입니다.

1. Chrome Task Manager 열기
   - macOS/Windows/Linux Chrome에서 More tools → Task manager
   - 여러 site를 열었을 때 renderer process가 어떻게 나뉘는지 관찰
2. `chrome://process-internals` 확인
   - site instance, process assignment 관찰
3. iframe 실험 확장
   - cross-origin iframe을 넣고 DOM 접근 실패 확인
   - 가능하면 process 분리 여부 관찰

### 산출물

`notes.md`에 아래 문장을 완성합니다.

```text
SOP는 ________ 계층의 규칙이고, Site Isolation은 ________ 계층의 방어 전략이다. renderer process 배치는 SOP의 origin 판정과 ________ 대응하지 않는다.
```

## 10. Phase 7 — 개념 경계 리뷰

아래 문장을 각각 한 문단으로 설명합니다.

- SOP는 서버 인증/인가를 대체하지 않는다.
- CORS는 공격을 막는 벽이라기보다 허용 정책이다.
- CSRF는 “요청이 가는 것”이 문제이고, SOP는 주로 “응답을 읽는 것”을 제한한다.
- XSS는 공격자 코드가 피해 origin 안에서 실행되는 문제이므로 SOP 경계 자체가 다른 방식으로 무력화된다.
- SameSite Cookie는 SOP가 아니라 cookie가 cross-site 요청에 포함되는 조건을 다룬다.
- Site Isolation은 SOP와 같은 규칙이 아니라 renderer compromise 피해를 줄이는 브라우저 내부 격리 전략이다.
- renderer process 배치는 same-origin/cross-origin만으로 결정되지 않는다.

## 11. 다음 확장 후보

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
6. renderer process 관찰 실험 고도화
   - `chrome://process-internals`
   - Out-of-Process iframe
   - origin-keyed process 실험은 고급 주제로 분리
   - SiteInstance와 process reuse 사례 비교

## 12. 진행 체크리스트

### 시작 전

- [ ] `guide.md`를 읽고 핵심 질문을 확인한다.
- [ ] `notes.md`의 위협 모델 문장을 먼저 채운다.
- [ ] origin 판정 표를 스스로 풀어본다.

### Session A 완료

- [ ] same-origin / cross-origin without CORS / cross-origin with CORS 결과를 예측했다.
- [ ] `practice/sop_lab.py`를 실행했다.
- [ ] 브라우저 콘솔과 Network 탭에서 결과를 확인했다.
- [ ] SOP와 CORS의 차이를 한 문단으로 설명했다.

### Session B 완료

- [ ] renderer process가 웹 콘텐츠 실행을 담당한다는 점을 설명했다.
- [ ] renderer compromise를 가정하면 왜 Site Isolation이 필요한지 설명했다.
- [ ] origin 기준과 site 기준을 구분했다.
- [ ] SiteInstance/process model이 renderer process 배치에 관여한다는 점을 설명했다.
- [ ] SOP와 Site Isolation의 계층 차이를 한 문단으로 설명했다.
- [ ] “same-origin이면 같은 renderer process”라는 일반화가 틀릴 수 있음을 설명했다.

### Closeout

- [ ] 작성한 코드 또는 관찰 결과가 있다.
- [ ] 리뷰받은 설명이 있다.
- [ ] 다음 수정 하나가 있다.

## 13. 참고 자료

- MDN Same-origin policy: https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy
- MDN CORS guide: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- web.dev Same-site and same-origin: https://web.dev/articles/same-site-same-origin
- Chromium Site Isolation overview: https://www.chromium.org/Home/chromium-security/site-isolation
- Chromium Site Isolation design document: https://www.chromium.org/developers/design-documents/site-isolation
- Chromium Process Model and Site Isolation: https://chromium.googlesource.com/chromium/src/+/main/docs/process_model_and_site_isolation.md
