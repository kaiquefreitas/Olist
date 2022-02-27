SELECT count(distinct t2.seller_id),
       MAX(t1.order_approved_at),
       MIN(t1.order_approved_at)
FROM tb_orders as T1
LEFT JOIN tb_order_items as t2 
ON t1.order_id = t2.order_id
where t1.order_approved_at BETWEEN '2017-06-01' AND '2018-06-01'