import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from sympy import sympify, symbols
from PIL import Image, ImageTk

# Global variable for the symbol used in equations
x = symbols('x')  # Define 'x' as a symbol for sympy to recognize it in equations

# Function to safely parse and evaluate equations using sympy
def parse_equation(equation_str):
    try:
        equation_str = equation_str.replace('^', '**').replace(' ', '')  # Preprocess the equation
        processed_str = ''
        for i, char in enumerate(equation_str):
            if i > 0 and char.isalpha() and equation_str[i-1].isdigit():
                processed_str += '*' + char  # Insert '*' for implicit multiplication
            elif i > 0 and char.isdigit() and equation_str[i-1].isalpha():
                processed_str += '*' + char  # Insert '*' for implicit multiplication
            else:
                processed_str += char

        expression = sympify(processed_str)
        return lambda val: float(expression.subs(x, val))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid equation format: {e}")
        return None

# Function to update the graph based on user input and selected graph type
def plot_graph():
    equation_str = equation_input.get()
    graph_type = graph_type_combo.get()

    equation_func = parse_equation(equation_str)
    if not equation_func:
        return

    try:
        x_vals = np.linspace(-10, 10, 400)
        y_vals = [equation_func(val) for val in x_vals]

        ax.clear()
        
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

        if graph_type == "Line Plot":
            ax.plot(x_vals, y_vals, label=equation_str, color="green")
            ax.legend()
        elif graph_type == "Bar Graph":
            # Get data from the bar graph input
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
            data_pairs = pictograph_input.get("1.0", tk.END).strip().splitlines()
            categories = []
            for pair in data_pairs:
                try:
                    category, count = pair.split(',')
                    categories.extend([category.strip()] * int(count.strip()))  # Repeat category based on count
                except ValueError:
                    messagebox.showerror("Error", "Invalid format for Pictograph. Use 'Category, Count' format.")
                    return
            ax.text(0.5, 0.5, ', '.join(categories), fontsize=15, ha='center')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
        elif graph_type == "Histogram":
            data_values = hist_input.get("1.0", tk.END).strip().split(',')
            data_values = [float(val) for val in data_values if val]  # Convert input to float
            ax.hist(data_values, bins=10, color="green")  # Default 10 bins, adjust as necessary
        elif graph_type == "Area Graph":
            area_values = area_input.get("1.0", tk.END).strip().split(',')
            area_values = [float(val) for val in area_values if val]  # Convert input to float
            ax.fill_between(x_vals, area_values, color="green", alpha=0.5)
        elif graph_type == "Scatter Plot":
            x_values = scatter_input.get("1.0", tk.END).strip().splitlines()[0].split(',')
            y_values = scatter_input.get("1.0", tk.END).strip().splitlines()[1].split(',')
            x_values = [float(val) for val in x_values if val]  # Convert input to float
            y_values = [float(val) for val in y_values if val]  # Convert input to float
            ax.scatter(x_values, y_values, color="green")


        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid equation or selection: {e}")

# Function to clear the graph
def clear_graph():
    ax.clear()
    canvas.draw()
    equation_input.delete(0, tk.END)
    bar_input.delete("1.0", tk.END)
    pie_input.delete("1.0", tk.END)
    pictograph_input.delete("1.0", tk.END)
    
# Function to save the graph with user defined name
def save_graph():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        try:
            fig.savefig(file_path)
            messagebox.showinfo("Success", f"Graph saved as '{file_path}'")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save graph: {e}")


