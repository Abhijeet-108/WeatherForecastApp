import streamlit as st
import plotly.express as px
from fore_backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1 , max_value=5 , help="Select the number of Forecasted days")
option = st.selectbox("Select data to view", ("Temperature" , "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:

    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature(C)",})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png","Snow": "images/snow.png"}
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky]
            print(sky)
            st.image(image_paths,width=118)
    except KeyError:
        st.write("That Place does not Exit...... \n Write Correct Place.")