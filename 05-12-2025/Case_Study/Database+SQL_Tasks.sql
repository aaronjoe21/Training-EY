USE subscription_app; 

-- 1. Write SQL to fetch all subscriptions expiring within 10 days.
SELECT
  sub_id, customer_name, plan_type, start_date, expiry_date,
  DATEDIFF(expiry_date, CURRENT_DATE()) AS days_left
FROM subscriptions
WHERE DATEDIFF(expiry_date, CURRENT_DATE()) BETWEEN 0 AND 10
ORDER BY expiry_date;

-- 2. Write SQL to nd customers who subscribed in the current month.


SELECT sub_id, customer_name, plan_type, start_date
FROM subscriptions
WHERE MONTH(start_date) = MONTH(CURRENT_DATE())
  AND YEAR(start_date)  = YEAR(CURRENT_DATE())
ORDER BY start_date;

-- 3. Fetch all yearly plans and sort by expiry_date.


SELECT sub_id, customer_name, start_date, expiry_date, plan_type
FROM subscriptions
WHERE plan_type = 'Yearly'
ORDER BY expiry_date;

-- 4. Identify all subscriptions lasting more than 30 days (Quarterly/Yearly).

SELECT sub_id, customer_name, start_date, expiry_date, plan_type
FROM subscriptions
WHERE plan_type = 'Yearly'
ORDER BY expiry_date;


-- 5. Write SQL to check data quality: expiry_date < start_date.

SELECT sub_id, customer_name, start_date, expiry_date, plan_type
FROM subscriptions
WHERE expiry_date < start_date
ORDER BY start_date;

