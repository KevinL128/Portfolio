/* Dataset Information  

This project uses the dataset "Retail Sales Dataset" from Kaggle.
The dataset has been imported into an SQL database for analysis using Microsoft SQL Server Management Studio.

**Source**: https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset
*/ 


/* 1. Who is the most valuable customer? */
SELECT 
	TOP 1
	Customer_ID,
	Total_Amount
FROM retail_sales_dataset
ORDER BY Total_Amount DESC;

/* 2. What is the average age of customers for each product category */
SELECT 
	Product_category,
	AVG(Age) AS avg_age_customer
FROM retail_sales_dataset
GROUP BY product_category;

/* 3. What is the gender distribution of customers for each product category */

SELECT
	Product_category,
	Gender,
	COUNT(DISTINCT Customer_ID) AS Customer_Count,
	COUNT(DISTINCT Customer_ID) * 100 / SUM(COUNT(DISTINCT Customer_ID)) OVER (PARTITION BY Product_category) AS Gender_Percentage
FROM retail_sales_dataset
GROUP BY Product_category, Gender
Order by Product_category, gender;


/* 4. What are the top-performing product categories */

SELECT 
	Product_category,
	SUM(Total_Amount) AS Total_Sales
FROM retaiL_sales_dataset
GROUP BY product_category;

/* 5. What is the average order value (AOV) per transaction? (Calculate how much customers typically spend in one transaction) */

SELECT 
	AVG(Total_Amount) AS AOV
FROM retail_sales_dataset;



/* 6. Which day of the week has the highest sales volume */

SELECT
	DATENAME(weekday, date) AS Day_of_Week,
	SUM(quantity) AS Total_Quantity
FROM retail_sales_dataset
GROUP BY DATENAME(weekday, date)
ORDER BY Total_Quantity DESC;

/* 7. Which product are sold the most and least by quantity?  */
/* 7.1. Most Sold Product Category */

SELECT
	TOP 1
	Product_Category AS Most_Sold_Product_Category,
	SUM(Quantity) AS Total_Quantity
FROM retail_sales_dataset
GROUP BY Product_Category
ORDER BY Total_Quantity DESC;

/* 7.2. Least sold product category */
SELECT
	TOP 1
	Product_Category AS Least_Sold_Product_Category,
	SUM(Quantity) AS Total_Quantity
FROM retail_sales_dataset
GROUP BY Product_Category
ORDER BY Total_Quantity ASC;



