import streamlit as st
import pandas as pd
import pickle

# Page config must be first Streamlit command
st.set_page_config(page_title="Petrol Consumption Predictor", layout="wide")

@st.cache_resource
def load_model():
    try:
        with open("model.pkl", "rb") as file:
            return pickle.load(file)
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

def main():
    st.title("⛽ Petrol Consumption Prediction App")
    st.write("Predict petrol consumption based on economic and infrastructure factors.")

    model_loaded = load_model()
    if model_loaded is None:
        return

    # Feature names & ranges
    input_features = [
        'Petrol_tax',
        'Average_income',
        'Paved_Highways',
        'Population_Driver_licence(%)'
    ]

    feature_ranges = {
        'Petrol_tax': {'min': 5.0, 'max': 10.0},
        'Average_income': {'min': 3063, 'max': 5342},
        'Paved_Highways': {'min': 431, 'max': 17782},
        'Population_Driver_licence(%)': {'min': 0.451, 'max': 0.724}
    }

    st.sidebar.header("🔧 Input Features")

    input_values = {}

    for feature in input_features:
        min_val = feature_ranges[feature]['min']
        max_val = feature_ranges[feature]['max']
        label = feature.replace('_', ' ')

        if feature == 'Petrol_tax':
            input_values[feature] = st.sidebar.slider(label, float(min_val), float(max_val), (min_val + max_val) / 2)
        elif feature in ['Average_income', 'Paved_Highways']:
            input_values[feature] = st.sidebar.slider(label, int(min_val), int(max_val), int((min_val + max_val) / 2))
        else:
            input_values[feature] = st.sidebar.slider(label, float(min_val), float(max_val), (min_val + max_val) / 2, step=0.001)

    st.subheader("📋 Your Input Values")
    st.dataframe(pd.DataFrame([input_values]))

    if st.button("🚀 Predict Petrol Consumption"):
        input_df = pd.DataFrame([input_values])
        prediction = model_loaded.predict(input_df)[0]

        st.success(f"🛢️ Predicted Petrol Consumption: **{prediction:.2f}** units")

        st.caption("Note: Output is based on the trained regression model and dataset scale.")

if __name__ == "__main__":
    main()
