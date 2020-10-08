CREATE TABLE `travel_map_db`.`travel_map_tbl`(
    `id` bigint(16) unsigned NOT NULL AUTO_INCREMENT,
    `latlng` geometry NOT NULL,
    `date` DATE,
    `name` VARCHAR(40),
    `note` VARCHAR(40),
    PRIMARY KEY (`id`),
    SPATIAL KEY (`latlng`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

以下メモ
CREATE TABLE `dcard_db`.`csv_tbl`(
    `paymant_month` INT,
    `name` VARCHAR(10),
    `date` DATE,
    `description` VARCHAR(45),
    `amount` INT,
    `amount2` INT,
    `note` VARCHAR(45)
);
