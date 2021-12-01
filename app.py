import streamlit as st
import pandas as pd
import seaborn as sns

"# Welcome to Streamlit!"


# Read in the data
df_books = pd.read_csv("./data/bestsellers-with-categories.csv")

# Get the min and max prices for the slider
max_price = max(df_books['Price'])
min_price = min(df_books['Price'])

# Get the min and max ratings for the slider
max_rating = max(df_books['User Rating'])
min_rating = min(df_books['User Rating'])

# Set up sidebar
st.sidebar.write("## Filter book review data")
price_low, price_high = st.sidebar.slider('Select max price', step=5, value=(min_price, max_price), min_value=min_price, max_value=max_price)
rating_low, rating_high = st.sidebar.slider('Select max rating', step=0.1, value=(float(min_rating),float(max_rating)), min_value=float(min_rating), max_value=float(max_rating))

# Filter data on price
df_books = df_books[df_books['Price'] <= price_high]
df_books = df_books[df_books['Price'] >= price_low]

# Filter data on rating
df_books = df_books[df_books['User Rating'] <= rating_high]
df_books = df_books[df_books['User Rating'] >= rating_low]

# Web Page
with st.container():
    
    "### Amazon Top 50 Best Sellers 2009-19"
    "Data source: https://www.kaggle.com/sootersaalu/amazon-top-50-bestselling-books-2009-2019"

    "### Seaborn Plots"

    col_1, col_2 = st.columns(2)
    
    with col_1:
        # Plot Price as distribution
        "#### Price Distribution"
        plot = sns.displot(df_books, x="Price", kind="kde")
        st.pyplot(plot)

    with col_2:
        # Plot rating as distribution plot
        "#### User Rating Distribution"
        plot = sns.displot(df_books, x="User Rating", kind="kde")
        st.pyplot(plot)
    
    "#### Let's see what a data frame looks like"
    st.dataframe(df_books)

"Made with :heart: by [Intellify](https://intellify.com.au/)"