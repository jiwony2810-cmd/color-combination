import streamlit as st
import pandas as pd

# 1. 색상 리스트 구성
color_list_1 = ["빨강", "주황", "노랑", "초록", "파랑", "남색", "보라", "검정", "하양", "회색"]
color_list_2 = ["하양", "검정", "베이지", "연두", "하늘", "분홍", "갈색", "금색", "은색", "네이비"]

# 2. '하' 뱃지가 나오는 특정 조합
bad_combos = [
    ("빨강", "연두"), ("주황", "분홍"), ("초록", "분홍"), 
    ("파랑", "갈색"), ("보라", "갈색"), ("검정", "갈색"), ("노랑", "은색")
]

# 3. 디테일한 색상 혼합 로직
def get_mixed_color(c1, c2):
    mix_map = {
        ("빨강", "하양"): "핑크", ("빨강", "검정"): "다크레드", ("빨강", "베이지"): "코랄(산호색)", 
        ("빨강", "하늘"): "자주(마젠타)", ("빨강", "갈색"): "벽돌색", ("빨강", "금색"): "브론즈", 
        ("빨강", "네이비"): "버건디",
        ("주황", "하양"): "살구색", ("주황", "검정"): "브라운", ("주황", "베이지"): "탠(Tan)",
        ("노랑", "하양"): "크림색", ("노랑", "검정"): "카키그린", ("노랑", "베이지"): "버터색",
        ("노랑", "하늘"): "민트그린", ("노랑", "분홍"): "피치", ("노랑", "갈색"): "머스터드(겨자색)",
        ("초록", "하양"): "파스텔그린", ("초록", "하늘"): "청록(시안)", ("초록", "베이지"): "카모플라쥬",
        ("파랑", "하양"): "스카이블루", ("파랑", "검정"): "미드나잇블루", ("파랑", "베이지"): "애쉬블루",
        ("파랑", "연두"): "틸(Teal)", ("파랑", "분홍"): "라벤더", ("파랑", "은색"): "아이스블루",
        ("남색", "하늘"): "오션블루", ("남색", "분홍"): "모브(Mauve)", ("남색", "은색"): "스틸블루",
        ("보라", "하양"): "라일락", ("보라", "연두"): "형광보라", ("보라", "금색"): "로열퍼플",
        ("검정", "하양"): "차콜그레이", ("하양", "검정"): "라이트그레이", ("회색", "베이지"): "그레이지"
    }

    if (c1, c2) in mix_map:
        return mix_map[(c1, c2)]

    if c2 == "하양": return f"파스텔 {c1}"
    if c2 == "검정": return f"다크 {c1}"
    if c2 == "베이지": return f"소프트 {c1}"
    if c2 == "은색": return f"메탈릭 {c1}"
    if c2 == "금색": return f"웜(Warm) {c1}"
    if c2 == "갈색": return f"빈티지 {c1}"
    if c2 == "네이비": return f"딥(Deep) {c1}"
    if c2 == "하늘": return f"쿨(Cool) {c1}"
    if c2 == "분홍": return f"로지(Rosy) {c1}"
    if c2 == "연두": return f"프레시 {c1}"

    return f"혼합된 {c1}"

def evaluate_combo(c1, c2):
    score = "🔴 하" if (c1, c2) in bad_combos else "🟢 상"
    mixed_color = get_mixed_color(c1, c2)
    return score, mixed_color

# ==========================================
# 4. Streamlit 화면 구성
# ==========================================

st.set_page_config(page_title="색깔 조합 가이드", page_icon="🎨")
st.title("🎨 색깔 조합 가이드 시스템")
st.write("두 가지 색상을 선택하고 조합해보세요!")

if "history" not in st.session_state:
    st.session_state.history = []

col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    c1 = st.selectbox("리스트 1:", color_list_1, index=color_list_1.index("빨강"))

with col2:
    c2 = st.selectbox("리스트 2:", color_list_2, index=color_list_2.index("하늘"))

with col3:
    st.write("") 
    st.write("")
    combine_clicked = st.button("✨ 조합하기", use_container_width=True)

if combine_clicked:
    score, mixed_color = evaluate_combo(c1, c2)
    
    st.session_state.history.insert(0, {
        "선택 색상 1": c1,
        "선택 색상 2": c2,
        "결과 색상": mixed_color,
        "맑음 수치": score
    })

if st.session_state.history:
    st.markdown("### 📊 조합 결과")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True, hide_index=True)
