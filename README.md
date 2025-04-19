# InsuranceRiskAnalyzer
The **Insurance Risk Analyzer** is a Python-powered data science project that analyzes and predicts healthcare risk and insurance charges using demographic and lifestyle data. It includes a machine learning model and a Streamlit-powered web app that allows users to input personal health data and receive a predicted medical charge and risk category.
- See web: https://estmaria-insurance-risk-analyzer.streamlit.app/

## 🚀 Features
- 📊 **Data Analysis** of medical charges by smoking status, BMI, age, and region
- 📈 **Linear Regression Model** to predict individual medical insurance costs
- 🧠 **Custom Risk Scoring Algorithm** based on age, BMI, and smoking status
- 🎨 **Interactive Visualizations** (box plots, histograms, scatter plots)
- 🌐 **Streamlit Web App**: User-friendly form to estimate insurance risk and costs in real time

## 💻 Technologies Used
- Python (pandas, numpy, sklearn, seaborn, matplotlib)
- Machine Learning: Linear Regression
- Web App: Streamlit
- Model Persistence: joblib

## 📥 User Inputs (via Web App)
- Age
- Sex
- BMI
- Smoker status
- Number of children
- Region

The app returns:
- 🔢 A calculated **Risk Score**
- 🟢 A **Risk Category**: Low, Medium, or High
- 💰 **Predicted Medical Charges**

## 📁 Project Files
- `insurance.csv`: Source dataset
- `insurance_risk_report.csv`: Output file with predicted charges
- `risk_analyzer.ipynb`: Data analysis and visualization
- `linreg_model.pkl`: Trained linear regression model
- `streamlit_app.py`: Streamlit UI script

## 📸 Sample Visualizations
- Medical Charges vs. Age/BMI by Smoking Status
  ![image](https://github.com/user-attachments/assets/bf44924b-e6a1-4f6c-b9da-38aa9f87b67b)
- Risk Score Distribution
  ![image](https://github.com/user-attachments/assets/bd250d82-173e-4645-a284-0952d7dea9be)
- Actual vs. Predicted Charges Scatter Plot
![image](https://github.com/user-attachments/assets/267c3b74-7168-4b4f-a210-07afec8ec804)

  ## 🧠 Insights
- Smokers have significantly higher charges, across all ages and BMI
- The Southeast region tends to have higher medical costs
- There is a compounding effect between smoking and high BMI on risk and charges
- The model slightly underestimates costs for high-risk individuals

  ## ⚙️ Getting Started
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run streamlit_app.py`

   ## 📚 Data Source
- [Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
