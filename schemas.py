from marshmallow import Schema , fields


class PlainItemSchemas(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    price = fields.Float(required=True)
    
    
    
class ItemUpdateSchemas(Schema):
    name=fields.Str()
    price=fields.Str()
    store_id=fields.Int()
    
    
class PlainStoreSchmas(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    

class PlainTagSchmas(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str()
        
    

class ItemSchemas(PlainItemSchemas):
    store_id=fields.Int(required=True,load_only=True)
    store=fields.Nested(PlainStoreSchmas(),doump_only=True)
    

    
class StoreSchemas(PlainStoreSchmas):
    items = fields.List(fields.Nested(PlainItemSchemas()),dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchmas()),dump_only=True)
        
    
class TagSchema(PlainTagSchmas):
    store_id=fields.Int(load_only=True)
    store=fields.Nested(PlainStoreSchmas(),doump_only=True)
    
    
class UserSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str(required=True)
    password=fields.Str(required=True,load_only=True)
        
        
    
    
    
            