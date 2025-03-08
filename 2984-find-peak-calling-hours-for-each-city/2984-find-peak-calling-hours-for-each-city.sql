# Write your MySQL query statement below
WITH HourlyCallCount AS (
    SELECT
        city,
        EXTRACT(HOUR FROM call_time) as calling_hour,
        COUNT(*) as number_of_calls
    FROM Calls
    GROUP BY city, EXTRACT(HOUR FROM call_time)
),
MaxCallCountPerCity AS (
    SELECT
        city,
        MAX(number_of_calls) as max_calls
    FROM HourlyCallCount
    GROUP BY city
)
SELECT
    h.city,
    h.calling_hour as peak_calling_hour,
    h.number_of_calls
FROM HourlyCallCount h
JOIN MaxCallCountPerCity m ON h.city = m.city AND h.number_of_calls = m.max_calls
ORDER BY h.calling_hour DESC, h.city DESC;