CREATE TABLE `travel_map_db`.`travel_map_tbl`(
    `id` bigint(16) unsigned NOT NULL AUTO_INCREMENT,
    `latlng` geometry NOT NULL,
    PRIMARY KEY (`id`),
    SPATIAL KEY (`latlng`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;