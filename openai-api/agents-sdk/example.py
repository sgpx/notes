import dotenv
dotenv.load_dotenv(override=True)

import asyncio
import subprocess
from agents import Agent, Runner, function_tool, ModelSettings

# 1. Define the custom CLI search tool
@function_tool
def ai_search_tool(term: str) -> str:
    """
    Search the web for information by invoking the local runownagent.sh CLI tool.
    Call this whenever you need up-to-date facts, news, or external data.
    """
    try:
        # Execute the shell script and pass the search term as an argument
        result = subprocess.run(
            ["runownagent.sh", term], 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Search failed with error: {e.stderr.strip()}"
    except Exception as e:
        return f"Could not execute script: {str(e)}"

# 2. Define the Orchestrator Agent
problem_solver_agent = Agent(
    name="Problem Solver", model="gpt-5.4-mini",
    instructions=(
        "You are a strategic problem-solving assistant. When given a complex task:\n"
        "1. Break the main problem down into smaller, logical subproblems.\n"
        "2. Tackle each subproblem step-by-step.\n"
        "3. If you lack information for any subproblem, use the ai_search_tool to search the web.\n"
        "4. Synthesize the gathered data and intermediate solutions into a comprehensive final answer."
    ),
    model_settings=ModelSettings(parallel_tool_calls=False),
    tools=[ai_search_tool]
)

# 3. Run the Agent Loop
async def main():
    user_prompt = open("input.txt", "r").read()
    print(f"Task: {user_prompt}\n")
    
    # The Runner manages the loop. It will break the problem down, 
    # execute ai_search_tool multiple times as needed, and return the synthesized answer.
    result = await Runner.run(problem_solver_agent, user_prompt)
    #print(dir(result))    
    # Print tool errors and execution details
    print(result.new_items)
    print(f"Final Response:\n{result.final_output}")

if __name__ == "__main__":
    # Ensure runownagent.sh is executable (chmod +x) and in the same directory
    asyncio.run(main())
