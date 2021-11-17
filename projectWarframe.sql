PRAGMA foreign_keys = ON;
DROP TABLE weaponsP;
DROP TABLE weaponsS;
DROP TABLE weaponsM;

DROP TABLE warframe_release;
DROP TABLE warframe_health;
DROP TABLE warframe_shields;
DROP TABLE warframe_energy;
DROP TABLE warframe_armor;
DROP TABLE warframe_speed;
DROP TABLE warframe;

DROP TABLE loadouts;


CREATE TABLE weaponsP(wp_id PRIMARY KEY, wp_name, wp_class, wp_DamageTypes, wp_fireRate, wp_fireType, wp_noise);
CREATE TABLE weaponsS(wp_id PRIMARY KEY, wp_name, wp_class, wp_DamageTypes, wp_fireRate, wp_fireType, wp_noise);
CREATE TABLE weaponsM(wp_id PRIMARY KEY, wp_name, wp_class, wp_DamageTypes, wp_fireRate, wp_fireType, wp_noise);


CREATE TABLE warframe (
    wf_id int primary key,
    wf_name varchar(255) NOT NULL,
    wf_ranked varchar(255) NOT NULL
);
CREATE TABLE warframe_release (
    wf_release date,
    wf_id int,
    foreign key(wf_id) references warframe(wf_id) 
);
CREATE TABLE warframe_health (
    wf_health int,
    wf_id int,
    foreign key(wf_id) references warframe(wf_id) 
);

CREATE TABLE warframe_shields (
    wf_shields int,
    wf_id int,
    foreign key(wf_id) references warframe(wf_id) 
);

CREATE TABLE warframe_energy (
    wf_energy varchar(4),
    wf_id int,
    foreign key(wf_id) references warframe(wf_id) 
);

CREATE TABLE warframe_armor (
    wf_armor int,
    wf_id int,
    foreign key(wf_id) references warframe(wf_id) 
);

CREATE TABLE warframe_speed (
    wf_speed varchar(4),
    wf_id int,
    foreign key(wf_id) references warframe(wf_id) 
);


CREATE TABLE loadouts( 
    l_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    l_name, l_primaryWeapon, l_secondaryWeapon, l_meleeWeapon, l_warframe,
    FOREIGN KEY (l_primaryWeapon) REFERENCES weaponsP(wp_id) ON DELETE CASCADE
    FOREIGN KEY (l_secondaryWeapon) REFERENCES weaponsP(wp_id) ON DELETE CASCADE
    FOREIGN KEY (l_warframe) REFERENCES warframe(wf_id) ON DELETE CASCADE
    FOREIGN KEY (l_meleeWeapon) REFERENCES weaponsM(wp_id) ON DELETE CASCADE
);

INSERT INTO weaponsP VALUES(1, 'basmu', 'rifle', 'electricity, heat', 12, 'auto', 'alarming');
INSERT INTO weaponsP VALUES(2, 'azima', 'secondary', 'slash', 10, 'auto', 'alarming');
INSERT INTO weaponsP VALUES(3, 'ceramic dagger', 'melee', 'puncture', 1, 'melee', 'silent');
INSERT INTO weaponsP VALUES(4, 'soma', 'rifle', 'slash', 15, 'auto', 'alarming');
INSERT INTO weaponsP VALUES(5, 'grinlok', 'rifle', 'impact', 1.67, 'semi-auto', 'alarming');
INSERT INTO weaponsP VALUES(6, 'miter', 'rifle', 'slash', 2.5, 'charge', 'alarming');
INSERT INTO weaponsP VALUES(7, 'battacor', 'rifle', 'magnetic, radiation', 3.57, 'auto-burst', 'alarming');
INSERT INTO weaponsP VALUES(8, 'sobek', 'shotgun', 'impact', 2.5, 'auto', 'alarming');
INSERT INTO weaponsP VALUES(9, 'tigris', 'shotgun', 'slash', 2, 'duplex', 'alarming');
INSERT INTO weaponsP VALUES(10, 'hek', 'shotgun', 'puncture', 2.17, 'sem-auto', 'alarming');
INSERT INTO weaponsP VALUES(11, 'cedo', 'shotgun', 'puncture', 3.83, 'auto', 'alarming');
INSERT INTO weaponsP VALUES(12,'lanka','sniper', 'electricity', 1,'charge', 'alarming');
INSERT INTO weaponsP VALUES(13,'komorex','sniper', 'slash, puncture', 6,'semi-auto', 'alarming');
INSERT INTO weaponsP VALUES(14,'snipetron','sniper', 'puncture', 2, 'semi-auto', 'alarming');
INSERT INTO weaponsP VALUES(15,'sporothrix','sniper', 'slash', 1.83 ,'semi-auto', 'alarming');
INSERT INTO weaponsP VALUES(16,'vulkar','sniper', 'impact', 1.5 ,'semi-auto', 'alarming');



