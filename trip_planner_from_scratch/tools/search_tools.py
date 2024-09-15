from langchain.tools import tool

from pydantic import BaseModel, Field


# This tool is very basic and simple
class CalculatorTools():
    
    @tool("Make a calculation")
    def calculate(operation):
        """ Useful to perform any mathematical  calculations,
        like sum, minus, multiplication, division, etc.
        The input to this tool should be a mathematical
        expression, a couple examples are "200*7" or "5000/2*10"
        """

        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntex in mathematical expression"





# # Define a Pydantic model for the tool's input parameters

# class CalculationInput(BaseModel):
#     operation: str = Field(..., description= "The mathematical operation to perform")
#     factor: float = Field(..., description= "A Factor by which to multiply the result of the operation")


# # Use th tool decorator with the args_schema parameter pointing to the Pydantic Model
# @tool("perform_calculation", args_schema=CalculationInput, return_direct=True)
# def perform_calculation(operation: str, factor: float) -> str:
#     """
#     Perform a specified mathematical operation and multiplies the result by a given factor.

#     Parameters:
#     - operation (str): A string representing a mathematical operation (e.g., "10+5").
#     - factor (float): A factor by which to multiply the result of the operation.

#     Returns:
#     - A string representation of the calculation result.
#     """

#     # perform the calculation
#     result = eval(operation) * factor

#     # Return the result as a string
#     return f"The result of '{operation}' multiplied by {factor} is {result}."