from flask import Flask,render_template, request
import joblib

app=Flask(__name__)

# code business logic


@app.route('/')
def base():
    return render_template('home.html')

@app.route('/predict', methods=['post'])
def predict():
    # load the model
    model=joblib.load('emp_att_rate.pkl')

    Age=request.form.get('Age')
    DailyRate=request.form.get('DailyRate')
    DistanceFromHome=request.form.get('DistanceFromHome')
    Education=request.form.get('Education')
    EnvironmentSatisfaction=request.form.get('EnvironmentSatisfaction')
    JobInvolvement=request.form.get('JobInvolvement')
    JobLevel=request.form.get('JobLevel')
    JobSatisfaction=request.form.get('JobSatisfaction')
    MonthlyIncome=request.form.get('MonthlyIncome')
    MonthlyRate=request.form.get('MonthlyRate')
    NumCompaniesWorked=request.form.get('NumCompaniesWorked')
    RelationshipSatisfaction=request.form.get('RelationshipSatisfaction')
    StockOptionLevel=request.form.get('StockOptionLevel')
    TotalWorkingYears=request.form.get('TotalWorkingYears')
    TrainingTimesLastYear=request.form.get('TrainingTimesLastYear')
    WorkLifeBalance=request.form.get('WorkLifeBalance')
    YearsAtCompany=request.form.get('YearsAtCompany')
    YearsInCurrentRole=request.form.get('YearsInCurrentRole')
    YearsSinceLastPromotion=request.form.get('YearsSinceLastPromotion')
    YearsWithCurrManager=request.form.get('YearsWithCurrManager')
    BusinessTravel_Non_Travel=request.form.get('BusinessTravel_Non_Travel')
    Business_Travel_Frequently=request.form.get('Business_Travel_Frequently')
    Business_Travel_Rarely=request.form.get('Business_Travel_Rarely')
    Department_Human_Resources=request.form.get('Department_Human_Resources')
    Department_RD=request.form.get('Department_RD')
    Department_Sales=request.form.get('Department_Sales')
    Education_HR=request.form.get('Education_HR')
    Education_Life_Sci=request.form.get('Education_Life_Sci')
    Education_Marketing=request.form.get('Education_Marketing')
    Education_Medical=request.form.get('Education_Medical')
    Education_Other=request.form.get('Education_Other')
    Education_Tech_deg=request.form.get('Education_Tech_deg')
    Gender_Male=request.form.get('Gender_Male')
    JobRole_Health_Rep=request.form.get('JobRole_Health_Rep')
    JobRole_HR=request.form.get('JobRole_HR')
    JobRole_Tech_lab=request.form.get('JobRole_Tech_lab')
    JobRole_Manager=request.form.get('JobRole_Manager')
    JobRole_Mnf_Dir=request.form.get('JobRole_Mnf_Dir')
    JobRole_RD=request.form.get('JobRole_RD')
    JobRole_Res_Sci=request.form.get('JobRole_Res_Sci')
    JobRole_Sales_Exe=request.form.get('JobRole_Sales_Exe')
    JobRole_Sales_Rep=request.form.get('JobRole_Sales_Rep')
    MaritalStatus_Divorced=request.form.get('MaritalStatus_Divorced')
    MaritalStatus_Married=request.form.get('MaritalStatus_Married')
    MaritalStatus_Single=request.form.get('MaritalStatus_Single')
    OverTime_Yes=request.form.get('OverTime_Yes')
    

    Age=int(Age)
    DailyRate=int(DailyRate)
    DistanceFromHome=int(DistanceFromHome)
    Education=int(Education)
    EnvironmentSatisfaction=int(EnvironmentSatisfaction)
    JobInvolvement=int(JobInvolvement)
    JobLevel=int(JobLevel)
    JobSatisfaction=int(JobSatisfaction)
    MonthlyIncome=int(MonthlyIncome)
    MonthlyRate=int(MonthlyRate)
    NumCompaniesWorked=int(NumCompaniesWorked)
    RelationshipSatisfaction=int(RelationshipSatisfaction)
    StockOptionLevel=int(StockOptionLevel)
    TotalWorkingYears=int(TotalWorkingYears)
    TrainingTimesLastYear=int(TrainingTimesLastYear)
    WorkLifeBalance=int(WorkLifeBalance)
    YearsAtCompany=int(YearsAtCompany)
    YearsInCurrentRole=int(YearsInCurrentRole)
    YearsSinceLastPromotion=int(YearsSinceLastPromotion)
    YearsWithCurrManager=int(YearsWithCurrManager)
    Business_Travel_Frequently=int(Business_Travel_Frequently)
    Business_Travel_Rarely=int(Business_Travel_Rarely)
    Department_Human_Resources=int(Department_Human_Resources)
    Department_RD=int(Department_RD)
    Department_Sales=int(Department_Sales)
    Education_HR=int(Education_HR)
    Education_Life_Sci=int(Education_Life_Sci)
    Education_Marketing=int(Education_Marketing)
    Education_Medical=int(Education_Medical)
    Education_Other=int(Education_Other)
    Education_Tech_deg=int(Education_Tech_deg)
    Gender_Male=int(Gender_Male)
    JobRole_Health_Rep=int(JobRole_Health_Rep)
    JobRole_HR=int(JobRole_HR)
    JobRole_Tech_lab=int(JobRole_Tech_lab)
    JobRole_Manager=int(JobRole_Manager)
    JobRole_Mnf_Dir=int(JobRole_Mnf_Dir)
    JobRole_RD=int(JobRole_RD)
    JobRole_Res_Sci=int(JobRole_Res_Sci)
    JobRole_Sales_Exe=int(JobRole_Sales_Exe)
    JobRole_Sales_Rep=int(JobRole_Sales_Rep)
    MaritalStatus_Divorced=int(MaritalStatus_Divorced)
    MaritalStatus_Married=int(MaritalStatus_Married)
    MaritalStatus_Single=int(MaritalStatus_Single)
    OverTime_Yes=int(OverTime_Yes)

    print(Age, DailyRate, DistanceFromHome, Education,
       EnvironmentSatisfaction, JobInvolvement, JobLevel,
       JobSatisfaction, MonthlyIncome, MonthlyRate, NumCompaniesWorked,
       RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears,
       TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany,
       YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager,
       BusinessTravel_Non_Travel,Business_Travel_Frequently, Business_Travel_Rarely,
       Department_Human_Resources, Department_RD,
       Department_Sales, Education_HR,
    Education_Life_Sci,Education_Marketing,Education_Medical, Education_Other,
       Education_Tech_deg, Gender_Male,
       JobRole_Health_Rep, JobRole_HR,
       JobRole_Tech_lab, JobRole_Manager,
       JobRole_Mnf_Dir, JobRole_RD,
       JobRole_Res_Sci, JobRole_Sales_Exe,
       JobRole_Sales_Rep, MaritalStatus_Divorced,
       MaritalStatus_Married, MaritalStatus_Single, OverTime_Yes)
    
    out=model.predict([[Age, DailyRate, DistanceFromHome, Education,
       EnvironmentSatisfaction, JobInvolvement, JobLevel,
       JobSatisfaction, MonthlyIncome, MonthlyRate, NumCompaniesWorked,
       RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears,
       TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany,
       YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager,
       BusinessTravel_Non_Travel,Business_Travel_Frequently, Business_Travel_Rarely,
       Department_Human_Resources, Department_RD,
       Department_Sales, Education_HR,Education_Life_Sci,Education_Marketing,Education_Medical, Education_Other,
       Education_Tech_deg, Gender_Male,
       JobRole_Health_Rep, JobRole_HR,
       JobRole_Tech_lab, JobRole_Manager,
       JobRole_Mnf_Dir, JobRole_RD,
       JobRole_Res_Sci, JobRole_Sales_Exe,
       JobRole_Sales_Rep, MaritalStatus_Divorced,
       MaritalStatus_Married, MaritalStatus_Single, OverTime_Yes]])
    print(out)
    
    if out<=0:
        data="The model prediction of the employee attrition as per the given data is 'NO'"
    else:
        data="The model prediction of the employee attrition as per the given data is 'YES'"

    return render_template('predict.html',data=data)
if __name__=="__main__":
    app.run(debug=True)
