import tkinter as tk
import os
import sys
import csv
from tkinter import ttk, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import sympy as sp
from sympy import sympify, symbols, pi
from matplotlib import rcParams
from PIL import Image, ImageTk
#from sympy import sympify, symbols, pi, sqrt



# Global variable for the symbol used in equations
x = symbols('x')  # Define 'x' as a symbol for sympy to recognize it in equations

# Set font family globally for emojis
rcParams['font.family'] = 'Segoe UI Emoji' # Windows-compatible
# For MacOS or Linux, replace 'Segoe UI Emoji' with 'Apple Color Emoji' or similar

## Used to make executable
def get_resource_path(relative_path):
    """Get the path to the resource (image) depending on whether running as a script or an executable."""
    if getattr(sys, 'frozen', False):  # Check if running as a bundled executable
        # Running in a bundled app
        base_path = sys._MEIPASS
    else:
        # Running as a script
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

#####################################################################
# Function to safely parse and evaluate equations using sympy
#####################################################################

def parse_equation(equation_str):
    try:
        # Replace '^' with '**' for exponentiation, and handle whitespace
        equation_str = equation_str.replace('^', '**').replace(' ', '')  
        
        equation_str = equation_str.replace('pi', str(pi))
        
        # Ensure that 'sqrt' is correctly interpreted as the SymPy sqrt function (not working properly still)
        #equation_str = equation_str.replace('sqrt', 'sqrt(') + ')' * equation_str.count('sqrt')
        
        processed_str = ''
        for i, char in enumerate(equation_str):
            if i > 0 and char.isalpha() and equation_str[i-1].isdigit():
                processed_str += '*' + char  # Insert '*' for implicit multiplication
            elif i > 0 and char.isdigit() and equation_str[i-1].isalpha():
                processed_str += '*' + char  # Insert '*' for implicit multiplication
            else:
                processed_str += char

        expression = sympify(processed_str)
        return lambda val: float(expression.subs(x, val))  # Return lambda for evaluation
    except Exception as e:
        messagebox.showerror("Error", f"Invalid equation format: {e}")
    return None

# placeholder for plot_data

# placeholder for clear_graph

# placeholder for save_graph

# placeholder to import from file ()

# placeholder for import_file

# Function to customize the graph
# def customize_graph():
    # title = title_input.get()
    # x_label = x_label_input.get()
    # y_label = y_label_input.get()

    # ax.set_title(title)
    # ax.set_xlabel(x_label)
    # ax.set_ylabel(y_label)
    # canvas.draw()
    
#####################################################################
# Function to resize logo based on window size
#####################################################################

def resize_logo(event):
    new_width = event.width // 8  # Adjust size based on window width
    new_height = event.height // 8  # Adjust size based on window height
    resized_logo = original_logo.resize((new_width, new_height), Image.ANTIALIAS)
    logo_image = ImageTk.PhotoImage(resized_logo)
    logo_label.config(image=logo_image)
    logo_label.image = logo_image  # Keep a reference to prevent garbage collection

#####################################################################
# Function to show/hide input fields based on selected graph type
#####################################################################

