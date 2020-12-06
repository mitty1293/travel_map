USE travel_map_db;

SET CHARACTER_SET_CLIENT = utf8;
SET CHARACTER_SET_CONNECTION = utf8;

INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(35.70994915351262 139.80104704754638)"), "2020-11-20", "東京", "自然", "地点_東京自然1", "備考_東京自然1");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(35.76012838102881 139.69586735824032)"), "2005-07-17", "東京", "自然", "地点_東京自然2", "備考_東京自然2");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(35.74898374653144 139.84659974453976)"), "2019-08-05", "東京", "レストラン", "地点_東京レストラン1", "備考_東京レストラン1");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(35.639683766995155 139.4703180062585)"), "2015-04-22", "東京", "レストラン", "地点_東京レストラン2", "備考_東京レストラン2");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(35.63856768919061 139.42258244613095)"), "2019-08-05", "東京", "施設", "地点_東京施設1", "備考_東京施設1");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(35.33492631565827 138.6622566245895)"), "2018-10-29", "静岡", "自然", "地点_静岡自然1", "備考_静岡自然1");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(34.99263671160548 138.95152073334006)"), "2018-10-29", "静岡", "レストラン", "地点_静岡レストラン1", "備考_静岡レストラン1");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(35.11463783140103 138.9089487118557)"), "2018-10-28", "静岡", "施設", "地点_静岡施設1", "備考_静岡施設1");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(35.060136859840604 139.0091989559963)"), "2018-10-30", "静岡", "施設", "地点_静岡施設2", "備考_静岡施設2");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(34.76493517804641 135.6111263163075)"), "2016-03-04", "大阪", "自然", "地点_大阪自然1", "備考_大阪自然1");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(34.76493517804641 135.4683040506825)"), "2020-12-16", "大阪", "レストラン", "地点_大阪レストラン1", "備考_大阪レストラン1");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(34.46355994452484 135.64202663173813)"), "2002-11-07", "大阪", "施設", "地点_大阪施設1", "備考_大阪施設1");
INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(34.29773749241069 135.1139302760881)"), "2010-05-07", "大阪", "施設", "地点_大阪施設2", "備考_大阪施設2");
