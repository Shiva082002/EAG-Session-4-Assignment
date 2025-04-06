# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
from pywinauto.application import Application
import win32gui
import win32con
import time
from win32api import GetSystemMetrics
import pyautogui
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import io

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# Load environment variables
load_dotenv()

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


@mcp.tool()
async def draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Draw a rectangle in Paint from (x1,y1) to (x2,y2)"""
    global paint_app
    try:
        if not paint_app:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Paint is not open. Please call open_paint first."
                    )
                ]
            }
        
        # Get the Paint window
        paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Get primary monitor width to adjust coordinates
        primary_width = GetSystemMetrics(0)
        
        # Ensure Paint window is active
        if not paint_window.has_focus():
            paint_window.set_focus()
            time.sleep(1)
        
        # Click on the Rectangle tool using the correct coordinates for secondary screen
        paint_window.click_input(coords=(687, 105 ))
        time.sleep(1.5)
        
        # Get the canvas area
        canvas = paint_window.child_window(class_name='MSPaintView')
        time.sleep(1)
        # Draw rectangle - coordinates should already be relative to the Paint window
        # No need to add primary_width since we're clicking within the Paint window
        # canvas.press_mouse_input(coords=(x1, y1))
        # time.sleep(3)
        # canvas.move_mouse_input(coords=(x2, y1))
        # time.sleep(1)
        # canvas.press_mouse_input(coords=(x2, y1))
        # time.sleep(2)
        # canvas.move_mouse_input(coords=(x2, y2))
        # time.sleep(1)
        pyautogui.moveTo(x1, y1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(2)

        # Drag to (x2, y1)
        pyautogui.moveTo(x2, y1, duration=1)
        time.sleep(1)

        # Drag to (x2, y2)
        pyautogui.moveTo(x2, y2, duration=1)
        time.sleep(2)

        # Release
        pyautogui.mouseUp()
        '''        
        canvas.move_mouse_input(coords=(x1, y2))
        time.sleep(1)
        canvas.release_mouse_input(coords=(x1, y2))'''
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Rectangle drawn from ({x1},{y1}) to ({x2},{y2})"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error drawing rectangle: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def add_text_in_paint(text: str, x1: int, y1: int, x2: int, y2: int) -> dict:
    """Add text in Paint"""
    global paint_app
    try:
        if not paint_app:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Paint is not open. Please call open_paint first."
                    )
                ]
            }
        
        # Get the Paint window
        paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Ensure Paint window is active
        if not paint_window.has_focus():
            paint_window.set_focus()
            time.sleep(1)
        
        # Select text tool using keyboard shortcut 't'
        paint_window.type_keys('t')
        time.sleep(1)
        
        # Get the canvas area
        canvas = paint_window.child_window(class_name='MSPaintView')
        
        # Calculate position for text placement
        center_x = x1+(x2-x1)//4
        text_y = y1 + (y2-y1)//5
        
        # Click where to start typing
        canvas.click_input(coords=(center_x, text_y))
        time.sleep(1)
        
        # Create a larger text box by dragging
        # First click and hold at the starting position
        pyautogui.moveTo(center_x, text_y)
        pyautogui.mouseDown()
        time.sleep(0.5)
        
        # Drag to create a larger text box
        # Make the text box about 1/3 of the rectangle width and 1/4 of the height
        box_width = (x2 - x1) // 1.5
        box_height = (y2 - y1) // 3
        pyautogui.moveTo(center_x + box_width, text_y + box_height, duration=0.5)
        time.sleep(0.5)
        
        # Release the mouse button
        pyautogui.mouseUp()
        time.sleep(1)
        
        # Increase text size using keyboard shortcuts
        # Press Ctrl+A to select all text (even though there's no text yet)
        paint_window.type_keys('^a')
        time.sleep(0.5)
        
        # Press Ctrl+Shift+> multiple times to increase font size
        # Each press increases the size by one step
        for _ in range(5):  # Increase size 5 times
            paint_window.type_keys('^+>')
            time.sleep(0.2)
        
        # Type the text passed from client
        paint_window.type_keys(text, with_spaces=True)
        time.sleep(1)
        
        # Click to exit text mode
        canvas.click_input(coords=(1450, 850))
        rect = canvas.rectangle()
        print(f"Paint window bounds: {rect}")
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Text:'{text}' added successfully at position ({center_x}, {text_y}) with increased size and larger text box"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error adding text: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def open_paint() -> dict:
    """Open Microsoft Paint maximized"""
    global paint_app
    try:
        paint_app = Application().start('mspaint.exe')
        time.sleep(0.2)
        
        # Get the Paint window
        paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Get primary monitor width
        primary_width = GetSystemMetrics(0)
        
        # First move to secondary monitor without specifying size
        win32gui.SetWindowPos(
            paint_window.handle,
            win32con.HWND_TOP,
            #primary_width + 1, 0,  # Position it on secondary monitor
            0, 0,
            0, 0,  # Let Windows handle the size
            win32con.SWP_NOSIZE  # Don't change the size
        )
        
        # Now maximize the window
        win32gui.ShowWindow(paint_window.handle, win32con.SW_MAXIMIZE)
        time.sleep(0.2)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Paint opened successfully on secondary monitor and maximized"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error opening Paint: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def take_screenshot_and_send_email(recipient_email: str, subject: str, message: str) -> dict:
    """Take a screenshot of the Paint window and send it via email"""
    global paint_app
    try:
        if not paint_app:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Paint is not open. Please call open_paint first."
                    )
                ]
            }
        
        # Get the Paint window
        paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Ensure Paint window is active
        if not paint_window.has_focus():
            paint_window.set_focus()
            time.sleep(1)
        
        # Get window position and size
        window_rect = win32gui.GetWindowRect(paint_window.handle)
        x, y, width, height = window_rect[0], window_rect[1], window_rect[2] - window_rect[0], window_rect[3] - window_rect[1]
        
        # Take screenshot of the Paint window
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        
        # Save screenshot to a temporary file
        temp_file = "paint_screenshot.png"
        screenshot.save(temp_file)
        
        # Get the answer from the Paint window
        # This is a simplified approach - in a real implementation, you might need to
        # extract the text from the Paint window or use OCR
        answer = "The answer is displayed in the attached screenshot."
        
        # Enhance the message with the answer
        enhanced_message = f"""
{message}

