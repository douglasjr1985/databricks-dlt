-- Cria uma tabela Delta Live Table transformada no catálogo e esquema especificados
CREATE OR REFRESH STREAMING LIVE TABLE catalog_name.schema_name.transformed_data
AS SELECT *
FROM STREAM(LIVE.catalog_name.schema_name.raw_data)
WHERE age > 18;
