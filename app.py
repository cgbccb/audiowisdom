import streamlit as st
import pandas as pd

st.set_page_config(page_title="오디오위즈덤 - 시니어 오디오북 트렌드", page_icon="🎧", layout="wide")

st.title("🎧 오디오위즈덤 (AudioWisdom)")
st.markdown("시니어를 위한 유튜브 오디오북 트렌드를 쉽게 찾을 수 있는 도구입니다.")

keyword = st.text_input("🔍 검색어를 입력하세요 (예: 인생, 명언, 힐링 등)")
category = st.selectbox("카테고리 선택", ["전체", "오디오북", "명상", "라이프스타일", "시니어"])
date_range = st.date_input("검색 기간 선택", [])

if st.button("트렌드 분석 시작"):
    st.info(f"'{keyword}' 관련 인기 영상을 불러오는 중입니다... (예시 데이터)")
    data = pd.DataFrame({
        "제목": ["행복의 기술", "인생 후반전의 지혜", "하루를 밝히는 명언"],
        "조회수": [78000, 65000, 42000],
        "좋아요": [2800, 2100, 1900],
        "채널명": ["마음의서재", "오디오북TV", "인생명언채널"],
        "썸네일": [
            "https://i.ytimg.com/vi/ysz5S6PUM-U/mqdefault.jpg",
            "https://i.ytimg.com/vi/aqz-KE-bpKQ/mqdefault.jpg",
            "https://i.ytimg.com/vi/ScMzIvxBSi4/mqdefault.jpg"
        ]
    })
    for i, row in data.iterrows():
        st.image(row["썸네일"], width=120)
        st.write(f"**{row['제목']}**")
        st.write(f"📺 채널: {row['채널명']} | 👁️ {row['조회수']}회 | 👍 {row['좋아요']}개")
        st.divider()

st.caption("© 2025 오디오위즈덤 - 시니어 오디오북 트렌드 파인더")
