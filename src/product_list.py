# (자동 줄바꿈 방지)
# fmt: off
product_list = {
    "옷": ["티셔츠", "청바지", "드레스", "자켓", "모자", "가디건", "스웨터", "스커트", "후드티", "비치웨어", "트레이닝복", "수영복", "비올레인 코트", "한복", "목도리", "팬티", "코트", "내복 상의", "내복 하의", "니트", "벨트"],
    "전자 기기": ["노트북", "스마트폰", "테블릿", "냉장고", "세탁기", "에어컨", "카메라", "드론", "스마트 워치", "게임 콘솔", "헤드폰 앰프", "모니터", "마우스", "키보드", "노이즈 캔슬링 이어폰", "충전기", "휴대폰 케이스", "헤어 드라이기", "보조 배터리", "USB", "외장하드", "SSD"],
    "가구": ["소파", "침대", "탁자", "의자", "장롱", "서랍장", "화장대", "식탁", "거울", "선반", "책상", "책장", "옷장", "화장실 세트", "침대 테이블"],
    "스포츠 용품": ["축구공", "농구공","테니스공", "셔틀콕", "헬스 자전거", "등산 모자", "스케이트보드", "테니스 라켓", "골프 클럽", "스키 장비", "야구 글러브", "스노보드", "체육복", "수영 기구", "스쿼시 라켓"],
    "오디오 디바이스": ["헤드폰", "스피커", "이어폰", "오디오 레코더", "사운드 바", "이퀄라이저", "음향 카드", "마이크", "턴테이블", "DJ 컨트롤러", "이어폰 케이스", "블루투스 스피커", "음악 플레이어", "오디오 인터페이스", "음향 프로세서"],
    "캠핑 용품": ["텐트", "취사도구", "침낭", "등산화", "캠핑 의자", "랜턴", "아이젠", "포터블 그릴", "햇빛 차단 우산", "손전등", "캠핑 테이블", "카약", "등산 지팡이", "캠핑 코티", "야외 매트"],
    "헤어": ["샴푸", "린스", "헤어 드라이어", "헤어 스프레이", "헤어 컬러", "헤어 클리퍼", "헤어 롤", "헤어 브러시", "헤어 마스크", "헤어 오일", "헤어 밴드", "헤어 핀", "헤어 터번", "헤어 스트레이트너", "헤어 커버"],
    "골프 용품": ["골프 클럽 세트", "골프 공", "골프 가방", "골프 슈즈", "골프 장갑", "골프 캡", "골프 트레이닝 에이드", "골프 티", "골프 우산", "골프 스탠드백", "골프 카트", "골프 풀종", "골프 스윙 트레이너", "골프 코스용 지폐 매트", "골프 퍼터"],
    "운동 기구": ["트레드밀", "사이클", "레그 프레스 머신", "덤벨", "바벨", "풀업 바", "평행봉", "플라이 박스", "스탭 박스", "헬스볼", "요가 매트", "폼 롤러", "키네시올로지 테이프", "밴드", "스텝 플랫폼"],
    "식품": ["쌀", "밀가루", "설탕", "소금", "식용유", "우유", "계란", "닭고기", "소고기", "생선", "과일", "야채", "떡", "라면", "커피", "초콜릿", "즉석밥", "과자", "버터", "생수", "닭가슴살", "닭다리", "영양제", "반찬", "견과류", "빵", "샌드위치", "차", "삼겹살"],
    "뷰티": ["폼클렌징", "마스크팩", "앰플", "세럼", "스킨", "로션", "올인원", "크림", "달팽이크림", "향수", "네일", "수딩젤", "쿠션", "립스틱", "립밤", "안티에이징", "미스트", "오일", "썬크림"],
    "신발": ["런닝화", "스니커즈", "컨버스", "운동화", "경량 운동화", "에어 운동화", "샌들", "슬리퍼", "쪼리", "구두", "하이힐", "아쿠아슈즈", "양말", "축구화", "풋살화", "농구화", "배드민턴화"]
}


combi = {
    "옷": ["", "남자", "여자", "아기"],
    "식품": ["", "농심", "오뚜기"],
    "전자 기기": ["", "삼성", "애플", "샤오미"],
    "뷰티": ["", "닥터지", "이니스프리", "AHC", "일리윤", "라운드랩"],
    "신발": ["", "나이키", "아디다스"]
}


# fmt: on
def make_combi(a: list, b: list):
    lst = []
    for x in a:
        for y in b:
            if x == "":
                lst.append(y)
            else:
                lst.append(x + " " + y)
    return lst


# 개수 몇개인지 & 중복 검사

COMBI_PRODUCT_LIST: list[str] = []

for key in product_list.keys():
    # 단어 조합 생성
    combi_list = (
        product_list[key]
        if key not in combi.keys()
        else make_combi(combi[key], product_list[key])
    )
    for x in combi_list:
        if x in COMBI_PRODUCT_LIST:  # 중복 검사
            print(x)
        COMBI_PRODUCT_LIST.append(x)

if __name__ == "__main__":
    print(COMBI_PRODUCT_LIST)
