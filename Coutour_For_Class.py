import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def generate_contour (roll):
    squares_per_side = 5  
    square_size_cm = 10
    total_grid_cm = squares_per_side * square_size_cm
    cm_to_inch = 1 / 2.54
    grid_size_inch = total_grid_cm * cm_to_inch
    
    # Create figure with exact dimensions
    fig = plt.figure(figsize=(grid_size_inch, grid_size_inch), facecolor='white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, total_grid_cm)
    ax.set_ylim(0, total_grid_cm)
    ax.set_aspect('equal')
    ax.axis('off')  
    
    # Drawing 5×5 grid of squares
    
    for x in range(0, total_grid_cm, square_size_cm):
        for y in range(0, total_grid_cm, square_size_cm):
            rect = Rectangle((x, y), square_size_cm, square_size_cm, edgecolor='black', facecolor='none', linewidth=2)
            ax.add_patch(rect)
    
    # RL Values (6x6 array for 5x5 grid corners
    
    Z_real_5x5 = [
        [849.20, 854.60, 859.30, 862.20, 863.30, 862.80],
        [848.50, 854.00, 858.40, 858.70, 858.10, 857.90],
        [847.63, 859.50, 858.00, 855.30, 851.10, 849.55],
        [848.47, 854.30, 856.70, 854.50, 848.70, 838.30],
        [847.62, 852.00, 854.30, 853.20, 848.70, 839.31],
        [843.95, 848.00, 848.51, 848.42, 847.30, 842.26], 
    ]
    
    Z_arr = np.array(Z_real_5x5) + roll
    
    # Annotate each square with RL values
    
    offset = 0.5  # cm
    for i in range(squares_per_side+1):  
        for j in range(squares_per_side+1):
            x_begin = j * square_size_cm
            y_begin = total_grid_cm - i * square_size_cm  
            ax.text(x_begin + offset, y_begin - offset, f'{Z_arr[i, j]:.2f}', color='black', fontsize=8, verticalalignment='top', horizontalalignment='left')
    
    
    # Preparing coordinates and RL array for contouring
    x_padded = np.arange(0, total_grid_cm + square_size_cm, square_size_cm)  
    y_padded = np.arange(total_grid_cm, -square_size_cm, -square_size_cm)       
    RL_padded = Z_arr.copy()  # Directly use the 6x6 RL data
    
    X_pad, Y_pad = np.meshgrid(x_padded, y_padded)
    
    Lowest_Rl = np.ceil(RL_padded.min() / 2.5) * 2.5
    levels = np.arange(Lowest_Rl, RL_padded.max() + 2.5, 2.5)
    levels_new = np.arange(Lowest_Rl, RL_padded.max() + 0.5, 0.5)
    
    contour_lines_index = ax.contour(X_pad, Y_pad, RL_padded, levels=levels,
                           colors='red', linewidths=4.5)
    contour_lines = ax.contour(X_pad, Y_pad, RL_padded, levels=levels_new,
                           colors='blue', linewidths=0.5)
    
    ax.clabel(contour_lines_index, inline=True, fontsize=12, fmt="%.1f")
    ax.clabel(contour_lines, inline=True, fontsize=7, fmt="%.1f")
    
    ax.text(total_grid_cm / 2, 7, f"Contour Map for roll number: {roll} and your min. RL is {Lowest_Rl}",
        fontsize=12, ha='center', va='top', fontweight='bold')
    
    plt.savefig(f'C:\\Users\\ACER\\Desktop\\contour\\For Class\\grid_contour_new_final_fitted_079BCE{roll}.pdf', bbox_inches='tight', pad_inches=0, dpi=300)


generate_contour(157)

#for i in range (98, 145):
#    generate_contour(i)
#    print(f"generated for roll number {i}")

#print("")
#print("generated for all")