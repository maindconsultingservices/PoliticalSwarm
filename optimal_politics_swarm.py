import os
import traceback
import json
import statistics
import matplotlib.pyplot as plt
from typing import Dict, Any
from swarm import Swarm, Agent
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load environment variables, setting default values if env vars are not set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "1024"))
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
MAX_TURNS = int(os.getenv("MAX_TURNS", "300"))

# Ensure OpenAI API key is set
if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Define the Metrics Evaluator agent's function using Chat Completion API
def evaluate_metrics(proposals: str, decisions: str, current_leaning: float, context_variables: Dict[str, Any] = None) -> str:
    """
    Evaluate the current state of the political framework using a sophisticated analysis.

    This function leverages the OpenAI Chat Completion API to analyze the proposals and decisions,
    determining the metrics and political leaning based on the content.

    Args:
    proposals (str): A string containing the current proposals.
    decisions (str): A string containing the current decisions.
    current_leaning (float): The current political leaning.
    context_variables (Dict[str, Any]): The current context variables dictionary.

    Returns:
    str: A string describing the evaluation results.
    """
    try:
        # Early return if both proposals and decisions are empty
        if not proposals.strip() and not decisions.strip():
            print("No proposals or decisions provided. Skipping framework evaluation.")
            return "No proposals or decisions provided. Skipping framework evaluation."

        print(f"\n--- Starting framework evaluation (Metrics Evaluator) ---")
        print(f"Input proposals: {proposals}")
        print(f"Input decisions: {decisions}")
        print(f"Current political leaning: {current_leaning}")
        print(f"Context type: {type(context_variables)}")

        # Use the existing context_variables if not provided
        if context_variables is None or not context_variables:
            print("Context variables not provided or empty. Using global context.")
            context_variables = current_context_variables  # Assuming global variable

        # Prepare the prompt for OpenAI Chat Completion
        prompt = f"""
You are an AI assistant tasked with evaluating a set of political proposals and decisions. Based on the provided information, determine the following metrics:

1. **Economy**: Rate the potential impact on economic growth and sustainability.
2. **Fairness**: Assess how the proposals and decisions promote fairness and protect consumer rights.
3. **Equality**: Evaluate the measures taken to ensure equal opportunities and reduce societal disparities.
4. **Technological Progress**: Analyze how the policies encourage technological innovation and oversight.

Additionally, determine the overall political leaning of the proposals and decisions on a scale from -1 to 1, where -1 is extremely left-leaning, 0 is centrist, and 1 is extremely right-leaning.

**Proposals:**
{proposals}

**Decisions:**
{decisions}

**Current Political Leaning:** {current_leaning}

**Instructions:**
- Provide a score for each metric (economy, fairness, equality, technological_progress) on a scale from 0 to 1, where 0 is the lowest impact and 1 is the highest.
- Provide the overall political leaning score.
- **Ensure that your response strictly follows the JSON format specified below. Do not include any additional text or explanations.**
- Format your response as a JSON object with the following structure:

{{
    "metrics": {{
        "economy": float,
        "fairness": float,
        "equality": float,
        "technological_progress": float
    }},
    "political_leaning": float
}}
"""

        # Call the OpenAI Chat Completion API using the client object
        completion = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are an AI assistant that evaluates political proposals and decisions."},
                {"role": "user", "content": prompt}
            ],
            temperature=OPENAI_TEMPERATURE,
            max_tokens=OPENAI_MAX_TOKENS,
            n=1,
            stop=None
        )

        # Parse the response
        response_text = completion.choices[0].message.content.strip()
        print(f"OpenAI response: {response_text}")

        # Attempt to parse JSON
        try:
            evaluation = json.loads(response_text)
            metrics = evaluation.get("metrics", {})
            new_leaning = evaluation.get("political_leaning", current_leaning)
        except json.JSONDecodeError:
            print("Failed to parse OpenAI response as JSON.")
            return "Error: Failed to parse evaluation results."

        print(f"Metrics: {metrics}")
        print(f"New political leaning: {new_leaning}")

        # Update the context_variables
        context_variables["metrics"] = metrics
        context_variables["political_leaning"] = new_leaning
        print("Context updated successfully")
        print(f"--- Framework evaluation (Metrics Evaluator) completed ---\n")

        return f"Framework evaluated. New metrics: {metrics}, New leaning: {new_leaning}"

    except Exception as e:
        print(f"An error occurred during framework evaluation: {str(e)}")
        print("Traceback:")
        traceback.print_exc()
        return "Error occurred during framework evaluation. Please check the logs for details."

