import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="🍦 배스킨라빈스 키오스크 🥰", page_icon="🍧", layout="centered")

# --- 스타일 ---
st.markdown("""
<style>
.stApp { background-color: #ffffff; font-family: 'Comic Sans MS', sans-serif; }
.big-font { font-size:28px !important; color:#ff99cc; font-weight:bold; }
.cute-button { background-color:#ffb3d9; color:white; font-weight:bold; border-radius:12px; padding:10px 20px; }
.flavor-box { background-color:#ffe6f2; border-radius:10px; padding:5px 10px; margin:5px; display:inline-block; }
</style>
""", unsafe_allow_html=True)

# --- 상태 초기화 ---
if "step" not in st.session_state:
    st.session_state.step = 1
if "language" not in st.session_state:
    st.session_state.language = None
if "service_type" not in st.session_state:
    st.session_state.service_type = None
if "container" not in st.session_state:
    st.session_state.container = None
if "selected_flavors" not in st.session_state:
    st.session_state.selected_flavors = []
if "payment_method" not in st.session_state:
    st.session_state.payment_method = None

# --- 언어별 텍스트 ---
def get_text():
    lang = st.session_state.language
    if lang == "한국어 🇰🇷":
        return {
            "service":"🥄 이용 방식을 선택해주세요",
            "container":"🍨 용기를 선택해주세요",
            "flavor":"🍦 맛을 선택해주세요 (여러 개 가능)",
            "cart":"🛒 총 가격: {}원",
            "payment":"💳 결제 방법을 선택해주세요",
            "order_done":"주문 완료! {} {} 선택됨 🥰\n총 {}원, 결제: {}"
        }
    elif lang == "日本語 🇯🇵":
        return {
            "service":"🥄 ご利用方法を選んでください",
            "container":"🍨 容器を選んでください",
            "flavor":"🍦 フレーバーを選んでください (複数選択可)",
            "cart":"🛒 合計金額: {}円",
            "payment":"💳 支払い方法を選んでください",
            "order_done":"注文完了! {} {} 選択されました 🥰\n合計 {}円, 支払い: {}"
        }
    else:
        return {
            "service":"🥄 Please choose your service type",
            "container":"🍨 Please choose a container",
            "flavor":"🍦 Choose your flavors (multiple allowed)",
            "cart":"🛒 Total Price: {} won",
            "payment":"💳 Choose payment method",
            "order_done":"Order complete! {} {} selected 🥰\nTotal: {} won, Payment: {}"
        }

# --- 다음 단계 버튼 ---
def next_step():
    st.session_state.step += 1

# --- 단계별 화면 ---
if st.session_state.step == 1:
    st.markdown('<p class="big-font">🍦 언어를 선택해주세요 🥰 ナルトまき!</p>', unsafe_allow_html=True)
    st.session_state.language = st.radio("Language / 言語 / 언어", ("한국어 🇰🇷", "日本語 🇯🇵", "English 🇺🇸"))
    if st.button("다음", key="lang_next"):
        next_step()

elif st.session_state.step == 2:
    text = get_text()
    st.markdown(f'<p class="big-font">{text["service"]}</p>', unsafe_allow_html=True)
    st.session_state.service_type = st.radio("Service / サービス / 서비스", ("매장", "포장"))
    if st.button("다음", key="service_next"):
        next_step()

elif st.session_state.step == 3:
    text = get_text()
    st.markdown(f'<p class="big-font">{text["container"]}</p>', unsafe_allow_html=True)
    st.session_state.container = st.selectbox("Container / 容器 / 용기", ("싱글", "더블", "파인트"))
    if st.button("다음", key="container_next"):
        next_step()

elif st.session_state.step == 4:
    text = get_text()
    st.markdown(f'<p class="big-font">{text["flavor"]}</p>', unsafe_allow_html=True)
    flavors = ["바닐라", "초코", "스트로베리", "민트초코", "쿠키앤크림"]
    st.session_state.selected_flavors = st.multiselect("Flavors / フレーバー / 맛", flavors)
    if st.button("다음", key="flavor_next"):
        next_step()

elif st.session_state.step == 5:
    text = get_text()
    price_dict = {"싱글":3000,"더블":5000,"파인트":10000}
    base_price = price_dict[st.session_state.container]
    flavor_count = len(st.session_state.selected_flavors)
    total_price = base_price + flavor_count * 500
    st.markdown(f'<p class="big-font">{text["cart"].format(total_price)}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">{text["payment"]}</p>', unsafe_allow_html=True)
    st.session_state.payment_method = st.radio("Payment / 支払い / 결제", ("현금", "카드", "간편결제"))
    if st.button("주문 완료", key="order_finish"):
        st.session_state.total_price = total_price
        next_step()

elif st.session_state.step == 6:
    text = get_text()
    st.success(text["order_done"].format(
        st.session_state.container,
        st.session_state.selected_flavors,
        st.session_state.total_price,
        st.session_state.payment_method
    ))
    if st.button("처음으로 돌아가기"):
        st.session_state.step = 1
        st.session_state.language = None
        st.session_state.service_type = None
        st.session_state.container = None
        st.session_state.selected_flavors = []
        st.session_state.payment_method = None
