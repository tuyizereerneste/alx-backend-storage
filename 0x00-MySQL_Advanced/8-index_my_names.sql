-- script that creates an index idx_name_first on
-- the table names and the first letter of name.
-- Only the first letter of name must be indexed
CREATE INDEX idx_first_name ON names(name(1))
