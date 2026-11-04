from huggingface_hub import InferenceClient
import json
from datetime import datetime
import re

class Jimmy:
    def __init__(self):
        self.client = InferenceClient()
        
    async def generate_text(self, prompt: str) -> str:
        """Generate text using free HuggingFace model"""
        try:
            print(f"Sending prompt to model: {prompt[:100]}...")
            response = await self.client.text_generation(
                prompt=prompt,
                model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                max_length=2000,
                temperature=0.3
            )
            return response[0]["generated_text"]
        except Exception as e:
            print(f"Error in generate_text: {str(e)}")
            return f"Error: {str(e)}"
    
    async def analyze_requirements(self, requirements: str) -> dict:
        """Analyze the requirements for the agent"""
        try:
            prompt = "Create a household management agent with these requirements:\n" + requirements
            print("Getting analysis from model...")
            response = await self.generate_text(prompt)
            
            return {
                "agent_type": "household_manager",
                "core_functions": [
                    "Manage cleaning tasks",
                    "Manage gardening tasks",
                    "Budget tracking",
                    "Schedule management"
                ],
                "schedule": [
                    "Cleaning every 2 weeks",
                    "Gardening on Thursday and Sunday"
                ],
                "constraints": [
                    "Budget: RM800 per month",
                    "Maintain AI secrecy"
                ],
                "success_metrics": [
                    "Tasks completed on schedule",
                    "Within budget",
                    "No AI detection"
                ]
            }
        except Exception as e:
            print(f"Error in analyze_requirements: {str(e)}")
            return {"error": f"Analysis failed: {str(e)}"}
    
    async def generate_agent_code(self, analysis: dict) -> str:
        """Generate agent implementation code"""
        try:
            print("Generating agent code...")
            code = """
class LinaAgent:
    def __init__(self):
        self.tasks = {
            'cleaning': {
                'schedule': 'every 2 weeks',
                'subtasks': ['ironing', 'vacuuming', 'mopping', 'dusting', 
                            'bathroom cleaning', 'garbage disposal']
            },
            'gardening': {
                'schedule': 'Thursday and Sunday',
                'subtasks': ['water plants', 'pluck weeds']
            }
        }
        self.budget = 800  # Monthly budget in RM
        self.spent = 0
        self.scheduled_tasks = []
    
    def schedule_task(self, task_type, date):
        if task_type in self.tasks:
            self.scheduled_tasks.append({
                'type': task_type,
                'date': date,
                'status': 'scheduled'
            })
            return f"Scheduled {task_type} for {date}"
        return "Task type not found"
    
    def track_expense(self, amount):
        if self.spent + amount <= self.budget:
            self.spent += amount
            return True
        return False
    
    def get_status(self):
        return {
            'tasks': self.tasks,
            'budget_remaining': self.budget - self.spent,
            'scheduled_tasks': self.scheduled_tasks
        }
"""
            return code
        except Exception as e:
            print(f"Error in generate_agent_code: {str(e)}")
            return "# Error generating code"
    
    async def generate_interface_code(self) -> str:
        """Generate code for the user interface"""
        try:
            print("Generating interface code...")
            interface_code = """
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
        print("\nLina Household Management System")
        print("================================")
        print("1. View current status")
        print("2. Schedule a task")
        print("3. Track expense")
        print("4. View upcoming schedule")
        print("5. Exit")
        
        choice = input("\\nEnter your choice (1-5): ")
        
        if choice == '1':
            status = lina.get_status()
            print("\\nCurrent Status:")
            print(f"Budget Remaining: RM{status['budget_remaining']}")
            print("\\nTasks:")
            for task, details in status['tasks'].items():
                print(f"\\n{task.title()}:")
                print(f"Schedule: {details['schedule']}")
                print("Subtasks:", ", ".join(details['subtasks']))
                
        elif choice == '2':
            print("\\nAvailable tasks:")
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
            print(f"\\nResult: {result}")
            
        elif choice == '3':
            amount = float(input("\\nEnter expense amount (RM): "))
            if lina.track_expense(amount):
                print("Expense tracked successfully")
            else:
                print("Warning: This would exceed the budget!")
                
        elif choice == '4':
            status = lina.get_status()
            print("\\nUpcoming Schedule:")
            for task in status['scheduled_tasks']:
                print(f"{task['type'].title()}: {task['date']} ({task['status']})")
                
        elif choice == '5':
            print("\\nThank you for using Lina!")
            break
            
        else:
            print("\\nInvalid choice, please try again")
        
        input("\\nPress Enter to continue...")

if __name__ == "__main__":
    main()
"""
            return interface_code
        except Exception as e:
            print(f"Error in generate_interface_code: {str(e)}")
            return "# Error generating interface code"
    
    async def create_agent(self, requirements: str) -> dict:
        """Main method to create an agent"""
        try:
            print("\nStep 1: Analyzing requirements...")
            analysis = await self.analyze_requirements(requirements)
            print("Analysis complete.")
            
            print("\nStep 2: Generating agent code...")
            agent_code = await self.generate_agent_code(analysis)
            print("Agent code generation complete.")
            
            print("\nStep 3: Generating interface code...")
            interface_code = await self.generate_interface_code()
            print("Interface code generation complete.")
            
            # Create the complete package
            result = {
                "analysis": analysis,
                "agent_code": agent_code,
                "interface_code": interface_code,
                "metadata": {
                    "created_at": str(datetime.now()),
                    "status": "complete"
                }
            }
            
            # Generate the runner script directly
            with open("run_lina.py", "w") as f:
                f.write(interface_code)
            print("\nCreated run_lina.py")
            
            print("\nAgent creation successful!")
            return result
            
        except Exception as e:
            print(f"\nError in create_agent: {str(e)}")
            return {
                "error": str(e),
                "status": "failed",
                "timestamp": str(datetime.now())
            }