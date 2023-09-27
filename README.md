# E-commerce Customer Churn - Classification Modeling
---

[Model Deployement Click Here !](https://huggingface.co/spaces/riki-profile/churn-predictor)

## 1. Introduction

### Background

Customer churn is when customers stop using a company's product or service. Churn rate is calculated by dividing the number of customers lost during a specific time period by the number of customers at the beginning of that period. [(*source*)](https://blog.hubspot.com/service/what-is-customer-churn)

BukaOnline is an e-commerce platform that offers a wide range of products. The company is concerned about losing customers and wants to build a predictive model to identify potential churners. This will enable BukaOnline to take proactive measures to retain these customers, such as targeted marketing campaigns.

### Problem Statement

The project aims to create a predictive machine learning model to identify potential churn customers so that BukaOnline can implement effective marketing measures to prevent churn. The challenge is to avoid misidentifying customers who are likely to churn but are incorrectly identified as non-churn customers.

### Objectives

- Understand machine learning concepts comprehensively.
- Prepare data for use in Classification Supervised Learning models.
- Implement Classification Supervised Learning using selected datasets.
- Conduct Hyperparameter Tuning and enhance models.
- Deploy models effectively.

### Dataset

- **Title**: ecommerce.csv
- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction?resource=download&select=E+Commerce+Dataset.xlsx)

| Column                     | Description                                      |
| -------------------------- | ------------------------------------------------ |
| CustomerID                 | Unique customer ID                               |
| Churn                      | Churn Flag (1 = Churn, 0 = Not Churn)           |
| Tenure                     | Length of time customer has been engaged        |
| PreferredLoginDevice       | Preferred login device of customer               |
| CityTier                   | City tier                                        |
| WarehouseToHome            | Distance between warehouse and customer's home    |
| PreferredPaymentMode       | Preferred payment method of customer              |
| Gender                     | Gender of customer                               |
| HourSpendOnApp             | Hours spent on mobile app or website             |
| NumberOfDeviceRegistered   | Total number of devices registered by customer   |
| PreferedOrderCat           | Preferred order category in the last month       |
| SatisfactionScore          | Customer satisfaction score                      |
| MaritalStatus              | Marital status of customer                       |
| NumberOfAddress            | Total number of addresses added by customer      |
| Complain                   | Complaint raised in the last month               |
| OrderAmountHikeFromlastYear| Percentage increase in order amount from last year |
| CouponUsed                 | Total number of coupons used in the last month   |
| OrderCount                 | Total number of orders placed in the last month  |
| DaySinceLastOrder          | Days since last order by customer                |
| CashbackAmount             | Average cashback received in the last month      |

## 2. Conclusion

- A classification model was successfully built and benchmarked using cross-validation among five models. The KNN model achieved the best recall score.
- The XGBoost model, after tuning and feature selection, showed the best overall performance with a recall score of 93.15%.
- The model, however, still has limitations in identifying certain data characteristics.
- Recommendations and strategies were provided to address these limitations.

## 3. Business Recommendations

### 1. Implement Predictive Churn Alerts
- Set up real-time predictive churn alerts to notify the team when a customer is at risk of churning.

### 2. Segment Customers for Targeted Interventions
- Segment customers into high-risk and low-risk churn groups based on model predictions and implement targeted interventions.

### 3. Customer Feedback Loop and Improvement
- Establish a feedback loop with customer service and marketing teams to gather insights from churned customers.

### 4. Model Refinement for Precision
- Refine the churn prediction model to improve precision and reduce false positives.

---

This README provides an overview of the customer churn prediction project for BukaOnline, including the background, problem statement, objectives, dataset details, conclusions, and business recommendations. It serves as a guide for understanding the project's context and findings.