

print("=== DECODELABS EXPENSE TRACKER ACTIVATED ===")
print("Instructions: Enter expense amounts one by one. Type 'quit' to halt and display the final total.\n")


total = 0 


while True:
   
    user_input = input("Enter expense amount (or 'quit'): ").strip()
    
   
    if user_input.lower() == 'quit':
        print("\n[ALERT] Execution halted via sentinel switch.")
        break
        
   
    try:
        
        new_expense = float(user_input)
        
        
        total += new_expense
        print(f"Current Total Spent: ${total:.2f}")
        
    except ValueError:
        
        print("[WARNING] Invalid Data Detected! Please enter a valid number or 'quit'.")


print("-" * 44)
print(f"FINAL TOTAL SPENT: ${total:.2f}")
print("============================================")