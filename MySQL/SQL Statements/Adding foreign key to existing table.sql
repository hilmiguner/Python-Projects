# Adding foreign key to existing table
ALTER TABLE products
ADD CONSTRAINT fk_categories_products FOREIGN KEY (categoryId)
REFERENCES categories(id)