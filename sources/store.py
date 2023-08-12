
from flask.views import MethodView
from flask_smorest import Blueprint , abort
from db import db
from models import StoreModel
from sqlalchemy.exc import IntegrityError,SQLAlchemyError

from schemas import StoreSchemas

blp = Blueprint("stores",__name__,description="Operation on store")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200,StoreSchemas)
    def get(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store 
    
    def delete(self,store_id):
        item=StoreModel.query.get_or_404(store_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Store deleted successfully"}
            
@blp.route("/store")            
class StoreList(MethodView):
    @blp.response(200,StoreSchemas(many=True))
    def get(self):
        return StoreModel.query.all()
    
    @blp.arguments(StoreSchemas)
    @blp.response(201,StoreSchemas)
    def post(self,store_data):
        
        store=StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(409,message="this store already exist")
        except SQLAlchemyError:
             abort(500,message="An Error occured while inserting the item")       
        
        return store           