# Political Framework Development using OpenAI Swarm

## Table of Contents

- [Project Overview](#project-overview)
- [Goals](#goals)
- [High-Level Architecture](#high-level-architecture)
  - [Agents and Their Roles](#agents-and-their-roles)
  - [Multi-Agent Orchestration](#multi-agent-orchestration)
- [Metrics Tracked](#metrics-tracked)
- [How the Code Works](#how-the-code-works)
- [Test Results and Analysis](#test-results-and-analysis)
  - [Test Configurations](#test-configurations)
  - [Results](#results)
  - [Conclusion](#conclusion)
- [Generated Files](#generated-files)
- [References](#references)
- [How to Run the Code](#how-to-run-the-code)
- [Conclusion](#conclusion-1)

---

## Project Overview

This project leverages the OpenAI Swarm framework to simulate a multi-agent environment where various specialized agents collaborate to develop an optimal political framework. The primary focus is to explore which type of policies—left-leaning or right-leaning—maximize the collective goals of fairness, equality, economy, and technological progress.

## Goals

- **Primary Goal**: Determine which policies (left-leaning or right-leaning) are most effective in maximizing fairness, equality, economy, and technological progress.
- Develop a comprehensive political framework through multi-agent collaboration.
- Analyze the impact of different political leanings on societal evolution metrics.
- Utilize AI agents to simulate expert discussions and policy development.

## High-Level Architecture

### Agents and Their Roles

The system comprises multiple specialized agents, each representing an expert in a particular domain. Below is a list of the agents and their roles:

1. **Director**: Leads the development process, synthesizes ideas, and makes final decisions.
2. **Economic Strategist**: Proposes and evaluates economic policies for sustainable growth.
3. **Equality Advocate**: Ensures policies promote equal opportunities and reduce disparities.
4. **Fairness Arbitrator**: Focuses on equitable and just policy implementation.
5. **Political Scientist**: Analyzes frameworks within existing political theories.
6. **Futurist**: Considers long-term societal trends and impacts.
7. **Environmental Scientist**: Ensures environmental sustainability in policies.
8. **Ethicist**: Evaluates ethical implications of proposed frameworks.
9. **Data Scientist**: Provides data-driven insights using quantitative methods.
10. **Urban Planner**: Considers the impact on urban environments and infrastructure.
11. **Education Specialist**: Focuses on the role of education in society.
12. **Healthcare Policy Expert**: Addresses healthcare needs and societal well-being.
13. **Labor Rights Advocate**: Promotes fair labor practices and workers' rights.
14. **International Relations Expert**: Considers global interactions and impacts.
15. **Cultural Anthropologist**: Examines cultural factors within society.
16. **AI and Automation Specialist**: Explores the impact of AI and automation technologies.
17. **Metrics Evaluator**: Evaluates the effectiveness of policies using predefined metrics.

### Multi-Agent Orchestration

The agents interact in a simulated environment orchestrated by the OpenAI Swarm framework. The process involves:

- **Message Passing**: Agents communicate through messages, proposing ideas, and providing feedback.
- **Function Calls**: Agents can invoke functions, including transferring control to other agents or evaluating the framework.
- **Context Sharing**: Agents share a common `context_variables` dictionary to store proposals, decisions, metrics, and the current political leaning.
- **Evaluation Cycle**: The `Metrics Evaluator` assesses the current state based on proposals and decisions, updating the metrics and political leaning accordingly.
- **Summarization**: Periodic summaries are generated to condense the conversation, aiding in managing long simulations.

## Metrics Tracked

The effectiveness of the political framework is evaluated using the following metrics (ranging from 0 to 1, being 1 the most desirable outcome):

1. **Economy**: Impact on economic growth and sustainability.
2. **Fairness**: Promotion of fairness and protection of consumer rights.
3. **Equality**: Measures to ensure equal opportunities and reduce disparities.
4. **Technological Progress**: Encouragement of technological innovation and oversight.

Political leaning is also measured on scale from from -1 to 1 (-1 being far left, 0 neutral, +1 far right).

These metrics are updated after each evaluation cycle, allowing the agents to adjust their proposals and decisions accordingly.

## How the Code Works

1. **Initialization**:
   - Loads environment variables and initializes the OpenAI client.
   - Sets up agents with their respective roles and instructions.
   - Defines transfer functions for agent communication.

2. **Main Loop**:
   - Runs for a specified number of turns (`MAX_TURNS`).
   - The `Director` agent initiates the conversation with an initial message.
   - Agents interact by passing messages and invoking functions.
   - The `Metrics Evaluator` periodically evaluates the framework, updating metrics and political leaning.

3. **Summarization**:
   - Every 10, 100, and 1000 turns, the conversation is summarized to maintain manageability.
   - Summaries are written to `summary.txt`.

4. **Finalization**:
   - After the simulation, final summaries and metrics are generated.
   - Results are saved to output files and visualized through graphs.

## Test Results and Analysis

### Test Configurations

The system was tested under different configurations to observe how temperature (randomness in agent responses) and the number of turns affect the outcomes.

1. **Test 1**: `Turns = 500`, `Temperature = 0.7`
2. **Test 2**: `Turns = 300`, `Temperature = 0.0`
3. **Test 3**: `Turns = 1000`, `Temperature = 1`

### Results

#### Test 1: Turns = 500, Temperature = 0.7

- **Final Metrics**:
  - Economy: 0.7
  - Fairness: 0.6
  - Equality: 0.5
  - Technological Progress: 0.8
- **Final Political Leaning**: **0.5** (Moderate right-leaning)
- **Average Political Leaning**: **0.294**
- **Standard Deviation**: 0.362

**Summary**:
The agents developed a framework emphasizing economic growth through tax incentives for startups and infrastructure investments. Technological progress was fostered by enhancing research and development. Fairness and equality were addressed but scored lower, indicating a focus on economic and technological aspects over social programs.

#### Test 2: Turns = 300, Temperature = 0.0

- **Final Metrics**:
  - Economy: 0.7
  - Fairness: 0.8
  - Equality: 0.9
  - Technological Progress: 0.6
- **Final Political Leaning**: **0.5** (Moderate right-leaning)
- **Average Political Leaning**: **0.084**
- **Standard Deviation**: 0.390

**Summary**:
The focus was on social policies like expanding universal healthcare and increasing public education funding, which improved fairness and equality metrics. However, the political leaning remained slightly positive, indicating that even with social programs, the policies had right-leaning elements, possibly due to strategies like supporting private sector involvement.

#### Test 3: Turns = 1000, Temperature = 1

- **Final Metrics**:
  - Economy: 0.7
  - Fairness: 0.8
  - Equality: 0.9
  - Technological Progress: 0.9
- **Final Political Leaning**: **0.2** (Moderate right-leaning)
- **Average Political Leaning**: **0.192**
- **Standard Deviation**: 0.371

**Summary**:
A comprehensive framework was developed, highlighting progressive taxation, universal basic income (UBI), and significant investments in green technologies. Technological advancement scored highly. The political leaning was moderately positive, suggesting that while social equity was emphasized, the policies still had right-leaning characteristics, perhaps due to market-based solutions or incentives for private enterprises.

### Conclusion

Based on the tests:

- **Right-Leaning Policies**:
  - Consistently resulted in higher scores across all metrics, including fairness and equality.
  - Emphasized economic growth and technological progress through incentives for businesses and innovation.
  - Integrated social programs in a way that aligns with market mechanisms.

- **Left-Leaning Policies**:
  - While traditionally associated with higher fairness and equality, in these simulations, the policies that maximized all metrics had moderate right-leaning elements.

**Final Observation**:

- A **moderate right-leaning** approach seems to most effectively balance and maximize fairness, equality, economy, and technological progress.
- The positive political leaning values across all tests indicate that policies incorporating right-leaning principles, such as market incentives and private sector engagement, were most effective in achieving high metrics in all areas, probably due to the fact the economic prosperity brought by these policies are the only way to fund fairness and equality policies in the long term.
- This suggests that integrating social programs with economic strategies that encourage innovation and growth leads to a holistic and effective political framework.

## Generated Files

- **`summary.txt`**: Contains periodic summaries of the conversation at every 10, 100, and 1000 turns.
- **`results_<MAX_TURNS>_<TEMPERATURE>.txt`**: Stores the final political framework, decisions, metrics, political leaning, and summary for each test configuration.
- **`political_leaning_over_time_<MAX_TURNS>_<TEMPERATURE>.png`**: Graphical representation of political leaning over the course of the simulation.

## References

- **OpenAI Swarm Framework**: This project utilizes the [OpenAI Swarm](https://github.com/openai/swarm) framework for multi-agent orchestration.

## How to Run the Code

1. **Prerequisites**:
   - Python 3.7 or higher
   - OpenAI API Key
   - Required Python packages: `openai`, `dotenv`, `matplotlib`, etc.

2. **Setup**:
   - Clone the repository.
   - Create a `.env` file with your OpenAI API key:
     ```
     OPENAI_API_KEY=your-api-key
     ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```

3. **Configuration**:
   - Adjust parameters in the `.env` file or within the script:
     - `OPENAI_TEMPERATURE`: Controls randomness in agent responses.
     - `OPENAI_MAX_TOKENS`: Maximum tokens per API call.
     - `MAX_TURNS`: Number of turns for the simulation.

4. **Run the Script**:
   ```
   python main.py
   ```

5. **View Results**:
   - Summaries and results will be saved in the output files mentioned above.
   - Graphs will be displayed and saved to the project directory.

## Conclusion

This project demonstrates how a multi-agent AI system can simulate the development of a political framework. By analyzing the interactions and evaluating the metrics, we conclude that a **moderate right-leaning** approach tends to maximize fairness, equality, economy, and technological progress. The positive political leaning values in all tests indicate that policies integrating right-leaning principles, such as market-driven solutions and private sector incentives, effectively balance social objectives with economic growth. The integration of diverse expert opinions through specialized agents provides a comprehensive view of policy impacts, showcasing the potential of AI in complex decision-making processes.
