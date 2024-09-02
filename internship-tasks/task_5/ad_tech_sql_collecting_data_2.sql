 SELECT impressions_id,
    count(impressions_time) AS impressions_before_count
   FROM df_impressions_before
  GROUP BY impressions_id;