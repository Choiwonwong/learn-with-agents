# Same-Origin Policy Guide

## 오늘의 핵심 질문

브라우저가 `http://localhost:8000`에서 열린 페이지에게 `http://localhost:8001`의 응답 본문을 읽지 못하게 하는 이유는 무엇일까?

## 선행 개념

- HTTP request / response
- URL의 scheme, host, port
- 브라우저와 서버의 책임 차이
- 쿠키가 요청에 자동 포함될 수 있다는 사실

## 이론 체크포인트

### 1. Origin 정의

origin은 아래 세 요소가 모두 같을 때만 같습니다.

```text
scheme + host + port
```

예시:

| A | B | Same origin? | 이유 |
|---|---|---:|---|
| `http://localhost:8000` | `http://localhost:8000` | yes | 세 요소 동일 |
| `http://localhost:8000` | `http://localhost:8001` | no | port 다름 |
| `http://localhost:8000` | `https://localhost:8000` | no | scheme 다름 |
| `http://127.0.0.1:8000` | `http://localhost:8000` | no | host 문자열 다름 |

### 2. SOP의 핵심

SOP는 “요청 자체를 항상 막는 규칙”이 아니라, 주로 브라우저 JavaScript가 다른 origin의 민감한 응답을 읽는 것을 제한하는 규칙입니다.

구분해야 합니다.

- 페이지 삽입: 이미지, script, form submit처럼 역사적으로 허용된 cross-origin 동작이 있습니다.
- 응답 읽기: `fetch()`로 받은 JSON/text를 JS가 읽는 것은 CORS 허가 없이는 제한됩니다.
- 서버 보호: SOP는 브라우저 정책입니다. 서버 API의 인증/인가를 대신하지 않습니다.

### 3. CORS와의 관계

CORS는 SOP를 없애는 기능이 아니라, 서버가 “이 origin의 브라우저 JS에게 응답 읽기를 허용한다”고 명시하는 예외 메커니즘입니다.

핵심 응답 헤더:

```http
Access-Control-Allow-Origin: http://localhost:8000
```

### 4. 헷갈리기 쉬운 보안 개념

| 개념 | 주 관심사 | SOP와의 관계 |
|---|---|---|
| SOP | 다른 origin 응답 읽기 제한 | 브라우저 기본 격리 규칙 |
| CORS | cross-origin 읽기 허용 선언 | SOP의 통제된 예외 |
| CSRF | 사용자의 인증 상태로 원치 않는 요청 발생 | SOP만으로 방어 불충분 |
| XSS | 같은 origin 안에서 공격자 JS 실행 | SOP를 우회하는 게 아니라 같은 origin 권한을 획득 |
| SameSite Cookie | cross-site 요청의 쿠키 포함 제어 | CSRF 완화에 도움 |

## 실습 목표

1. `practice/sop_lab.py`를 실행한다.
2. 브라우저에서 `http://localhost:8000`을 연다.
3. same-origin 요청과 cross-origin 요청의 차이를 확인한다.
4. CORS 허용 서버와 미허용 서버의 차이를 확인한다.
5. 관찰 결과를 `notes.md`에 기록한다.

## 성공 기준

학습 후 아래 문장을 자신의 말로 설명할 수 있어야 합니다.

> SOP는 서버 간 통신 규칙이 아니라 브라우저가 웹 페이지 JavaScript의 cross-origin 읽기 권한을 제한하는 보안 경계다.
