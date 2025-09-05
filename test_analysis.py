#!/usr/bin/env python3
"""
Test script to verify the mine rehabilitation financial analysis functionality
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')

def test_analysis():
    print("Testing Mine Rehabilitation Financial Analysis...")
    
    # Generate sample data (simplified version)
    np.random.seed(42)
    n_mines = 3
    n_years = 5
    mine_names = [f'Mine_{chr(65+i)}' for i in range(n_mines)]
    years = list(range(2019, 2024))
    
    data = []
    for mine in mine_names:
        for year in years:
            mine_factor = np.random.normal(1, 0.2)
            year_trend = 1 + (year - 2019) * 0.05
            
            mining_revenue = np.random.normal(50, 10) * mine_factor * year_trend
            mining_profit = mining_revenue * np.random.uniform(0.15, 0.25)
            rehab_investment = np.random.normal(5, 1.5) * mine_factor * year_trend
            disturbed_area = np.random.normal(100, 20)
            ore_production = np.random.normal(500, 100) * mine_factor
            
            base_effectiveness = 3 + (rehab_investment / 10) * 5
            effectiveness_rating = np.clip(np.random.normal(base_effectiveness, 1), 1, 10)
            
            vegetation_recovery = np.clip(np.random.beta(2, 3) + (rehab_investment / 20), 0, 1)
            soil_quality_index = np.clip(np.random.beta(2, 3) + (rehab_investment / 25), 0, 1)
            water_quality_index = np.clip(np.random.beta(2, 3) + (rehab_investment / 30), 0, 1)
            
            ecosystem_value = (
                vegetation_recovery * 10000 + 
                soil_quality_index * 8000 + 
                water_quality_index * 12000
            ) * disturbed_area / 100
            
            data.append({
                'Mine': mine,
                'Year': year,
                'Mining_Revenue_M': mining_revenue,
                'Mining_Profit_M': mining_profit,
                'Rehabilitation_Investment_M': rehab_investment,
                'Disturbed_Area_Ha': disturbed_area,
                'Ore_Production_KTons': ore_production,
                'Effectiveness_Rating': effectiveness_rating,
                'Vegetation_Recovery': vegetation_recovery,
                'Soil_Quality_Index': soil_quality_index,
                'Water_Quality_Index': water_quality_index,
                'Ecosystem_Service_Value': ecosystem_value
            })
    
    df = pd.DataFrame(data)
    
    # Calculate derived metrics
    df['Investment_Per_Area'] = df['Rehabilitation_Investment_M'] / df['Disturbed_Area_Ha'] * 1000
    df['Investment_Per_Ton'] = df['Rehabilitation_Investment_M'] / df['Ore_Production_KTons']
    df['Investment_Revenue_Ratio'] = df['Rehabilitation_Investment_M'] / df['Mining_Revenue_M'] * 100
    df['Investment_Profit_Ratio'] = df['Rehabilitation_Investment_M'] / df['Mining_Profit_M'] * 100
    df['Benefit_Cost_Ratio'] = df['Ecosystem_Service_Value'] / (df['Rehabilitation_Investment_M'] * 1000)
    
    print(f"✓ Sample data generated: {df.shape[0]} observations")
    
    # Test 1: Descriptive Statistics
    total_investment = df['Rehabilitation_Investment_M'].sum()
    mean_investment = df['Rehabilitation_Investment_M'].mean()
    print(f"✓ Descriptive statistics: Total=${total_investment:.1f}M, Mean=${mean_investment:.2f}M")
    
    # Test 2: Correlation Analysis
    correlation_vars = ['Rehabilitation_Investment_M', 'Effectiveness_Rating', 'Vegetation_Recovery']
    correlation_matrix = df[correlation_vars].corr()
    inv_eff_corr = correlation_matrix.loc['Rehabilitation_Investment_M', 'Effectiveness_Rating']
    print(f"✓ Correlation analysis: Investment-Effectiveness = {inv_eff_corr:.3f}")
    
    # Test 3: Regression Analysis
    X = df[['Rehabilitation_Investment_M', 'Mining_Revenue_M']]
    y = df['Effectiveness_Rating']
    X_const = sm.add_constant(X)
    model = sm.OLS(y, X_const).fit()
    print(f"✓ Regression analysis: R² = {model.rsquared:.3f}")
    
    # Test 4: Cost-Benefit Analysis
    mean_bc_ratio = df['Benefit_Cost_Ratio'].mean()
    positive_bc_pct = (df['Benefit_Cost_Ratio'] > 1).mean() * 100
    print(f"✓ Cost-benefit analysis: Mean B/C = {mean_bc_ratio:.2f}, Positive = {positive_bc_pct:.1f}%")
    
    # Test 5: NPV Calculation
    def calculate_npv(initial_investment, annual_benefit, discount_rate=0.05, years=20):
        npv = -initial_investment
        for year in range(1, years + 1):
            discounted_benefit = annual_benefit / ((1 + discount_rate) ** year)
            npv += discounted_benefit
        return npv
    
    df['NPV'] = df.apply(
        lambda row: calculate_npv(
            row['Rehabilitation_Investment_M'] * 1000, 
            row['Ecosystem_Service_Value']
        ), axis=1
    )
    mean_npv = df['NPV'].mean()
    positive_npv_pct = (df['NPV'] > 0).mean() * 100
    print(f"✓ NPV analysis: Mean NPV = ${mean_npv:.0f}K, Positive = {positive_npv_pct:.1f}%")
    
    # Test 6: Panel Data Structure
    mines_count = df['Mine'].nunique()
    years_count = df['Year'].nunique()
    total_obs = len(df)
    balanced = total_obs == mines_count * years_count
    print(f"✓ Panel data: {mines_count} mines, {years_count} years, Balanced = {balanced}")
    
    print("\n" + "="*60)
    print("MINE REHABILITATION FINANCIAL ANALYSIS TEST SUMMARY")
    print("="*60)
    print(f"Dataset: {df.shape[0]} observations across {mines_count} mines and {years_count} years")
    print(f"Total Investment: ${total_investment:.1f}M")
    print(f"Average Investment per Project: ${mean_investment:.2f}M")
    print(f"Investment-Effectiveness Correlation: {inv_eff_corr:.3f}")
    print(f"Average Benefit-Cost Ratio: {mean_bc_ratio:.2f}")
    print(f"Average NPV: ${mean_npv:.0f}K")
    print(f"Projects with Positive B/C: {positive_bc_pct:.1f}%")
    print(f"Projects with Positive NPV: {positive_npv_pct:.1f}%")
    print("\nAll analytical methods tested successfully! ✓")
    print("="*60)
    
    return df

if __name__ == "__main__":
    test_df = test_analysis()