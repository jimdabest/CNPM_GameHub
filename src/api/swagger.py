from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from api.schemas.todo import TodoRequestSchema, TodoResponseSchema
from api.schemas.user import UserRequestSchema, UserResponseSchema
from api.schemas.developer import DeveloperRequestSchema, DeveloperResponseSchema
from api.schemas.asset_purchases import AssetPurchaseRequestSchema, AssetPurchaseResponseSchema
from api.schemas.asset import AssetRequestSchema, AssetResponseSchema
from api.schemas.designer import DesignerRequestSchema, DesignerResponseSchema
from api.schemas.apiaccess import ApiaccessRequestSchema, ApiaccessResponseSchema

spec = APISpec(
    title="Todo API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Đăng ký schema để tự động sinh model
spec.components.schema("TodoRequest", schema=TodoRequestSchema)
spec.components.schema("TodoResponse", schema=TodoResponseSchema)
spec.components.schema("UserRequest", schema=UserRequestSchema)
spec.components.schema("UserResponse", schema=UserResponseSchema)
spec.components.schema("DesignerRequest", schema=DesignerRequestSchema)
spec.components.schema("DesignerResponse", schema=DesignerResponseSchema)
spec.components.schema("DeveloperRequest", schema=DeveloperRequestSchema)
spec.components.schema("DeveloperResponse", schema=DeveloperResponseSchema)
spec.components.schema("AssetPurchaseRequest", schema=AssetPurchaseRequestSchema)
spec.components.schema("AssetPurchaseResponse", schema=AssetPurchaseResponseSchema)
spec.components.schema("AssetRequest", schema=AssetRequestSchema)
spec.components.schema("AssetResponse", schema=AssetResponseSchema)
spec.components.schema("ApiaccessRequest", schema=ApiaccessRequestSchema)
spec.components.schema("ApiaccessResponse", schema=ApiaccessResponseSchema)


