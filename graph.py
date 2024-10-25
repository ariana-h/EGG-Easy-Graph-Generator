import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

# Function to update the graph based on user input and selected graph type
def plot_graph():
    equation = equation_input.get()
    graph_type = graph_type_combo.get()

    try:
        x = np.linspace(-10, 10, 400)
        y = eval(equation)
        
        ax.clear()

        if graph_type == "Line Plot":
            ax.plot(x, y, label=equation, color="green")
            ax.legend()
        elif graph_type == "Bar Graph":
            ax.bar(x[:10], y[:10], color="green")  # Plot only 10 bars for visibility
        elif graph_type == "Pie Chart":
            values = np.abs(y[:5])  # Use absolute values for pie chart and limit to 5 slices
            labels = [f"{equation[:10]} {i}" for i in range(5)]
            ax.pie(values, labels=labels, autopct='%1.1f%%')

        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid equation or selection: {e}")

# Function to clear the graph
def clear_graph():
    ax.clear()
    canvas.draw()
    equation_input.delete(0,tk.END)

# Function to save the graph
def save_graph():
    try:
        fig.savefig("graph.png")
        messagebox.showinfo("Success", "Graph saved as 'graph.png'")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save graph: {e}")

# Create the main window
root = tk.Tk()
root.title("egg - Easy Graph Generator")

# Set window background color to light green
root.configure(bg="#d0f0c0")

# Create frame for input elements on the left
left_frame = tk.Frame(root, bg="#d0f0c0")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

# Create figure for plotting
fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)

# Create a canvas to hold the graph on the right
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

image = tk.PhotoImage(file="EGG.png")

# Display logo above the equation label
image_label = tk.Label(left_frame, image=image, bg="#d0f0c0")
image_label.pack(pady=5)

# Label for the equation input
equation_label = tk.Label(left_frame, text="Enter Equation:", bg="#d0f0c0", font=("Helvetica", 12, "bold"))
equation_label.pack(pady=5)

# Textbox for user to input
equation_input = tk.Entry(left_frame, width=30)
equation_input.pack(pady=5)

# Dropdown menu to selecting graph type
graph_type_label = tk.Label(left_frame, text="Select Graph Type:", bg="#d0f0c0", font=("Helvetica", 12, "bold"))
graph_type_label.pack(pady=5)

graph_type_combo = tk.StringVar(value="Line Plot")
graph_type_menu = tk.OptionMenu(left_frame, graph_type_combo, "Line Plot", "Bar Graph", "Pie Chart")
graph_type_menu.pack(pady=5)

# Create buttons with tk.Button to change bg color
plot_button = tk.Button(left_frame, text="Plot", command=plot_graph, bg="#006400", fg="white")
plot_button.pack(pady=10, fill=tk.X)

clear_button = tk.Button(left_frame, text="Clear", command=clear_graph, bg="#006400", fg="white")
clear_button.pack(pady=10, fill=tk.X)

save_button = tk.Button(left_frame, text="Save Graph", command=save_graph, bg="#006400", fg="white")
save_button.pack(pady=10, fill=tk.X)

# Main loop to display window
root.mainloop()
