SELECT CART_ID
FROM CART_PRODUCTS
WHERE CART_ID in (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') AND NAME = 'Milk'
ORDER BY CART_ID;