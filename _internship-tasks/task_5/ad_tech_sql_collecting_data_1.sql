SELECT imp.impressions_id,
    imp.impressions_time,
    imp.user_id,
    imp.app_code,
    imp.os_version,
    imp.is_4g,
    imp.is_click,
    imp_before.impressions_time AS impression_time_before,
    date_part('day'::TEXT, (imp.impressions_time - imp_before.impressions_time)) AS days_between
   FROM impressions imp
     JOIN impressions imp_before ON imp.user_id = imp_before.user_id 
   WHERE imp.impressions_time > imp_before.impressions_time 
   AND date_part('day'::TEXT, (imp.impressions_time - imp_before.impressions_time)) <= (7)::DOUBLE PRECISION;