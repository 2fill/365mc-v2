import streamlit as st
from pathlib import Path
import base64
#streamlit run page.py

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
        position: relative;
    }}
    
    div[role="radiogroup"] label {{
        display: flex;
        align-items: center; /* 세로 가운데 정렬 */
        gap: 4px; /* 버튼과 텍스트 사이 간격 */
        margin-right: 50px;
    }}
    
    div[role="radiogroup"] label > input[type="radio"] {{
        display: none;
    }}

    div[role="radiogroup"] label > div {{
        color: rgba(0, 0, 0, 0.7);
        cursor: pointer;
    }}

    div[role="radiogroup"] label > input[type="radio"]:checked + div {{
        color: #F36F20 !important;
    }}
    
    div[role="radiogroup"] label > div > div {{
      font-size: 20px !important;
    }}
    
    /* 좌우 컬럼 부모 */
    div[data-testid="stVerticalBlock"] > div {{
        height: 100% !important;
        display: flex !important;
    }}
    
    /* Age */
    input[type="number"] {{
        background-color: #F36F20 !important;
        border-radius: 5px !important;
        padding: 5px 10px !important;
        box-shadow: none !important; 
        height: 40px !important; 
        width: 150px;
        font-size: 20px !important;
    }}
    
    /* 스핀 버튼 */
    input[type=number]::-webkit-inner-spin-button,
    input[type=number]::-webkit-outer-spin-button {{
        -webkit-appearance: none !important;
        margin: 0 !important;
    }}
    
    /* Next 버튼 위치 */
    .next-btn-wrapper {{
        position: absolute;
        bottom: 0px;
        right: 0px;
    }}
    
    </style>



    <img src="data:image/png;base64,{img_b64}" class="custom-logo" />
    """,
    unsafe_allow_html=True
)





with st.container():
    # 좌우 박스 생성
    left_col, right_col = st.columns([1, 3])  # 비율

    with left_col:
        st.markdown('''
        <div style="position: relative; background-color: #FFF3EB; min-height: 60vh; border-radius: 8px; display: flex; flex-direction: column; align-items: flex-start; justify-content: center; font-size: 25px; font-weight: bold; color: rgba(0, 0, 0, 0.7); padding: 0; gap: 20px; margin-right: 70px;">
            <div style="display: flex; align-items: center;">
                <div style="background-color: rgba(138, 138, 138, 0.2); color: rgba(0, 0, 0, 0.7); border: 3px solid #F36F20; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin: 50px 15px 50px 20px; flex-shrink: 0;">1</div>
                Demographics
            </div>
            <div style="position: absolute; top: 138px; left: 40px; width: 3px; height: 110px; background-color: rgba(138, 138, 138, 0.2);"></div>
            <div style="display: flex; align-items: center;">
                <div style="background-color: rgba(138, 138, 138, 0.2); color: #777777; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin: 50px 15px 50px 20px; flex-shrink: 0;">2</div>
                <span style="color: #777777;">Liposuction Information</span>
            </div>
            <div style="position: absolute; top: 298px; left: 40px; width: 3px; height: 110px; background-color: rgba(138, 138, 138, 0.2);"></div>
            <div style="display: flex; align-items: center;">
                <div style="background-color: rgba(138, 138, 138, 0.2); color: #777777; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin: 50px 15px 50px 20px; flex-shrink: 0;">3</div>
                <span style="color: #777777;">Body Composition</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)





    with right_col:
        st.markdown(
        """
        <div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; margin: 0; padding: 0; position: relative;">
        """, unsafe_allow_html=True)
        
        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <label style="font-weight: 600; font-size: 24px;">Sex</label>
            """, unsafe_allow_html=True
        )
        
        gender = st.radio(
            label="",
            options=["Male", "Female"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div style="display: flex; align-items: center;">
                <label style="font-weight: 600; font-size: 24px;">Age</label>
            """, unsafe_allow_html=True
        )
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

        st.markdown('<div class="next-btn-wrapper">', unsafe_allow_html=True)
        if st.button("Next"):
            if gender and st.session_state.age:
                sex_value = 1 if gender.lower() == "male" else 2
                input_data = {"Sex": sex_value, "Age": st.session_state.age}
                st.json(input_data)
            else:
                st.error("⚠ Please fill in *all fields* with valid values.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)