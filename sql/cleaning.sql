-- Data Cleaning Script for Nigeria Electricity Analytics

-- View all records
SELECT * FROM electricity_data;

-- Find records with missing values
SELECT *
FROM electricity_data
WHERE disco IS NULL
   OR region IS NULL
   OR year IS NULL;

-- Find duplicate records
SELECT disco, year, COUNT(*) AS duplicate_count
FROM electricity_data
GROUP BY disco, year
HAVING COUNT(*) > 1;

-- Standardize DisCo names to uppercase
UPDATE electricity_data
SET disco = UPPER(disco);

-- Remove leading and trailing spaces
UPDATE electricity_data
SET disco = TRIM(disco),
    region = TRIM(region);

-- Verify cleaned data
SELECT * FROM electricity_data;
