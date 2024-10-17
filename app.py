import streamlit as st
from fastapi import FastAPI

app = FastAPI()

@app.post("/predict")
def predict():
    pass


st.title("Alzheimer's Classification")
st.file_uploader("Upload image")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)