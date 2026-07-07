-- Create Electricity Analytics Table

CREATE TABLE electricity_data (
    id INT PRIMARY KEY,
    disco VARCHAR(50) NOT NULL,
    region VARCHAR(20),
    year INT,
    registered_customers INT,
    metering_rate DECIMAL(5,2),
    billing_efficiency DECIMAL(5,2),
    collection_efficiency DECIMAL(5,2),
    total_complaints INT,
    revenue_billion_naira DECIMAL(10,2),
    customer_satisfaction_score DECIMAL(5,2)
);