ANSWER:
{answer}

Please see the attached screenshot for visual representation.
"""
        
        # Send email with the screenshot
        success = send_email_with_attachment(recipient_email, subject, enhanced_message, temp_file)
        
        # Clean up the temporary file
        # if os.path.exists(temp_file):
        #     os.remove(temp_file)
        
        if success:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text=f"Screenshot taken and email sent successfully to {recipient_email}"
                    )
                ]
            }
        else:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text=f"Screenshot taken but failed to send email to {recipient_email}"
                    )
                ]
            }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error taking screenshot and sending email: {str(e)}"
                )
            ]
        }

def send_email_with_attachment(recipient_email: str, subject: str, message: str, attachment_path: str) -> bool:
    """Send email with attachment using SMTP."""
    try:
        # Create message
        msg = MIMEMultipart()
        msg["From"] = os.getenv("SENDER_EMAIL")
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Create email body
        body = f"""
        {message}

        Best regards,
        Shivansh Yadav.
        """

        msg.attach(MIMEText(body, "plain"))

        # Attach the screenshot
        with open(attachment_path, "rb") as attachment:
            part = MIMEImage(attachment.read())
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(attachment_path)}",
            )
            msg.attach(part)

        # Create SMTP session
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT"))
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        
        print(f"Connecting to SMTP server: {smtp_server}:{smtp_port}")
        server = smtplib.SMTP(smtp_server, smtp_port)
        
        print("Starting TLS...")
        server.starttls()
        
        print(f"Logging in as {sender_email}...")
        server.login(sender_email, sender_password)

        # Send email
        print("Sending email...")
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
        return True
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {str(e)}")
        print("This is likely because Gmail requires an App Password instead of your regular password.")
        print("To fix this:")
        print("1. Enable 2-Step Verification in your Google Account")
        print("2. Generate an App Password: Google Account > Security > 2-Step Verification > App passwords")
        print("3. Use that App Password in your .env file instead of your regular password")
        return False
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        return False

# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution