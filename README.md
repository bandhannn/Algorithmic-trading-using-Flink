# Algorithmic Trading using Flink

This repository contains the implementation of a **Real-Time Algorithmic Trading** system. The project leverages cutting-edge tools and technologies to automate trading actions based on real-time stock market data and sentiment analysis.

## 📚 Project Overview
Algorithmic trading has become a crucial aspect of modern financial markets, enabling traders to make data-driven, real-time decisions at scale. This project focuses on building a robust and scalable trading system for Apple stock using:

- **Real-time and historical data**
- **Redpanda** for data streaming
- **Apache Flink** for data transformation
- **Docker** for containerization
- **AWS EC2** for cloud deployment
- **Slack** for real-time trade notifications

## 🧩 Data Pipeline Design
![Data Pipeline Design](images/algotrading.jpg)


## 🎯 Objectives
- Develop a structured data pipeline for ingesting, analyzing, and executing stock trades in real time.
- Automate buy and sell actions based on:
  - **Technical indicators** (e.g., SMA20, SMA50)
  - **News sentiment analysis**
- Deploy the system on the cloud for scalability and reliability.

## 🛠️ Tools and Technologies
- **Redpanda**: Manages high-throughput, low-latency data streaming.
- **Apache Flink SQL**: Processes and transforms data efficiently.
- **NLTK**: Performs sentiment analysis on news headlines.
- **Slack API**: Sends real-time trade notifications.
- **Docker**: Ensures portability of the application.
- **AWS EC2**: Hosts the application in a scalable cloud environment.

## 📊 Strategies Implemented
1. **All-Weather Strategy**
2. **Golden Cross Strategy**
3. **Momentum Strategy**

## 🧩 Data Pipeline Design
### **Data Ingestion**
- Fetches real-time and historical data from APIs for:
  - Stock prices
  - News headlines
- Streams data using **Redpanda**.

### **Data Transformation**
- Computes technical indicators (SMA20, SMA50).
- Analyzes sentiment of news headlines (scores range from -1 to 1).
- Implements trading strategies:
  - **Pullback Condition**: Buy signal when specific criteria are met.
  - **Breakout Condition**: Sell signal based on other specific criteria.

### **Trade Execution and Notification**
- Automates buy/sell actions based on SQL-based conditions.
- Sends notifications to Slack with:
  - Stock symbol
  - Action (Buy/Sell)
  - Timestamp

### **Deployment**
- Fully containerized using **Docker**.
- Deployed on **AWS EC2** for scalable and efficient management.

## 📈 Results
- Automated trade execution and notifications were successfully integrated.
- Profitability was observed using the SMA crossover strategy combined with sentiment analysis.
- Real-time Slack notifications provided actionable trading insights.

## 🔮 Future Scope
- Extend the system to support additional stocks and asset types.
- Enhance sentiment analysis using advanced NLP techniques.
- Integrate machine learning models for improved decision-making and profitability.


---

Feel free to contribute to this project by raising issues or submitting pull requests!

