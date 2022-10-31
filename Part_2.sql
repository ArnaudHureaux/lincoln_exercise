SELECT 
	client_id,
    sum(case when product_type = 'MEUBLE' then CA end) 'MEUBLE',
    sum(case when product_type = 'DECO' then CA end) 'DECO'
FROM
    (SELECT client_id, 
     		SUM(prod_price*prod_qty) as CA, 
     		product_type 
     FROM dataproduit LEFT  JOIN dataclient ON dataproduit.prod_id = dataclient.product_id
     WHERE product_type in  ('DECO','MEUBLE') AND strftime('%YYYY-%mm-%dd',date) BETWEEN date('2020-01-01') AND date('2021-01-01')
     GROUP BY client_id, product_type )
GROUP BY client_id


SELECT date, SUM(CA) FROM (SELECT date, prod_price*prod_qty as CA FROM dataproduit) GROUP BY date ;