# Same-Origin Policy Notes

## 위협 모델

SOP가 없다면 evil.example은 사용자의 브라우저가 세션/권한을 가진 다른 origin의 민감한 응답을 읽을 수 있고, 그래서 계정 정보, 개인 데이터, 내부 API 응답 같은 데이터 유출이 위험해진다.

멘토 리뷰: “다른 모든 브라우저의 사이트”라기보다, 현재 브라우저 컨텍스트에서 사용자가 접근 권한을 가진 다른 origin의 응답을 공격자 JavaScript가 읽는 위험으로 좁혀 이해한다.

## 관찰 기록

- 실행 날짜: 2026-06-07
- 브라우저: 로컬 브라우저
- 실험 URL: http://localhost:8000

## 실험 결과

| 실험 | 예상 | 실제 | 이유 |
|---|---|---|---|
| same-origin fetch | 성공 | 성공 | 같은 origin(`http://localhost:8000`)의 `/api/message` 응답은 JS가 읽을 수 있다. |
| cross-origin fetch without CORS | 실패 | 실패 | `http://localhost:8001`은 port가 달라 cross-origin이고, 서버가 CORS 허용 헤더를 주지 않아 브라우저가 JS에 응답을 노출하지 않았다. |
| cross-origin fetch with CORS | 성공 | 성공 | API 서버가 `Access-Control-Allow-Origin: http://localhost:8000`을 응답해 현재 origin의 JS가 응답을 읽을 수 있었다. |

## 내 설명

### Origin이 같다는 뜻

Origin은 `scheme + host + port`가 모두 같을 때만 같다.

| A | B | 내 최초 판정 | 리뷰 후 판정 | 이유 |
|---|---|---|---|---|
| `http://localhost:8000` | `http://localhost:8000` | same-origin | same-origin | scheme, host, port가 모두 같다. |
| `http://localhost:8000` | `http://localhost:8001` | same-origin | cross-origin | port가 다르면 origin이 다르다. |
| `http://localhost:8000` | `https://localhost:8000` | same-origin | cross-origin | scheme이 다르면 origin이 다르다. |
| `http://127.0.0.1:8000` | `http://localhost:8000` | cross-origin | cross-origin | host 문자열이 다르면 origin이 다르다. |
| `https://app.example.com` | `https://api.example.com` | same-origin | cross-origin | subdomain이 다르면 host가 다르므로 origin이 다르다. 같은 site일 수는 있지만 same-origin은 아니다. |

멘토 리뷰: SOP의 same-origin은 직관적인 “같은 서비스/같은 회사/비슷한 URL” 기준이 아니라 `scheme + host + port`의 엄격한 튜플 비교다.

### SOP가 막은 것

SOP는 cross-origin 동작 전체를 막기보다, JavaScript가 다른 origin의 응답 본문이나 객체 내부에 접근하는 것을 주로 제한한다.

| 동작 | 내 최초 예측 | 리뷰 후 정리 | 이유 |
|---|---|---|---|
| `<img src="https://other.example/a.png">` | 로드 가능 / 못 읽음 | 로드 가능 / 응답 본문·픽셀 읽기 제한 | 이미지는 cross-origin 로드가 가능하지만 JS가 응답 본문을 fetch처럼 읽을 수는 없다. canvas에 그린 뒤 픽셀을 읽는 것도 CORS 없이는 제한될 수 있다. |
| `<script src="https://other.example/a.js">` | 로드 가능 / 못 읽음 | 로드·실행 가능 / 응답 본문을 임의로 읽는 것과는 다름 | script는 역사적으로 cross-origin 로드와 실행이 가능하다. 다만 JS가 script 파일 내용을 문자열로 읽는 것과는 구분한다. |
| `<form action="https://other.example/pay">` | 로드 가능 / 못 읽음 | 요청 가능 / 응답 읽기 제한 | form submit은 cross-origin으로 보낼 수 있다. 이 때문에 CSRF는 SOP만으로 막히지 않는다. |
| `<iframe src="https://other.example">` | 로드 불가능 / 못 읽음 | 로드 가능 / DOM 접근 제한 | iframe embed 자체는 가능할 수 있지만, 부모 페이지 JS가 cross-origin iframe의 DOM을 읽거나 조작하는 것은 제한된다. |
| `fetch("https://other.example/api")` | 로드 불가능 / 못 읽음 | 요청은 나갈 수 있음 / CORS 없으면 응답 읽기 제한 | CORS 실패는 보통 네트워크 요청 자체가 없다는 뜻이 아니라 브라우저가 JS에 응답을 노출하지 않는다는 뜻에 가깝다. |
| `localStorage`에서 `other.example` 데이터 읽기 | 로드 불가능 / 못 읽음 | 접근 불가 / 읽기 불가 | Web Storage는 origin별로 분리되므로 다른 origin의 localStorage에 접근할 수 없다. |

### SOP가 막지 않은 것

SOP는 cross-origin 요청이나 리소스 포함을 모두 금지하지 않는다. 이미지 로드, script 로드/실행, form submit, iframe embed, 일부 fetch 요청은 발생할 수 있다. 핵심은 “요청/로드가 가능한가”와 “현재 origin의 JavaScript가 응답이나 객체 내부를 읽을 수 있는가”를 분리하는 것이다.