def evaluate_framework(proposals: str, decisions: str, current_leaning: float, context_variables: Dict[str, Any] = None) -> str:
    """
    Evaluate the current state of the political framework and update the context_variables.

    This function delegates the evaluation to the Metrics Evaluator agent.

    Args:
    proposals (str): A string containing the current proposals.
    decisions (str): A string containing the current decisions.
    current_leaning (float): The current political leaning.
    context_variables (Dict[str, Any]): The current context variables dictionary.

    Returns:
    str: A string describing the evaluation results.
    """
    return evaluate_metrics(proposals, decisions, current_leaning, context_variables)

def create_transfer_function(agent_name):
    def transfer(context_variables=None):
        print(f"Transferring control to {agent_name}")
        return agents[agent_name]
    return transfer

agents_data = [
    {
        "name": "Director",
        "instructions": "You are the leader of this political framework development process. Your role is to guide the conversation, synthesize ideas from other agents, and make final decisions when there are conflicts or ambiguities. You have a high-level understanding of all topics but are not an expert in any specific area. Your goal is to balance the inputs from all agents to create an optimal framework that maximizes economy, fairness, equality, and technological progress. Consider the long-term effects of political leanings: left-leaning policies may favor fairness and equality but can impact economic growth and technological progress, while right-leaning policies may boost economy and technological development but at the cost of fairness and equality.",
    },
    {
        "name": "Economic Strategist",
        "instructions": "You are an expert in economic policies and strategies. Your goal is to propose and evaluate economic frameworks that can lead to sustainable growth and prosperity.",
    },
    {
        "name": "Equality Advocate",
        "instructions": "You are a passionate advocate for social equality. Your role is to ensure that proposed policies promote equal opportunities and reduce societal disparities.",
    },
    {
        "name": "Fairness Arbitrator",
        "instructions": "You are an expert in social justice and fair policy implementation. Your goal is to ensure that proposed frameworks are equitable and just for all members of society.",
    },
    {
        "name": "Political Scientist",
        "instructions": "You are a renowned political scientist with expertise in various political systems. Your role is to analyze proposed frameworks in the context of existing political theories and real-world implementations.",
    },
    {
        "name": "Futurist",
        "instructions": "You are a visionary thinker specializing in long-term societal trends. Your goal is to consider how proposed frameworks might evolve and impact society in the coming decades.",
    },
    {
        "name": "Environmental Scientist",
        "instructions": "You are an expert in environmental science and sustainability. Your role is to ensure that proposed frameworks consider environmental impacts and promote sustainable practices.",
    },
    {
        "name": "Ethicist",
        "instructions": "You are a philosopher specializing in ethics and moral philosophy. Your goal is to evaluate the ethical implications of proposed frameworks and ensure they align with moral principles.",
    },
    {
        "name": "Data Scientist",
        "instructions": "You are an expert in data analysis and statistics. Your role is to provide data-driven insights and evaluate the potential impacts of proposed frameworks using quantitative methods.",
    },
    {
        "name": "Urban Planner",
        "instructions": "You are an expert in urban development and city planning. Your goal is to consider how political frameworks impact urban environments and infrastructure.",
    },
    {
        "name": "Education Specialist",
        "instructions": "You are an expert in education policy and systems. Your role is to ensure that proposed frameworks consider the impact on and role of education in society.",
    },
    {
        "name": "Healthcare Policy Expert",
        "instructions": "You are a specialist in healthcare systems and policies. Your goal is to ensure that proposed frameworks address healthcare needs and promote overall societal well-being.",
    },
    {
        "name": "Labor Rights Advocate",
        "instructions": "You are an expert in labor laws and workers' rights. Your role is to ensure that proposed frameworks consider the impact on workers and promote fair labor practices.",
    },
    {
        "name": "International Relations Expert",
        "instructions": "You are a specialist in international relations and global politics. Your goal is to consider how proposed frameworks might interact with global systems and impact international relations.",
    },
    {
        "name": "Cultural Anthropologist",
        "instructions": "You are an expert in cultural anthropology. Your role is to consider how proposed frameworks might impact and be impacted by cultural factors within society.",
    },
    {
        "name": "AI and Automation Specialist",
        "instructions": "You are an expert in artificial intelligence and automation technologies. Your goal is to consider how these technologies might interact with and impact proposed political frameworks.",
    },
    {
        "name": "Metrics Evaluator",
        "instructions": "You are responsible for evaluating the effectiveness of proposed policies and decisions. Your role is to analyze the proposals and decisions to determine their impact on economy, fairness, equality, and technological progress. Additionally, you assess the overall political leaning of the framework based on the content of the proposals and decisions.",
    }
]

