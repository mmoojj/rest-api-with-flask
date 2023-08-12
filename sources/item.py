import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint , abort
from models import ItemModel
from db import db
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError

from schemas import ItemSchemas , ItemUpdateSchemas


blp = Blueprint("Items" , __name__ , description="operation on item")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200,ItemSchemas)
    def get(self,item_id):
        item=ItemModel.query.get_or_404(item_id)
        return item
            
    @jwt_required()        
    def delete(self,item_id):
        item=ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message":"the item was deleted"}
        
    @jwt_required()
    @blp.arguments(ItemUpdateSchemas)
    @blp.response(200,ItemUpdateSchemas)
    def put(self,item_data,item_id):
        item=ItemModel.query.get(item_id)
        
        if item:
            item.price=item_data['price']
            item.name=item_data['name']
            
        else:
            item = ItemModel(id=item_id,**item_data)  
        
        db.session.add(item)
        db.session.commit()    
            
        return item      
        
            
@blp.route("/item")            
class ItemList(MethodView):
    @jwt_required()
    @blp.response(200,ItemSchemas(many=True))
    def get(self):
        return ItemModel.query.all()
    
    @jwt_required()
    @blp.arguments(ItemSchemas)
    @blp.response(201,ItemUpdateSchemas)
    def post(self,item_data):
        item = ItemModel(**item_data)
        
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="An Error occured while inserting the item")    
    
        
        return item                   