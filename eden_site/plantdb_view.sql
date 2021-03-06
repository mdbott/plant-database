﻿-- View: plantdb_vegetation_view

-- DROP VIEW vegetation_view;

CREATE OR REPLACE VIEW plantdb_vegetationview AS 
 SELECT plantdb_vegetationview.row_number,
    plantdb_vegetationview.vegetationid,
    plantdb_vegetationview.plantid,
    plantdb_vegetationview.rootstockid,
    plantdb_vegetationview.cultivarid,
    plantdb_vegetationview.legacy_pfaf_latin_name,
    plantdb_vegetationview.family,
    plantdb_vegetationview.genus,
    plantdb_vegetationview.species,
    plantdb_vegetationview.ssp,
    plantdb_vegetationview.common_name,
    plantdb_vegetationview.cultivarname,
    plantdb_vegetationview.rootstockname,
    plantdb_vegetationview.plant_function,
    plantdb_vegetationview.border_colour,
    plantdb_vegetationview.fill_colour,
    plantdb_vegetationview.symbol,
    plantdb_vegetationview.form,
    plantdb_vegetationview.locations,
    plantdb_vegetationview.width,
    plantdb_vegetationview.height,
    plantdb_vegetationview.grafted,
    plantdb_vegetationview.comment,
    plantdb_vegetationview.germination_date
   FROM ( SELECT row_number() OVER (ORDER BY plantdb_vegetation.id) AS row_number,
            plantdb_vegetation.id AS vegetationid,
            plantdb_plant.id AS plantid,
            plantdb_plant.legacy_pfaf_latin_name,
            plantdb_plant.family,
            plantdb_plant.genus,
            plantdb_plant.species,
            plantdb_plant.ssp,
            plantdb_plant.common_name,
            plantdb_plant.plant_function,
            plantdb_plant.border_colour,
            plantdb_plant.fill_colour,
            plantdb_plant.symbol,
            plantdb_plant.form,
            plantdb_vegetation.locations,
            plantdb_rootstock.id AS rootstockid,
            plantdb_rootstock.name AS rootstockname,
            plantdb_rootstock.height,
            plantdb_rootstock.width,
            plantdb_cultivar.id AS cultivarid,
            plantdb_cultivar.name AS cultivarname,
            plantdb_cultivar.production_startmonth,
            plantdb_cultivar.production_endmonth,
            plantdb_vegetation.grafted,
            plantdb_vegetation.comment,
            plantdb_vegetation.germination_date
           FROM plantdb_vegetation
             LEFT JOIN plantdb_plant ON plantdb_vegetation.plant_id = plantdb_plant.id
             LEFT JOIN plantdb_cultivar ON plantdb_vegetation.cultivar_id = plantdb_cultivar.id
             LEFT JOIN plantdb_rootstock ON plantdb_vegetation.rootstock_id = plantdb_rootstock.id) plantdb_vegetationview;

ALTER TABLE plantdb_vegetationview
  OWNER TO postgres;
COMMENT ON VIEW plantdb_vegetationview
  IS '-- View: plantdb_vegetationview';

-- Rule: view_delete ON plantdb_vegetationview

-- DROP RULE view_delete ON plantdb_vegetationview;

CREATE OR REPLACE RULE view_delete AS
    ON DELETE TO plantdb_vegetationview DO INSTEAD  DELETE FROM plantdb_vegetation
  WHERE plantdb_vegetation.id = old.vegetationid;

-- Rule: view_insert ON plantdb_vegetationview

-- DROP RULE view_insert ON plantdb_vegetationview;

CREATE OR REPLACE RULE view_insert AS
    ON INSERT TO plantdb_vegetationview DO INSTEAD  INSERT INTO plantdb_vegetation (plant_id, cultivar_id, rootstock_id, locations, grafted, comment, germination_date)
  VALUES (new.plantid, new.cultivarid, new.rootstockid, new.locations, new.grafted, new.comment, new.germination_date);

-- Rule: view_update ON plantdb_vegetationview

-- DROP RULE view_update ON plantdb_vegetationview;

CREATE OR REPLACE RULE view_update AS
    ON UPDATE TO plantdb_vegetationview DO INSTEAD ( 
      UPDATE plantdb_vegetation SET 
        plant_id = new.plantid,
        cultivar_id = new.cultivarid,
        rootstock_id = new.rootstockid,
        locations = new.locations,
        grafted = new.grafted,
        comment = new.comment, 
        germination_date = new.germination_date
    WHERE plantdb_vegetation.id = new.vegetationid;
 UPDATE plantdb_plant SET form = new.form
  WHERE plantdb_plant.id = new.plantid;
);