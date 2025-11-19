import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# 1. 데이터 불러오기
# ----------------------------
# CSV 파일 경로 (스트림릿 클라우드에 업로드한 파일명)
DATA_FILE = "mbti_country.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    return df

df = load_data()

# ----------------------------
# 2. 사이드바: 국가 선택
# ----------------------------
st.sidebar.title("국가 선택")
countries = df['Country'].unique()
selected_country = st.sidebar.selectbox("국가를 선택하세요:", countries)

# ----------------------------
# 3. 선택된 국가 데이터 필터링
# ----------------------------
country_df = df[df['Country'] == selected_country]

# MBTI 비율 기준 내림차순 정렬
country_df = country_df.sort_values(by='Percentage', ascending=False)

# ----------------------------
# 4. Plotly 막대그래프
# ----------------------------
# 색상: 1등 빨강, 나머지는 그라데이션
colors = ['red'] + px.colors.sequential.Oranges[len(country_df)-1] if len(country_df) > 1 else ['red']

fig = px.bar(
    country_df,
    x='MBTI',
    y='Percentage',
    color=country_df['Percentage'],  # 색상 스케일
    color_continuous_scale=colors,
    text='Percentage',
    labels={'Percentage': '비율 (%)', 'MBTI': 'MBTI 유형'},
    title=f"{selected_country} 국가별 MBTI 비율"
)

fig.update_traces(marker_line_color='black', marker_line_width=1, texttemplate='%{text:.1f}%', textposition='outside')
fig.update_layout(coloraxis_showscale=False, yaxis=dict(range=[0, country_df['Percentage'].max()*1.2]))

# ----------------------------
# 5. Streamlit에 표시
# ----------------------------
st.plotly_chart(fig, use_container_width=True)
