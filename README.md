## Real Estate Price Prediction App 🏠

### Overview 📖

Hello Dear User,
This Streamlit application provides predictions on real estate prices based on user-inputted property details. Leveraging a trained machine learning model(GradientBoostingRegressor), it interprets factors such as type, size, amenities, and location to estimate market values effectively.

### Features ✨

- User Inputs: Users can input various property details including type, number of rooms, size, and amenities through an intuitive interface.
- Dynamic Predictions: Provides real-time property price predictions as users input or modify the details.
- Styled Components: Custom HTML and CSS are used for styling, enhancing the visual presentation of the app.

### Installation

```bash

# Clone the repository
git clone git@github.com:mstfgul/Immo_Eliza_Deployment.git
cd myStreamlit

# Set up a virtual environment 
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install required packages
pip install -r requirements.txt

### How to Run the App

With the dependencies installed, you can start the app using Streamlit:

streamlit run app.py

The app will be live at http://localhost:8501 in your web browser.

```

### Dependencies

- streamlit: For creating the web interface and handling app logic.

- pandas: For managing data structures.

- pickle: To load pre-trained models and some features data.

```bash
app/
│
├── app.py               # Main application script
├── model.pkl            # Serialized machine learning model
├── commune_encoder.pkl  # Serialized label encoder for communes
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```


### Authors

Mustafa Gul - Initial Work - https://github.com/mstfgul