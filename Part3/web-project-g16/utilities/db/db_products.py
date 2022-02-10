from interact_with_DB import interact_db

class DBproducts:

    def delete_product(self,product_id):
        query = "delete from web_project_g16.products WHERE product_id='%s';" % product_id
        interact_db(query=query, query_type='commit')
        return True

    def insert_product(self, name, price, sale_price, color, link, InStock):
            sale= None
            price_level= None
            check_input = "SELECT name FROM web_project_g16.products WHERE name='%s';" % name
            answer = interact_db(query=check_input, query_type='fetch')
            if len(answer) == 0:
                if sale_price > 0:
                    sale = 'sale'
                    if sale_price <= 50:
                        price_level = 'low'
                    elif sale_price <= 100:
                        price_level = 'mid'
                    else:
                        price_level = 'high'

                    query = "insert into web_project_g16.products (name, price, sale_price, color, sale, price_level, link,InStock)\
                                                        value ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
                    name, price, sale_price, color, sale, price_level, link,InStock)
                    interact_db(query=query, query_type='commit')

                else:
                    if price <= 50:
                        price_level = 'low'
                    elif price <= 100:
                        price_level = 'mid'
                    else:
                        price_level = 'high'

                    query = "insert into web_project_g16.products (name, price, color, price_level, link, InStock)\
                                    value ('%s', '%s', '%s', '%s', '%s', '%s');" % (name, price, color, price_level, link, InStock)
                    interact_db(query=query, query_type='commit')
                return True
            else:
                return False

    def get_products(self,price = False,sale = False,color = False):
        if sale:
            get_products = "SELECT * FROM web_project_g16.products where sale IS NOT NULL;"
        elif price == 'whole':
            get_products = "SELECT * FROM web_project_g16.products;"
        elif price != False:
            get_products = "SELECT * FROM web_project_g16.products where price_level = '%s';"% (price)
        elif color != False:
            get_products = "SELECT * FROM web_project_g16.products where color = '%s';"% (color)
        else:
            get_products = "SELECT * FROM web_project_g16.products;"
        answer = interact_db(query=get_products, query_type='fetch')
        return answer

    def update_stock_admin(self,product_id,inStock):
        query = "UPDATE web_project_g16.products SET inStock='%s' WHERE product_id='%s';" % (inStock, product_id)
        interact_db(query=query, query_type='commit')
        return True


    def update_product(self, product_id, sale):
        if sale == -1:
            query = "UPDATE web_project_g16.products SET sale_price=null ,sale=null WHERE product_id='%s';" % (product_id)
        else:
            query = "UPDATE web_project_g16.products SET sale_price='%s',sale='sale' WHERE product_id='%s';" % (sale, product_id)
        interact_db(query=query, query_type='commit')

    def update_stock(self, products_in_cart):
        for product in products_in_cart:
            query = "SELECT inStock FROM web_project_g16.products where product_id = '%s';"% (product.product_id)
            inStock = interact_db(query=query, query_type='fetch')[0]
            inStock = inStock.inStock
            newStock = inStock-product.quantity
            query = "UPDATE web_project_g16.products SET inStock='%s' WHERE product_id='%s';" % (newStock, product.product_id)
            interact_db(query=query, query_type='commit')

    def isProductMiss(self, products_in_cart):
        for product in products_in_cart:
            query = "SELECT inStock, name FROM web_project_g16.products where product_id = '%s';"% (product.product_id)
            ans = interact_db(query=query, query_type='fetch')[0]
            inStock = ans.inStock
            if inStock < product.quantity:
                return True, ans.name
        return False, None

# Creates an instance for the DBproducts class for export.
dbProducts = DBproducts()