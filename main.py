import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="🍦 배스킨라빈스 키오스크",
    page_icon="🍧",
    layout="centered"
)

# 2. 스타일 적용 (연핑크 + 체크무늬)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #ffe6f0, #fff);
        font-family: 'Comic Sans MS', sans-serif;
    }
    .big-font {
        font-size:30px !important;
        color:#ff69b4;
        font-weight:bold;
    }
    .cute-button {
        background-color:#ffb6c1;
        color:white;
        font-weight:bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 언어 선택
st.markdown('<p class="big-font">🍦 안녕하세요! 언어를 선택해주세요 🥰</p>', unsafe_allow_html=True)
language = st.radio("Language / 言語 / 언어", ("한국어 🇰🇷", "日本語 🇯🇵", "English 🇺🇸"))

# 4. 이용 방식 선택
st.markdown('<p class="big-font">🥄 이용 방식을 선택해주세요</p>', unsafe_allow_html=True)
service_type = st.radio("이용 방식", ("매장", "포장"))

# 5. 용기 선택
st.markdown('<p class="big-font">🍨 용기를 선택해주세요</p>', unsafe_allow_html=True)
container = st.selectbox("용기", ("싱글", "더블", "파인트"))

# 6. 맛 선택 (용기별 가격)
flavors = ["바닐라", "초코", "스트로베리", "민트초코", "쿠키앤크림"]
price_dict = {"싱글": 3000, "더블": 5000, "파인트": 10000}

st.markdown('<p class="big-font">🍦 맛을 선택해주세요 (여러 개 가능)</p>', unsafe_allow_html=True)
selected_flavors = st.multiselect("맛 선택", flavors)

# 7. 장바구니 가격 계산
base_price = price_dict[container]
flavor_count = len(selected_flavors)
total_price = base_price + flavor_count * 500  # 맛 추가 시 500원씩

st.markdown(f'<p class="big-font">🛒 총 가격: {total_price}원</p>', unsafe_allow_html=True)

# 8. 결제 방법
st.markdown('<p class="big-font">💳 결제 방법을 선택해주세요</p>', unsafe_allow_html=True)
payment_method = st.radio("결제 방법", ("현금", "카드", "간편결제"))

if st.button("✅ 주문 완료", key="order"):
    st.success(f"주문 완료! {container} {selected_flavors} 선택됨 🥰\n총 {total_price}원, 결제: {payment_method}")
