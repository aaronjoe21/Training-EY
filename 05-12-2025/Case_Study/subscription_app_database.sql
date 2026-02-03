CREATE DATABASE subscription_app; 
USE subscription_app; 
CREATE TABLE subscriptions ( 
    sub_id INT PRIMARY KEY, 
    customer_name VARCHAR(50), 
    start_date DATE, 
    expiry_date DATE, 
    created_at DATETIME, 
    plan_type VARCHAR(20)   -- Monthly, Quarterly, Yearly 
); 

INSERT INTO subscriptions (sub_id, customer_name, start_date, expiry_date, created_at, plan_type) VALUES
(1,  'Aisha Khan',   '2025-11-25', '2025-12-25', '2025-11-25 10:30:00', 'Monthly'),
(2,  'Rahul Sharma', '2025-12-01', '2025-12-31', '2025-12-01 09:45:00', 'Monthly'),
(3,  'Meera Iyer',   '2025-09-15', '2025-12-14', '2025-09-15 14:12:00', 'Quarterly'),
(4,  'Sanjay Patel', '2025-01-05', '2026-01-05', '2025-01-05 17:05:00', 'Yearly'),
(5,  'Priya Nair',   '2025-10-20', '2025-11-19', '2025-10-20 12:00:00', 'Monthly'),     -- expired
(6,  'Imran Ali',    '2025-12-10', '2026-01-09', '2025-12-10 11:15:00', 'Monthly'),
(7,  'Neha Verma',   '2025-07-01', '2025-09-29', '2025-07-01 08:10:00', 'Quarterly'),   -- expired
(8,  'Kiran Kumar',  '2024-12-15', '2025-12-15', '2024-12-15 10:00:00', 'Yearly'),      -- expiring soon
(9,  'Anil Singh',   '2025-12-11', '2026-01-10', '2025-12-11 07:45:00', 'Monthly'),
(10, 'Deepa Joseph', '2025-03-01', '2026-03-01', '2025-03-01 18:20:00', 'Yearly'),
(11, 'QA Error',     '2025-12-05', '2025-12-01', '2025-12-05 09:00:00', 'Monthly'),     -- data quality issue (expiry < start)
(12, 'Megha Das',    '2025-12-08', '2026-01-07', '2025-12-08 13:40:00', 'Monthly');
