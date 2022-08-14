import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'person_age':24, 'person_income':54400, 'person_home_ownership':0, 
                            'person_emp_length':8, 'loan_grade':4, 'loan_amnt':23625, 'loan_int_rate':14.27, 
                            'loan_percent_income':0.44, 'cb_person_default_on_file':0, 'cb_person_cred_hist_length':4})

print(r.json())