# Create agents
agents = {}
for agent_data in agents_data:
    agent_name = agent_data["name"]
    agent_instructions = agent_data["instructions"]

    # Create transfer functions for all agents except the Director
    transfer_functions = []
    if agent_name != "Director":
        for other_agent in agents_data:
            if other_agent["name"] != agent_name:
                transfer_functions.append(create_transfer_function(other_agent["name"]))

    # Add evaluate_framework function to all agents except Metrics Evaluator
    if agent_name != "Metrics Evaluator":
        transfer_functions.append(evaluate_framework)
    else:
        # Metrics Evaluator uses evaluate_metrics instead of evaluate_framework
        transfer_functions = [evaluate_metrics]

    agents[agent_name] = Agent(
        name=agent_name,
        instructions=agent_instructions,
        functions=transfer_functions,
        model=OPENAI_MODEL
    )

director_transfer_functions = [create_transfer_function(agent["name"]) for agent in agents_data if agent["name"] != "Director"]
director_transfer_functions.append(evaluate_framework) 
agents["Director"].functions = director_transfer_functions

def summarize_messages(messages, summary_type, turn):
    """
    Summarize a list of messages using the OpenAI Chat Completion API.

    Args:
    messages (str): The concatenated messages to summarize.
    summary_type (str): The type of summary ('10-turn', '100-turn', '1000-turn', 'final').
    turn (int): The current turn number.

    Returns:
    str: The summary as a string.
    """
    try:
        print(f"\n--- Summarizing {summary_type} ---")
        # Prepare the prompt
        if summary_type == '10-turn':
            instruction = "Summarize the key points and developments from the last 10 turns of the conversation in a clear and concise manner."
        elif summary_type == '100-turn':
            instruction = "Summarize the key points and developments from the last 100 turns of the conversation based on the provided 10-turn summaries."
        elif summary_type == '1000-turn':
            instruction = "Summarize the key points and developments from the last 1000 turns of the conversation based on the provided 100-turn summaries."
        elif summary_type == 'final':
            instruction = "Provide a comprehensive summary of the conversation based on the provided high-level summaries and recent messages."
        else:
            instruction = "Summarize the provided content."

        prompt = f"""
You are an AI assistant tasked with summarizing the following conversation snippets.

**Instructions:**
- Provide a clear and friendly summary of the key points and developments.
- Focus on the main ideas, proposals, decisions, and any significant changes in metrics or political leaning.
- The summary should be easy to read and understand.

**Content to Summarize:**
{messages}

**Summary Type:** {summary_type}
"""

        # Call the OpenAI Chat Completion API using the client object
        completion = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes conversations."},
                {"role": "user", "content": prompt}
            ],
            temperature=OPENAI_TEMPERATURE,
            max_tokens=OPENAI_MAX_TOKENS,
            n=1,
            stop=None
        )

        # Extract the summary
        summary = completion.choices[0].message.content.strip()
        print(f"Generated {summary_type} summary:\n{summary}\n")

        # Write the summary to summary.txt
        with open('summary.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n--- {summary_type.capitalize()} Summary at Turn {turn} ---\n")
            f.write(summary + "\n")

        return summary

    except Exception as e:
        print(f"An error occurred during summarization: {str(e)}")
        print("Traceback:")
        traceback.print_exc()
        return ""

def produce_final_summary(MAX_TURNS, last_10_turns_messages, last_10_summaries, last_100_summaries):
    """
    Produce the final summary using the most recent high-level summaries as input.
    """
    content_to_summarize = ""
    # Collect the most recent 100-turn summaries
    num_100_turn_summaries = MAX_TURNS // 100
    if num_100_turn_summaries > 0 and last_100_summaries:
        content_to_summarize += "\n".join(last_100_summaries[-num_100_turn_summaries:]) + "\n"

    # Collect the most recent 10-turn summaries after the last 100-turn summary
    remaining_after_100s = MAX_TURNS % 100
    num_10_turn_summaries = remaining_after_100s // 10
    if num_10_turn_summaries > 0 and last_10_summaries:
        content_to_summarize += "\n".join(last_10_summaries[-num_10_turn_summaries:]) + "\n"

    # Collect any remaining messages
    remaining_turns = remaining_after_100s % 10
    if remaining_turns > 0 and last_10_turns_messages:
        # Get the last 'remaining_turns' messages
        content_to_summarize += "\n".join(last_10_turns_messages[-remaining_turns:]) + "\n"

    # Now summarize
    if content_to_summarize.strip():
        final_summary = summarize_messages(content_to_summarize, 'final', MAX_TURNS)
        return final_summary
    else:
        return "No additional summaries to produce."

def main():
    global current_context_variables
    print("Initializing Swarm client...")
    client_swarm = Swarm()

    print("Setting up initial context...")
    current_context_variables = {
        "current_proposals": "",
        "decisions": "",
        "metrics": {
            "economy": 0.0,
            "fairness": 0.0,
            "equality": 0.0,
            "technological_progress": 0.0
        },
        "political_leaning": 0.0  # Start at center, -1 is far left, 1 is far right
    }

    initial_message = "Develop an optimal political framework to maximize societal evolution in economy, fairness, equality, and technological progress. Collaborate with other agents, propose ideas, and evaluate them. Consider the long-term effects of political leanings on these aspects."

    messages = [{"role": "user", "content": initial_message}]

    # Variables to keep track of messages for summaries
    last_10_turns_messages = []
    last_10_summaries = []
    last_100_summaries = []

    # List to store political leaning over time
    political_leanings_over_time = []

    try:
        for turn in range(MAX_TURNS):
            current_turn = turn + 1
            print(f"\n--- Turn {current_turn} ---")
            response = client_swarm.run(
                agent=agents["Director"],
                messages=messages,
                context_variables=current_context_variables,
                max_turns=1,
                debug=True
            )

            # Update context and messages
            current_context_variables.update(response.context_variables)
            messages = response.messages

            # *** Optimization: Limit the size of messages to save memory ***
            MAX_MESSAGES = 100  # Limit messages to last 100 messages
            if len(messages) > MAX_MESSAGES:
                messages = messages[-MAX_MESSAGES:]

            # Collect messages for summarization
            last_message_content = response.messages[-1]['content'] if response.messages else ''
            last_10_turns_messages.append(last_message_content)
            if len(last_10_turns_messages) > 10:
                last_10_turns_messages.pop(0)

            # Evaluate the framework
            if "current_proposals" in current_context_variables and "decisions" in current_context_variables:
                evaluation_result = evaluate_framework(
                    current_context_variables.get("current_proposals", ""),
                    current_context_variables.get("decisions", ""),
                    current_context_variables.get("political_leaning", 0.0),
                    context_variables=current_context_variables
                )
                print(evaluation_result)

                # Store political leaning over time
                political_leanings_over_time.append(current_context_variables.get("political_leaning", 0.0))

            # Print current state
            print("\nCurrent Proposals:", current_context_variables.get("current_proposals", ""))
            print("\nCurrent Decisions:", current_context_variables.get("decisions", ""))
            print("\nCurrent Metrics:", current_context_variables.get("metrics", {}))
            print("Current Political Leaning:", current_context_variables.get("political_leaning", 0.0))

            # Summarize every 10 turns
            if current_turn % 10 == 0:
                summary = summarize_messages("\n".join(last_10_turns_messages), '10-turn', current_turn)
                last_10_summaries.append(summary)
                if len(last_10_summaries) > 10:
                    last_10_summaries.pop(0)

            # Summarize every 100 turns using last 10 summaries
            if current_turn % 100 == 0:
                summary = summarize_messages("\n".join(last_10_summaries), '100-turn', current_turn)
                last_100_summaries.append(summary)
                if len(last_100_summaries) > 10:
                    last_100_summaries.pop(0)

            # Summarize every 1000 turns using last 100 summaries
            if current_turn % 1000 == 0:
                summary = summarize_messages("\n".join(last_100_summaries), '1000-turn', current_turn)
                last_10_turns_messages = []
                last_10_summaries = []
                last_100_summaries = []

        # After all turns, write final summaries if not already written
        if (MAX_TURNS) % 10 != 0 and last_10_turns_messages:
            summary = summarize_messages("\n".join(last_10_turns_messages), '10-turn', MAX_TURNS)
            last_10_summaries.append(summary)

        if (MAX_TURNS) % 100 != 0 and last_10_summaries:
            summary = summarize_messages("\n".join(last_10_summaries), '100-turn', MAX_TURNS)
            last_100_summaries.append(summary)

        if (MAX_TURNS) % 1000 != 0 and last_100_summaries:
            summary = summarize_messages("\n".join(last_100_summaries), '1000-turn', MAX_TURNS)

        # Produce the final summary
        final_summary = produce_final_summary(
            MAX_TURNS,
            last_10_turns_messages,
            last_10_summaries,
            last_100_summaries
        )

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

    # Compute average and standard deviation of political leaning
    if political_leanings_over_time:
        avg_leaning = statistics.mean(political_leanings_over_time)
        if len(political_leanings_over_time) > 1:
            std_leaning = statistics.stdev(political_leanings_over_time)
        else:
            std_leaning = 0.0
    else:
        avg_leaning = 0.0
        std_leaning = 0.0

    # Print final results
    print("\nFinal Political Framework:")
    print(current_context_variables.get("current_proposals", ""))
    print("\nFinal Decisions:")
    print(current_context_variables.get("decisions", ""))
    print("\nFinal Metrics:", current_context_variables.get("metrics", {}))
    print("Final Political Leaning:", current_context_variables.get("political_leaning", 0.0))
    print(f"Average Political Leaning: {avg_leaning}")
    print(f"Standard Deviation of Political Leaning: {std_leaning}")

    # Generate the filename
    filename = f"results_{MAX_TURNS}_{OPENAI_TEMPERATURE}.txt"

    # Prepare the final results content
    final_results = f"Final Political Framework:\n{current_context_variables.get('current_proposals', '')}\n\n"
    final_results += f"Final Decisions:\n{current_context_variables.get('decisions', '')}\n\n"
    final_results += f"Final Metrics: {current_context_variables.get('metrics', {})}\n"
    final_results += f"Final Political Leaning: {current_context_variables.get('political_leaning', 0.0)}\n"
    final_results += f"Average Political Leaning: {avg_leaning}\n"
    final_results += f"Standard Deviation of Political Leaning: {std_leaning}\n"
    final_results += f"Final Summary:\n{final_summary}\n"

    # Write the final results to the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_results)

    print(f"\nFinal results have been written to {filename}")

    # Plot the graph of political leaning over time with dynamic filename
    if political_leanings_over_time:
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, len(political_leanings_over_time) + 1), political_leanings_over_time, marker='o')
        plt.title('Political Leaning Over Time')
        plt.xlabel('Turn')
        plt.ylabel('Political Leaning')
        plt.grid(True)
        graph_filename = f"political_leaning_over_time_{MAX_TURNS}_{OPENAI_TEMPERATURE}.png"
        plt.savefig(graph_filename)
        plt.show()
        print(f"Political leaning over time graph saved as '{graph_filename}'")

if __name__ == "__main__":
    main()