INSERT INTO weaponsS VALUES(1,'kohmak','secondary', 'slash', 1, 'auto-spool', 'alarming');
INSERT INTO weaponsS VALUES(2,'bronco','secondary','impact', 5, 'semi-auto', 'alarming');
INSERT INTO weaponsS VALUES(3,'kraken','secondary', 'impact', 4.42, 'burst', 'alarming');
INSERT INTO weaponsS VALUES(4,'Sicarus','secondary', 'impact', 7.39, 'burst' , 'alarming');

INSERT INTO weaponsM VALUES(1,'gram','melee', 'slash', 0, 'none', 'silent');
INSERT INTO weaponsM VALUES(2,'war','melee', 'impact', 0, 'none', 'silent');
INSERT INTO weaponsM VALUES(3,'ripkas','melee', 'impact', 0, 'none', 'silent');

INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(1, 'Ash', 'unranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(2, 'Ash', 'ranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(3, 'Ash Prime', 'unranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(4, 'Ash Prime', 'ranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(5, 'Atlas', 'unranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(6, 'Atlas', 'ranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(7, 'Atlas Prime', 'unranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(8, 'Atlas Prime', 'ranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(9, 'Banshee', 'unranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(10, 'Banshee', 'ranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(11, 'Banshee Prime', 'unranked');
INSERT INTO warframe (wf_id, wf_name, wf_ranked) VALUES(12, 'Banshee Prime', 'ranked');

INSERT INTO warframe_release (wf_release, wf_id) VALUES('2012-10-25', 1);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2012-10-25', 2);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2015-07-07', 3);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2015-07-07', 4);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2015-10-01', 5);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2015-10-01', 6);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2019-10-01', 7);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2019-10-01', 8);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2013-03-18', 9);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2013-03-18', 10);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2017-02-28', 11);
INSERT INTO warframe_release (wf_release, wf_id) VALUES('2017-02-28', 12);

INSERT INTO warframe_health (wf_health, wf_id) VALUES(150, 1);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(450, 2);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(150, 3);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(450, 4);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(100, 5);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(300, 6);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(175, 7);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(525, 8);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(100, 9);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(300, 10);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(100, 11);
INSERT INTO warframe_health (wf_health, wf_id) VALUES(300, 12);

INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(100, 1);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(300, 2);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(125, 3);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(375, 4);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(100, 5);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(300, 6);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(150, 7);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(450, 8);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(100, 9);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(300, 10);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(100, 11);
INSERT INTO warframe_shields (wf_shields, wf_id) VALUES(300, 12);

INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('100', 1);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('150', 2);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('125', 3);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('375', 4);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('150', 5);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('225', 6);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('175', 7);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('262.5', 8);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('150', 9);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('225', 10);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('175', 11);
INSERT INTO warframe_energy (wf_energy, wf_id) VALUES('262.5', 12);

INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(100, 1);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(100, 2);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(175, 3);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(175, 4);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(450, 5);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(450, 6);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(475, 7);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(475, 8);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(100, 9);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(100, 10);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(125, 11);
INSERT INTO warframe_armor (wf_armor, wf_id) VALUES(125, 12);

INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1.15', 1);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1.15', 2);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1.2', 3);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1.2', 4);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('0.9', 5);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('0.9', 6);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1', 7);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1', 8);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1.1', 9);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1.1', 10);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1.15', 11);
INSERT INTO warframe_speed (wf_speed, wf_id) VALUES('1.15', 12);


--Display Warframes Table
SELECT "---WARFRAMES---";
SELECT warframe.wf_id, warframe.wf_name, warframe.wf_ranked, warframe_release.wf_release, warframe_health.wf_health, warframe_shields.wf_shields, warframe_armor.wf_armor, warframe_speed.wf_speed
FROM warframe
INNER JOIN warframe_release
ON warframe.wf_id = warframe_release.wf_id
INNER JOIN warframe_health
ON warframe.wf_id = warframe_health.wf_id
INNER JOIN warframe_shields
ON warframe.wf_id = warframe_shields.wf_id
INNER JOIN warframe_energy
ON warframe.wf_id = warframe_energy.wf_id
INNER JOIN warframe_armor
ON warframe.wf_id = warframe_armor.wf_id
INNER JOIN warframe_speed
ON warframe.wf_id = warframe_speed.wf_id;

--Display weaponsP Table
SELECT "---Primary Weapons---";
SELECT * from weaponsP;

SELECT "---Secondary Weapons---";

--CREATE LOADOUTS
INSERT INTO loadouts (l_name,l_primaryWeapon, l_secondaryWeapon, l_warframe) VALUES('firstLoadout', 1, 3, 1); 
INSERT INTO loadouts (l_name,l_primaryWeapon, l_secondaryWeapon, l_warframe) VALUES('secondLoadout', 3, 1, 3);



SELECT l_id, l_name, primaryW.wp_name, secondaryW.wp_name as Secondary, warframe.wf_name
FROM loadouts, weaponsP as primaryW, weaponsS as secondaryW, warframe
WHERE primaryW.wp_id = l_primaryWeapon
AND secondaryW.wp_id = l_secondaryWeapon
AND warframe.wf_id = l_warframe;

SELECT "---Updated---";

UPDATE warframe_release
    SET wf_release = '1842-05-05'
WHERE wf_id = 1;
SELECT * FROM warframe_release WHERE wf_id = 1;