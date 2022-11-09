SELECT notebooks_brand.title, COUNT(*) AS count
FROM notebooks_brand,notebooks_notebook
WHERE notebooks_brand.id = notebooks_notebook.brand_id
GROUP BY notebooks_brand.title
ORDER BY count DESC