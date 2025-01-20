from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.post("/convert/{input_unit}/{output_unit}")
async def convert_units(input_unit: str, output_unit: str, input_value: Union[float, int]) -> float:
    if input_unit == "m" and output_unit == "cm":
        return input_value * 100
    elif input_unit == "cm" and output_unit == "m":
        return input_value / 100
    else:
        return "Conversion not supported"
    
@app.get("/")
async def read_root():
    return {"Hello": "World"}