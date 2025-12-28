import streamlit as st
import pandas as pd
import pickle
import os

# Page config must be first Streamlit command
st.set_page_config(page_title="Petrol Consumption Predictor", layout="wide")

def load_model():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        st.write("📂 Files in app directory:", os.listdir(base_dir))  # 🔍 Debug line

        model_path = os.path.join(base_dir, "petrol_consumption_model.pkl")

        with open(model_path, "rb") as file:
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

    # Features expected by the trained model
    expected_features = [
        'Petrol_tax',
        'Average_income',
        'Paved_Highways',
        'Population_Driver_licence(%)'
    ]

    # User-friendly rounded ranges
    feature_ranges = {
        'Petrol_tax': {'min': 5.0, 'max': 10.0},
        'Average_income': {'min': 3000, 'max': 5500},
        'Paved_Highways': {'min': 0, 'max': 18000},
        'Population_Driver_licence(%)': {'min': 0, 'max': 100}  # shown as %
    }

    st.sidebar.header("🔧 Input Features")
    input_values = {}

    for feature in expected_features:
        min_val = feature_ranges[feature]['min']
        max_val = feature_ranges[feature]['max']
        label = feature.replace('_', ' ')

        if feature == 'Petrol_tax':
            input_values[feature] = st.sidebar.slider(
                label, float(min_val), float(max_val), (min_val + max_val) / 2
            )

        elif feature in ['Average_income', 'Paved_Highways']:
            input_values[feature] = st.sidebar.slider(
                label, int(min_val), int(max_val), int((min_val + max_val) / 2)
            )

        else:
            # Show 0–100% to user, convert to 0–1 for model
            perc = st.sidebar.slider(label + " (%)", int(min_val), int(max_val), 50)
            input_values[feature] = perc / 100

    # Display values back to user (with %)
    display_values = input_values.copy()
    display_values['Population_Driver_licence(%)'] *= 100

    st.subheader("📋 Your Input Values")
    st.dataframe(pd.DataFrame([display_values]))

    if st.button("🚀 Predict Petrol Consumption"):
        input_df = pd.DataFrame([input_values])

        # Ensure correct column order & names
        input_df = input_df[expected_features]

        prediction = model_loaded.predict(input_df)[0]

        st.success(f"🛢️ Predicted Petrol Consumption: **{prediction:.2f}** units")
        st.caption("Note: Output is based on the trained regression model and dataset scale.")

if __name__ == "__main__":
    main()
