import tkinter as tk
from tkinter import font

# Function to update the display
def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

# Function to clear the display
def clear_display():
    display_var.set("0")

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to handle button clicks
def on_button_click(value):
    if value == "C":
        clear_display()
    elif value == "=":
        evaluate_expression()
    else:
        update_display(value)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")
root.configure(bg="#fafafa")  # background

# style color palette
BG_COLOR = "#fafafa"  # Main background
DISPLAY_BG = "#ffffff"  # White display background
BUTTON_BG = "#ffffff"  # White button background
BUTTON_ACTIVE_BG = "#e0f2ff"  # Light blue active state
TEXT_COLOR = "#262626"  # dark text
ACCENT_COLOR = "#0095f6"  # blue

# Custom font
custom_font = font.Font(family="Helvetica", size=18, weight="bold")

# Display variable
display_var = tk.StringVar()
display_var.set("0")

# Display label
display_label = tk.Label(
    root,
    textvariable=display_var,
    font=custom_font,
    bg=DISPLAY_BG,
    fg=TEXT_COLOR,
    anchor="e",
    padx=20,
    pady=20,
    highlightthickness=1,
    highlightbackground="#dbdbdb"  # Add subtle border
)
display_label.pack(fill=tk.BOTH, expand=True)

# Button frame
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Button layout
buttons = [
    ('7', '#ffffff'), ('8', '#ffffff'), ('9', '#ffffff'), ('/', '#e0f2ff'),
    ('4', '#ffffff'), ('5', '#ffffff'), ('6', '#ffffff'), ('*', '#e0f2ff'),
    ('1', '#ffffff'), ('2', '#ffffff'), ('3', '#ffffff'), ('-', '#e0f2ff'),
    ('C', '#ffcccc'), ('0', '#ffffff'), ('=', ACCENT_COLOR), ('+', '#e0f2ff')
]

# Create and place buttons
row, col = 0, 0
for text, color in buttons:
    action = lambda x=text: on_button_click(x)
    tk.Button(
        button_frame,
        text=text,
        font=custom_font,
        bg=color,
        fg=TEXT_COLOR if text not in ['=', 'C'] else '#ffffff',
        activebackground=BUTTON_ACTIVE_BG,
        activeforeground=TEXT_COLOR,
        bd=0,
        highlightthickness=0,
        relief="flat",
        command=action
    ).grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=3,
        pady=3
    )
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid weights
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)

# Add subtle shadow to buttons
for child in button_frame.winfo_children():
    widget_type = child.winfo_class()
    if widget_type == "Button":
        child.config(highlightbackground="#dbdbdb", highlightthickness=1)

# Run the application
root.mainloop()