import streamlit as st
from groq import Groq
from datasets import load_dataset

# Initialize the Groq client
client = Groq(api_key="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")

# Load the TravelPlanner dataset
@st.cache
def load_data():
    return load_dataset("osunlp/TravelPlanner", split="train")

train_ds = load_data()

def retrieve_travel_data(dest, days, people_number, local_constraint):
    filtered_data = train_ds.filter(lambda example: dest in example.get('destination', ''))
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

def sidebar_controllers():
    st.sidebar.header("Travel Planning")
    
    org = st.sidebar.text_input("Enter the city of origin:")
    dest = st.sidebar.text_input("Enter the destination city:")
    days = st.sidebar.number_input("Enter the number of days:", min_value=1)
    visiting_city_number = st.sidebar.number_input("Enter the number of cities to visit:", min_value=1)
    date = st.sidebar.date_input("Enter the start date:")
    people_number = st.sidebar.number_input("Enter the number of people:", min_value=1)
    local_constraint = st.sidebar.text_input("Enter any local constraints (e.g., dietary restrictions, transportation preferences):")
    query = st.sidebar.text_input("Enter your travel query (e.g., what to visit, where to stay):")

    return org, dest, days, visiting_city_number, date, people_number, local_constraint, query

def body(org, dest, days, visiting_city_number, date, people_number, local_constraint, query):
    st.title('Travel Planner')

    if st.button('Get Recommendations'):
        if org and dest and date and query:
            try:
                recommendations = get_travel_recommendations(
                    org,
                    dest,
                    days,
                    visiting_city_number,
                    date.strftime('%Y-%m-%d'),
                    people_number,
                    local_constraint,
                    query
                )
                st.write("\nTravel Recommendations:\n")
                st.write(recommendations)
            except Exception as e:
                st.write(f"An error occurred: {e}")
        else:
            st.write("Please fill in all required fields.")

if __name__ == "__main__":
    org, dest, days, visiting_city_number, date, people_number, local_constraint, query = sidebar_controllers()
    body(org, dest, days, visiting_city_number, date, people_number, local_constraint, query)
