import tkinter as tk

def draw_circle():
    canvas.create_oval(50, 50, 150, 150, fill="red")

def draw_rectangle():
    canvas.create_rectangle(200, 50, 300, 150, fill="blue")

def draw_triangle():
    canvas.create_polygon(400, 50, 450, 150, 350, 150, fill="green")

# Create the main window
root = tk.Tk()
root.title("Graphic Models using Tkinter")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=500, height=200)
canvas.pack()

# Create buttons to draw different shapes
circle_button = tk.Button(root, text="Draw Circle", command=draw_circle)
circle_button.pack(side=tk.LEFT, padx=10)

rectangle_button = tk.Button(root, text="Draw Rectangle", command=draw_rectangle)
rectangle_button.pack(side=tk.LEFT, padx=10)

triangle_button = tk.Button(root, text="Draw Triangle", command=draw_triangle)
triangle_button.pack(side=tk.LEFT, padx=10)

# Run the main event loop
root.mainloop()
