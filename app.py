import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 1. 색상 리스트 구성
color_list_1 = ["빨강", "주황", "노랑", "초록", "파랑", "남색", "보라", "검정", "하양", "회색"]
color_list_2 = ["하양", "검정", "베이지", "연두", "하늘", "분홍", "갈색", "금색", "은색", "네이비"]

# 2. '하' 뱃지가 나오는 특정 조합
bad_combos = [
    ("빨강", "연두"), 
    ("주황", "분홍"), 
    ("초록", "분홍"), 
    ("파랑", "갈색"), 
    ("보라", "갈색"), 
    ("검정", "갈색"), 
    ("노랑", "은색")
]

# 3. 디테일한 색상 혼합 로직
def get_mixed_color(c1, c2):
    # 특수하게 완전히 새로운 색이 나오는 세밀한 조합 사전
    mix_map = {
        # 빨강 계열
        ("빨강", "하양"): "핑크", ("빨강", "검정"): "다크레드", ("빨강", "베이지"): "코랄(산호색)", 
        ("빨강", "하늘"): "자주(마젠타)", ("빨강", "갈색"): "벽돌색", ("빨강", "금색"): "브론즈", 
        ("빨강", "네이비"): "버건디",
        
        # 주황/노랑 계열
        ("주황", "하양"): "살구색", ("주황", "검정"): "브라운", ("주황", "베이지"): "탠(Tan)",
        ("노랑", "하양"): "크림색", ("노랑", "검정"): "카키그린", ("노랑", "베이지"): "버터색",
        ("노랑", "하늘"): "민트그린", ("노랑", "분홍"): "피치", ("노랑", "갈색"): "머스터드(겨자색)",

        # 초록/파랑 계열 (사용자 예시 뉘앙스 적용)
        ("초록", "하양"): "파스텔그린", ("초록", "하늘"): "청록(시안)", ("초록", "베이지"): "카모플라쥬",
        ("파랑", "하양"): "스카이블루", ("파랑", "검정"): "미드나잇블루", ("파랑", "베이지"): "애쉬블루",
        ("파랑", "연두"): "틸(Teal)", ("파랑", "분홍"): "라벤더", ("파랑", "은색"): "아이스블루",

        # 남색/보라/무채색 계열
        ("남색", "하늘"): "오션블루", ("남색", "분홍"): "모브(Mauve)", ("남색", "은색"): "스틸블루",
        ("보라", "하양"): "라일락", ("보라", "연두"): "형광보라", ("보라", "금색"): "로열퍼플",
        ("검정", "하양"): "차콜그레이", ("하양", "검정"): "라이트그레이", ("회색", "베이지"): "그레이지"
    }

    # 1. 위 사전에 정확히 일치하는 조합이 있다면 그 이름을 반환
    if (c1, c2) in mix_map:
        return mix_map[(c1, c2)]

    # 2. 사전에 없는 나머지 조합들은 색상의 특징을 살린 세련된 단어로 조합
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

# 4. 최종 평가 함수
def evaluate_combo(c1, c2):
    if (c1, c2) in bad_combos:
        score = "하"
    else:
        score = "상"
        
    mixed_color = get_mixed_color(c1, c2)
    return score, mixed_color

# 5. GUI 시스템 구성
def on_combine_click():
    c1 = combo1.get()
    c2 = combo2.get()
    
    if not c1 or not c2:
        messagebox.showwarning("입력 오류", "두 가지 색상을 모두 선택해주세요!")
        return
        
    score, mixed_color = evaluate_combo(c1, c2)
    
    # 표(Treeview)의 맨 윗줄에 최신 결과 추가
    tree.insert("", "0", values=(c1, c2, mixed_color, score))

# 메인 윈도우 생성
root = tk.Tk()
root.title("🎨 색깔 조합 가이드 시스템")
root.geometry("520x400")
root.configure(padx=20, pady=20)

# 상단 입력부 프레임 (힌트 제거됨)
input_frame = tk.Frame(root)
input_frame.pack(pady=(20, 10))

tk.Label(input_frame, text="리스트 1:").grid(row=0, column=0, padx=5)
combo1 = ttk.Combobox(input_frame, values=color_list_1, state="readonly", width=10)
combo1.grid(row=0, column=1, padx=5)
combo1.set("빨강")

tk.Label(input_frame, text=" + ").grid(row=0, column=2, padx=5)

tk.Label(input_frame, text="리스트 2:").grid(row=0, column=3, padx=5)
combo2 = ttk.Combobox(input_frame, values=color_list_2, state="readonly", width=10)
combo2.grid(row=0, column=4, padx=5)
combo2.set("하늘")

# 조합하기 버튼
btn_combine = tk.Button(root, text="✨ 조합하기", command=on_combine_click, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black", pady=5)
btn_combine.pack(pady=15)

# 하단 결과 표(Treeview) 프레임
columns = ("color1", "color2", "mixed", "score")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)

tree.heading("color1", text="선택 색상 1")
tree.heading("color2", text="선택 색상 2")
tree.heading("mixed", text="결과 색상")
tree.heading("score", text="맑음 수치")

tree.column("color1", width=80, anchor="center")
tree.column("color2", width=80, anchor="center")
tree.column("mixed", width=180, anchor="center") # 결과 색상 글자가 길어질 수 있어 너비 확대
tree.column("score", width=80, anchor="center")

tree.pack(fill="x")

root.mainloop()
