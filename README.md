# EAG-Session-4-Assignment

# MCP Agent with Paint and Email Integration

This project implements an intelligent agent that can solve mathematical problems, display results in Microsoft Paint, and send screenshots via email MCP. It uses the MCP (Model Control Protocol) framework to connect a client with a server that provides various mathematical and utility tools.

## Features

- **Mathematical Operations**: Perform various mathematical calculations including addition, subtraction, multiplication, division, power, square root, cube root, factorial, log, remainder, trigonometric functions, and more.
- **Paint Integration**: Automatically open Microsoft Paint, draw shapes, and add text to visualize results.
- **Email Functionality**: Take screenshots of the Paint window and send them via email with the results included in the message body.
- **Logging**: Comprehensive logging of all operations for debugging and tracking.
- **Gemini AI Integration**: Uses Google's Gemini AI model for intelligent problem-solving.

## Project Structure

- `mcp_server.py`: The server component that provides tools for mathematical operations, Paint manipulation, and email sending.
- `mcp_client.py`: The client component that communicates with the server and uses Gemini AI to solve problems.
- `*.log`: Log files generated during execution.

## Usage

1. Run the client:
   ```
   python mcp_client.py
   ```

2. The agent will:
   - Solve the mathematical problem
   - Open Paint
   - Draw a rectangle with the specified coordinates
   - Add the answer as text in the rectangle
   - Take a screenshot of the Paint window
   - Send the screenshot via email with the answer included in the message body

3. Check the log file for detailed information about the execution and iteration of the llm.

## Customization

### Changing the Query

You can modify the query in `mcp_client.py` to solve different mathematical problems:

```python
query = """Find the ASCII values of characters in INDIA and then return sum of exponentials of those values. After getting the final answer, open Paint, draw a rectangle with coordinates (680, 436) to (1133, 614), add the answer as text, and send a screenshot of the Paint window via email to tanjirofake2002@gmail.com."""
```


