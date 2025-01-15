import turtle

# Recursive function to draw the tree
def draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth <= 0 or branch_length <=0:
        return

        # Set color for branches
    if depth == original_depth:
        turtle.color("red")  # Main branches
    else:
        turtle.color("green")  # Leaves at the end branches

    # Draw the current branch
    turtle.pensize(depth)
    turtle.forward(branch_length)

    # Draw the left branch
    turtle.left(left_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.right(left_angle)  # Return to the main branch

    # Draw the right branch
    turtle.right(right_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.left(right_angle)  # Return to the main branch

    # Retrace to the parent branch
    turtle.backward(branch_length)

# Main program
def main():
    # Get parameters from the user
    left_angle = int(input("Enter the left branch angle (in degrees): "))
    right_angle = int(input("Enter the right branch angle (in degrees): "))
    starting_length = int(input("Enter the starting branch length (in pixels): "))
    depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7 for 70%): "))
    global original_depth  # To track the depth of the main branch
    original_depth = depth

    # Setup turtle
    turtle.penup()
    turtle.goto(0, -200)  # Start at the bottom center of the screen
    turtle.left(90)
    turtle.pendown()
    turtle.speed(150)

    # Draw the tree
    draw_tree(starting_length, left_angle, right_angle, depth, reduction_factor)

    # Finish
    turtle.done()
# Run the program
if __name__ == "__main__":
    main()