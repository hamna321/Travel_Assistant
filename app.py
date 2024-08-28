import streamlit as st
from groq import Groq
from datasets import load_dataset

# Set up Groq API client
client = Groq(api_key="api_key")

# Load datasets
train_ds = load_dataset("osunlp/TravelPlanner", "train")
test_ds = load_dataset("osunlp/TravelPlanner", "test")
validation_ds = load_dataset("osunlp/TravelPlanner", "validation")

def retrieve_travel_data(dest, days, people_number, local_constraint):
    filtered_data = train_ds['train'].filter(lambda example: dest in example.get('destination', ''))
    return [item['annotated_plan'] for item in filtered_data][:3]

def get_travel_recommendations(org, dest, days, visiting_city_number, date, people_number, local_constraint, query):
    retrieved_info = retrieve_travel_data(dest, days, people_number, local_constraint)
    prompt = f"""
    I am planning a trip from {org} to {dest} for {days} days.
    The trip includes {visiting_city_number} cities, starting on {date}, with {people_number} people.
    The constraints include: {local_constraint}.
    Here is some relevant travel information: {retrieved_info}.
    My query is: {query}.
    Please provide a travel plan that complies with all these requirements.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# Streamlit UI
st.title("AI Travel Planner")

org = st.text_input("Enter the city of origin:")
dest = st.text_input("Enter the destination city:")
days = st.number_input("Enter the number of days:", min_value=1)
visiting_city_number = st.number_input("Enter the number of cities to visit:", min_value=1)
date = st.date_input("Enter the start date:")
people_number = st.number_input("Enter the number of people:", min_value=1)
local_constraint = st.text_input("Enter any local constraints (e.g., dietary restrictions, transportation preferences):")
query = st.text_input("Enter your travel query (e.g., what to visit, where to stay):")

if st.button("Get Travel Recommendations"):
    if org and dest and days and visiting_city_number and date and people_number and query:
        recommendations = get_travel_recommendations(
            org, dest, days, visiting_city_number, date, people_number, local_constraint, query
        )
        st.subheader("Travel Recommendations:")
        st.write(recommendations)
    else:
        st.warning("Please fill in all fields to get recommendations.")
