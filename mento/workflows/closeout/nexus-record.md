# NexusV1 Record Gate

작업 마무리 시에는 `nexus-vault` 스킬을 명시적으로 사용해 NexusV1 기록을 반드시 남깁니다.

NexusV1 기록은 상세한 중복 문서가 아니라 "오늘 이런 공부를 했다"는 가벼운 로깅이 기본 목적입니다. 이 공개 저장소의 독자가 접근하거나 재현해야 하는 필수 시스템이 아니므로, public repo 문서에는 NexusV1 내부 경로/개인 맥락을 요구사항처럼 남기지 않습니다.

자동화가 실제 NexusV1 기록 대상을 알아야 한다면 tracked 문서가 아니라 `nexus-vault` 스킬, ignored local runtime configuration, 또는 사용자별 agent memory에서 해석합니다.

## 기록 기준

- 한 세션 또는 모듈이 `learning-complete` 상태
- 작업 마무리, 방향 전환, 운영 규칙 변경처럼 closeout이 발생함
- 코드/리뷰/검증/다음 수정이 정리됨
- 공개 안전 검열 통과

## 기록 내용

- Daily Agent Activity에 요약 append
- 큰 학습 단위라면 Request 또는 Decision note 생성
- 공개 가능한 학습 증거만 기록
- private/company/account/interview/credential 맥락은 기록하지 않음

## 안전 규칙

- `500_Sanctum/` 접근 금지
- 삭제 금지, 필요 시 archive 이동
- Obsidian CLI는 `path=`를 사용
- Daily는 오늘 날짜에만 append
- 한국어로 요약하되 파일명/태그/frontmatter는 영어 사용
- Obsidian CLI 사용 전 가능한 범위에서 target vault가 NexusV1인지 확인
