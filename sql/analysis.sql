-- Nigeria Electricity Analytics
-- Business Analysis Queries

-- 1. View all data
SELECT * FROM electricity_data;

-- 2. Total revenue generated
SELECT
    SUM(revenue_billion_naira) AS total_revenue
FROM electricity_data;

-- 3. Revenue by DisCo
SELECT
    disco,
    revenue_billion_naira
FROM electricity_data
ORDER BY revenue_billion_naira DESC;

-- 4. Top 5 DisCos by revenue
SELECT
    disco,
    revenue_billion_naira
FROM electricity_data
ORDER BY revenue_billion_naira DESC
LIMIT 5;

-- 5. Average metering rate
SELECT
    AVG(metering_rate) AS average_metering_rate
FROM electricity_data;

-- 6. Average billing efficiency
SELECT
    AVG(billing_efficiency) AS average_billing_efficiency
FROM electricity_data;

-- 7. Average collection efficiency
SELECT
    AVG(collection_efficiency) AS average_collection_efficiency
FROM electricity_data;

-- 8. DisCo with the highest customer satisfaction
SELECT
    disco,
    customer_satisfaction_score
FROM electricity_data
ORDER BY customer_satisfaction_score DESC
LIMIT 1;

-- 9. DisCo with the most complaints
SELECT
    disco,
    total_complaints
FROM electricity_data
ORDER BY total_complaints DESC
LIMIT 1;

-- 10. Regional performance summary
SELECT
    region,
    SUM(revenue_billion_naira) AS total_revenue,
    AVG(metering_rate) AS avg_metering_rate,
    AVG(collection_efficiency) AS avg_collection_efficiency
FROM electricity_data
GROUP BY region
ORDER BY total_revenue DESC;
