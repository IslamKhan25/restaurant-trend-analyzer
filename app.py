uploaded_file = st.file_uploader("Upload Zomato CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
