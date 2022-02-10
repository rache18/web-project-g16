# Flask Skeleton Project

### Flask skeleton project as a base project for app development
##### [https://github.com/rache18/web-project-g16](https://github.com/rache18/web-project-g16)
<br/>

##### Description: 
This is a base skeleton Flask project to start developing on.
<br/>
You may want to modify some of the configurations and files as needed. 
   
###
##### Keywords: 
flask, lean, skeleton, project, structure, environment, setup, template, fullstack, web, development, app, university, education.
###

##### By Racheli Elyiahu, Alon Erlich, Ariel Hamami and Tomer Levavi 

 
### Setup and run instructions:

#### Prerequisites:
Open the project's dir in the terminal and run the following commands:
1. pip install virtualenv
1. virtualenv venv
1. pip install python-dotenv
<br/>

#### Configurations:
Open the project's dir in the terminal and:
1. Run the command: **python -c "import os; print(os.urandom(16))"**
1. Copy the output string
1. Edit the project's **.env** file found inside the root folder
1. Overwrite the **SECRET_KEY** value with the string you copied
<br/>
 
#### Run:
 Run the project with your IDE's configuration, or from the terminal by using the **flask run** command
 
 ##
 
### Usage:

#### Connecting and querying a database:
1) Connect to the database with **DB as the argument (db_manager)
   db_connection = mysql.connector.connect(**DB)
   
2) Retrieving and updating data from a particular table will be done by
   importing an object belonging to the same class and using its methods

3) example of method that belongs to product: 
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

      while using this method at shop route:
      
   def index():
         if request.args.get('sale') is not None:
              products = dbProducts.get_products(sale=True)
          elif request.args.get('price') is not None:
              products = dbProducts.get_products(price=request.args.get('price'))
          elif request.args.get('color') is not None:
              products = dbProducts.get_products(color=request.args.get('color'))
          else:
              products = dbProducts.get_products()
          return render_template('shop.html', products=products)

