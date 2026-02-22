import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

# Load the exported model and preprocessing components
model = joblib.load('logistic_regression_model.joblib')
encoder = joblib.load('one_hot_encoder.joblib')
scaler = joblib.load('standard_scaler.joblib')
pca = joblib.load('pca_model.joblib')

# Define feature lists (these were identified during preprocessing)
categorical_features = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
numerical_features = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']

st.title('Adult Income Prediction')
def preprocess_input(input_df):
    # One-hot encode categorical features
    input_encoded = encoder.transform(input_df[categorical_features])
    input_encoded_df = pd.DataFrame(input_encoded, columns=encoder.get_feature_names_out(categorical_features))

    # Scale numerical features
    input_scaled = scaler.transform(input_df[numerical_features])
    input_scaled_df = pd.DataFrame(input_scaled, columns=numerical_features)

    # Concatenate processed features
    input_processed = pd.concat([input_encoded_df, input_scaled_df], axis=1)

    # Apply PCA
    input_pca = pca.transform(input_processed)
    return input_pca
# Streamlit UI for user input
st.sidebar.header('User Input Features')

def user_input_features():
    # Get unique values for categorical features from the encoder (assuming they were fitted properly)
    # This is a workaround as encoder.categories_ returns arrays, which need to be converted to lists/tuples

    # For 'workclass'
    workclass_options = encoder.categories_[categorical_features.index('workclass')].tolist()
    workclass = st.sidebar.selectbox('Workclass', workclass_options)

    # For 'education'
    education_options = encoder.categories_[categorical_features.index('education')].tolist()
    education = st.sidebar.selectbox('Education', education_options)

    # For 'marital-status'
    marital_status_options = encoder.categories_[categorical_features.index('marital-status')].tolist()
    marital_status = st.sidebar.selectbox('Marital Status', marital_status_options)

    # For 'occupation'
    occupation_options = encoder.categories_[categorical_features.index('occupation')].tolist()
    occupation = st.sidebar.selectbox('Occupation', occupation_options)

    # For 'relationship'
    relationship_options = encoder.categories_[categorical_features.index('relationship')].tolist()
    relationship = st.sidebar.selectbox('Relationship', relationship_options)

    # For 'race'
    race_options = encoder.categories_[categorical_features.index('race')].tolist()
    race = st.sidebar.selectbox('Race', race_options)

    # For 'sex'
    sex_options = encoder.categories_[categorical_features.index('sex')].tolist()
    sex = st.sidebar.selectbox('Sex', sex_options)

    # For 'native-country'
    native_country_options = encoder.categories_[categorical_features.index('native-country')].tolist()
    native_country = st.sidebar.selectbox('Native Country', native_country_options)

    age = st.sidebar.slider('Age', 17, 90, 30)
    fnlwgt = st.sidebar.slider('Final Weight (fnlwgt)', 10000, 1500000, 200000)
    education_num = st.sidebar.slider('Education Number', 1, 16, 9)
    capital_gain = st.sidebar.slider('Capital Gain', 0, 100000, 0)
    capital_loss = st.sidebar.slider('Capital Loss', 0, 4356, 0)
    hours_per_week = st.sidebar.slider('Hours per Week', 1, 99, 40)

    data = {
        'age': age,
        'workclass': workclass,
        'fnlwgt': fnlwgt,
        'education': education,
        'education-num': education_num,
        'marital-status': marital_status,
        'occupation': occupation,
        'relationship': relationship,
        'race': race,
        'sex': sex,
        'capital-gain': capital_gain,
        'capital-loss': capital_loss,
        'hours-per-week': hours_per_week,
        'native-country': native_country
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('User Input features')
st.write(input_df)

if st.sidebar.button('Predict Income'):
    processed_input = preprocess_input(input_df)
    prediction = model.predict(processed_input)

    st.subheader('Prediction')
    st.write('The predicted income is: ')
    if prediction[0] == '>50K':
        st.write('**>50K**')
    else:
        st.write('**<=50K**')
