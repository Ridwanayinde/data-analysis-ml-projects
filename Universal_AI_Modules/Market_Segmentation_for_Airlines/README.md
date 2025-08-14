# ✈️ Market Segmentation for Airlines

📌 Introduction

Market segmentation is a strategy that divides a broad target market into
smaller, similar groups and designs targeted marketing strategies for each group.
In this project, we use **clustering** — an unsupervised machine learning technique —
to automatically discover patterns in customer behavior for an airline’s **frequent flyer program**.

The goal is to help the airline:

- 🎯 Understand customer groups

- 📈 Target them with tailored mileage offers

- 🤝 Improve customer engagement and loyalty

## 📂 Dataset Overview

The dataset AirlinesCluster.csv contains 3,999 records of frequent flyer program members.
📖 Source: "Data Mining for Business Intelligence" by Galit Shmueli, Nitin R. Patel, and Peter C. Bruce.

📊 Features:

| Variable               | Description                                                      |
| ---------------------- | ---------------------------------------------------------------- |
| **Balance** 💰         | Number of miles eligible for award travel                        |
| **QualMiles** 🎖️      | Miles qualifying for TopFlight status                            |
| **BonusMiles** 🎁      | Miles earned from non-flight bonus transactions (past 12 months) |
| **BonusTrans** 🔄      | Number of non-flight bonus transactions (past 12 months)         |
| **FlightMiles** ✈️     | Flight miles in the past 12 months                               |
| **FlightTrans** 🛫     | Number of flight transactions in the past 12 months              |
| **DaysSinceEnroll** 📅 | Days since enrollment in the program                             |

## 🔍 Project Pipeline

- 📥 Data Loading & Exploration – Read CSV, check missing values, and understand distributions.

- 🧹 Data Preprocessing – Handle outliers, scaling, and feature selection.

- 🌀 Clustering with K-Means – Apply clustering to group customers based on behavior.

- 📊 Visualization – Create bar plots, scatter plots, and cluster profile summaries.

- 📝 Insights & Recommendations – Suggest marketing actions for each segment.

## 🛠️ Tools & Libraries

- Python 🐍

- pandas, numpy

- matplotlib, seaborn

- scikit-learn

## 📌 Key Outcome

- Identified distinct customer segments.

- Provided data-driven recommendations for targeted mileage offers.
