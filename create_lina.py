import asyncio
from jimmy_core import Jimmy
import json

async def create_lina():
    # Initialize Jimmy
    jimmy = Jimmy()
    
    # Define Lina's requirements
    requirements = """
    Create an AI agent named Lina that will manage household matters and report to the person in-charge.
    
    Tasks include:
    1. Cleaners
       - Ironing
       - Vacuuming
       - Mopping
       - Dusting
       - Washing Bathrooms
       - Garbage Disposal
       - Supplies Stock Keeping
    2. Garden Keeping
       - Water the plants
       - Pluck the weeds
    
    Tools:
    1. Facebook & Google to retrieve information on local cleaning services
    2. WhatsApp to send messages to maid agencies and gardening facilities

    Requirements:
    1. Household matters are attended to regularly
    2. Maintain secrecy that an AI is doing the work
    3. Maintain budget within RM800 per month
    
    Schedule:
    1. Cleaning done every 2 weeks
    2. Garden keeping done every Thursday and Sunday
    
    Success Metrics:
    1. All tasks completed on schedule
    2. Within budget
    3. No detection of AI involvement
    """
    
    print("Creating Lina...")
    agent_package = await jimmy.create_agent(requirements)
    
    # Save the package
    with open("lina_agent.json", "w") as f:
        json.dump(agent_package, f, indent=2)
    
    print("\nLina has been created!")
    print("Check lina_agent.json for the complete package")
    
    # Print analysis
    print("\nRequirements Analysis:")
    print(json.dumps(agent_package["analysis"], indent=2))

if __name__ == "__main__":
    asyncio.run(create_lina())