import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('myStreamlit/model.pkl', 'rb'))


st.markdown("""<style>.big-font {font-size:40px !important;color: #FF6347;}</style>""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Real Estate Price Prediction App (BE)</p>', unsafe_allow_html=True)

st.markdown('Please enter the details below to predict the price:')


with open('myStreamlit/commune_encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)


dict_subtype = {'apartment': 1, 'house': 2, 'ground_floor': 3, 'villa': 4, 'penthouse': 5, 'duplex': 6, 'flat_studio': 7, 'apartment_block': 8, 'mixed_use_building': 9, 'service_flat': 10, 'town_house': 11, 'kot': 12, 'bungalow': 13, 'mansion': 14, 'loft': 15, 'country_cottage': 16, 'farmhouse': 17, 'triplex': 18, 'exceptional_property': 19, 'chalet': 20, 'other_property': 21, 'manor_house': 22, 'castle': 23, 'pavilion': 24}
PEB_grade = {'A++': 9, 'A+': 8, 'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 1}
kitchen_new_mapping = {'NOT_INSTALLED': 0, 'INSTALLED': 1, 'SEMI_EQUIPPED': 2, 'HYPER_EQUIPPED': 3, 'USA_HYPER_EQUIPPED': 4, 'USA_INSTALLED': 5, 'USA_SEMI_EQUIPPED': 6, 'USA_UNINSTALLED': 7}
Building_state_grade = {'GOOD': 4, 'AS_NEW': 6, 'TO_RENOVATE': 1, 'TO_BE_DONE_UP': 3, 'JUST_RENOVATED': 5, 'TO_RESTORE': 2}
type_house = {'House': 1, 'Apartment': 2}


col1, col2, col3 = st.columns(3)

with col1:
    district_name = st.selectbox('Name of The Commune:', options=encoder.classes_)
    bathroom = st.number_input('Number of Bathrooms', min_value=0, max_value=100, value=1)
    bedroom = st.number_input('Number of Bedrooms', min_value=0, max_value=100, value=1)
    construction_year = st.number_input('Construction Year', min_value=1700, max_value=2030, value=2000)
    kitchen = kitchen_new_mapping[st.selectbox('Kitchen Type', options=list(kitchen_new_mapping.keys()), index=0)]

with col2:
    living_area = st.number_input('Living Area (m²)', min_value=0, max_value=10000, value=100)
    postal_code = st.number_input('Postal Code', min_value=1000, max_value=9999, value=1000)
    room_count = st.number_input('Number of Rooms', min_value=0, max_value=500, value=1)
    garden_area = st.number_input('Garden Area (m²)', min_value=0, max_value=50000, value=100)
    subtype_of_property = dict_subtype[st.selectbox('Subtype of Property', options=list(dict_subtype.keys()), index=0)]
    surface_of_plot = st.number_input('Surface of Plot (m²)', min_value=0, max_value=500000, value=100)

with col3:
    garden = st.checkbox('Does the house have a Garden?')
    swimming_pool = st.checkbox('Does the house have a Swimming Pool?')
    terrace = st.checkbox('Does the house have a Terrace?')
    fireplace = st.checkbox('Does the house have a Fireplace?')
    flooding_zone = st.checkbox('Is the house in a Flooding Zone?')
    furnished = st.checkbox('Is the house Furnished?')


toilet_count = st.number_input('Number of Toilets', min_value=0, max_value=500, value=1)
type_of_property = type_house[st.selectbox('Type of Property', options=list(type_house.keys()), index=0)]
PEB_grade_selection = PEB_grade[st.selectbox('PEB Grade', options=list(PEB_grade.keys()), index=0)]
building_state_grade = Building_state_grade[st.selectbox('Building State Grade', options=list(Building_state_grade.keys()), index=0)]


district_encoded = encoder.transform([district_name])[0]


user_input = {
    'bathroom': bathroom, 'bedroom': bedroom, 'construction_year': construction_year, 'fireplace': fireplace,
    'flooding_zone': flooding_zone, 'furnished': furnished, 'garden': garden, 'garden_area': garden_area,
    'kitchen': kitchen, 'living_area': living_area, 'postal_code': postal_code, 'room_count': room_count,
    'subtype_of_property': subtype_of_property, 'surface_of_plot': surface_of_plot, 'swimming_pool': swimming_pool,
    'terrace': terrace, 'toilet_count': toilet_count, 'type_of_property': type_of_property, 'PEB_grade': PEB_grade_selection,
    'Building_state_grade': building_state_grade, 'Nom_commune_encoded': district_encoded
}
user_input_df = pd.DataFrame([user_input])


prediction = model.predict(user_input_df)
st.subheader('Live Predicted Price:')
st.markdown(f'<p style="color: #FF6347; font-size: 24px;">{prediction[0]:.2f}€</p>', unsafe_allow_html=True)




