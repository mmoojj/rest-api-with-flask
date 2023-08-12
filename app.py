# import uuid
# import jsonify
from flask import Flask , request
from flask_smorest import Api
from sources.store import blp as StoreBluePrint
from sources.item import blp as ItemBluePrint
from sources.tags import blp as TagsBluePrint
from sources.user import blp as UserBluePrint
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import models
from db import db
import os
from models import ItemModel
from models import StoreModel
from models import TagModel
# from db import items , stores
# from flask_smorest import abort


def create_app(db_url=None):
    
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"]="Store rest api"
    app.config["API_VERSION"]="v1"
    app.config["OPENAPI_VERSION"]="3.0.3"
    app.config["OPENAPI_URL_PREFIX"]="/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/" 
    app.config["SQLALCHEMY_DATABASE_URI"]=db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    db.init_app(app)
    migrate=Migrate(app,db)
    api = Api(app)
    app.config["JWT_SECRET_KEY"]="mohammad"
    jwt=JWTManager(app)

    
    # @jwt.invalid_token_loader
    # def invalid_token_callback():
    #     return (jsonify({"message":"invalid token"}),401)
    
    
    # @jwt.expired_token_loader
    # def expired_token_callback():
    #     return (jsonify({"message":"expired token"}),401)
    
    
    
    
    
   
    
    
    
    @app.before_request
    def create_tabale():
        db.create_all()
    
        
    api.register_blueprint(ItemBluePrint)
    api.register_blueprint(StoreBluePrint)
    api.register_blueprint(TagsBluePrint)
    api.register_blueprint(UserBluePrint)
    return app



# @app.get("/store")
# def get_store():
#     return {"store":list(stores.values())}


# @app.post("/store")
# def create_store():
#     store_data=request.get_json()
    
#     if "name" not in store_data:
#         abort(400,message="bad request ensure the 'price' or  'name' or 'store_id' exist in body")
        
#     for store in stores.values():
#         if store_data['name'] == store['name']:
#             abort(400,message="this store already exsist")
            
    
#     store_id=uuid.uuid4().hex
#     new_store={**store_data,"id":store_id}
#     stores[store_id]=new_store
#     return new_store,201
    
    
# @app.post("/item")
# def create_item():
#     item_data=request.get_json()
    
#     if ("price" not in item_data or "name" not in item_data or "store_id" not in item_data):
#         abort(400,message="bad request ensure the 'price' or  'name' or 'store_id' exist in body ")
    
#     for item in items:
#         if (item_data['name'] == item['name'] and item_data['store_id'] == item['store_id']):
#             abort(400,message="this item already exsist")
            
#     if item_data["store_id"] not in stores:
#         abort(404,message="store not found") 
    
#     item_id=uuid.uuid4().hex
#     new_item={**item_data,"id":item_id}
#     items[item_id]=new_item
#     return items , 201


# @app.get("/item")
# def get_all_item():
#     return {"item":list(items.values())}


# @app.delete("/item/<string:item_id>")
# def delet_item(item_id):
#     try:
#         del items[item_id]
#         return {"message":"the item was delete"}
#     except KeyError:
#         abort(404,message="item not found.")
        

# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data=request.get_json()
#     if "price" not in item_data or "name" not in item_data:
#         abort(400,message="bad request ensure the 'price' or  'name' or 'store_id' exist in body")
    
#     try:
#         item=items[item_id]
#         item |= item_data
#         return item
#     except KeyError:
#         abort(404,message="item not found")            
    
    
# @app.get("/store/<string:store_id>")
# def get_store_by_name(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#          return  {"message":"store not found yet"} , 404  
        