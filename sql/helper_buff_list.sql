DROP TABLE IF EXISTS `helper_buff_list`;
#----------------------------
# Table structure for helper_buff_list
#----------------------------
CREATE TABLE `helper_buff_list` (
`id` int(11) NOT NULL default '0',
`skill_id` int(10) unsigned NOT NULL default '0',
`name` varchar(25) NOT NULL default '',
`skill_level` int(10) unsigned NOT NULL default '0',
`lower_level` int(10) unsigned NOT NULL default '0',
`upper_level` int(10) unsigned NOT NULL default '0',
`is_magic_class` varchar(5) default NULL,
PRIMARY KEY  (`id`)
);

#----------------------------
# Records for table helper_buff_list
#----------------------------

insert  into helper_buff_list values 
(0, 4322, 'WindWalk', 1, 8, 24, 'false'),
(1, 4323, 'Shield', 1, 11, 24, 'false'),
(2, 4338, 'Life Cubic', 1, 16, 21, 'false'),
(3, 4324, 'Bless the Body', 1, 12, 23, 'false'),
(4, 4325, 'Vampiric Rage', 1, 13, 23, 'false'),
(5, 4326, 'Regeneration', 1, 14, 23, 'false'),
(6, 4327, 'Haste', 1, 15, 22, 'false'),
(7, 4322, 'WindWalk', 1, 8, 24, 'true'),
(8, 4323, 'Shield', 1, 11, 24, 'true'),
(9, 4338, 'Life Cubic', 1, 16, 21, 'true'),
(10, 4328, 'Bless the Soul', 1, 12, 23, 'true'),
(11, 4329, 'Acumen', 1, 13, 23, 'true'),
(12, 4330, 'Concentration', 1, 14, 23, 'true'),
(13, 4331, 'Empower', 1, 15, 22, 'true');