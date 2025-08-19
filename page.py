import streamlit as st
from pathlib import Path
import base64
import pandas as pd
import joblib
import gdown
#streamlit run page.py

if "page" not in st.session_state:
    st.session_state.page = "page1"

if st.session_state.page == "page1":
    img_path = Path("assets/Logo.png")
    jibang_path = Path("assets/Jibang-1.png")

    def img_to_base64(img_path):
        with open(img_path, "rb") as img_file:
            b64_str = base64.b64encode(img_file.read()).decode()
        return b64_str

    img_b64 = img_to_base64(img_path)
    jibang_b64 = img_to_base64(jibang_path)

    # 마크다운
    st.markdown(
        f"""
        <style>
        
        .stApp {{
            background: linear-gradient(296.81deg, #F4E1D6 -47.61%, #F36F20 50%);
        }}

        .custom-logo {{
            position: fixed;
            top: 30px;
            left: 50px;
            width: 300px;
        }}

        header[data-testid="stHeader"] {{
            display: none;
        }}
        
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
            align-items: center; 
            gap: 4px; 
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
        
        div[data-testid="stVerticalBlock"] > div {{
            height: 100% !important;
            display: flex !important;
        }}
        
        input[type="number"] {{
            background-color: #FFFFFF !important;
            border-radius: 5px !important;
            padding: 5px 10px !important;
            box-shadow: none !important; 
            height: 40px !important; 
            width: 150px;
            font-size: 20px !important;
            color: rgba(0, 0, 0, 0.7);
        }}
        
        input[type=number]::-webkit-inner-spin-button,
        input[type=number]::-webkit-outer-spin-button {{
            -webkit-appearance: none !important;
            margin: 0 !important;
        }}
        
        .stButton>button {{
            background-color: #E9E3E0 !important;  /* 회색 */
            color: rgba(0, 0, 0, 0.7) !important;
            border: none !important;
            border-radius: 20px !important;
            cursor: pointer !important;
            transition: background-color 0.3s ease !important;
            width: 100px;
        }}

        .stButton>button:active {{
            background-color: #F36F20 !important; 
            color: white !important;
        }}
        
        .custom-jibang {{
            position: absolute;
            top: -130px;
            right: 20px;
            width: 170px;
            z-index: 10;
        }}
        </style>
        
        <img src="data:image/png;base64,{img_b64}" class="custom-logo" />
        <img src="data:image/png;base64,{jibang_b64}" class="custom-jibang" />
        """,
        unsafe_allow_html=True
    )





    with st.container():
        left_col, right_col = st.columns([1, 3])  

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
            <div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; position: relative;">
            """, unsafe_allow_html=True)
            
            st.markdown(
                """
                <div style="display: flex; align-items: center;">
                    <label style="font-weight: 600; font-size: 24px;">Sex</label>
                """, unsafe_allow_html=True
            )
            
            if "gender" not in st.session_state:
                st.session_state.gender = 0
            gender_str = st.radio(
                label="",
                options=["Male", "Female"],
                index=st.session_state.gender,
                horizontal=True,
                label_visibility="collapsed"
            )
            gender = 0 if gender_str == "Male" else 1
            st.session_state.gender = gender
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown(
                """
                <div style="display: flex; align-items: center;">
                    <label style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Age</label>
                """, unsafe_allow_html=True
            )
            
            if "age" not in st.session_state:
                st.session_state.age = 1

            age = st.number_input(
                label="",
                min_value=1,
                max_value=121,
                label_visibility="collapsed",
                key="age"
            )

            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown('<div style="flex-grow: 1;"></div>', unsafe_allow_html=True)
            
            st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
            if st.button("Next", key="next_page1"):
                st.session_state.page = "page2"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)










elif st.session_state.page == "page2":
    img_path = Path("assets/Logo.png")
    checkbox_path = Path("assets/CheckBox.png")
    jibang_path = Path("assets/Jibang-1.png")

    def img_to_base64(img_path):
        with open(img_path, "rb") as img_file:
            b64_str = base64.b64encode(img_file.read()).decode()
        return b64_str

    img_b64 = img_to_base64(img_path)
    
    checkbox_path = Path("assets/CheckBox.png") 
    checkbox_b64 = img_to_base64(checkbox_path)
    jibang_b64 = img_to_base64(jibang_path)

    st.markdown(
        f"""
        <style>
        
        .stApp {{
            background: linear-gradient(296.81deg, #F4E1D6 -47.61%, #F36F20 50%);
        }}

        .custom-logo {{
            position: fixed;
            top: 30px;
            left: 50px;
            width: 300px;
        }}

        header[data-testid="stHeader"] {{
            display: none;
        }}
        
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
            align-items: center;
            gap: 4px; 
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
        
        div[data-testid="stVerticalBlock"] > div {{
            height: 100% !important;
            display: flex !important;
        }}
        
        input[type="number"] {{
            background-color: #FFFFFF !important;
            border-radius: 5px !important;
            padding: 5px 10px !important;
            box-shadow: none !important; 
            height: 40px !important; 
            width: 150px;
            font-size: 20px !important;
            color: rgba(0, 0, 0, 0.7);
        }}

        input[type=number]::-webkit-inner-spin-button,
        input[type=number]::-webkit-outer-spin-button {{
            -webkit-appearance: none !important;
            margin: 0 !important;
        }}
        
        .stButton>button {{
            background-color: #E9E3E0 !important;  /* 회색 */
            color: rgba(0, 0, 0, 0.7) !important;
            border: none !important;
            border-radius: 20px !important;
            cursor: pointer !important;
            transition: background-color 0.3s ease !important;
            width: 100px;
        }}

        .stButton>button:active {{
            background-color: #F36F20 !important; 
            color: white !important;
        }}
        
        div[data-testid="stRadio"],
        div[data-testid="stNumberInput"] {{
            margin-bottom: -20px !important;
        }}
        
        .custom-jibang {{
            position: absolute;
            top: -130px;
            right: 20px;
            width: 170px;
            z-index: 10;
        }}
        </style>

        <img src="data:image/png;base64,{img_b64}" class="custom-logo" />
        <img src="data:image/png;base64,{jibang_b64}" class="custom-jibang" />
        """,
        unsafe_allow_html=True
        )
        
    with st.container():
        left_col, right_col = st.columns([1, 3])

        with left_col:
            st.markdown(f'''
            <div style="position: relative; background-color: #FFF3EB; min-height: 60vh; border-radius: 8px; display: flex; flex-direction: column; align-items: flex-start; justify-content: center; font-size: 25px; font-weight: bold; color: rgba(0, 0, 0, 0.7); padding: 0; gap: 20px; margin-right: 70px;">
                <div style="display: flex; align-items: center;">
                    <img src="data:image/png;base64,{checkbox_b64}" width="40" height="40" style="margin: 50px 15px 50px 20px;"/>
                    <span style="color: rgba(0, 0, 0, 0.7);">Liposuction Information</span>
                </div>
                <div style="position: absolute; top: 138px; left: 40px; width: 3px; height: 110px; background-color: #F36F20;"></div>
                <div style="display: flex; align-items: center;">
                    <div style="background-color: rgba(138, 138, 138, 0.2); color: rgba(0, 0, 0, 0.7); border: 3px solid #F36F20; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin: 50px 15px 50px 20px; flex-shrink: 0;">2</div>
                    <span style="color: rgba(0, 0, 0, 0.7);">Liposuction Information</span>
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
                    <label style="font-weight: 600; font-size: 24px;">Liposuction type</label>
                """, unsafe_allow_html=True
            )
            if "type" not in st.session_state:
                st.session_state.type = 0
            type_str = st.radio(
                label="",
                options=["Lams", "Surgery"],
                index=st.session_state.type,
                horizontal=True,
                label_visibility="collapsed"
            )
            type_ = 0 if type_str == "Lams" else 1
            st.session_state.type = type_
            
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(
                """
                <div style="display: flex; align-items: center;">
                    <label style="font-weight: 600; font-size: 24px;">Liposuction site</label>
                """, unsafe_allow_html=True
            )
            if "site" not in st.session_state:
                st.session_state.site = 0
            site_options = ["Abdomen", "Arms", "Backs", "Buttocks", "Calves", "Flanks", "Thighs"]
            site_str = st.radio(
                label="",
                options=site_options,
                index=st.session_state.site,
                horizontal=True,
                label_visibility="collapsed"
            )
            st.session_state.site = site_options.index(site_str)
            
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(
                """
                <div style="display: flex;">
                """, unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(
                    '<div style="display: flex; align-items: center;">'
                    '<label style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Preoperative size</label>', 
                    unsafe_allow_html=True
                )
                if "size" not in st.session_state:
                    st.session_state.size = 1
                preop_size = st.number_input(
                    label="",
                    min_value=1,
                    max_value=1000,
                    label_visibility="collapsed",
                    key="size"
                )

            with col2:
                st.markdown(
                    '<div style="display: flex; align-items: center;">'
                    '<label style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Fat volume</label>',
                    unsafe_allow_html=True
                )
                if "fat_volume" not in st.session_state:
                    st.session_state.fat_volume = 50
                fat_volume = st.number_input(
                    label="",
                    min_value=50,
                    max_value=10000,
                    label_visibility="collapsed",
                    key="fat_volume"
                )

            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown('<div style="flex-grow: 1;"></div>', unsafe_allow_html=True)

            st.markdown(
                """
                <div style="display: flex; align-items: center;">
                    <label style="font-weight: 600; font-size: 24px;">Edema</label>
                """, unsafe_allow_html=True
            )
            
            edema_options = ["No edema", "Mild edema", "Moderate to severe edema"]
            if "edema" not in st.session_state:
                st.session_state.edema = 0
            edema_str = st.radio(
                label="",
                options=["No edema", "Mild edema", "Moderate to severe edema"],
                index=st.session_state.edema,
                horizontal=True,
                label_visibility="collapsed"
            )
            st.session_state.edema = edema_options.index(edema_str)
            
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(
                """
                <div style="display: flex;">
                """, unsafe_allow_html=True
            )
            
            st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)

            col_back, col_next = st.columns([1, 10])

            with col_back:
                if st.button("Back", key="back_page2"):
                    st.session_state.page = "page1"
                    st.rerun()
            with col_next:
                if st.button("Next", key="next_page2"):
                    st.session_state.page = "page3"
                    st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)










