# Verification Gate

이 gate는 closeout 전에 변경 종류에 맞는 최소 검증을 수행하도록 고정합니다.

| 변경 종류 | 최소 검증 |
|---|---|
| Python 코드 | `python3 -m py_compile` 또는 관련 테스트 |
| 문서만 변경 | 링크/경로/중복 참조 검색 |
| 학습 방향 변경 | `roadmap.md`, `backlog.md`, `session-log.md` 정합성 확인 |
| closeout / 리뷰 마무리 | 이번 학습에 사용한 파일 재읽기, 최신 코드 기준 검증 명령 재실행 |
| 공개 안전성 | 민감 후보 grep, `git diff`, `git status --short` |
| 삭제/정리 | 남은 참조 검색, 파일 목록 확인 |

## 절차

1. 이번 closeout에서 증명할 claim을 한 문장으로 정한다.
2. claim을 증명하는 가장 작은 검증 명령을 실행한다.
3. 출력 내용을 읽고 실제 통과 여부를 확인한다.
4. 실패하면 수정 후 같은 claim을 다시 검증한다.
5. 실행하지 못한 검증은 `Not-tested:` 또는 세션 로그에 blocker로 남긴다.

## 문서 구조 변경 기본 검증

```bash
rg -n "mentor-routing|session-closeout|workflows/closeout|NexusV1|commit \\+ push|public safety|공개 안전|검증|git publish" AGENTS.md README.md mento
find mento/workflows/closeout -maxdepth 1 -type f | sort
git diff --stat
git status --short
```