멘토 리뷰: iframe과 fetch를 “로드 불가능”으로 보면 SOP를 요청 차단 규칙으로 오해하기 쉽다. 더 정확히는 iframe은 로드되지만 DOM 접근이 막히고, fetch는 요청이 나갈 수 있지만 CORS 허용 없이는 응답이 JS에 노출되지 않는다.

확인 질문 답변: cross-origin form submit은 나갈 수 있지만, 공격자 페이지가 그 응답을 읽는 것은 제한된다. 웹의 특성상 다른 endpoint로 요청을 보내는 것 자체는 가능할 수 있으나, 해당 응답 값을 읽는 것은 보안상 브라우저가 제한한다. 이 지점 때문에 SOP만으로 CSRF를 막을 수 없다.

### CORS를 켜면 달라지는 것

CORS는 Cross-Origin Resource Sharing의 약자다. 이름 그대로 다른 origin의 resource를 현재 origin의 JavaScript에 공유할지 정하는 메커니즘이다.

SOP가 기본적으로 cross-origin 응답 읽기를 제한하고, CORS는 서버가 특정 origin에 대해 그 제한을 통제된 방식으로 완화하는 허용 정책으로 함께 쓰인다.

CORS에서 `Access-Control-Allow-Origin: http://localhost:8000`은 `http://localhost:8000`의 JavaScript에게 이 cross-origin 응답을 읽게 해도 된다는 서버의 허용 선언이다.

멘토 리뷰: “cross-origin을 허용한다”는 표현은 맞지만, 더 정확히는 요청 자체보다 응답을 JS에 노출하는 것을 허용한다는 뜻이다. SOP가 완전히 꺼지는 것이 아니라 특정 origin에 대한 통제된 예외다.

추가 정리: CORS 허용은 요청하는 프론트엔드가 아니라 리소스를 가진 받는 서버/API 서버가 응답 헤더로 선언한다. 브라우저는 요청에 `Origin` 헤더를 붙이고, 서버의 `Access-Control-Allow-Origin` 응답 헤더가 현재 origin을 허용하는지 보고 JS에 응답을 노출할지 결정한다.


## Renderer Process / Site Isolation

SOP는 ________ 계층의 규칙이고, Site Isolation은 ________ 계층의 방어 전략이다. renderer process 배치는 SOP의 origin 판정과 ________ 대응하지 않는다.

- renderer process가 하는 일:
- renderer compromise를 가정하면 SOP만으로 부족한 이유:
- origin 기준과 site 기준의 차이:
- SiteInstance / process model이 필요한 이유:
- 관찰한 process 분리 결과:
- “same-origin이면 같은 renderer process”라고 일반화하면 안 되는 이유:

## 개념 경계 리뷰

- SOP는 서버 인증/인가를 대체하지 않는다: SOP는 브라우저가 JS의 cross-origin 읽기 권한을 제한하는 정책이다. 서버 API가 사용자를 인증하고 요청 권한을 검사하는 책임은 그대로 남는다.
- CORS는 SOP를 제거하는 기능이 아니라: 서버가 특정 origin의 JavaScript에게 cross-origin 응답 읽기를 허용하는 통제된 예외 정책이다.
- CSRF와 SOP의 차이: CSRF는 사용자의 인증 상태로 원치 않는 요청이 나가는 문제다. SOP는 응답 읽기를 제한할 수 있지만 form submit 같은 요청 자체를 전부 막지 않으므로 CSRF 방어로 충분하지 않다.
- XSS와 SOP의 차이: XSS는 공격자 JavaScript가 피해 origin 내부에서 실행되는 문제다. 이 경우 SOP 관점에서는 같은 origin 코드가 되므로 피해 사이트의 API/DOM 접근이 가능해질 수 있다.
- SameSite Cookie와 SOP의 차이: SOP는 origin 기준 JS 읽기 권한을 다루고, SameSite Cookie는 cross-site 요청에 쿠키를 붙일지 결정하는 쿠키 전송 정책이다.
- Site Isolation과 SOP의 차이:

## 다음 수정

- [ ] Session B에서 renderer process, SiteInstance, Site Isolation을 SOP와 같은 계층으로 혼동하지 않도록 정리한다.
- [ ] `practice/sop_lab.py`에서 preflight가 필요한 요청을 추가한다.
- [ ] 쿠키와 `SameSite` 실험을 별도 단계로 분리한다.

## Session A Closeout

- 완료한 범위: 위협 모델, origin 판정, SOP가 막는 것/막지 않는 것, CORS 기본, 로컬 fetch 관찰 실험.
- 핵심 이해: SOP는 서버나 HTTP 자체의 규칙이 아니라 브라우저가 현재 origin의 JavaScript에 cross-origin 응답/객체를 노출할지 결정하는 보안 정책이다.
- 검증 증거: 로컬 서버 `localhost:8000`/`localhost:8001` 실험에서 same-origin fetch 성공, CORS 없는 cross-origin fetch 실패, CORS 허용 cross-origin fetch 성공을 관찰했다. 서버 로그상 no-cors 요청도 200 응답이 발생해 “요청 자체”와 “JS 응답 읽기”가 다르다는 점을 확인했다.
- 남은 범위: renderer process / Site Isolation은 Session B에서 진행한다.
