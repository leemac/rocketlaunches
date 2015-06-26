-- Table: rocketapp_rocket_manufacturers

-- DROP TABLE rocketapp_rocket_manufacturers;

CREATE TABLE rocketapp_rocket_manufacturers
(
  id serial NOT NULL,
  rocket_id integer NOT NULL,
  manufacturer_id integer NOT NULL,
  CONSTRAINT rocketapp_rocket_manufacturers_pkey PRIMARY KEY (id),
  CONSTRAINT rocket_id_refs_id_d964f429 FOREIGN KEY (rocket_id)
      REFERENCES rocketapp_rocket (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT rocketapp_rocket_manufacturers_manufacturer_id_fkey FOREIGN KEY (manufacturer_id)
      REFERENCES rocketapp_manufacturer (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT rocketapp_rocket_manufacturers_rocket_id_manufacturer_id_key UNIQUE (rocket_id, manufacturer_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE rocketapp_rocket_manufacturers
  OWNER TO test;

-- Index: rocketapp_rocket_manufacturers_manufacturer_id

-- DROP INDEX rocketapp_rocket_manufacturers_manufacturer_id;

CREATE INDEX rocketapp_rocket_manufacturers_manufacturer_id
  ON rocketapp_rocket_manufacturers
  USING btree
  (manufacturer_id);

-- Index: rocketapp_rocket_manufacturers_rocket_id

-- DROP INDEX rocketapp_rocket_manufacturers_rocket_id;

CREATE INDEX rocketapp_rocket_manufacturers_rocket_id
  ON rocketapp_rocket_manufacturers
  USING btree
  (rocket_id);

