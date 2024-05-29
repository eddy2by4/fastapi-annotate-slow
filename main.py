from typing import Annotated

from fastapi import FastAPI, Depends

app = FastAPI()


def my_dep_fn():
    return 2


@app.get("/")
async def root():
    return 1


@app.get("/slow")
async def slow(my_dep=Annotated[int, Depends(my_dep_fn)]):
    return 1