elif st.session_state.page == "page3":
    img_path = Path("assets/Logo.png")
    checkbox_path = Path("assets/CheckBox.png")
    jibang_path = Path("assets/Jibang-1.png")

    def img_to_base64(img_path):
        with open(img_path, "rb") as img_file:
            b64_str = base64.b64encode(img_file.read()).decode()
        return b64_str

    img_b64 = img_to_base64(img_path)
    
    checkbox_path = Path("assets/CheckBox.png") 
    checkbox_b64 = img_to_base64(checkbox_path)
    jibang_b64 = img_to_base64(jibang_path)

    st.markdown(
        f"""
        <style>
        
        .stApp {{
            background: linear-gradient(296.81deg, #F4E1D6 -47.61%, #F36F20 50%);
        }}

        .custom-logo {{
            position: fixed;
            top: 30px;
            left: 50px;
            width: 300px;
        }}

        header[data-testid="stHeader"] {{
            display: none;
        }}
        
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
        
        div[data-testid="stVerticalBlock"] > div {{
            height: 100% !important;
            display: flex !important;
        }}
        
        input[type="number"] {{
            background-color: #FFFFFF !important;
            border-radius: 5px !important;
            padding: 5px 10px !important;
            box-shadow: none !important; 
            height: 40px !important; 
            width: 150px;
            font-size: 20px !important;
            color: rgba(0, 0, 0, 0.7);
        }}
        
        input[type=number]::-webkit-inner-spin-button,
        input[type=number]::-webkit-outer-spin-button {{
            -webkit-appearance: none !important;
            margin: 0 !important;
        }}
        
        .stButton>button {{
            background-color: #E9E3E0 !important;
            color: rgba(0, 0, 0, 0.7) !important;
            border: none !important;
            border-radius: 20px !important;
            cursor: pointer !important;
            transition: background-color 0.3s ease !important;
            width: 100px;
        }}

        .stButton>button:active {{
            background-color: #F36F20 !important; 
            color: white !important;
        }}
        
        .custom-jibang {{
            position: absolute;
            top: -130px;
            right: 20px;
            width: 170px;
            z-index: 10;
        }}     
        </style>

        <img src="data:image/png;base64,{img_b64}" class="custom-logo" />
        <img src="data:image/png;base64,{jibang_b64}" class="custom-jibang" />
        """,
        unsafe_allow_html=True
        )
        
    with st.container():
        left_col, right_col = st.columns([1, 3])

        with left_col:
            st.markdown(f'''
            <div style="position: relative; background-color: #FFF3EB; min-height: 60vh; border-radius: 8px; display: flex; flex-direction: column; align-items: flex-start; justify-content: center; font-size: 25px; font-weight: bold; color: rgba(0, 0, 0, 0.7); padding: 0; gap: 20px; margin-right: 70px;">
                <div style="display: flex; align-items: center;">
                    <img src="data:image/png;base64,{checkbox_b64}" width="40" height="40" style="margin: 50px 15px 50px 20px;"/>
                    <span style="color: rgba(0, 0, 0, 0.7);">Liposuction Information</span>
                </div>
                <div style="position: absolute; top: 138px; left: 40px; width: 3px; height: 110px; background-color: #F36F20;"></div>
                <div style="display: flex; align-items: center;">
                    <img src="data:image/png;base64,{checkbox_b64}" width="40" height="40" style="margin: 50px 15px 50px 20px;"/>
                    <span style="color: rgba(0, 0, 0, 0.7);">Liposuction Information</span>
                </div>
                <div style="position: absolute; top: 298px; left: 40px; width: 3px; height: 110px; background-color: #F36F20;"></div>
                <div style="display: flex; align-items: center;">
                    <div style="background-color: rgba(138, 138, 138, 0.2); color: #777777; border: 3px solid #F36F20; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin: 50px 15px 50px 20px; flex-shrink: 0;">3</div>
                    <span style="color: rgba(0, 0, 0, 0.7);">Body Composition</span>
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
                <div style="display: flex; gap: 30px; margin-bottom: 15px;">
                """, unsafe_allow_html=True
            )

            if "height" not in st.session_state:
                st.session_state.height = 1 
            if "weight" not in st.session_state:
                st.session_state.weight = 1
    
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Height</div>', unsafe_allow_html=True)
                height = st.number_input("", min_value=1, max_value=300, key="height", label_visibility="collapsed")
            with col2:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Weight</div>', unsafe_allow_html=True)
                weight = st.number_input("", min_value=1, max_value=200, key="weight", label_visibility="collapsed")
            with col3:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">BMI</div>', unsafe_allow_html=True)

                if height > 0:
                    bmi = weight / ((height / 100) ** 2)
                    bmi = round(bmi, 2)
                else:
                    bmi = 0
                    
                st.session_state.bmi = bmi

                st.markdown(
                    f"""
                    <div style="background-color: #E9E3E0; color: rgba(0, 0, 0, 0.7); border: none; border-radius: 20px; width: 100px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 500;">{bmi}</div>
                    """,
                    unsafe_allow_html=True
                )

            col1, col2, col3 = st.columns(3)
            if "smm" not in st.session_state:
                st.session_state.smm = 10.0
            with col1:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Skeletal muscle mass</div>', unsafe_allow_html=True)
                smm = st.number_input("", min_value=10.0, max_value=80.0, key="smm", label_visibility="collapsed")
                
            if "bfm" not in st.session_state:
                st.session_state.bfm = 5.0
            with col2:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Body fat mass</div>', unsafe_allow_html=True)
                bfm = st.number_input("", min_value=5.0, max_value=80.0, key="bfm", label_visibility="collapsed")
            
            if "tbw" not in st.session_state:
                st.session_state.tbw = 25.0
            with col3:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Total body water</div>', unsafe_allow_html=True)
                tbw = st.number_input("", min_value=25.0, max_value=70.0, key="tbw", label_visibility="collapsed")
                
            col1, col2, col3 = st.columns(3)
            if "ffm" not in st.session_state:
                st.session_state.ffm = 30.0
            with col1:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Fat-free mass</div>', unsafe_allow_html=True)
                ffm = st.number_input("", min_value=30.0, max_value=120.0, key="ffm", label_visibility="collapsed")
                
            if "protein" not in st.session_state:
                st.session_state.protein = 5.0
            with col2:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Body protein</div>', unsafe_allow_html=True)
                protein = st.number_input("", min_value=5.0, max_value=40.0, key="protein", label_visibility="collapsed")
                
            if "mineral" not in st.session_state:
                st.session_state.mineral = 2.0
            with col3:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Body mineral</div>', unsafe_allow_html=True)
                mineral = st.number_input("", min_value=2.0, max_value=10.0, key="mineral", label_visibility="collapsed")

            col1 = st.columns(1)[0]
            if "whr" not in st.session_state:
                st.session_state.whr = 0.3
            with col1:
                st.markdown('<div style="font-weight: 600; font-size: 24px; margin-bottom: 5px;">Waist-hip ratio</div>', unsafe_allow_html=True)
                whr = st.number_input("", min_value=0.3, max_value=1.5, key="whr", label_visibility="collapsed")

            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown('<div style="display: flex; justify-content: flex-end; gap: 20px;">', unsafe_allow_html=True)

            col_back, col_next = st.columns([1, 10])

            with col_back:
                if st.button("Back", key="back_page3"):
                    st.session_state.page = "page2"
                    st.rerun()
            with col_next:
                if st.button("Complete", key="next_page3"):
                    st.session_state.page = "page4"
                    st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)











elif st.session_state.page == "page4":
    img_path = Path("assets/Logo.png")
    check_path = Path("assets/check.png")
    jibang2_path = Path("assets/Jibang-2.png")

    def img_to_base64(img_path):
        with open(img_path, "rb") as img_file:
            b64_str = base64.b64encode(img_file.read()).decode()
        return b64_str

    img_b64 = img_to_base64(img_path)
    check_b64 = img_to_base64(check_path)
    jibang2_b64 = img_to_base64(jibang2_path)

    gender = st.session_state.get('gender', 0)
    age = st.session_state.get('age', 1)
    type_ = st.session_state.get('type', 0)
    site = st.session_state.get('site', 0)
    size = st.session_state.get('size', 1)
    fat_volume = st.session_state.get('fat_volume', 50)
    edema = st.session_state.get('edema', 0)
    height = st.session_state.get('height', 1)
    weight = st.session_state.get('weight', 1)
    bmi = st.session_state.get('bmi', None)
    smm = st.session_state.get('smm', 10.0)
    bfm = st.session_state.get('bfm', 5.0)
    tbw = st.session_state.get('tbw', 25.0)
    ffm = st.session_state.get('ffm', 30.0)
    protein = st.session_state.get('protein', 5.0)
    mineral = st.session_state.get('mineral', 2.0)
    whr = st.session_state.get('whr', 0.3)
    
    input_dict = {
        'Liposuction site': site,
        'Edema': edema,
        'Sex': gender,
        'Age': age,
        'Height': height,
        'Fat volume': fat_volume,
        'Weight': weight,
        'Size': size,
        'TBW': tbw,
        'Body protein': protein,
        'Body mineral': mineral,
        'FFM': ffm,
        'SMM': smm,
        'BFM': bfm,
        'WHR': whr,
        'BMI': bmi,
        'Liposuction type': type_
    }
    
    FEATURES = [
        'Liposuction site', 'Edema', 'Sex', 'Age', 'Height', 'Fat volume',
        'Weight', 'Size', 'TBW', 'Body protein', 'Body mineral', 'FFM',
        'SMM', 'BFM', 'WHR', 'BMI', 'Liposuction type'
    ]
    
    input_df = pd.DataFrame([input_dict], columns=FEATURES)

    @st.cache_resource
    def load_model():
        file_id = "1ytC-ErD43EkZuFWJqr3oEHWSOdcE92_M"
        url = f"https://drive.google.com/uc?id={file_id}"
        output = "chained_et_reverse.pkl"
        gdown.download(url, output, quiet=False)
        return joblib.load(output)
    model = load_model()

    result = model.predict(input_df)
    pred_weight, pred_size = result[0]

    st.markdown(
        f"""
        <style>
        
        .stApp {{
            background: linear-gradient(296.81deg, #F4E1D6 -47.61%, #F36F20 50%);
        }}

        .custom-logo {{
            position: fixed;
            top: 30px;
            left: 50px;
            width: 300px;
        }}

        header[data-testid="stHeader"] {{
            display: none;
        }}
        
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
            display: flex !important;         
            flex-direction: column !important; 
            justify-content: center !important; 
            align-items: center !important;    
        }}
        
        .info-box {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid #E9E3E0;
            border-radius: 20px;
            padding: 10px 20px;
            margin: 15px auto;
            width: 400px;
            font-size: 20px;
            color: rgba(0, 0, 0, 0.7);
        }}

        .value-box {{
            background-color: #F36F20;
            color: white;
            padding: 5px 20px;
            border-radius: 10px;
            font-size: 20px;
        }}
        
        .complete-text {{
            font-size: 40px;
            font-weight: 800;
            margin: 20px 0;
        }}

        .stButton>button {{
            background-color: #E9E3E0 !important;
            color: rgba(0, 0, 0, 0.7) !important;
            border: none !important;
            border-radius: 20px !important;
            cursor: pointer !important;
            transition: background-color 0.3s ease !important;
            width: 200px;
            margin-top: 30px;
        }}

        .stButton>button:active {{
            background-color: #F36F20 !important;
            color: white !important;
        }}
        
        .custom-jibang {{
            position: absolute;
            bottom: -600px;
            right: -150px;
            width: 350px;
            z-index: 10;
        }}     
        </style>

        <img src="data:image/png;base64,{img_b64}" class="custom-logo" />
        <img src="data:image/png;base64,{jibang2_b64}" class="custom-jibang" />
        """,
        unsafe_allow_html=True
        )
        
    with st.container():
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
                <div><img src="data:image/png;base64,{check_b64}" width="60"/></div>
                <div class="complete-text">COMPLETE</div>
                <div class="info-box" style="margin-bottom: -5px;"><span>Postoperative weight</span><span class="value-box">{pred_weight:.2f}</span></div>
                <div class="info-box"><span>Postoperative size</span><span class="value-box">{pred_size:.2f}</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2, col3 = st.columns([1.5, 1, 1])
        with col2:
            if st.button("Back to Start"):
                st.session_state.page = "page1"
                st.rerun()