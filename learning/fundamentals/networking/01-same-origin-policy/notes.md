# Same-Origin Policy Notes

## 위협 모델

SOP가 없다면 evil.example은 사용자의 브라우저가 세션/권한을 가진 다른 origin의 민감한 응답을 읽을 수 있고, 그래서 계정 정보, 개인 데이터, 내부 API 응답 같은 데이터 유출이 위험해진다.

멘토 리뷰: “다른 모든 브라우저의 사이트”라기보다, 현재 브라우저 컨텍스트에서 사용자가 접근 권한을 가진 다른 origin의 응답을 공격자 JavaScript가 읽는 위험으로 좁혀 이해한다.

## 관찰 기록

- 실행 날짜:
- 브라우저:
- 실험 URL:

## 실험 결과

| 실험 | 예상 | 실제 | 이유 |
|---|---|---|---|
| same-origin fetch | 성공 |  |  |
| cross-origin fetch without CORS | 실패 |  |  |
| cross-origin fetch with CORS | 성공 |  |  |

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


### SOP가 막지 않은 것


### CORS를 켜면 달라지는 것


## Renderer Process / Site Isolation

SOP는 ________ 계층의 규칙이고, Site Isolation은 ________ 계층의 방어 전략이다. renderer process 배치는 SOP의 origin 판정과 ________ 대응하지 않는다.

- renderer process가 하는 일:
- renderer compromise를 가정하면 SOP만으로 부족한 이유:
- origin 기준과 site 기준의 차이:
- SiteInstance / process model이 필요한 이유:
- 관찰한 process 분리 결과:
- “same-origin이면 같은 renderer process”라고 일반화하면 안 되는 이유:

## 개념 경계 리뷰

- SOP는 서버 인증/인가를 대체하지 않는다:
- CORS는 SOP를 제거하는 기능이 아니라:
- CSRF와 SOP의 차이:
- XSS와 SOP의 차이:
- SameSite Cookie와 SOP의 차이:
- Site Isolation과 SOP의 차이:

## 다음 수정

- [ ] `practice/sop_lab.py`에서 preflight가 필요한 요청을 추가한다.
- [ ] 쿠키와 `SameSite` 실험을 별도 단계로 분리한다.