# Function to import data from CSV or Excel
def import_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
    if file_path:
        try:
            global imported_data
            if file_path.endswith('.csv'):
                imported_data = pd.read_csv(file_path)
            else:
                imported_data = pd.read_excel(file_path)
            messagebox.showinfo("Data Imported", "Data imported successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

# Function to customize the graph
# def customize_graph():
    # title = title_input.get()
    # x_label = x_label_input.get()
    # y_label = y_label_input.get()

    # ax.set_title(title)
    # ax.set_xlabel(x_label)
    # ax.set_ylabel(y_label)
    # canvas.draw()

# Function to resize logo based on window size
def resize_logo(event):
    new_width = event.width // 8  # Adjust size based on window width
    new_height = event.height // 8  # Adjust size based on window height
    resized_logo = original_logo.resize((new_width, new_height), Image.ANTIALIAS)
    logo_image = ImageTk.PhotoImage(resized_logo)
    logo_label.config(image=logo_image)
    logo_label.image = logo_image  # Keep a reference to prevent garbage collection

# Function to show/hide input fields based on selected graph type
def update_input_fields(event):
    graph_type = graph_type_combo.get()
    bar_input.pack_forget()
    pie_input.pack_forget()
    pictograph_input.pack_forget()
    hist_input.pack_forget()
    area_input.pack_forget()
    scatter_input.pack_forget()

    if graph_type == "Bar Graph":
        bar_input.pack(pady=5)
    elif graph_type == "Pie Chart":
        pie_input.pack(pady=5)
    elif graph_type == "Pictograph":
        pictograph_input.pack(pady=5)
    elif graph_type == "Histogram":
        hist_input.pack(pady=5)
    elif graph_type == "Area Graph":
        area_input.pack(pady=5)
    elif graph_type == "Scatter Plot":
        scatter_input.pack(pady=5)


# Function to clear the placeholder when the user clicks the entry box
def on_entry_click(event):
    if equation_input.get() == "Click to add new equation (e.g., 2*x^2 + 3*x - 5)":
        equation_input.delete(0, tk.END)  # Clear the placeholder
        equation_input.config(fg="black")  # Change text color to black

# Function to add the placeholder back if the entry box is left empty
def on_focusout(event):
    if equation_input.get() == "":
        equation_input.insert(0, "Click to add new equation (e.g., 2*x^2 + 3*x - 5)")  # Restore placeholder
        equation_input.config(fg="grey")  # Set the placeholder text color to grey

# Main function encapsulating all the GUI code
def main():
    global equation_input, graph_type_combo, ax, canvas, original_logo, logo_label
    # global title_input, x_label_input, y_label_input, 
    global imported_data, fig
    global bar_input, pie_input, pictograph_input, hist_input, area_input, scatter_input

    # Create the main window
    root = tk.Tk()
    root.title("Easy Graph Generator")
    root.geometry("900x600")  # Original size
    root.configure(bg="#d0f0c0")

    # Set the window to be resizable
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Create a frame for the controls on the left
    control_frame = tk.Frame(root, bg="#d0f0c0")
    control_frame.grid(row=0, column=0, sticky="ns")

    # Create figure for plotting
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_facecolor('#f5fff2')
    ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
    ax.minorticks_on()
    ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)

    # Load and resize the logo
    original_logo = Image.open('EGG.png')
    logo_image = ImageTk.PhotoImage(original_logo.resize((100, 100)))
    logo_label = tk.Label(control_frame, image=logo_image, bg="#d0f0c0")
    logo_label.pack(pady=5)
    
    # Graph type selection
    graph_type_label = tk.Label(control_frame, text="Select Graph Type", bg="#d0f0c0")
    graph_type_label.pack(pady=5)
    
    # Dropdown menu for selecting graph type with prompt
    graph_type_combo = ttk.Combobox(control_frame, values=["Line Plot", "Bar Graph", "Pie Chart", "Pictograph", "Histogram", "Area Graph", "Scatter Plot"], state="readonly", width=35)
    graph_type_combo.set("Choose a graph")  # Default prompt
    graph_type_combo.pack(pady=5)
    graph_type_combo.bind("<<ComboboxSelected>>", update_input_fields)
    
    # Bar Graph input
    bar_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    bar_input.insert("1.0", "Category, Value\nA, 5\nB, 3\nC, 8")

    # Pie Chart input
    pie_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    pie_input.insert("1.0", "Label, Value\nCategory A, 50\nCategory B, 30\nCategory C, 20")

    # Pictograph input
    pictograph_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    pictograph_input.insert("1.0", "Category, Count\nCat A, 3\nCat B, 1\nCat C, 2")
    
    # Histogram input
    hist_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    hist_input.insert("1.0", "Data values (comma separated)\n1, 2, 2, 3, 3, 3, 4, 4, 5")

    # Area Graph input
    area_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    area_input.insert("1.0", "Y values (comma separated)\n1, 2, 3, 4, 5")

    # Scatter Plot input
    scatter_input = tk.Text(control_frame, height=5, width=30, wrap=tk.WORD)
    scatter_input.insert("1.0", "X values (comma separated)\n1, 2, 3, 4, 5\nY values (comma separated)\n2, 3, 5, 1, 4")


    # Equation entry box
    equation_input = tk.Entry(control_frame, width=40)
    equation_input.insert(0, "Click to add new equation (e.g., 2*x^2 + 3*x - 5)")
    equation_input.config(fg="grey")  # Set the placeholder text color to grey
    equation_input.pack(pady=5)
    
    # Bind the focus-in and focus-out events to the equation input box
    equation_input.bind("<FocusIn>", on_entry_click)
    equation_input.bind("<FocusOut>", on_focusout)

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
    

    # Control buttons
    plot_button = tk.Button(control_frame, text="Generate Graph", command=plot_graph, bg="#006400", fg="white")
    plot_button.pack(pady=5, fill=tk.X)

    save_button = tk.Button(control_frame, text="Save Graph", command=save_graph, bg="#006400", fg="white")
    save_button.pack(pady=5, fill=tk.X)

    import_button = tk.Button(control_frame, text="Import Data", command=import_data, bg="#006400", fg="white")
    import_button.pack(pady=5, fill=tk.X)

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
