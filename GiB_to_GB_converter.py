import re


def convert_size():

    while True:    
        print("\n\nStorage Size Converter (GB ↔ GiB)")
        print("1 GB = 0.931323 GiB (1024^3 bytes)")
        print("1 GiB = 1.073742 GB (2^30 bytes)\n")


        try:
            size_input = input("Enter size in either GB or GiB: ").strip().lower()
            from_unit = input("Enter unit to convert from: ").strip()
            to_unit = input("Enter unit to convert to: ").strip()

            # Check if input is a valid number (allowing decimals and optional signs)
            if not re.match(r'\d*\.?\d+$', size_input):
                raise ValueError("Invalid number format. Please enter a valid number.")

            size = float(size_input)

            if from_unit == "GB" and to_unit == "GiB":
                converted_value = size * 0.93132257461548  # Convert GB to GiB (Decimal to Binary)
            elif from_unit == "GiB" and to_unit == "GB":
                converted_value = size / 0.93132257461548  # Convert GiB to GB (Binary to Decimal)
            else:
                raise ValueError("Invalid units. Use 'GB' or 'GiB'.")

            print(f"\nResult: {converted_value:.6f} {to_unit}")

        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number and specify 'GB' or 'GiB'.")

        except KeyboardInterrupt:
            print("\nExiting due to KeyboardInterrupt...")
            break 
    
# Run the function
convert_size()
