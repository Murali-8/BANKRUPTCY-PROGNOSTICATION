from copyreg import pickle
import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))


def main():
    st.title('Bankruptcy Prediction')
    st.text('This model will helps to predict the Company will Bankrupt or Not based on various Parameters.')

    st.title('Inputs')

     # Input
    st.write('ROA(C) before interest and depreciation before interest')
    ROA_C = st.number_input('ROA(C)',step=0.01,format="%.5f")
    
    st.write('Net Value Growth Rate')
    Net_Value_Growth_Rate= st.number_input('Net Value Growth Rate',step=0.01,format="%.5f")

    st.write('Interest Expense Ratio')
    Interest_Expense_Ratio= st.number_input('Interest Expense Ratio',step=0.01,format="%.5f")

    st.write('Pre-tax net Interest Rate')
    Pre_tax_net_IR = st.number_input('Pre-tax net Interest Rate',step=0.01,format="%.5f")
    
    st.write('After-tax net Interest Rate')
    After_tax_net_IR= st.number_input('After-tax net Interest Rate',step=0.01,format="%.5f")

    st.write('Non-industry income and expenditure/revenue')
    Non_industryincome= st.number_input('Non-industry income and expenditure/revenue',step=0.01,format="%.5f")

    st.write('Continuous interest rate (after tax)')
    Continuous_IR = st.number_input('Continuous interest rate (after tax)',step=0.01,format="%.5f")

    st.write('Interest-bearing debt interest rate')
    debt_IR = st.number_input('Interest-bearing debt interest rate',step=0.01,format="%.5f")

    st.write('Revenue per person')
    Revenue_per_person= st.number_input('Revenue per person',step=0.01,format="%.5f")

    st.write('Persistent EPS in the Last Four Seasons')
    EPS= st.number_input('Persistent EPS in the Last Four Seasons',step=0.01,format="%.5f")

    st.write('Per Share Net profit before tax (Yuan ¥)')
    Net_profit_per_Share_Yuan= st.number_input('Per Share Net profit before tax (Yuan ¥)',step=0.01,format="%.5f")
    
    st.write('Quick Ratio')
    Quick_Ratio = st.number_input('Quick Ratio',step=0.01,format="%.5f")

    st.write('Total debt/Total net worth')
    Total_debt_Total_net_worth = st.number_input('Total debt/Total net worth',step=0.01,format="%.5f")

    st.write('Debt ratio %')
    Debt_ratio_Percentage = st.number_input('Debt ratio %',step=0.01,format="%.5f")

    st.write('Net worth/Assets')
    Net_worth_Assets = st.number_input('Net worth/Assets',step=0.01,format="%.5f")

    st.write('Borrowing dependency')
    Borrowing_dependency= st.number_input('Borrowing dependency',step=0.01,format="%.5f")
    
    st.write('Net profit before tax/Paid-in capital')
    Net_profit_before_tax= st.number_input('Net profit before tax/Paid-in capital',step=0.01,format="%.5f")
    
    st.write('Allocation rate per person')
    Allocation_rate_per_person= st.number_input('Allocation rate per person',step=0.01,format="%.5f")

    st.write('Inventory/Working Capital')
    Inventory_Working_Capital= st.number_input('Inventory/Working Capital',step=0.01,format="%.5f")
    
    st.write('Current Liabilities/Equity')
    Current_Liabilities_Equity = st.number_input('Current Liabilities/Equity',step=0.01,format="%.5f")
    
    st.write('Long-term Liability to Current Assets')
    Longterm_Liability_to_Current_Assets= st.number_input('Long-term Liability to Current Assets',step=0.01,format="%.5f")

    st.write('Retained Earnings to Total Assets')
    Retained_Earnings_to_Total_Assets = st.number_input('Retained Earnings to Total Assets',step=0.01,format="%.5f")

    st.write('Total income/Total expense')
    Total_income_Total_expense= st.number_input('Total income/Total expense',step=0.01,format="%.5f")

    st.write('Cash Turnover Rate')
    Cash_Turnover_Rate= st.number_input('Cash Turnover Rate',step=0.01,format="%.5f")

    st.write('Current Liability to Equity')
    Current_Liability_to_Equity= st.number_input('Current Liability to Equity',step=0.01,format="%.5f")

    st.write('Net Income to Total Assets')
    Net_Income_to_Total_Assets= st.number_input('Net Income to Total Assets',step=0.01,format="%.5f")
 
    st.write("Net Income to Stockholders Equity")
    Net_Income_to_Stockholders_Equity = st.number_input("Net Income to Stockholder's Equity",step=0.01,format="%.5f")
    
    st.write('Liability to Equity')
    Liability_to_Equity= st.number_input('Liability to Equity',step=0.01,format="%.5f")
   
    st.write('Degree of Financial Leverage (DFL)')
    DFL = st.number_input('Degree of Financial Leverage (DFL)',step=0.01,format="%.5f")

    st.write('Equity to Liability')
    Equity_to_Liability= st.number_input('Equity to Liability',step=0.01,format="%.5f")

    input = [[ROA_C,Net_Value_Growth_Rate,Interest_Expense_Ratio,Pre_tax_net_IR,After_tax_net_IR,Non_industryincome,Continuous_IR,debt_IR,
            Revenue_per_person,EPS,Net_profit_per_Share_Yuan ,Quick_Ratio,Total_debt_Total_net_worth,
            Debt_ratio_Percentage,Net_worth_Assets,Borrowing_dependency,Net_profit_before_tax,Allocation_rate_per_person,
            Inventory_Working_Capital,Current_Liabilities_Equity,Longterm_Liability_to_Current_Assets,Retained_Earnings_to_Total_Assets,
            Total_income_Total_expense,Cash_Turnover_Rate,Current_Liability_to_Equity,Net_Income_to_Total_Assets,Net_Income_to_Stockholders_Equity,
            Liability_to_Equity,DFL,Equity_to_Liability]]

  
    # Output
    
    
    potential="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;">Bankrupt</h2>
       </div>
    """
    not_potential="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;">Not Bankrupt</h2>
       </div>
    """

    if st.button('Predict'):
        output = model.predict(input)
        res  =  output.flatten().astype(float)

        if res > 0.5:
            st.markdown(potential, unsafe_allow_html = True)
            st.write('Suggestion: please consider your inputs and try to reduce the liabilities.')

        else:
            st.markdown(not_potential, unsafe_allow_html = True)
            st.write('Suggestion :please analyse your inputs and try to increase the assets')

if __name__ == '__main__':
    main()
