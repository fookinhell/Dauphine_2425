from fastapi import FastAPI

from rest.dependencies import generator_controller_adapter as controller
from rest.endpoint.generator_rest_adapter import GeneratorRestAdapter
from rest.endpoint.root import router as root_router

rest_api = FastAPI()

rest_api.include_router(root_router)

generator_rest_adapter = GeneratorRestAdapter(controller)
rest_api.include_router(generator_rest_adapter.get_router())