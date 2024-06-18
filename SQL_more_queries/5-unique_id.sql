-- ! --
CREATE TABLE IF NOT EXISTS unique_id (
    id INT default 1,
    UNIQUE (id),
    name VARCHAR(256)
);