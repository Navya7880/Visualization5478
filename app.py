import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 File Upload & Visualization App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of the uploaded file:")
    st.dataframe(df.head())

    # Select numeric columns only for visualization
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if len(numeric_columns) < 1:
        st.warning("No numeric columns found for visualization.")
    else:
        st.sidebar.header("Choose your visualization settings")

        # Let user pick columns
        x_axis = st.sidebar.selectbox("Select X-axis column", numeric_columns)
        y_axis = st.sidebar.selectbox("Select Y-axis column (if applicable)", numeric_columns)

        # Visualization options
        chart_type = st.sidebar.multiselect(
            "Choose up to 4 visualizations",
            ["Line Chart", "Bar Chart", "Histogram", "Scatter Plot"],
            default=["Line Chart", "Bar Chart"]
        )

        for chart in chart_type:
            st.write(f"### {chart}")
            fig, ax = plt.subplots(figsize=(6, 4))

            if chart == "Line Chart":
                ax.plot(df[x_axis], df[y_axis], marker='o')
                ax.set_xlabel(x_axis)
                ax.set_ylabel(y_axis)

            elif chart == "Bar Chart":
                sns.barplot(x=x_axis, y=y_axis, data=df, ax=ax)

            elif chart == "Histogram":
                sns.histplot(df[x_axis], bins=30, kde=True, ax=ax)

            elif chart == "Scatter Plot":
                ax.scatter(df[x_axis], df[y_axis], alpha=0.6)
                ax.set_xlabel(x_axis)
                ax.set_ylabel(y_axis)

            st.pyplot(fig)
else:
    st.info("Please upload a CSV file to get started.")

