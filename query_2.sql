SELECT (CASE WHEN CAST (FLOOR(width)AS DECIMAL)%10>5
		THEN ROUND((CAST (width AS DECIMAL)),-1)
		WHEN CAST (FLOOR(width)AS DECIMAL)%10=0
		THEN CAST (FLOOR(width)AS DECIMAL) ELSE
		ROUND((CAST (width AS DECIMAL)),-1)+5 END
) as width,
		(CASE WHEN CAST (FLOOR(depth)AS DECIMAL)%10>5
		THEN ROUND((CAST (depth AS DECIMAL)),-1)
		WHEN CAST (FLOOR(depth)AS DECIMAL)%10=0
		THEN CAST (FLOOR(depth)AS DECIMAL) ELSE
		ROUND((CAST (depth AS DECIMAL)),-1)+5 END
) as depth,
		(CASE WHEN CAST (FLOOR(height)AS DECIMAL)%10>5
		THEN ROUND((CAST (height AS DECIMAL)),-1)
		WHEN CAST (FLOOR(height)AS DECIMAL)%10=0
		THEN CAST (FLOOR(height)AS DECIMAL) ELSE
		ROUND((CAST (height AS DECIMAL)),-1)+5 END
) as height, COUNT(*) AS count
FROM notebooks_notebook
WHERE width = width AND depth = depth AND height = height AND diagonal = diagonal
GROUP BY width, depth, height
ORDER BY width