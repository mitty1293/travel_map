CREATE TABLE `travel_map_db`.`travel_map_tbl`(
    `id` bigint(16) unsigned NOT NULL AUTO_INCREMENT,
    `latlng` geometry NOT NULL,
    `date` DATE,
    `destination` VARCHAR(40),
    `category` VARCHAR(20),
    `spot_name` VARCHAR(40),
    `note` VARCHAR(40),
    `img_path` VARCHAR(128),
    PRIMARY KEY (`id`),
    SPATIAL KEY (`latlng`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
