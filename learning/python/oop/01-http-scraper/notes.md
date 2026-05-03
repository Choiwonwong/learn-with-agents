# Notes

## 오늘 배운 점

- 값 객체가 누락 정책까지 책임져야 하는가?
    - quote 하나의 데이터와 quote에 가까운 행동을 가져야한다.
    - None author를 unknown으로 바꿀지, tag가 없으면 어떻게 보여줄지 같은 정책은 나중에 parser나 출력 계층에서 다시 다루는 편이 책임 분리가 더 선명

- Python의 None..
    - f"{None}"은 format(None, "") 흐름을 타며, 결과적으로 str(None)과 같은 "None" 문자열
    - Python NoneType 값인 None은 문자열로 표현될 때 "None"이 된다.(Runtime Error X)

- conversion flag
    - f"{value!r}" -> repr(value)
    - f"{value!s}" -> str(value)
- str / repr 차이?
    - str(x): 사람이 읽기 좋은 문자열
    - repr(x): 개발자가 디버깅하기 좋은, 가능한 한 정확한 표현

```python
text = "hello"
print(str(text))  # hello
print(repr(text))  # 'hello'

print(f"{text!s}")  # hello
print(f"{text!r}")  # 'hello'

# 문자열에서는 차이 명확

name = "Alice"
print(f"name={name!s}")  # name=Alice
print(f"name={name!r}")  # name='Alice'

# repr은 따옴표까지 보여줘서 “이게 문자열 값이구나”를 디버깅할 때 좋습니다.

# None은 둘이 같습니다.
print(str(None))  # None
print(repr(None))  # None

print(f"{None!s}")  # None
print(f"{None!r}")  # None

# 숫자도 보통 비슷합니다.
print(str(123))  # 123
print(repr(123))  # 123

# 차이가 잘 나는 건 문자열, 날짜, 커스텀 객체 같은 것들입니다.
# 여기서 !r이 유용한 이유는 이겁니다.

value = "123"
print(f"value={value}")  # value=123

# 출력: value=123
# 이러면 숫자 123인지 문자열 "123"인지 헷갈립니다.
print(f"value={value!r}")  # value='123'

# 정리:
# !s = str()로 변환해서 넣기. 사용자에게 보여줄 출력에 가깝다.
# !r = repr()로 변환해서 넣기. 개발자가 디버깅할 때 좋다.
```

- :s는 다른 의미이다 - format specifier
    - !s, !r은 포맷 전에 어떤 문자열 변환할지 고르는 `conversion flag`
    - !a도 존재한다. -> ascii 로 변환.
    - 이들은 문자열과 관련된 것, 숫자 / 소수들은 format specifier 개념으로 :을 사용한다. -> :d, :f, :.2f, :x, :>10 같은 것들은 format specifier
- 문자열 관련된 것들은 !s, !r, !a // 숫자들은 :d, :f 처럼. -> 숫자는 추후에 다시 확인

- frozen=True인 dataclass는 생성 후 필드 재할당을 막는다.
- slots=True: 객체가 가질 속성을 고정해 메모리 사용과 오타 실수를 줄인다. -> Why?
    - 객체가 가질 필드를 고정해서 오타/불필요한 속성 추가를 막고 메모리를 줄인다

- tuple[str, ...]: tag 목록도 불변에 가깝게 다룬다. -> Why?
    - tags를 “변하지 않는 문자열 여러 개”로 표현한다.

slots=True

- 객체 필드를 고정한다.
- 오타 속성 추가를 막는다.
- 메모리 사용을 줄인다.

tags: tuple[str, ...]

- tag 목록을 변경 불가능한 값처럼 다룬다.
- str 태그가 0개 이상 들어가는 tuple이라는 뜻이다.

- abc.ABC & abstractmethod & Protocol
    - abc + abstractmethod 조합은 런타임 에러가 발생

- dataclass는 Python 내부에서 다루는 값 객체에 좋다.
- 하지만 외부 입력이 믿을 수 없고, 타입 변환/검증/직렬화가 중요하면 pydantic이 더 적합

