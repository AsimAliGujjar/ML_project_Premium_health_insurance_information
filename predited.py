import pandas as pd
import joblib

# import sklearn
# Load the model
young_model = joblib.load('artifacts\model_young.joblib')
young_scaler= joblib.load('artifacts\scaler_young.joblib')
rest_model= joblib.load('artifacts\model_rest.joblib')
rest_scaler=joblib.load('artifacts\scaler_rest.joblib')
d={}
# d.
def risk_score(data):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    if "&"in data:
        d1, d2= data.split(" & ")
        ris=risk_scores.get(d1.lower())+risk_scores.get(d1.lower())
        return (ris- 5) / (14 - 5)
    return (risk_scores.get(data.lower())- 5) / (14 - 5)

def get_input_df(input_data):
    insurance_plan_d={'Gold': 3,'Silver': 2,'Bronze': 1}
    input_data['insurance_plan']=insurance_plan_d.get(input_data['insurance_plan'])
    df_col=['age',	'number_of_dependants',	'income_lakhs','insurance_plan','genetical_risk','normalized_risk_score','gender_Male','region_Northwest','region_Southeast','region_Southwest','marital_status_Unmarried','bmi_category_Obesity','bmi_category_Overweight','bmi_category_Underweight','smoking_status_Occasional','smoking_status_Regular','employment_status_Salaried','employment_status_Self-Employed']
    df= pd.DataFrame(columns=df_col)
    df['age']=pd.Series(input_data['age'])
    df['number_of_dependants']=pd.Series(input_data['number_of_dependants'])
    df['income_lakhs']=pd.Series(input_data['income_lakhs'])
    df['insurance_plan']=pd.Series(input_data['insurance_plan'])
    df['genetical_risk']= pd.Series(input_data['genetical_risk'])
    df['normalized_risk_score']=pd.Series(risk_score(input_data['medical_history']))
    if input_data['gender']=='Male':
        df['gender_Male']=pd.Series(1)
    else:
        df['gender_Male']=pd.Series(0)
    if input_data['region']=='Northeast':
        df['region_Northwest']=pd.Series(0)
        df['region_Southeast']=pd.Series(0)
        df['region_Southwest']=pd.Series(0)
    elif input_data['region']=='Northwest':
        df['region_Northwest'] = pd.Series(1)
        df['region_Southeast'] = pd.Series(0)
        df['region_Southwest'] = pd.Series(0)
    elif input_data['region']=='Southeast':
        df['region_Northwest'] = pd.Series(0)
        df['region_Southeast'] = pd.Series(1)
        df['region_Southwest'] = pd.Series(0)
    elif input_data['region']=='Southwest':
        df['region_Northwest']=pd.Series(0)
        df['region_Southeast']=pd.Series(0)
        df['region_Southwest']=pd.Series(1)
    if input_data['marital_status']=='Unmarried':
        df['marital_status_Unmarried']=pd.Series(1)
    else:
        df['marital_status_Unmarried'] = pd.Series(0)
    if input_data['bmi_category']=='Overweight':
        df['bmi_category_Obesity']=pd.Series(0)
        df['bmi_category_Overweight'] =pd.Series(1)
        df['bmi_category_Underweight']=pd.Series(0)
    elif input_data['bmi_category']=='Obesity':
        df['bmi_category_Obesity']=pd.Series(1)
        df['bmi_category_Overweight'] =pd.Series(0)
        df['bmi_category_Underweight']=pd.Series(0)
    elif input_data['bmi_category']=='Underweight':
        df['bmi_category_Obesity']=pd.Series(0)
        df['bmi_category_Overweight'] =pd.Series(0)
        df['bmi_category_Underweight']=pd.Series(1)
    elif input_data['bmi_category']=='Normal':
        df['bmi_category_Obesity']=pd.Series(0)
        df['bmi_category_Overweight'] =pd.Series(0)
        df['bmi_category_Underweight']=pd.Series(0)
    if input_data['smoking_status']=='Occasional':
        df['smoking_status_Occasional']=pd.Series(1)
        df[ 'smoking_status_Regular']=pd.Series(0)
    elif input_data['smoking_status']=='Regular':
        df['smoking_status_Occasional']=pd.Series(0)
        df[ 'smoking_status_Regular']=pd.Series(1)
    elif input_data['smoking_status']=='No Smoking':
        df['smoking_status_Occasional']=pd.Series(0)
        df[ 'smoking_status_Regular']=pd.Series(0)
    if input_data['employment_status']=='Salaried':
        df['employment_status_Salaried']=pd.Series(1)
        df['employment_status_Self-Employed']=pd.Series(0)
    elif input_data['employment_status']=='Self-Employed':
        df['employment_status_Salaried']=pd.Series(0)
        df['employment_status_Self-Employed']=pd.Series(1)
    elif input_data['employment_status']=='Freelancer':
        df['employment_status_Salaried']=pd.Series(0)
        df['employment_status_Self-Employed']=pd.Series(0)
    df['income_level']=pd.Series(0)
    return pre(df)


def pre(df):
    if df['age'][0]<=25:
        y_s = young_scaler['scaler']
        y_c = young_scaler['cols_to_scale']
        df[y_c]=y_s.fit_transform(df[y_c])
        df.drop(['income_level'],axis=1,inplace=True)
        return young_model.predict(df)
    else:
        r_s = rest_scaler['scaler']
        r_c = rest_scaler['cols_to_scale']
        df[r_c] = r_s.fit_transform(df[r_c])
        df.drop(['income_level'], axis=1,inplace=True)
        return rest_model.predict(df)
# Define the prediction function
def predict_data(input_data):

    return get_input_df(input_data)

