def calculate_knowledge_levels(total_points):
    # Initialize constants
    initial_points = 10
    knowledge_increase_per_unit = 1
    points_increase_factor = 0.5

    # Calculate the difference in points
    points_difference = total_points - initial_points

    # Calculate the number of knowledge levels completed
    knowledge_levels_completed = points_difference / (initial_points * points_increase_factor)

    return int(knowledge_levels_completed)

def main():
    try:
        # Get the total points from the user
        total_points = float(input("Enter the total points of the programmer: "))

        # Calculate knowledge levels completed
        knowledge_levels = calculate_knowledge_levels(total_points)

        print(f"The programmer has completed {knowledge_levels} knowledge level(s).")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for total points.")

if __name__ == "__main__":
    main()
