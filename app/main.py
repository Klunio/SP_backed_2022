# -*- coding: utf-8 -*-
# Create Time: 01/05 2022
# Author: Yunquan (Clooney) Gu
from typing import Union

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from loguru import logger
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from app.db import database
from app.models.schema import InventoryItem

app = FastAPI(debug=False)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['0.0.0.0'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], )
templates = Jinja2Templates(directory="app/templates")

db = database()


@app.on_event("startup")
async def start_up():
    await db.begin()


@app.get("/", status_code=200)
async def root(request: Request):
    return templates.TemplateResponse(
        "item.html",
        {
            "request": request,
            "body": await db.get_all()
        }
    )


@app.post("/add_item")
async def add_item(*, Description: str = Form(...)):
    logger.info(f"[submit] Description='{Description}'")
    item = InventoryItem(description=Description)
    await db.add_item(item)
    return RedirectResponse(url="/",
                            status_code=status.HTTP_302_FOUND)


@app.get("/delete_item")
async def delete_item(item_id: str):
    logger.info(f"[delete] Id='{item_id}'")
    await db.delete_item(item_id)

    return RedirectResponse(url="/",
                            status_code=status.HTTP_302_FOUND)

@app.post("/update_item")
async def update_item(*, item_id: int = Form(...), Description: str = Form(...)):
    logger.info(f"[update] id={item_id} Description='{Description}'")
    await db.update_item(item_id, Description)

    return RedirectResponse(url="/",
                            status_code=status.HTTP_302_FOUND)

import pandas as pd
import tempfile

@app.get("/download")
async def download():
    data = await db.get_all()
    file_path = f'/tmp/{next(tempfile._get_candidate_names())}.csv'
    pd.DataFrame(data).to_csv(file_path)
    return FileResponse(file_path)