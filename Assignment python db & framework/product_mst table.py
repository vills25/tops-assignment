'''
Product_mst table with product id as primary key o Admin can add product subcategory details Like (Product price, product image, 
Product model, product Ram) data should store in Product_sub_cat table o Admin can get product name as foreign key from product_mst table 
in product_sub_category_details page Admin can view, update and delete all registered details of product manager can search product on
search bar and get all details about product.
'''

'''
CREATE TABLE Product_mst (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL
    -- Add other relevant fields specific to the product here
);

CREATE TABLE Product_sub_cat (
    subcat_id INT PRIMARY KEY,
    product_id INT,
    price DECIMAL(10, 2),
    image_url VARCHAR(255),
    model VARCHAR(255),
    ram VARCHAR(50),
    FOREIGN KEY (product_id) REFERENCES Product_mst(product_id)
);

Insert data into the Product_mst table:
sql

INSERT INTO Product_mst (product_id, product_name)
VALUES (1, 'Product 1');
Insert data into the Product_sub_cat table:
sql

INSERT INTO Product_sub_cat (subcat_id, product_id, price, image_url, model, ram)
VALUES (1, 1, 99.99, 'image.jpg', 'Model XYZ', '8GB');
Retrieve all product details:
sql

SELECT *
FROM Product_mst
JOIN Product_sub_cat ON Product_mst.product_id = Product_sub_cat.product_id;
Update product details:
sql

UPDATE Product_mst
SET product_name = 'New Product Name'
WHERE product_id = 1;
Delete product details:
sql

DELETE FROM Product_mst
WHERE product_id = 1;

'''