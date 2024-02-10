'''
Product_mst table with product id as primary key o Admin can add product subcategory details Like (Product price, product image, 
Product model, product Ram) data should store in Product_sub_cat table o Admin can get product name as foreign key from product_mst table 
in product_sub_category_details page Admin can view, update and delete all registered details of product manager can search product on
search bar and get all details about product.
'''

'''
create table Product_mst (
    product_id int primary key,
    product_name varchar(255) not null
);

create table Product_sub_cat (
    subcat_id int primary key,
    product_id int,
    price decimal(10, 2),
    image_url varchar(255),
    model varchar(255),
    ram varchar(50),
    foreign key (product_id) references Product_mst(product_id)
);

Insert data into the Product_mst table:
insert into Product_mst (product_id, product_name)
values (1, 'Product 1');

Insert data into the Product_sub_cat table:
insert into Product_sub_cat (subcat_id, product_id, price, image_url, model, ram)
values (1, 1, 99.99, 'image.jpg', 'Model XYZ', '8GB');

Retrieve all product details:
select *
from Product_mst
join Product_sub_cat on Product_mst.product_id = Product_sub_cat.product_id;

Update product details:
update Product_mst
set product_name = 'New Product Name'
where product_id = 1;

Delete product details:
delete from Product_mst where product_id=1;

'''