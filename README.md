# AI Travel Planner

This project is an AI-powered travel planning app built using Streamlit, Groq API, and the `osunlp/TravelPlanner` dataset. The app provides personalized travel recommendations based on user input, including origin, destination, trip duration, number of cities to visit, and more.

## Features

- **Destination Filtering**: The app filters travel plans based on the destination and provides annotated plans as per the dataset.
- **Personalized Travel Plans**: Using the Groq API, the app generates personalized travel recommendations based on user input.
- **Interactive Interface**: Streamlit's user-friendly interface allows for easy input and instant travel recommendations.

## Installation

To run this app, you'll need to install the necessary dependencies. If you're running this in a Google Colab environment, follow these steps:

1. Install the required Python packages:

    ```bash
    !pip install groq
    !pip install datasets
    ```

2. Downgrade `pyarrow` and ensure compatibility with other packages:

    ```bash
    !pip install pyarrow==14.0.1
    !pip install cudf-cu12==24.4.1 ibis-framework==8.0.0
    ```

## Usage

### Running the App

1. Save the Streamlit app code in a file named `app.py`.
2. Run the Streamlit app using the following command:

    ```bash
    !pip install streamlit
    !wget -q -O - ipv4.icanhazip.com
    !streamlit run app.py & npx localtunnel --port 8501
    ```

3. A URL will be provided in the Colab output. Click on it to open the app in a new tab.

### Interacting with the App

- Enter the city of origin, destination, number of days, number of cities to visit, start date, number of people, and any local constraints.
- Provide your travel query, such as what to visit or where to stay.
- Click on "Get Travel Recommendations" to receive a personalized travel plan.

## Example

Here's an example of how to fill out the form:

- **Origin**: New York
- **Destination**: Paris
- **Days**: 7
- **Number of Cities**: 3
- **Start Date**: 2024-09-15
- **People**: 2
- **Local Constraints**: Vegetarian food options
- **Query**: Best places to visit in Paris

The app will then generate a detailed travel plan that meets your criteria.


## Acknowledgments

- The `osunlp/TravelPlanner` dataset used in this project from hugging face.
- Groq API for providing the AI capabilities.
- Streamlit for the user-friendly interface.