```python
from abc import ABC, abstractmethod


class BaseFetcher(ABC):
    @abstractmethod
    def fetch(self, url: str) -> str:
        raise NotImplementedError
```

#### abc.ABC, abc.abtractmethod vs typing.Protocol

- ABC는 명시적 상속 기반의 런타임 계약이고, Protocol은 구조 기반의 정적 타입 계약
- abstractmethod까지 활용해야 정확하게 런타임 계약 발생

#### Eclipse Object

- ...은 “구현은 여기에 없다”는 표시처럼 쓰입니다.

```
Protocol 안의 ...  -> 가능, 관례적으로 좋음
Protocol 안의 pass -> 가능, 동작상 거의 같음
일반 함수의 ...    -> 그냥 아무것도 안 하고 None 반환
ABC + abstractmethod 안의 ... -> 가능
```

## 헷갈린 점

- Python Formatting - PEP8, Black
    - 2개는 다른 영역.
    - PEP 8은 Python 코드 스타일의 공식 원칙이고, Black은 그 원칙을 바탕으로 포맷 논쟁을 줄이기 위해 만든 자동 포매터 스타일
    - 자동 적용은, VSCode에선 설치하고 opt + shf + f // com + opt + l(jetbrain 식)
    - ruff는 통합 도구로써, 실제 포맷팅은 ruff formatter가 수행함. -> 기본 스타일을 black compatible로 사용. 추가 커스터마이징 가능
    - VSCode에선 Black Formatter extension 설치하여 사용

- abc
    - 정확히는 ABC + @abstractmethod를 둘 다 선언한 부모 클래스를 하위 클래스가 상속받고 구현 안하면 런타임 에러 발생.

## 도구 선택 기준

### `class`

- 객체지향 프로그래밍을 하기 위한 기본
- 한줄로 표현하면, 명확하게 하기 위함.
    - 타입 명시(강제는 X)
    - 변수명이 뭔지 명확하게
- 메소드를 선언해서 출력과 같이 필요한 부가 기능 선언 가능.
- 이러한 부가 기능과 책임을 명확하게 하기 위해서 dict보다는 class로 관리

### `dataclass`

- 생성자 축약, frozen, slots 같은 옵션들이 존재함
- 데이터를 담는 클래스이면 안쓸 이유가 없음.
- frozen, slots들은 일반 클래스들에도 사용해도 괜찮아보임(Fetcher, Parser에도)
    - 없는거보단 나은 듯?

### `Protocol` / `ABC`

- Abstraction + Polymorphism의 영역
- Protocol은 비교적 단순하게 이렇게 쓸거다! 하는 타입 힌팅을 명확하게 명시하는 수준
    - 이것도 안쓰는 것보단 쓰는게 좋음
- ABC에서는 구현 규약을 명시적으로 선언이 필요할 때 사용 (상속 기반)
    - abstractmethod와 활용 시 런타임 제약이 필요한 상황에서 사용

### `pydantic`

- dataclass를 넘어서 실제 타입을 런타임에서 raise하거나, 직렬화 / 역직렬화의 기능이 필요할 때 사용
- dataclass는 파이썬 내부에서 사용되는 객체에서 편하게 쓰면 되지만, pydantic는 추가적으로 해당 데이터의 정합성이나 신뢰성을 갖기 위해 사용.

## 다음에 해볼 것

- v2 만들어서 확장 과제 진행

#### V2 실습

1. 2 페이지까지 가게한다. -> QuoteScraper의 책임?
2. quote 개수 집계 -> -> QuoteScraper의 책임?
3. tag 하나를 입력해서 해당 태그의 quote를 출력 -> QuoteScraper의 책임?

- 현재 클래스 구조에선 모두 QuoteScraper의 책임임.
- 다만, 2, 3은 QuoteScraper의 책임이라고 볼 수 있을까? 별도 작업자가 있어야할 것 같음. -> 검토 받자 

- 결론 : 나누는게 맞다. 2, 3 이 QuoteScraper의 책임으로 들어가면 책임이 너무 많아진다.
- 이를 나누기 위한 클래스는 별도로 잡는다.