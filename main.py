import numpy as np
import tkinter as tk
from tkinter import messagebox
import joblib
from PIL import ImageTk, Image

model = joblib.load('C:/Users/Admin/Desktop/MIASD/S2/Machine learning/model.pkl')
def predict():
    values = [float(entry.get()) for entry in entries]
    values = np.array(values).reshape(1, -1)
    prediction=model.predict(values)
    if prediction[0] == 0:
        messagebox.showinfo("Prediction", f"Le tumeur est BENINE")
    else :
        messagebox.showinfo("Prediction", f"Le tumeur est MALINE")


# Create the main window
root = tk.Tk()
root.title("Machine Learning Model Predictor")



#background_image = Image.open("image.jpeg")
#background_photo = ImageTk.PhotoImage(background_image)
#background_label = tk.Label(root, image=background_photo)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Labels for input fields
labels = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
          'mean smoothness', 'mean compactness', 'mean concavity',
          'mean concave points', 'mean symmetry', 'mean fractal dimension',
          'radius error', 'texture error', 'perimeter error', 'area error',
          'smoothness error', 'compactness error', 'concavity error',
          'concave points error', 'symmetry error',
          'fractal dimension error', 'worst radius', 'worst texture',
          'worst perimeter', 'worst area', 'worst smoothness',
          'worst compactness', 'worst concavity', 'worst concave points',
          'worst symmetry', 'worst fractal dimension']

num_entries = len(labels)
num_columns = 3
entries = []
for i, label in enumerate(labels):
    col = i % num_columns
    row = i // num_columns
    frame = tk.Frame(root)
    frame.grid(row=row, column=col, padx=5, pady=5)
    label_widget = tk.Label(frame, width=20, text=label, anchor='w')
    label_widget.grid(row=0, column=0)
    entry = tk.Entry(frame)
    entry.grid(row=0, column=1)
    entries.append(entry)



# Prediction button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=4,column=4, padx=5, pady=10)

# Run the application
root.mainloop()