def update_input_fields(event):
    bar_input.pack_forget()
    pie_input.pack_forget()
    pictograph_input.pack_forget()
    hist_input.pack_forget()
    area_input.pack_forget()
    scatter_input.pack_forget()
    equation_input.pack_forget()

    # Get selected graph from dropdown
    graph_type = graph_type_combo.get()

    # Display the appropriate input field based on selected graph type
    if graph_type == "Bar Graph":
        placeholder = "Enter data in 'Category, Value' format (e.g., A, 5)"
        initial(bar_input, placeholder)
        bar_input.bind("<FocusIn>", lambda event=None: on_entry_click(bar_input, placeholder))
        bar_input.bind("<FocusOut>", lambda event=None: on_focusout(bar_input, placeholder))
        bar_input.pack(pady=5)
    elif graph_type == "Pie Chart":
        placeholder = "Enter data in 'Label, Value' format (e.g., Category A, 50)"
        initial(pie_input, placeholder)
        pie_input.bind("<FocusIn>", lambda event=None: on_entry_click(pie_input, placeholder))
        pie_input.bind("<FocusOut>", lambda event=None: on_focusout(pie_input, placeholder))
        pie_input.pack(pady=5)
    elif graph_type == "Pictograph":
        placeholder = "Enter data in 'Emoji Name, Count' format (e.g., Cat, 3)"
        initial(pictograph_input, placeholder)
        pictograph_input.bind("<FocusIn>", lambda event=None: on_entry_click(pictograph_input, placeholder))
        pictograph_input.bind("<FocusOut>", lambda event=None: on_focusout(pictograph_input, placeholder))
        pictograph_input.pack(pady=5)
    elif graph_type == "Histogram":
        placeholder = "Enter comma-separated values (e.g., 1, 2, 3, 4)"
        initial(hist_input, placeholder)
        hist_input.bind("<FocusIn>", lambda event=None: on_entry_click(hist_input, placeholder))
        hist_input.bind("<FocusOut>", lambda event=None: on_focusout(hist_input, placeholder))
        hist_input.pack(pady=5)
    elif graph_type == "Area Graph":
        placeholder = "Enter comma-separated Y-values (e.g., 1, 2, 3, 4, 5)"
        initial(area_input, placeholder)
        area_input.bind("<FocusIn>", lambda event=None: on_entry_click(area_input, placeholder))
        area_input.bind("<FocusOut>", lambda event=None: on_focusout(area_input, placeholder))
        area_input.pack(pady=5)
    elif graph_type == "Scatter Plot":
        placeholder = "Enter X and Y coordinate values on separate lines (e.g., X, Y)"
        initial(scatter_input, placeholder)
        scatter_input.bind("<FocusIn>", lambda event=None: on_entry_click(scatter_input, placeholder))
        scatter_input.bind("<FocusOut>", lambda event=None: on_focusout(scatter_input, placeholder))
        scatter_input.pack(pady=5)
    elif graph_type == "Line Plot":
        placeholder = "Enter equation (e.g., 2*x^2 + 3*x - 5)"
        initial(equation_input, placeholder)
        equation_input.bind("<FocusIn>", lambda event=None: on_entry_click(equation_input, placeholder))
        equation_input.bind("<FocusOut>", lambda event=None: on_focusout(equation_input, placeholder))
        equation_input.pack(pady=5)

    
#####################################################################
# Function for placeholder text
#####################################################################

# Inital placeholder
def initial(input, placeholder):#
    if isinstance(input, tk.Entry):  # Single-line input (Entry widget)
        if input.get() == "":
            input.insert(0, placeholder)  
            input.config(fg="grey")  
    else:  # Multi-line input (Text widget)
        if input.get("1.0", "end-1c") == "":
            input.insert("1.0", placeholder) 
            input.config(fg="grey")

# Function to clear the placeholder when the user clicks the entry box
def on_entry_click(input, placeholder):
    if isinstance(input, tk.Entry):  # Single-line input (Entry widget)
        if input.get() == placeholder:
            input.delete(0, tk.END)  
            input.config(fg="black")  
    else:  # Multi-line input (Text widget)
        if input.get("1.0", "end-1c") == placeholder:
            input.delete("1.0", tk.END)  
            input.config(fg="black")  

# Function to add the placeholder back if the entry box is left empty
def on_focusout(input, placeholder):
    if isinstance(input, tk.Entry):  # Single-line input (Entry widget)
        if input.get() == "":
            input.insert(0, placeholder) 
            input.config(fg="grey")  
    else:  # Multi-line input (Text widget)
        if input.get("1.0", "end-1c") == "":
            input.insert("1.0", placeholder) 
            input.config(fg="grey") 
     
