# ITC Hotels Data Analytics Project
> Built as part of applied analytics work focused on real-world decision-making scenarios.
> Real-world hotel booking analysis using 3,00,000 records to uncover what actually drives revenue, not just what looks good on charts.

---

## Overview

This project analyzes large-scale hotel booking data to understand how revenue, customer behavior, and booking patterns interact in a real business environment.

The focus is not just on performing analysis, but on identifying signals that can support better decision-making.

---

## Why this project exists

Most data analytics projects are tool-driven.

This one is decision-driven.

The goal was to move beyond:
- writing queries  
- plotting charts  

and instead answer:

- What actually drives revenue?  
- What doesn’t matter as much as we think?  
- Where do assumptions fail when tested with data?  

Because in real-world scenarios, clean answers are rare.

---

## Dataset

The dataset contains approximately **3,00,000 booking records** covering:

- Hotel categories (Luxury, Business, Resort)  
- Booking channels  
- Customer ratings  
- Revenue (Gross and Net)  
- Discounts  
- Stay duration and guest count  

Due to size limitations, the dataset is hosted on Kaggle:

👉 https://kaggle.com/datasets/arjunguptadataanalyst/itc-hotels-sales

---

## Approach

The analysis was structured in three layers:

### 1. Data Preparation
- Removed duplicates  
- Standardized formats  
- Cleaned inconsistencies  
- Ensured data reliability  

### 2. Feature Engineering
- Revenue per Night  
- Revenue per Guest  
- Discount Percentage  
- High Rating Indicator  

These features helped shift the analysis from reporting to reasoning.

### 3. Analysis
- Revenue distribution  
- Trend analysis (monthly & quarterly)  
- Channel-level performance  
- Customer rating behavior  

---
## Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib

---

## Key Business Insights

### Revenue is concentrated, not distributed  
Luxury hotels contribute a disproportionate share of total revenue.

→ High-value segments matter more than high-volume segments.

---

### Discounts are not driving satisfaction  
Higher discounts do not show a meaningful improvement in customer ratings.

→ Pricing strategy should focus on value, not just reduction.

---

### Demand is stable, not volatile  
Revenue trends fluctuate, but within a controlled range.

→ Indicates predictable demand patterns useful for planning.

---

### Customer satisfaction lacks differentiation  
Ratings are clustered between 3–5 across categories.

→ Service quality is consistent, but not strongly differentiated.

---

## Visual Outputs

### Net Revenue by Hotel Category  
Highlights how revenue is concentrated in premium segments, with luxury hotels driving a disproportionate share.

[visuals/V1_category_revenue.png](https://github.com/arjunguptadataanalyst/itc-hotels-project/blob/3d08f58b4253eecc0a57ac8553859711728363fe/visuals/V1_category_revenue.png)

### Monthly Revenue Trend
Shows consistent revenue performance with controlled fluctuations, indicating stable underlying demand.

[visuals/V2_monthly_trend.png](https://github.com/arjunguptadataanalyst/itc-hotels-project/blob/200ded465ff5dcf7f7b5981d5849207d60971c91/visuals/V2_monthly_trend.png)

### Net vs Gross Revenue
Illustrates the impact of discounts, where gross revenue remains higher but does not fully translate into realized earnings.

[visuals/V4_net_vs_gross.png](https://github.com/arjunguptadataanalyst/itc-hotels-project/blob/200ded465ff5dcf7f7b5981d5849207d60971c91/visuals/V4_net_vs_gross.png)

---

## Project Structure

itc-hotels-project/
├─ data/
├─ notebooks/
├─ scripts/
├─ visuals/
├─ README.md

---

## What I would do next

- Build a revenue forecasting model (time series)  
- Segment customers based on booking behavior  
- Analyze cancellation patterns  
- Optimize pricing using demand signals  

The objective would be to move from descriptive analysis to predictive decision-making.

---

## Conclusion

The value of analysis is not in the tools used, but in the clarity produced.

This project is an attempt to move from:
data → information → understanding → better decisions

---

## About

Arjun Gupta  
Applied Data Analyst | Analytics Educator  

Focused on bridging the gap between learning analytics and applying it in real-world scenarios.
