PRAGMA foreign_keys = ON;

DROP TABLE loadout;
DROP TABLE weapons;
DROP TABLE classShotgun;
DROP TABLE classSniper;
DROP TABLE classSecondary;
DROP TABLE classMelee;
CREATE TABLE loadout(loadout_id, lo_name, lo_wfID, lo_w1, lo_w2, lo_w3, lo_noise1, lo_noise2, lo_noise3);


CREATE TABLE weapons(wp_id PRIMARY KEY, wp_name, wp_class, wp_DamageTypes, wp_fireRate, wp_fireType, wp_noise);


CREATE TABLE classShotgun(shotgun_id, shotgun_pelletCount);
CREATE TABLE classSniper(sniper_id, punchThroughDistance); 
CREATE TABLE classSecondary(secondary_id, weaponType);
CREATE TABLE classMelee(melee_id, melee_type, melee_attackSpeed);


INSERT INTO weapons VALUES(1, 'basmu', 'rifle', 'electricity, heat', 12, 'auto', 'alarming');
INSERT INTO weapons VALUES(2, 'azima', 'secondary', 'slash', 10, 'auto', 'alarming');
INSERT INTO weapons VALUES(3, 'ceramic dagger', 'melee', 'puncture', 1, 'melee', 'silent');
INSERT INTO weapons VALUES(4, 'soma', 'rifle', 'slash', 15, 'auto', 'alarming');
INSERT INTO weapons VALUES(5, 'grinlok', 'rifle', 'impact', 1.67, 'semi-auto', 'alarming');
INSERT INTO weapons VALUES(6, 'miter', 'rifle', 'slash', 2.5, 'charge', 'alarming');
INSERT INTO weapons VALUES(7, 'battacor', 'rifle', 'magnetic, radiation', 3.57, 'auto-burst', 'alarming');
INSERT INTO weapons VALUES(8, 'sobek', 'shotgun', 'impact', 2.5, 'auto', 'alarming');
INSERT INTO weapons VALUES(9, 'tigris', 'shotgun', 'slash', 2, 'duplex', 'alarming');
INSERT INTO weapons VALUES(10, 'hek', 'shotgun', 'puncture', 2.17, 'sem-auto', 'alarming');
INSERT INTO weapons VALUES(11, 'cedo', 'shotgun', 'puncture', 3.83, 'auto', 'alarming');
INSERT INTO weapons VALUES(12,'kohmak','secondary', 'slash', 1, 'auto-spool', 'alarming');
INSERT INTO weapons VALUES(13,'bronco','secondary','impact', 5, 'semi-auto', 'alarming');
INSERT INTO weapons VALUES(14,'kraken','secondary', 'impact', 4.42, 'burst', 'alarming');
INSERT INTO weapons VALUES(15,'Sicarus','secondary', 'impact', 7.39, 'burst' , 'alarming');
INSERT INTO weapons VALUES(16,'lanka','sniper', 'electricity', 1,'charge', 'alarming');
INSERT INTO weapons VALUES(17,'komorex','sniper', 'slash, puncture', 6,'semi-auto', 'alarming');
INSERT INTO weapons VALUES(18,'snipetron','sniper', 'puncture', 2, 'semi-auto', 'alarming');
INSERT INTO weapons VALUES(19,'Sporothrix','sniper', 'slash', 1.83 ,'semi-auto', 'alarming');
INSERT INTO weapons VALUES(20,'vulkar','sniper', 'impact', 1.5 ,'semi-auto', 'alarming');
INSERT INTO weapons VALUES(21,'gram','melee', 'slash', 0, 'none', 'silent');
INSERT INTO weapons VALUES(22,'war','melee', 'impact', 0, 'none', 'silent');
INSERT INTO weapons VALUES(23,'ripkas','melee', 'impact', 0, 'none', 'silent');


INSERT INTO classMelee (melee_id)
    SELECT wp_id
    FROM weapons 
    WHERE wp_class ='melee';



