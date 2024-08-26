WITH passengers_list AS
(
    SELECT 
        Passengers.passenger_id, 
        MIN(Buses.arrival_time) AS arrival_time
    FROM Passengers
    INNER JOIN Buses
        ON Passengers.arrival_time <= Buses.arrival_time
    GROUP BY Passengers.passenger_id
)

SELECT
    bus_id, 
    COUNT(passengers_list.arrival_time) AS passengers_cnt
FROM Buses
LEFT JOIN passengers_list
    ON Buses.arrival_time = passengers_list.arrival_time
GROUP BY Buses.bus_id
ORDER BY Buses.bus_id;
