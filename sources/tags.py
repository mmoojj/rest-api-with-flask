from flask.views import MethodView
from flask_smorest import abort , Blueprint
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import TagModel , StoreModel

from schemas import TagSchema


blp=Blueprint("tags","tags",description="operation on tags")

@blp.route("/store/<string:store_id>/tag")
class TagView(MethodView):
    @blp.response(200,TagSchema(many=True))
    def get(self, store_id):
        store=StoreModel.query.get_or_404(store_id)
        return store.tags.all()
    
    
    @blp.arguments(TagSchema)
    @blp.response(201,TagSchema)
    def post(self,tag_data,store_id):
        tag=TagModel(**tag_data,store_id=store_id)
        try:
            db.session.add(tag)
            db.session.commit()
            
        except SQLAlchemyError:
            abort(500,message="tag not created")
        
        return tag        
    
@blp.route("/tag/<string:tag_id>")    
class Tag(MethodView):
    @blp.response(200,TagSchema)
    def get(self,tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        
        return tag
        
    
        