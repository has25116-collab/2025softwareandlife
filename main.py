import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="🍦 배스킨라빈스 키오스크 🥰", page_icon="🍧", layout="centered")

# --- 스타일 (웜핑크, 버튼, 흰색 배경) ---
st.markdown("""
<style>
.stApp { background-color: #ffffff; font-family: 'Comic Sans MS', sans-serif; }
.big-font { font-size:28px !important; color:#ff80b3; font-weight:bold; }
.button-big { 
    background-color:#ffb6c1; color:white; font-weight:bold; border-radius:15px; padding:20px; 
    font-size:20px; width:200px; margin:10px 0px;
}
.flavor-box { background-color:#ffe6f2; border-radius:12px; padding:10px 15px; margin:5px; display:inline-block; }
</style>
""", unsafe_allow_html=True)

# --- 키티 이미지 (무료 예시 URL) ---
st.image("https://upload.wikimedia.org/wikipedia/en/0/0b/Hello_Kitty.svg", width=100)

# --- 상태 초기화 ---
if "step" not in st.session_state: st.session_state.step = 1
if "language" not in st.session_state: st.session_state.language = None
if "service_type" not in st.session_state: st.session_state.service_type = None
if "container" not in st.session_state: st.session_state.container = None
if "selected_flavors" not in st.session_state: st.session_state.selected_flavors = []
if "payment_method" not in st.session_state: st.session_state.payment_method = None

# --- 언어별 텍스트 ---
def get_text():
    lang = st.session_state.language
    if lang == "한국어":
        return {
            "service":["매장","포장"],
            "container":["싱글","더블","파인트"],
            "flavor":["바닐라","초코","스트로베리","민트초코","쿠키앤크림"],
            "payment":["현금","카드","간편결제"],
            "next":"다음",
            "order_done":"주문 완료! {} {} 선택됨 🥰\n총 {}원, 결제: {}",
            "lang_title":"🍦 언어를 선택해주세요 🥰"
        }
    elif lang == "日本語":
        return {
            "service":["店内","持ち帰り"],
            "container":["シングル","ダブル","パイント"],
            "flavor":["バニラ","チョコ","ストロベリー","ミントチョコ","クッキー＆クリーム"],
            "payment":["現金","カード","簡単決済"],
            "next":"次へ",
            "order_done":"注文完了! {} {} 選択されました 🥰\n合計 {}円, 支払い: {}",
            "lang_title":"🍦 言語を選んでください 🥰"
        }
    else:
        return {
            "service":["In-store","Takeout"],
            "container":["Single","Double","Pint"],
            "flavor":["Vanilla","Chocolate","Strawberry","Mint Choco","Cookies & Cream"],
            "payment":["Cash","Card","EasyPay"],
            "next":"Next",
            "order_done":"Order complete! {} {} selected 🥰\nTotal: {} won, Payment: {}",
            "lang_title":"🍦 Please select your language 🥰"
        }

# --- 다음 단계 ---
def next_step(): st.session_state.step += 1

# --- 단계별 화면 ---
if st.session_state.step == 1:
    st.markdown(f'<p class="big-font">{get_text()["lang_title"]}</p>', unsafe_allow_html=True)
    cols = st.columns(3)
    langs = ["한국어","日本語","English"]
    for i, l in enumerate(langs):
        if cols[i].button(l, key=f"lang_{l}"):
            st.session_state.language = l
            next_step()

elif st.session_state.step == 2:
    text = get_text()
    st.markdown('<p class="big-font">🥄 이용 방식을 선택해주세요</p>', unsafe_allow_html=True)
    cols = st.columns(len(text["service"]))
    for i, s in enumerate(text["service"]):
        if cols[i].button(s, key=f"service_{s}"):
            st.session_state.service_type = s
            next_step()

elif st.session_state.step == 3:
    text = get_text()
    st.markdown('<p class="big-font">🍨 용기를 선택해주세요</p>', unsafe_allow_html=True)
    cols = st.columns(len(text["container"]))
    for i, c in enumerate(text["container"]):
        if cols[i].button(c, key=f"container_{c}"):
            st.session_state.container = c
            next_step()

elif st.session_state.step == 4:
    text = get_text()
    st.markdown('<p class="big-font">🍦 맛을 선택해주세요 (여러 개 가능)</p>', unsafe_allow_html=True)
    selected = []
    cols = st.columns(3)
    for i, f in enumerate(text["flavor"]):
        if cols[i%3].button(f, key=f"flavor_{f}"):
            if f not in st.session_state.selected_flavors:
                st.session_state.selected_flavors.append(f)
    if st.button(text["next"]):
        next_step()

elif st.session_state.step == 5:
    text = get_text()
    price_dict = {"싱글":3000,"더블":5000,"파인트":10000,
                  "シングル":3000,"ダブル":5000,"パイント":10000,
                  "Single":3000,"Double":5000,"Pint":10000}
    base_price = price_dict[st.session_state.container]
    flavor_count = len(st.session_state.selected_flavors)
    total_price = base_price + flavor_count * 500
    st.markdown(f'<p class="big-font">🛒 총 가격: {total_price}원</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">💳 결제 방법을 선택해주세요</p>', unsafe_allow_html=True)
    cols = st.columns(len(text["payment"]))
    for i, p in enumerate(text["payment"]):
        if cols[i].button(p, key=f"payment_{p}"):
            st.session_state.payment_method = p
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
