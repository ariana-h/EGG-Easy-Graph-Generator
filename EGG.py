import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from PIL import Image, ImageTk

# Function to update the graph based on user input and selected graph type
def plot_graph():
    equation = equation_input.get()
    graph_type = graph_type_combo.get()

    try:
        x = np.linspace(-10, 10, 400)
        y = eval(equation)

        ax.clear()

        # Set background color of the graph to a faded green
        ax.set_facecolor('#e0f7da')  # Light faded green

        # Add a grid with major and minor lines to resemble graph paper
        ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)

        # Set minor ticks
        ax.minorticks_on()

        # Customize minor grid lines (finer)
        ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)

        if graph_type == "Line Plot":
            ax.plot(x, y, label=equation, color="green")
            ax.legend()
        elif graph_type == "Bar Graph":
            ax.bar(x[:10], y[:10], color="green")
        elif graph_type == "Pie Chart":
            values = np.abs(y[:5])
            labels = [f"{equation[:10]} {i}" for i in range(5)]
            ax.pie(values, labels=labels, autopct='%1.1f%%')
        elif graph_type == "Pictograph":
            symbols = ['🍏'] * 10
            y_scaled = [int(val) for val in (y[:10] / max(y[:10]) * 5)]  # Scale y values
            for i, val in enumerate(y_scaled):
                ax.text(i, 0.5, symbols[i] * val, fontsize=15)
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
        elif graph_type == "Histogram":
            ax.hist(y, bins=30, color="green")
        elif graph_type == "Area Graph":
            ax.fill_between(x, y, color="green", alpha=0.5)
        elif graph_type == "Scatter Plot":
            ax.scatter(x[:50], y[:50], color="green")

        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid equation or selection: {e}")

# Function to clear the graph
def clear_graph():
    ax.clear()
    canvas.draw()
    equation_input.delete(0, tk.END)

# Function to save the graph with user defined name
def save_graph():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        try:
            fig.savefig(file_path)
            messagebox.showinfo("Success", f"Graph saved as '{file_path}'")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save graph: {e}")

# Function to resize logo based on window size
def resize_logo(event):
    new_width = event.width // 8  # Adjust size based on window width
    new_height = event.height // 8  # Adjust size based on window height
    resized_logo = original_logo.resize((new_width, new_height), Image.ANTIALIAS)
    logo_image = ImageTk.PhotoImage(resized_logo)
    logo_label.config(image=logo_image)
    logo_label.image = logo_image  # Keep a reference to prevent garbage collection

# Function to clear the placeholder when the user clicks the entry box
def on_entry_click(event):
    if equation_input.get() == "Click to add new equation":
        equation_input.delete(0, tk.END)  # Clear the placeholder
        equation_input.config(fg="black")  # Change text color to black

# Function to add the placeholder back if the entry box is left empty
def on_focusout(event):
    if equation_input.get() == "":
        equation_input.insert(0, "Click to add new equation")  # Restore placeholder
        equation_input.config(fg="grey")  # Set the placeholder text color to grey

# Main function encapsulating all the GUI code
def main():
    global equation_input, graph_type_combo, ax, canvas, original_logo, logo_label, root, fig

    # Create the main window
    root = tk.Tk()
    root.title("Easy Graph Generator")
    root.geometry("800x500")
    root.configure(bg="#d0f0c0")  # Light green background

    # Set the window to be resizable
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Create a frame for the controls on the left
    control_frame = tk.Frame(root, bg="#d0f0c0")
    control_frame.grid(row=0, column=0, sticky="ns")

    # Create figure for plotting
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Set the initial pale green background and gridlines
    ax.set_facecolor('#f5fff2')  # Pale green background
    ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)  # Major grid
    ax.minorticks_on()
    ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)  # Minor grid

    # Create a canvas to hold the graph on the right
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")

    # Load and resize the logo
    original_logo = Image.open('EGG.png')
    logo_image = ImageTk.PhotoImage(original_logo.resize((100, 100)))  # Set initial size

    # Display the resizable logo above the equation prompt
    logo_label = tk.Label(control_frame, image=logo_image, bg="#d0f0c0")
    logo_label.pack(pady=5)

    # Textbox for user input equation with placeholder
    equation_input = tk.Entry(control_frame, width=30)
    equation_input.insert(0, "Click to add new equation")  # Placeholder text
    equation_input.config(fg="grey")  # Set the placeholder text color to grey
    equation_input.pack(pady=5)

    # Bind the focus-in and focus-out events to the equation input box
    equation_input.bind("<FocusIn>", on_entry_click)
    equation_input.bind("<FocusOut>", on_focusout)

    # Dropdown menu for selecting graph type with prompt
    graph_type_combo = ttk.Combobox(control_frame, values=["Line Plot", "Bar Graph", "Pie Chart", "Pictograph", "Histogram", "Area Graph", "Scatter Plot"], state="readonly")
    graph_type_combo.set("Choose a graph")  # Default prompt
    graph_type_combo.pack(pady=5)

    # Buttons for options
    plot_button = tk.Button(control_frame, text="Add Point", command=plot_graph, bg="#006400", fg="white")
    plot_button.pack(pady=5, fill=tk.X)

    generate_button = tk.Button(control_frame, text="Generate Graph", command=plot_graph, bg="#006400", fg="white")
    generate_button.pack(pady=5, fill=tk.X)

    remove_button = tk.Button(control_frame, text="Remove Point", command=clear_graph, bg="#006400", fg="white")
    remove_button.pack(pady=5, fill=tk.X)

    import_button = tk.Button(control_frame, text="Import Data", command=lambda: messagebox.showinfo("Import", "Import Data clicked"), bg="#006400", fg="white")
    import_button.pack(pady=5, fill=tk.X)

    save_button = tk.Button(control_frame, text="Save Graph", command=save_graph, bg="#006400", fg="white")
    save_button.pack(pady=5, fill=tk.X)

    # Configure root window to be resizable
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)

    # Bind window resizing event to the logo resizing function
    root.bind('<Configure>', resize_logo)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
