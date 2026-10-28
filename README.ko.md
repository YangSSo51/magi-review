# 마기식 검토 — MAGI Review

**문제 하나를 세 관점으로 검토하고, 근거를 확인해 실행 계획으로 연결합니다.**

[설치 안내](INSTALL.md) · [사용 예시](docs/EXAMPLE.md) · [연구 자료](docs/RESEARCH.md) · [MIT 라이선스](LICENSE)

Codex와 Claude Code에서 **명시적으로 호출할 때만** 사용하는 검토 스킬입니다. 동일한 사용자 선택 모델의 서브 에이전트 세 개가 목적·효용, 정확성·안전성, 단순성·운영성을 독립 평가하고 중요한 쟁점 확인 후 Plan과 실행용 Goal을 만듭니다.

## 사용 흐름

1. 현재 도구에서 서브 에이전트에 사용할 수 있는 모델 목록과 `Default`를 제시합니다. Default는 이 검토에서 현재 세션 모델을 상속한다는 뜻입니다. 계정 기본값을 변경하지 않습니다.
2. 사용자가 문제 상황이나 목적을 제시합니다. 필요한 경우 질문으로 구체화합니다.
3. AI가 판단 기준 3–6개, 추천 우선순위, 확인 가능한 성공 증거를 **먼저 리스트업**합니다. 사용자가 수락·수정한 뒤 평가합니다. 처음부터 추천 기준 사용을 명시적으로 맡길 수도 있습니다.
4. 같은 모델의 서브 에이전트 세 개가 서로의 첫 답변을 보지 않고 평가합니다.
5. 중요한 쟁점만 최대 한 차례 교차 검토하고 근거로 확인합니다.
6. Plan과 실행용 Goal을 제시합니다. 네이티브 Goal 등록과 구현 시작은 사용자의 요청 범위에 따릅니다.

모델은 대개 로컬에 설치된 프로그램이 아니라 계정·호스트에서 접근 가능한 원격 모델입니다. 스킬은 모델 설치나 타 제공업체 연결을 대신하지 않습니다. 목록을 확인할 수 없으면 한계를 알리고 선택을 요청합니다.

## 설치와 호출

설치 스크립트는 Python 3.10+ 표준 라이브러리만 사용하며 기존 경로를 덮어쓰지 않습니다. 아래 경로는 예시입니다. 대상 프로젝트에서 실행하거나 실제 절대 경로로 바꾸세요.

```sh
python /path/to/magi-review/scripts/install.py --host codex --destination .agents/skills/magi-review
python /path/to/magi-review/scripts/install.py --host claude --destination .claude/skills/magi-review
```

개인용 경로 및 Python 없이 복사하는 방법은 [설치 안내](INSTALL.md)에 있습니다. Claude용으로 수동 복사할 때는 SKILL.md frontmatter에 `disable-model-invocation: true`를 추가해야 합니다. 설치 스크립트는 이를 자동 적용합니다.

- Codex: `$magi-review 이 문제를 검토해줘. 모델 선택과 목적 구체화, 판단 기준 추천부터 시작해줘.`
- Claude Code: `/magi-review 이 문제를 검토해줘. 판단 기준을 추천하고 확인받은 후 진행해줘.`

핵심 지침은 영어로 작성했고 응답은 사용자 언어를 따릅니다. 일반 Claude 채팅처럼 서브 에이전트 도구가 없는 환경의 실제 3개 에이전트 실행은 지원하지 않습니다.

## 연구 근거와 검증 상태

[연구 노트](docs/RESEARCH.md)는 성공 사례와 부정적 결과를 함께 다룹니다. 특히 동일 모델의 세 역할을 사용한 MABPD, 역할 편향을 확인한 Beyond Consensus, 같은 예산의 독립 응답과 비교한 Beyond Symmetric Agents가 설계에 관련됩니다. 이 스킬 자체가 최신 고성능 모델의 개발 작업에서 성능을 높인다는 실험 결과는 아직 없습니다.

설치 동작과 설정의 로컬 검사를 제공하지만 Claude Code/Codex 실환경의 전체 모델 실행 검증은 아직 수행하지 않았습니다. 합의는 증명이나 테스트 통과가 아닙니다.

MIT 라이선스로 배포합니다. [GitHub 저장소](https://github.com/YangSSo51/magi-review)에서 설치할 수 있습니다. Ponytail·i-have-adhd·Graphify의 소개와 설치 안내 구성을 참고했고, 코드·스킬 본문·이미지는 가져오지 않았습니다. [참고 저장소와 라이선스](docs/ACKNOWLEDGMENTS.md)에 정리했습니다. [게시 및 검증 확인 사항](docs/RELEASE.md)
