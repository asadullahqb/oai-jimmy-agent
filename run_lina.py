
import json
from datetime import datetime

def load_lina():
    # Load the agent package
    with open('lina_agent.json', 'r') as f:
        package = json.load(f)
    
    # Execute the agent code in a safe context
    exec(package['agent_code'], globals())
    
    # Create an instance of the agent
    return LinaAgent()

def main():
    # Load and initialize Lina
    print("Initializing Lina...")
    lina = load_lina()
    
    while True:
        print("
Lina Household Management System")
        print("================================")
        print("1. View current status")
        print("2. Schedule a task")
        print("3. Track expense")
        print("4. View upcoming schedule")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            status = lina.get_status()
            print("\nCurrent Status:")
            print(f"Budget Remaining: RM{status['budget_remaining']}")
            print("\nTasks:")
            for task, details in status['tasks'].items():
                print(f"\n{task.title()}:")
                print(f"Schedule: {details['schedule']}")
                print("Subtasks:", ", ".join(details['subtasks']))
                
        elif choice == '2':
            print("\nAvailable tasks:")
            print("1. Cleaning")
            print("2. Gardening")
            task_choice = input("Choose task (1-2): ")
            
            if task_choice == '1':
                task_type = 'cleaning'
            elif task_choice == '2':
                task_type = 'gardening'
            else:
                print("Invalid choice")
                continue
                
            date = input("Enter date (YYYY-MM-DD): ")
            result = lina.schedule_task(task_type, date)
            print(f"\nResult: {result}")
            
        elif choice == '3':
            amount = float(input("\nEnter expense amount (RM): "))
            if lina.track_expense(amount):
                print("Expense tracked successfully")
            else:
                print("Warning: This would exceed the budget!")
                
        elif choice == '4':
            status = lina.get_status()
            print("\nUpcoming Schedule:")
            for task in status['scheduled_tasks']:
                print(f"{task['type'].title()}: {task['date']} ({task['status']})")
                
        elif choice == '5':
            print("\nThank you for using Lina!")
            break
            
        else:
            print("\nInvalid choice, please try again")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
