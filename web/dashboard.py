import streamlit as st
import matplotlib.pyplot as plt
from performance_analysis import run_analysis

st.title("Sorting Algorithm Performance Dashboard")

st.write("Compare sorting algorithms using Data Analytics")

size = st.slider("Select Dataset Size", 100, 5000, 500)

if st.button("Run Analysis"):

    df = run_analysis(size)

    st.write("Performance Results")
    st.dataframe(df)

    fig, ax = plt.subplots()

    ax.bar(df['Algorithm'], df['Time'])

    ax.set_xlabel("Sorting Algorithm")
    ax.set_ylabel("Execution Time (seconds)")
    ax.set_title("Sorting Algorithm Performance")

    st.pyplot(fig)