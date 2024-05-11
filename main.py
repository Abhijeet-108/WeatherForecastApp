import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1 , max_value=5 , help="Select the number of Forecasted days")
option = st.selectbox("Select data to view", ("Temperature" , "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_days(days):
    dates = ["2022-25-10","2022-26-10","2022-27-10","2022-28-10","2022-29-10"]
    temperature = [32,30,38,29,35]
    temperature = [days * i for i in temperature]
    return dates,temperature

d,t = get_days(days)

figure = px.line(x=d, y=t, labels={"x":"Date", "y":"Temperature(C)",})
st.plotly_chart(figure)