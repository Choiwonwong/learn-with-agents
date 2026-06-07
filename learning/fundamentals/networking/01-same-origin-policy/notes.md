# Same-Origin Policy Notes

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


## 다음 수정

- [ ] `practice/sop_lab.py`에서 preflight가 필요한 요청을 추가한다.
- [ ] 쿠키와 `SameSite` 실험을 별도 단계로 분리한다.