#####################################################################
# Main function encapsulating all the GUI code
#####################################################################
    
def main():
    global graph_type_combo, ax, canvas, original_logo, logo_label
    # global title_input, x_label_input, y_label_input, 
    global imported_data, fig
    global bar_input, pie_input, pictograph_input, hist_input, area_input, scatter_input, equation_input

    #####################################################################
    # Create the main window
    #####################################################################
    
    root = tk.Tk()
    root.title("Easy Graph Generator")
    root.geometry("900x600")  # Original size
    root.configure(bg="#d0f0c0")

    # Set the window to be resizable
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    
    # Logo on title bar
    image_path = get_resource_path("EGG.png")
    original_logo = Image.open(image_path)
    icon_image = ImageTk.PhotoImage(original_logo.resize((32, 32)))  # Resize for title bar
    root.iconphoto(True, icon_image)  # Set title bar icon

    # Create a frame for the controls on the left
    control_frame = tk.Frame(root, bg="#d0f0c0")
    control_frame.grid(row=0, column=0, sticky="ns")

    #####################################################################
    # Create empty graph for plotting
    #####################################################################
    
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_facecolor('#f5fff2')
    ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
    ax.minorticks_on()
    ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)


    #####################################################################
    # Load and resize the logo
    #####################################################################
    
    image_path = get_resource_path("EGG.png")
    original_logo = Image.open(image_path)
    logo_image = ImageTk.PhotoImage(original_logo.resize((100, 100)))
    logo_label = tk.Label(control_frame, image=logo_image, bg="#d0f0c0")
    logo_label.pack(pady=5)

    #####################################################################
    # Dropdown menu for selecting graph type with prompt
    #####################################################################
    
    graph_type_label = tk.Label(control_frame, text="Select Graph Type", bg="#d0f0c0")
    graph_type_label.pack(pady=5)
     
    graph_type_combo = ttk.Combobox(control_frame, values=["Line Plot", "Bar Graph", "Pie Chart", "Pictograph", "Histogram", "Area Graph", "Scatter Plot"], state="readonly", width=35)
    graph_type_combo.set("Choose a graph")  # Default prompt
    graph_type_combo.pack(pady=5)
    graph_type_combo.bind("<<ComboboxSelected>>", update_input_fields)
    
    #####################################################################
    # Graph inputs
    #####################################################################
            
    # Bar Graph input
    bar_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    #bar_input.insert("1.0", "Category, Value\nA, 5\nB, 3\nC, 8")

    # Pie Chart input
    pie_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    #pie_input.insert("1.0", "Label, Value\nCategory A, 50\nCategory B, 30\nCategory C, 20")

    # Pictograph input
    pictograph_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    #pictograph_input.insert("1.0", "Category, Count\nCat A, 3\nCat B, 1\nCat C, 2")
    
    # Histogram input
    hist_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    #hist_input.insert("1.0", "Data values (comma separated)\n1, 2, 2, 3, 3, 3, 4, 4, 5")

    # Area Graph input
    area_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    #area_input.insert("1.0", "Y values (comma separated)\n1, 2, 3, 4, 5")

    # Scatter Plot input
    scatter_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    #scatter_input.insert("1.0", "X values (comma separated)\n1, 2, 3, 4, 5\nY values (comma separated)\n2, 3, 5, 1, 4")
    
    # Equation input - hidden until type of graph is chosen
    equation_input = tk.Entry(control_frame, width=40)

    # Customize graph inputs
    # title_input = tk.Entry(control_frame, width=30)
    # title_input.insert(0, "Graph Title")
    # title_input.pack(pady=5)

    # x_label_input = tk.Entry(control_frame, width=30)
    # x_label_input.insert(0, "X-axis Label")
    # x_label_input.pack(pady=5)

    # y_label_input = tk.Entry(control_frame, width=30)
    # y_label_input.insert(0, "Y-axis Label")
    # y_label_input.pack(pady=5)
    
    #####################################################################
    # Function to update the graph based on user input and selected graph type
    #####################################################################

    def plot_graph():
        graph_type = graph_type_combo.get()

        # Clear the plot
        ax.clear()
        save_button.pack_forget()
        
        # Set background color and grid styling
        ax.set_facecolor('#e0f7da')
        ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
        ax.minorticks_on()
        ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)
        ax.axhline(0, color='black', linewidth=1.0)
        ax.axvline(0, color='black', linewidth=1.0)

        try:
            if graph_type == "Line Plot":
                equation_str = equation_input.get()
                equation_func = parse_equation(equation_str)
                if not equation_func:
                    return  # If the equation is invalid, exit without plotting

                x_vals = np.linspace(-10, 10, 400)
                y_vals = [equation_func(val) for val in x_vals]

                ax.plot(x_vals, y_vals, label=equation_str, color="green")
                ax.legend()
            
            elif graph_type == "Bar Graph":
                data_pairs = bar_input.get("1.0", tk.END).strip().splitlines()
                categories, values = [], []
                for pair in data_pairs:
                    try:
                        category, value = pair.split(',')
                        categories.append(category.strip())
                        values.append(float(value.strip()))
                    except ValueError:
                        messagebox.showerror("Error", "Invalid format for Bar Graph. Use 'Category, Value' format.")
                        return
                ax.bar(categories, values, color="green")
            
            elif graph_type == "Pie Chart":
                data_pairs = pie_input.get("1.0", tk.END).strip().splitlines()
                values, labels = [], []
                for pair in data_pairs:
                    try:
                        label, value = pair.split(',')
                        labels.append(label.strip())
                        values.append(float(value.strip()))
                    except ValueError:
                        messagebox.showerror("Error", "Invalid format for Pie Chart. Use 'Label, Value' format.")
                        return
                ax.pie(values, labels=labels, autopct='%1.1f%%')
            
            elif graph_type == "Pictograph":
                # Get input data from the text box
                data_pairs = pictograph_input.get("1.0", tk.END).strip().splitlines()

                # Initialize variables for storing parsed data
                data = []

                try:
                    # Parse the input into categories and counts
                    for pair in data_pairs:
                        category, count = pair.split(',')
                        count = int(count.strip())
                        data.append((category.strip(), count))  # Store as tuples
                except ValueError:
                # Handle parsing errors
                    messagebox.showerror("Error", "Invalid format for Pictograph. Use 'Category, Count' format.")
                    return
                # This is the emoji map more emojis can easily be added to this list
                emoji_mapping = {
                    "dog": "🐶", "cat": "🐱", "bird": "🐦", "fish": "🐟", "rabbit": "🐰", "mouse": "🐭", "turtle": "🐢", "frog": "🐸",
                    "horse": "🐴", "cow": "🐮", "sheep": "🐑", "monkey": "🐵", "chicken": "🐔", "pig": "🐷", "lion": "🦁", "tiger": "🐯",
                    "elephant": "🐘", "panda": "🐼", "bear": "🐻", "whale": "🐳", "dolphin": "🐬", "shark": "🦈", "octopus": "🐙", "bee": "🐝",
                    "ladybug": "🐞", "snail": "🐌", "crab": "🦀", "butterfly": "🦋", "hedgehog": "🦔", "kangaroo": "🦘", "koala": "🐨",
                    "camel": "🐫", "owl": "🦉", "bat": "🦇", "swan": "🦢", "flamingo": "🦩", "peacock": "🦚", "parrot": "🦜",
                    "unicorn": "🦄", "dragon": "🐉", "gorilla": "🦍", "wolf": "🐺", "fox": "🦊", "zebra": "🦓", "hippopotamus": "🦛",
                    "raccoon": "🦝", "penguin": "🐧", "duck": "🦆", "squid": "🦑", "lobster": "🦞", "seal": "🦭", "cheetah": "🐆",
                    "t-rex": "🦖", "sauropod": "🦕", "smile": "😊", "grin": "😁", "wink": "😉", "laugh": "😆", "heart": "❤️",
                    "heart_eyes": "😍", "kiss": "😘", "star": "⭐", "sparkles": "✨", "fire": "🔥", "thumbs_up": "👍", "clap": "👏",
                    "party": "🎉", "confetti": "🎊", "balloon": "🎈", "flower": "🌸", "tree": "🌳", "sun": "☀️", "moon": "🌙",
                    "apple": "🍎", "banana": "🍌", "cherry": "🍒", "grapes": "🍇", "lemon": "🍋", "melon": "🍈", "orange": "🍊",
                    "pear": "🍐", "pineapple": "🍍", "strawberry": "🍓", "watermelon": "🍉", "peach": "🍑", "kiwi": "🥝",
                    "coconut": "🥥", "avocado": "🥑",
                    # Add more mappings as needed
                    } 

                # Plot emojis on the graph
                x_positions = []  # X positions for categories
                max_count = max(count for _, count in data)  # Find the maximum count to scale the graph

                # Set up graph limits
                ax.set_xlim(0, len(data))  # One x-unit per category
                ax.set_ylim(0, max_count + 1)  # Allow some extra space on the y-axis

                # Iterate through data to plot emojis
                for i, (category, count) in enumerate(data):
                    emoji = emoji_mapping.get(category.lower(), "❓")  # Default to "❓" if no emoji mapping
                    x = i + 0.5  # Center emoji stack at category position
                
                    for j in range(count):
                        y = j + 0.5  # Position emojis vertically stacked
                        ax.text(x, y, emoji, fontsize=16, ha='center', va='center')  # Plot each emoji

                    # Add a label for the category below the emojis
                    ax.text(x,-0.15, category.capitalize(), fontsize=10, ha='center', va='center')  # Label below emojis

                    # Format the graph
                    ax.set_xticks([])  # Remove x-axis ticks
                    ax.set_yticks(range(max_count + 1))  # Show y-axis as counts
                    ax.set_ylabel("Count")
                    ax.set_xlabel("Categories")

                    # Remove top and right spines for cleaner look
                    ax.spines['top'].set_visible(False)  
                    ax.spines['right'].set_visible(False)

                    # Offset y-axis and x-axis spines for better visual separation
                    ax.spines['left'].set_position(('outward', 8))  
                    ax.spines['bottom'].set_position(('outward', 1))
            
            elif graph_type == "Histogram":
                # Get the input data from the text box and strip extra spaces and newlines
                data_values = hist_input.get("1.0", tk.END).strip().split(',')
    
                # Convert the data into a list of floats. If the input is empty or invalid, it is ignored.
                try:
                    data_values = [float(val) for val in data_values if val]  # Convert input to float
                except ValueError:
                    # Show an error message if the data includes non-numeric values
                    messagebox.showerror("Error", "Invalid input. Please enter numbers separated by commas.")
                    return

                # Create the histogram with the provided data
                # Use default 10 bins and specify the color as green
                ax.hist(data_values, bins=10, color="green")

                # Optional: Add axis labels and a title for better understanding
                ax.set_xlabel("Values")  # Label for the x-axis
                ax.set_ylabel("Frequency")  # Label for the y-axis
                ax.set_title("Histogram")  # Title for the plot

                # Optional: Customize the x-axis ticks to show the range of values
                ax.set_xticks(range(int(min(data_values)), int(max(data_values)) + 1, 1))  # Adjust tick spacing

                # Optional: Show grid for better readability
                ax.grid(True)

            
            elif graph_type == "Area Graph":
                # Get the input data from the text box, strip extra spaces and newlines, and split by commas
                area_values = area_input.get("1.0", tk.END).strip().split(',')

                # Try to convert the data into a list of floats. Handle invalid input with a try-except block.
                try:
                    area_values = [float(val) for val in area_values if val]  # Convert input to float
                except ValueError:
                # Show an error message if there are non-numeric values
                    messagebox.showerror("Error", "Invalid input. Please enter numbers separated by commas.")
                    return

                # Generate x values based on the length of the area values
                x_vals = np.linspace(0, len(area_values) - 1, len(area_values))

                # Create the area graph by filling the area under the curve with a semi-transparent color
                ax.fill_between(x_vals, area_values, color="green", alpha=0.5)  # Alpha for transparency

                # Optional: Set axis labels and a title to improve clarity
                ax.set_xlabel("Index")  # Label for the x-axis (index of the data points)
                ax.set_ylabel("Values")  # Label for the y-axis (data values)
                ax.set_title("Area Graph")  # Title for the plot

                # Optional: Show grid for better readability
                ax.grid(True)

                # Optional: Customize x-axis ticks if needed (for example, every 1 unit)
                ax.set_xticks(np.arange(0, len(area_values), step=1))  # Adjust step as needed

                # Optional: Customize y-axis ticks or limits to fit the range of the data
                ax.set_ylim(min(area_values) - 1, max(area_values) + 1)  # Adjust y-limits to give some space around data

            
            elif graph_type == "Scatter Plot":
                scatter_data = scatter_input.get("1.0", tk.END).strip().splitlines()
    
                # Ensure there's at least one coordinate pair
                if len(scatter_data) < 1:
                    messagebox.showerror("Error", "Scatter Plot requires at least one coordinate pair (e.g., 'x,y').")
                    return

                x_values = []
                y_values = []

                try:
                    # Iterate through each line in the input (each line should be a coordinate pair)
                    for pair in scatter_data:
                        # Split each line into x and y values (e.g., "2,3" -> x=2, y=3)
                        x, y = map(float, pair.split(','))  # Split each line into x and y values
                        # Append the x and y values to the respective lists
                        x_values.append(x)
                        y_values.append(y)
                except ValueError:
                    messagebox.showerror("Error", "Invalid format for Scatter Plot. Use 'x,y' format on each line.")
                    return

                # Plot the scatter plot
                ax.scatter(x_values, y_values, color="green")

            # Update the canvas to reflect the changes
            canvas.draw()
            save_button.pack()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while generating the graph: {e}")
        

    # Function to clear the graph
    def clear_graph():
        ax.clear()
        
        # Set background color and grid styling again after clearing the plot
        ax.set_facecolor('#f5fff2')
        ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
        ax.minorticks_on()
        ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)
        ax.axhline(0, color='black', linewidth=1.5)
        ax.axvline(0, color='black', linewidth=1.5)

        # Redraw the canvas
        canvas.draw()
        save_button.pack_forget()

        # Clear input fields
        equation_input.delete(0, tk.END)
        bar_input.delete("1.0", tk.END)
        pie_input.delete("1.0", tk.END)
        pictograph_input.delete("1.0", tk.END)
        scatter_input.delete("1.0", tk.END)
        hist_input.delete("1.0", tk.END)
        area_input.delete("1.0", tk.END)

    def import_data(): 
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
        if file_path:
            try:
                global imported_data

                # Variables for x and y values from file
                x_data = []
                y_data = []

                # Check file type and parse
                if file_path.endswith('.csv'):
                    with open(file_path, newline='') as csvfile:
                        reader = csv.reader(csvfile, quotechar='"')
                        for row in reader:
                            # Check if the row contains an equation
                            if len(row) == 1 and row[0].startswith("(") and row[0].endswith(")"):
                                equation = sympify(row[0].strip("()"))  # Parse equation
                                x_data = list(range(0, 11))  # Default x range
                                y_data = [float(equation.subs(x, val)) for val in x_data]  # Evaluate y
                                plot_data(x_data, y_data)
                                return
                            elif len(row) == 1 and ',' in row[0]:  # Check for "x,y" format
                                x_val, y_val = map(float, row[0].split(","))
                                x_data.append(x_val)
                                y_data.append(y_val)
                            elif len(row) == 2:  # Two-column CSV
                                x_data.append(float(row[0]))
                                y_data.append(float(row[1]))
                            else:
                                messagebox.showerror("Error", "Data is not in expected 'x,y' or equation format.")
                                return

                    # If data points are detected, plot them
                    if x_data and y_data:
                        plot_data(x_data, y_data)

                elif file_path.endswith('.xlsx'):
                    # Use pandas to handle Excel files
                    data = pd.read_excel(file_path, header=None, engine='openpyxl')
                    if len(data.columns) == 1:  # Single-column file (possible equations)
                        equations = data.iloc[:, 0].tolist()
                        for eq in equations:
                            if isinstance(eq, str) and eq.startswith("(") and eq.endswith(")"):
                                equation = sympify(eq.strip("()"))
                                x_data = list(range(0, 11))  # Default x range
                                y_data = [float(equation.subs(x, val)) for val in x_data]
                                plot_data(x_data, y_data)
                                return
                        messagebox.showerror("Error", "No valid equations detected in the file.")
                    elif len(data.columns) == 2:  # Two-column file (x and y values)
                        x_data = data.iloc[:, 0].astype(float).tolist()
                        y_data = data.iloc[:, 1].astype(float).tolist()
                        plot_data(x_data, y_data)
                    else:
                        messagebox.showerror("Error", "Data format in file is not recognized.")
                        return

                else:
                    messagebox.showerror("Error", "Unsupported file type.")
                    return
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import and plot data: '{e}'")

    #####################################################################
    # Function to plot data from file
    #####################################################################

    def plot_data(x_data, y_data):
        # Clear canvas
        ax.clear()
        save_button.pack_forget()
        # Plot the data if it contains any points
        if x_data and y_data:
            ax.plot(x_data, y_data, marker='o', linestyle='-', color="green")
            
            # Set axis limits dynamically based on data range with buffer
            ax.set_xlim([min(min(x_data), 0), max(max(x_data), 10)])
            ax.set_ylim([min(min(y_data), 0), max(max(y_data), 10)])
            
            # Set background color of the graph to a faded green
            ax.set_facecolor('#e0f7da')
            # Add a grid with major and minor lines to resemble graph paper
            ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
            # Set minor ticks
            ax.minorticks_on()
            # Customize minor grid lines (finer)
            ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)
            # Draw darker x and y axis lines
            ax.axhline(0, color='black', linewidth=1.5)  # Darker x-axis
            ax.axvline(0, color='black', linewidth=1.5)  # Darker y-axis

            # Draw canvas
            canvas.draw()
            save_button.pack()

        else:
            messagebox.showerror("Error", "No valid data to plot.")

    #####################################################################
    # Function to save the graph with user defined name
    #####################################################################
    def save_graph():
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            
            if file_path: 
                try:
                    fig.savefig(file_path)
                    messagebox.showinfo("Success", f"Graph saved as '{file_path}'")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save graph: {e}")
    
    # Control buttons
    plot_button = tk.Button(control_frame, text="Generate Graph", command=plot_graph, bg="#006400", fg="white")
    plot_button.pack(pady=5, fill=tk.X)

    save_button = tk.Button(control_frame, text="Save Graph", command=save_graph, bg="#006400", fg="white")
    #save_button.pack(pady=5, fill=tk.X)

    import_button = tk.Button(control_frame, text="Import Data", command=import_data, bg="#006400", fg="white")
    import_button.pack(pady=5, fill=tk.X)
    
    clear_button = tk.Button(control_frame, text="Clear Graph", command=clear_graph, bg="#006400", fg="white")
    clear_button.pack(pady=5, fill=tk.X)

    # Initialize data
    imported_data = None

    # Create a canvas for the graph
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=1, sticky="nsew")

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
