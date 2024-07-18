-- Cria ou atualiza a tabela LIVE TABLE customers
CREATE OR REFRESH LIVE TABLE customers
COMMENT "The customers buying finished products, ingested from /databricks-datasets."
TBLPROPERTIES ("myCompanyPipeline.quality" = "mapping")
AS SELECT * FROM hive_metastore.teste.usuarios;

-- Cria ou atualiza a tabela LIVE TABLE sales_orders_raw
CREATE OR REFRESH LIVE TABLE sales_orders_raw
COMMENT "The raw sales orders, ingested from /databricks-datasets."
TBLPROPERTIES ("myCompanyPipeline.quality" = "bronze")
AS SELECT * FROM hive_metastore.teste.usuarios;

-- Cria ou atualiza a tabela LIVE TABLE sales_orders_cleaned
CREATE OR REFRESH LIVE TABLE sales_orders_cleaned
COMMENT "The cleaned sales orders with valid order_number(s) and partitioned by order_datetime."
TBLPROPERTIES ("myCompanyPipeline.quality" = "silver")
AS
SELECT c.idade as idade
  FROM LIVE.sales_orders_raw f
  LEFT JOIN LIVE.customers c  ON c.idade = f.idade;

-- Cria ou atualiza a tabela LIVE TABLE sales_order_in_la
CREATE OR REFRESH LIVE TABLE sales_order_in_la
COMMENT "Sales orders in LA."
TBLPROPERTIES ("myCompanyPipeline.quality" = "gold")
AS
SELECT  COUNT(*) as product_count
FROM (
  SELECT idade
  FROM LIVE.sales_orders_cleaned );

-- Cria ou atualiza a tabela LIVE TABLE sales_order_in_chicago
CREATE OR REFRESH LIVE TABLE sales_order_in_chicago
COMMENT "Sales orders in Chicago."
TBLPROPERTIES ("myCompanyPipeline.quality" = "gold")
AS
SELECT  COUNT(*) as product_count
FROM (
  SELECT idade
  FROM LIVE.sales_orders_cleaned );
