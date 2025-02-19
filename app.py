import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from datetime import datetime
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    .reportview-container {
        background: #f0f2f6
    }
    .sidebar .sidebar-content {
        background: #f0f2f6
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Navigation")
    page = st.radio(
        "Choose a page",
        ["Home", "Data Analysis", "Interactive Charts", "Real-time Demo", "File Upload"]
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.info(
        """
        This is a demo application showing various features of Streamlit.
        Feel free to explore different pages and interact with the components!
        """
    )

# Home Page
if page == "Home":
    st.title("Welcome to Streamlit Demo! 👋")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Basic Components")
        name = st.text_input("Enter your name")
        age = st.slider("Select your age", 0, 100, 25)
        color = st.color_picker("Choose your favorite color")
        
        if name:
            st.success(f"Hello {name}! You are {age} years old and your favorite color is {color}")
    
    with col2:
        st.header("Interactive Elements")
        if st.button("Click me!"):
            st.balloons()
        
        option = st.selectbox(
            "What's your favorite programming language?",
            ["Python", "JavaScript", "Java", "C++", "Other"]
        )
        st.write(f"You selected: {option}")

# Data Analysis Page
elif page == "Data Analysis":
    st.title("Data Analysis Demo 📈")
    
    # Generate sample data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.normal(1000, 100, len(dates)),
        'Visitors': np.random.normal(500, 50, len(dates))
    })
    
    st.subheader("Sample Dataset")
    st.dataframe(data.head(10))
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sales Distribution")
        fig = px.histogram(data, x='Sales', nbins=30)
        st.plotly_chart(fig)
    
    with col2:
        st.subheader("Visitors vs Sales")
        fig = px.scatter(data, x='Visitors', y='Sales', trendline="ols")
        st.plotly_chart(fig)

# Interactive Charts Page
elif page == "Interactive Charts":
    st.title("Interactive Charts 📊")
    
    # Create sample data
    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.randint(10, 100, len(categories))
    
    chart_type = st.selectbox(
        "Select Chart Type",
        ["Bar", "Line", "Pie", "Scatter"]
    )
    
    if chart_type == "Bar":
        fig = go.Figure(data=[go.Bar(x=categories, y=values)])
    elif chart_type == "Line":
        fig = go.Figure(data=[go.Line(x=categories, y=values)])
    elif chart_type == "Pie":
        fig = go.Figure(data=[go.Pie(labels=categories, values=values)])
    else:
        fig = go.Figure(data=[go.Scatter(x=categories, y=values, mode='markers')])
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Customize Chart")
    color = st.color_picker("Choose chart color", "#00ff00")
    title = st.text_input("Enter chart title", "My Chart")
    
    fig.update_layout(
        title=title,
        showlegend=True,
        plot_bgcolor='white'
    )
    fig.update_traces(marker_color=color)
    st.plotly_chart(fig, use_container_width=True)

# Real-time Demo Page
elif page == "Real-time Demo":
    st.title("Real-time Data Demo ⚡")
    
    placeholder = st.empty()
    
    # Initialize progress bar
    progress_bar = st.progress(0)
    
    # Create real-time chart
    chart_data = pd.DataFrame(columns=['time', 'value'])
    chart_placeholder = st.empty()
    
    if st.button("Start Real-time Demo"):
        for i in range(100):
            with placeholder.container():
                # Update metrics
                kpi1, kpi2, kpi3 = st.columns(3)
                
                kpi1.metric(
                    label="Temperature",
                    value=f"{np.random.randint(20, 30)}°C",
                    delta=f"{np.random.randint(-2, 2)}°C"
                )
                
                kpi2.metric(
                    label="Humidity",
                    value=f"{np.random.randint(40, 60)}%",
                    delta=f"{np.random.randint(-5, 5)}%"
                )
                
                kpi3.metric(
                    label="CO2",
                    value=f"{np.random.randint(400, 500)} ppm",
                    delta=f"{np.random.randint(-10, 10)} ppm"
                )
            
            # Update progress bar
            progress_bar.progress((i + 1))
            
            # Update chart
            new_data = pd.DataFrame({
                'time': [datetime.now()],
                'value': [np.random.randint(0, 100)]
            })
            chart_data = pd.concat([chart_data, new_data], ignore_index=True)
            
            fig = px.line(chart_data, x='time', y='value', title='Real-time Data')
            chart_placeholder.plotly_chart(fig, use_container_width=True)
            
            time.sleep(0.1)

# File Upload Page
else:
    st.title("File Upload Demo 📁")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.success("File successfully uploaded!")
        
        st.subheader("Data Preview")
        st.dataframe(data.head())
        
        st.subheader("Data Info")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Basic Statistics")
            st.write(data.describe())
        
        with col2:
            st.write("Missing Values")
            st.write(data.isnull().sum())
        
        st.subheader("Data Visualization")
        if len(data.columns) >= 2:
            x_axis = st.selectbox("Select X axis", data.columns)
            y_axis = st.selectbox("Select Y axis", data.columns)
            
            fig = px.scatter(data, x=x_axis, y=y_axis)
            st.plotly_chart(fig, use_container_width=True)
