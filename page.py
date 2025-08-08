import streamlit as st
from pathlib import Path
import base64

# 로고
img_path = Path("assets/Logo.png")
print(img_path.exists())

def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        b64_str = base64.b64encode(img_file.read()).decode()
    return b64_str

img_b64 = img_to_base64(img_path)

# 마크다운
st.markdown(
    f"""
    <style>
    
    /* 배경 */
    .stApp {{
        background-color: #F36F20;
    }}

    /* 로고 */
    .custom-logo {{
        position: fixed;
        top: 30px;
        left: 50px;
        width: 300px;
    }}

    /* 헤더 숨기기 */
    header[data-testid="stHeader"] {{
        display: none;
    }}
    
    /* 메인 박스 */
    section > div {{
        height: 100% !important;
        max-height: none !important;
        width: 100% !important;
        max-width: none !important;
    }}

    section > div > div {{
        background-color: white !important;
        padding: 50px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
        height: 100% !important;
        width: 85% !important;
        margin: 80px auto 40px auto !important;
        color: rgba(0, 0, 0, 0.7) !important;
    }}
    
    </style>



    <img src="data:image/png;base64,{img_b64}" class="custom-logo" />
    """,
    unsafe_allow_html=True
)





with st.container():
    # 좌우 박스 생성
    left_col, right_col = st.columns([1, 4])  # 비율

    with left_col:
        st.markdown('''
        <div style="position: relative; background-color: #FFF3EB; min-height: 60vh; border-radius: 8px; display: flex; flex-direction: column; align-items: flex-start; justify-content: center; font-size: 25px; font-weight: bold; color: rgba(0, 0, 0, 0.7); padding: 0; gap: 20px;">
            <div style="display: flex; align-items: center;">
                <div style="background-color: rgba(138, 138, 138, 0.2); color: rgba(0, 0, 0, 0.7); border: 3px solid #F36F20; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin: 0 15px; flex-shrink: 0;">1</div>
                Demographics
            </div>
            <div style="position: absolute; top: 220px; left: 35px; width: 3px; height: 30px; background-color: rgba(138, 138, 138, 0.2);"></div>
            <div style="display: flex; align-items: center;">
                <div style="background-color: rgba(138, 138, 138, 0.2); color: #777777; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin: 0 15px; flex-shrink: 0;">2</div>
                <span style="color: #777777;">Liposuction Information</span>
            </div>
            <div style="position: absolute; top: 300px; left: 35px; width: 3px; height: 30px; background-color: rgba(138, 138, 138, 0.2);"></div>
            <div style="display: flex; align-items: center;">
                <div style="background-color: rgba(138, 138, 138, 0.2); color: #777777; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin: 0 15px; flex-shrink: 0;">3</div>
                <span style="color: #777777;">Body Composition</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)





    with right_col:
        st.subheader("Sex")
        gender = st.radio(
            label="",
            options=["Male", "Female"],
            horizontal=True,
            label_visibility="collapsed"
        )

        st.subheader("Age")
        col1, col2, col3 = st.columns([2, 1, 1])

        if "age" not in st.session_state:
            st.session_state.age = 20

        with col1:
            age_input = st.number_input(
                label="",
                min_value=1,
                max_value=120,
                value=st.session_state.age,
                label_visibility="collapsed"
            )

        st.session_state.age = age_input

        if st.button("Next"):
            if gender and st.session_state.age:
                sex_value = 1 if gender.lower() == "male" else 2
                input_data = {"Sex": sex_value, "Age": st.session_state.age}
                st.json(input_data)
            else:
                st.error("⚠ Please fill in *all fields* with valid values.")
