import streamlit as st

import requests



st.title("Ecommerce APP")

st.markdown("""
            ##  This application is for Ecommerce which takes items
            
            """)



name = st.text_input("Item Name")
price = st.number_input("Item Price", min_value=0.0, step=0.01)
tax = st.number_input("Tax Rate", min_value=0.0, step=0.01)
count = st.number_input("Count in Stock", min_value=0, step=1)

if st.button("calculate"):
    data = {
        "name": name,
        "price": price,
        "tax": tax,
        "count": [count]
    }
    
    response = requests.post("http://localhost:8000/items/", json=data)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Final Price for {result['name']}: {result['final_price']:.2f}")
    else:
        st.error("Failed to calculate final price. Please check the input and try again.")

