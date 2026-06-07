# Same-Origin Policy Notes

## 위협 모델

SOP가 없다면 evil.example은 ________ 할 수 있고, 그래서 ________ 가 위험해진다.

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


### SOP가 막은 것


### SOP가 막지 않은 것


### CORS를 켜면 달라지는 것


## Renderer Process / Site Isolation

SOP는 ________ 계층의 규칙이고, Site Isolation은 ________ 계층의 방어 전략이다.

- renderer process가 하는 일:
- renderer compromise를 가정하면 SOP만으로 부족한 이유:
- origin 기준과 site 기준의 차이:
- 관찰한 process 분리 결과:

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
