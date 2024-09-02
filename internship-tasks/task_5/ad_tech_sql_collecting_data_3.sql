 SELECT impressions.impressions_id,
 impressions.impressions_time,
 impressions.user_id,
 impressions.app_code,
 impressions.os_version,
 impressions.is_4g,
 impressions.is_click,
 COALESCE(df_impressions_before_count.impressions_before_count,0) AS impressions_before_count
FROM impressions LEFT JOIN df_impressions_before_count ON impressions.impressions_id = df_impressions_before_count.impressions_id