# Mine Rehabilitation Financial Investment Analysis

## Objective 3: Financial Investment Analysis for Mine Rehabilitation Projects

This repository contains a comprehensive Python-based financial analysis framework for analyzing investments in mine rehabilitation projects. The analysis addresses the research question: **"To analyse the financial investments made in rehabilitation projects of the selected mines."**

## 📊 Analysis Framework

### 1. Economic Data Analysis
- **Descriptive Statistics**: Calculate total, per-area, and per-ton rehabilitation investments
- **Trend Analysis**: Time series analysis to track changes in rehabilitation investments over time
- **Ratio Analysis**: Calculate rehabilitation investment as a percentage of mining revenue or profit

### 2. Correlation and Regression Analysis
- **Correlation Analysis**: Examine relationships between financial investments and rehabilitation effectiveness ratings
- **Multiple Regression**: Model the relationship between investment levels and ecological recovery indicators

### 3. Cost-Benefit Analysis
- **Cost-Effectiveness Analysis**: Estimate rehabilitation costs against recovered ecosystem service values
- **Net Present Value (NPV)**: Apply NPV calculations for long-term rehabilitation investments with discount rates and benefit degradation

### 4. Econometric Methods
- **Panel Data Models**: Use fixed-effects and random-effects models to analyze investment patterns while controlling for company-specific factors

## 🔧 Implementation

### Main Analysis Notebook
- **`Mine_Rehabilitation_Financial_Analysis.ipynb`**: Complete Jupyter notebook with all analytical methods
  - Interactive Google Colab compatible
  - Comprehensive visualizations
  - Statistical tests and model diagnostics
  - Sample data generation for demonstration

### Supporting Files
- **`test_analysis.py`**: Standalone test script to verify functionality
- **`tt.xlsx`**: Sample data file (original repository data)

## 📈 Key Features

### Data Generation
- Realistic sample data for 5 mines over 10 years (2014-2023)
- Financial metrics (revenue, profit, rehabilitation investments)
- Ecological indicators (vegetation recovery, soil quality, water quality)
- Derived metrics (per-area costs, ratios, effectiveness ratings)

### Statistical Methods
- Descriptive statistics and data visualization
- Correlation matrices and scatter plots
- Multiple regression with diagnostics
- Time series analysis and stationarity tests
- Panel data models (fixed/random effects)
- ANOVA tests for group differences

### Financial Metrics
- Benefit-Cost Ratios
- Net Present Value calculations
- Payback period analysis
- Sensitivity analysis for discount rates
- Investment effectiveness measures

### Visualizations
- Investment trend plots
- Correlation heatmaps
- Scatter plots with trend lines
- Distribution histograms
- Box plots by mine
- Residual analysis plots

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn statsmodels openpyxl linearmodels
```

### Running the Analysis

#### Option 1: Google Colab
1. Open the notebook in Google Colab using the badge link
2. Run all cells sequentially
3. The notebook will install required packages automatically

#### Option 2: Local Jupyter
1. Clone this repository
2. Install required packages
3. Launch Jupyter notebook
4. Open `Mine_Rehabilitation_Financial_Analysis.ipynb`

#### Option 3: Standalone Testing
```bash
python test_analysis.py
```

## 📋 Analysis Outputs

### 1. Descriptive Statistics
- Total and average investments across all projects
- Per-area and per-ton investment calculations
- Investment ratios relative to revenue and profit
- Mine-specific investment patterns

### 2. Trend Analysis
- Annual investment growth rates
- Linear trend analysis with statistical significance
- Stationarity testing for time series
- Seasonal and cyclical pattern identification

### 3. Effectiveness Analysis
- Investment-effectiveness correlations
- Multiple regression models predicting outcomes
- Ecological recovery composite indices
- Statistical significance testing

### 4. Economic Evaluation
- Benefit-cost ratios for all projects
- NPV calculations with sensitivity analysis
- Payback period estimates
- Risk assessment through Monte Carlo methods

### 5. Panel Data Insights
- Mine-specific fixed effects
- Time trends controlling for heterogeneity
- Between and within-mine variation analysis
- Policy recommendations based on model results

## 📊 Sample Results

Based on the simulated data:
- **Total Investment**: ~$250M across all projects
- **Average B/C Ratio**: 3.5-4.5 (highly favorable)
- **Positive NPV Projects**: 85-100% depending on discount rate
- **Investment-Effectiveness Correlation**: 0.6-0.8 (strong positive)
- **Average Payback Period**: 8-12 years

## 🔬 Methodology

### Analytical Approach
1. **Data Collection/Generation**: Comprehensive dataset with financial and ecological variables
2. **Exploratory Analysis**: Descriptive statistics and visualization
3. **Statistical Modeling**: Correlation, regression, and panel data analysis
4. **Economic Evaluation**: Cost-benefit and NPV analysis
5. **Interpretation**: Policy recommendations and insights

### Model Specifications
- **OLS Regression**: Basic relationship modeling
- **Fixed Effects**: Control for unobserved mine characteristics
- **Random Effects**: Efficient estimation under assumptions
- **NPV Models**: Multi-period investment evaluation

## 📚 Documentation

Each analysis section includes:
- Theoretical background
- Implementation details
- Results interpretation
- Statistical diagnostics
- Visualization outputs
- Policy implications

## ⚠️ Limitations and Considerations

### Data Limitations
- Sample data is simulated for demonstration
- Real applications require actual financial and ecological data
- External factors (regulations, market conditions) not included

### Methodological Considerations
- NPV calculations use simplified assumptions
- Benefit degradation rates are estimated
- Risk and uncertainty not fully quantified
- Causal inference limitations in observational data

## 🔮 Future Enhancements

### Recommended Extensions
1. **Risk Analysis**: Monte Carlo simulations and Value at Risk
2. **Optimization Models**: Optimal investment allocation
3. **Machine Learning**: Predictive models for investment outcomes
4. **Spatial Analysis**: Geographic factors in effectiveness
5. **Real Options**: Valuation of investment flexibility

### Data Integration
- Remote sensing data for ecological monitoring
- Market data for commodity prices
- Regulatory compliance costs
- Community impact assessments

## 🤝 Contributing

This analysis framework can be extended for:
- Different mining contexts (coal, metals, quarries)
- Various rehabilitation approaches
- Alternative economic evaluation methods
- Integration with environmental impact assessments

## 📄 License

This project is part of academic research on mine rehabilitation economics. Please cite appropriately if using for research purposes.

## 📞 Contact

For questions about the methodology or implementation, please refer to the detailed documentation within the Jupyter notebook.

---

**Note**: This implementation uses simulated data for demonstration purposes. Real-world applications should use actual financial and ecological monitoring data from rehabilitation projects.