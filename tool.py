from typing import Any
from pydantic import BaseModel
from agents import RunContextWrapper, FunctionTool
from datetime import datetime

def get_current_time(data: str) -> str:
    rightnow = datetime.now()
    x = rightnow.strftime("%H")
    x = int(x)
    z = "am"
    if x >= 12:
        z="pm"
    eenow = rightnow.strftime(f"The time is currenly %I:%M{z}")
    today = rightnow.strftime(f"The date today is %x")
    return eenow, today

def reader() -> str:
    with open("./something.txt", 'r') as f:
        entire_file_as_string = f.read()
    return entire_file_as_string


class FuncArgs(BaseModel):
    date: str
    time: str


async def run_func(ctx: RunContextWrapper[Any], args: str) -> str:
    parsed = FuncArgs.model_validate_json(args)
    return get_current_time(data=f"It is {parsed.time} on {parsed.date}")

time_tool = FunctionTool(
    name ="clock_check",
    description="Gives you the time and date",
    params_json_schema=FuncArgs.model_json_schema(),
    on_invoke_tool=run_func,
)

