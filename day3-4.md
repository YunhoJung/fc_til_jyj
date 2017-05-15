#Day 4
---
###1) CSS 화면 표시 속성

* `display`는 `block`으로 블록 속성을 가지게 할 수 있는 등 레이아웃 구성에 영향을 끼친다. 특히 `inline-block`은 인라인 요소 안에 블럭을 넣을 수 있게 해준다.
* `visibilty`는 보일지 숨길지를 정할 수 있지만 공간은 차지한다.
* `flow`는 내용이 박스보다 클 때 어떻게 보여줄지 정한다.

###2) float
`float`은 대상을 레이아웃 상에서 공중에 띄워주는 역할을 하며, 블럭이라고 하더라도 겹쳐지게끔 만들어준다. 다만 띄워졌다 해서 아래의 요소가 `float` 밑으로 들어갈 순 있지만, `float`이 위쪽의 요소로 말려 들어가진 않는다.

> `left`와 `right`를 이용해 `float`한 요소들을 좌우정렬할 수 있다.

#### -clear 속성
`clear` 속성은 요소가 `float`과 겹치는 경우 겹치지 않게끔 해주는 속성이다.
이를 응용해서 `float` 레이아웃을 만들 때 부모 요소가 찌그러지는 현상을 방지할 수도 있다.

> 레이아웃의 마지막에 아무런 크기를 가지지 않는 값에 `clear` 속성을 주면 된다.

### 3) position
`position`은 요소의 위치를 지정해주는 것으로 기본 속성은 `static`이다. 모두 `top`, `right` 등으로 세밀한 위치 조정이 가능하다.

* `relative` : 자기 자신을 기준으로 한다.
* `fixed` : 브라우저의 창을 기준으로 한다.
* `absolute` : `static` 속성이 아닌 가장 가까운 부모를 기준으로 한다.

### - 시멘틱 태그
아무련 뜻과 효과는 없지만 자주 사용하는 구조를 태그화 시킨 태그들. `nav`, `header` 등이 있다.

### 4) sass
`sass`란 `css`의 확장 언어로 개발자가 작업하기 쉽게 해준다.

> `sass` 같은 확장 언어를 사용할 땐 전처리기를 이용해 css파일로 변환하는 과정이 필요하다.

####간단한 기능들

* //주석 기능 지원 (css상에서는 사라짐)
* 대괄호 중첩 구조 지원.
	* 부모 참조 선택자(&) : 중첩 구조에서 &라는 부모를 지칭하는 선택자를 제공해준다.
	*중첩 속성 : `margin-left`, `margin-right`같이 동일한 카테고리의 속성을 대괄호로 묶어 한번에 정해줄 수 있다.
* 상속 지원.
	* `@extend 선택자`를 사용하면 대상의 스타일을 상속받을 수 있다.
	* 선택자 앞에 %를 붙여 가상의 스타일을 만들 수도 있다. 가상 스타일은 `css`상에서는 없어진다.
* 변수 지원. `$`를 이용해 선언 가능하다. 숫자부터 문자, 색상, boolean, 리스트, 맵, null 등 대부분의 변수 자료형을 제공한다. (자료형 선언은 필요없음.)
* import 지원. `@import '파일명';`으로 현재 파일의 위치를 기준으로 파일을 불러온다. 
	* `_`로 시작하는 파일명은 호출은 되지만 `css`로 컴파일이 되지는 않는다. 주로 변수 선언 시에 사용하면 된다.