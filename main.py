import streamlit as st

# 1️⃣ 페이지 설정
st.set_page_config(
    page_title="🍦 배스킨라빈스 키오스크 🥰",
    page_icon="🍧",
    layout="centered"
)

# 2️⃣ 스타일 적용 (흰색 배경 + 은은한 연핑크 포인트)
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        font-family: 'Comic Sans MS', sans-serif;
    }
    .big-font {
        font-size:28px !important;
        color:#ff99cc; /* 은은한 연핑크 */
        font-weight:bold;
    }
    .cute-button {
        background-color:#ffb3d9; /* 연핑크 포인트 */
        color:white;
        font-weight:bold;
        border-radius:12px;
        padding:10px 20px;
    }
    .flavor-box {
        background-color:#ffe6f2; /* 아주 연한 핑크 */
        border-radius:10px;
        padding:5px 10px;
        margin:5px;
        display:inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# 3️⃣ 언어 선택
st.markdown('<p class="big-font">🍦 언어를 선택해주세요 🥰 ナルトまき!</p>', unsafe_allow_html=True)
language = st.radio("Language / 言語 / 언어", ("한국어 🇰🇷", "日本語 🇯🇵", "English 🇺🇸"))

# 4️⃣ 언어별 텍스트 설정
text = {}
if language == "한국어 🇰🇷":
    text = {
        "service": "🥄 이용 방식을 선택해주세요",
        "container": "🍨 용기를 선택해주세요",
        "flavor": "🍦 맛을 선택해주세요 (여러 개 가능)",
        "cart": "🛒 총 가격: {}원",
        "payment": "💳 결제 방법을 선택해주세요",
        "order_done": "주문 완료! {} {} 선택됨 🥰\n총 {}원, 결제: {}"
    }
elif language == "日本語 🇯🇵":
    text = {
        "service": "🥄 ご利用方法を選んでください",
        "container": "🍨 容器を選んでください",
        "flavor": "🍦 フレーバーを選んでください (複数選択可)",
        "cart": "🛒 合計金額: {}円",
        "payment": "💳 支払い方法を選んでください",
        "order_done": "注文完了! {} {} 選択されました 🥰\n合計 {}円, 支払い: {}"
    }
else:  # English 🇺🇸
    text = {
        "service": "🥄 Please choose your service type",
        "container": "🍨 Please choose a container",
        "flavor": "🍦 Choose your flavors (multiple allowed)",
        "cart": "🛒 Total Price: {} won",
        "payment": "💳 Choose payment method",
        "order_done": "Order complete! {} {} selected 🥰\nTotal: {} won, Payment: {}"
    }

# 5️⃣ 이용 방식 선택
st.markdown(f'<p class="big-font">{text["service"]}</p>', unsafe_allow_html=True)
service_type = st.radio("Service / サービス / 서비스", ("매장", "포장"))

# 6️⃣ 용기 선택
st.markdown(f'<p class="big-font">{text["container"]}</p>', unsafe_allow_html=True)
container = st.selectbox("Container / 容器 / 용기", ("싱글", "더블", "파인트"))

# 7️⃣ 맛 선택
flavors = ["바닐라", "초코", "스트로베리", "민트초코", "쿠키앤크림"]
price_dict = {"싱글": 3000, "더블": 5000, "파인트": 10000}

st.markdown(f'<p class="big-font">{text["flavor"]}</p>', unsafe_allow_html=True)
selected_flavors = st.multiselect("Flavors / フレーバー / 맛", flavors)

# 8️⃣ 장바구니 계산
base_price = price_dict[container]
flavor_count = len(selected_flavors)
total_price = base_price + flavor_count * 500  # 맛 추가 시 500원

st.markdown(f'<p class="big-font">{text["cart"].format(total_price)}</p>', unsafe_allow_html=True)

# 9️⃣ 결제 방법
st.markdown(f'<p class="big-font">{text["payment"]}</p>', unsafe_allow_html=True)
payment_method = st.radio("Payment / 支払い / 결제", ("현금", "카드", "간편결제"))

# 10️⃣ 주문 완료 버튼
if st.button("✅ 주문 완료", key="order"):
    st.success(text["order_done"].format(container, selected_flavors, total_price, payment_method))
