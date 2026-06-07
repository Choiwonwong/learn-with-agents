# 01. Same-Origin Policy

브라우저 보안 모델의 핵심인 Same-Origin Policy(SOP)를 이론과 작은 로컬 실습으로 학습합니다.

## 목표

- origin을 `scheme + host + port`로 정확히 판정한다.
- SOP가 막는 것과 막지 않는 것을 구분한다.
- SOP, CORS, 쿠키 `SameSite`, CSRF, XSS의 책임 경계를 분리한다.
- renderer process와 Site Isolation이 SOP를 어떻게 보강하는지 설명한다.
- 브라우저에서 실제로 실패하는 cross-origin `fetch`를 관찰한다.
- 서버가 CORS 헤더를 추가했을 때 무엇이 달라지는지 설명한다.

## 산출물

- `learning-plan.md`: SOP, CORS, renderer process / Site Isolation까지 포함한 최종 학습 기획서.
- `practice/sop_lab.py`: 서로 다른 포트의 로컬 서버 두 개를 띄우고, 브라우저에서 cross-origin 요청을 실험한다.
- `notes.md`: 관찰 결과와 개념 정리.
- `reference/`: 실습 후 비교할 수 있는 기준 구현 공간.

## 권장 순서

0. `learning-plan.md`로 위협 모델과 개념 경계를 먼저 잡는다.
1. `guide.md`의 개념 질문에 답한다.
2. `practice/sop_lab.py`를 실행해 같은 origin / 다른 origin 요청 차이를 관찰한다.
3. CORS 헤더를 켜고 끄며 브라우저 콘솔과 Network 탭을 비교한다.
4. `notes.md`에 “SOP가 실제로 보호한 것”과 “SOP만으로 보호하지 못한 것”을 분리해 적는다.
