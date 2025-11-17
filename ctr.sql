SELECT
    T1.test_group,
    SUM(CASE WHEN T2.event_type = 'view' THEN 1 ELSE 0 END) AS total_views,
    SUM(CASE WHEN T2.event_type = 'click' THEN 1 ELSE 0 END) AS total_clicks,
    (SUM(CASE WHEN T2.event_type = 'click' THEN 1 ELSE 0 END) * 1.0) /
     SUM(CASE WHEN T2.event_type = 'view' THEN 1 ELSE 0 END) * 100 AS click_through_rate_pct
FROM
    users AS T1
JOIN
    events AS T2 ON T1.user_id = T2.user_id
GROUP BY
    T1.test_group;