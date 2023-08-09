import streamlit as st
import ShopSuggester as ss

st.header("A Simple Store Name suggester")

name = st.text_input("Enter the types of products you Want in your STORE")

but = st.button("Tell me a name", key = "primary")

if but:
    Store = ss.shop_suggestions(name)
    StoreName = Store['store_name']
    StoreArticals = Store["products"]
    st.subheader("Name Suggested for the store:")
    st.info(StoreName.strip())

    st.text("PRODUCTS THAT CANE BE HANDLED!")
    st.text(StoreArticals)
    # for articals in StoreArticals:
    #     st.text("-",articals)

