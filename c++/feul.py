def calculate_results(fuel):
    velocity = 2.21 * (fuel ** 0.6)
    duration = 10 * (fuel ** 0.3) / velocity
    fuel_cost = 10_000
    losses = 109_292_277.99
    value_lost = fuel_cost + losses

    return velocity, duration, fuel_cost, losses, value_lost

def print_csv_format(fuel, velocity, duration, fuel_cost, losses, value_lost):
    print("Fuel, Velocity, Duration, Fuel cost, Losses, Value lost")
    print(f"{fuel},{velocity},{duration},{fuel_cost},{losses},{value_lost}")

def print_human_readable_format(fuel, velocity, duration, fuel_cost, losses, value_lost):
    fuel_label = "Fuel"
    velocity_label = "Velocity"
    duration_label = "Duration"
    fuel_cost_label = "Fuel cost"
    losses_label = "Losses"
    value_lost_label = "Value lost"

    print(f"{fuel_label:<10}{fuel:>12,.2f} kg")
    print(f"{velocity_label:<10}{velocity:>12,.2f} m/s")
    print(f"{duration_label:<10}{duration:>12,.1f} days")
    print(f"{fuel_cost_label:<10}{fuel_cost:>12,.2f} USD")
    print(f"{losses_label:<10}{losses:>12,.2f} USD")
    print(f"{value_lost_label:<10}{value_lost:>12,.2f} USD")

def main():
    fuel = int(input("Enter value for fuel in kilograms [0-100,000kg]: "))

    print("How would you like to format the output?")
    print("1: CSV")
    print("2: Human-readable")
    choice = input("Enter 1 or 2: ")

    velocity, duration, fuel_cost, losses, value_lost = calculate_results(fuel)

    if choice == "1":
        print_csv_format(fuel, velocity, duration, fuel_cost, losses, value_lost)
    elif choice == "2":
        print_human_readable_format(fuel, velocity, duration, fuel_cost, losses, value_lost)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
