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
- [Spanish version](#Desarrollo-de-un-Marco-Político-utilizando-OpenAI-Swarm)

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

The effectiveness of the political framework is evaluated using the following metrics (ranging from 0 to 1, with 1 being the most desirable outcome):

1. **Economy**: Impact on economic growth and sustainability.
2. **Fairness**: Promotion of fairness and protection of consumer rights.
3. **Equality**: Measures to ensure equal opportunities and reduce disparities.
4. **Technological Progress**: Encouragement of technological innovation and oversight.

Political leaning is also measured on a scale from -1 to 1 (-1 being far left, 0 neutral, +1 far right).

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

The system was tested under different configurations to observe how the degree of freedom and creativity (`OPENAI_TEMPERATURE`) and the number of turns affect the outcomes.

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
- The positive political leaning values across all tests indicate that policies incorporating right-leaning principles, such as market incentives and private sector engagement, were most effective in achieving high metrics in all areas, probably due to the fact that the economic prosperity brought by these policies is the only way to fund fairness and equality policies in the long term.
- This suggests that integrating social programs with economic strategies that encourage innovation and growth leads to a holistic and effective political framework.

**Note on Model Bias**:

- The initial conclusions generated by the o1-preview model when analyzing raw results were:

  > "A moderate left-leaning approach seems to most effectively balance and maximize fairness, equality, economy, and technological progress."

- This was stated despite the numbers clearly indicating that moderate right-leaning policies were the best performing. After highlighting this discrepancy, the model provided more realistic conclusions, hinting that the o1-preview model may have an ideological left bias.

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
     pip install openai python-dotenv matplotlib
     pip install git+https://github.com/openai/swarm.git
     ```

3. **Configuration**:
   - Adjust parameters in the `.env` file or within the script:
     - `OPENAI_TEMPERATURE`: Controls the degree of freedom and creativity in agent responses.
     - `OPENAI_MAX_TOKENS`: Maximum tokens per API call.
     - `MAX_TURNS`: Number of turns for the simulation.

4. **Run the Script**:
   ```
   python optimal_politics_swarm.py
   ```

5. **View Results**:
   - Summaries and results will be saved in the output files mentioned above.
   - Graphs will be displayed and saved to the project directory.

## Conclusion

This project demonstrates how a multi-agent AI system can simulate the development of a political framework. By analyzing the interactions and evaluating the metrics, we conclude that a **moderate right-leaning** approach tends to maximize fairness, equality, economy, and technological progress. The positive political leaning values in all tests indicate that policies integrating right-leaning principles, such as market-driven solutions and private sector incentives, effectively balance social objectives with economic growth. The integration of diverse expert opinions through specialized agents provides a comprehensive view of policy impacts, showcasing the potential of AI in complex decision-making processes.

---

# Desarrollo de un Marco Político utilizando OpenAI Swarm

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Objetivos](#objetivos)
- [Arquitectura de Alto Nivel](#arquitectura-de-alto-nivel)
  - [Agentes y sus Roles](#agentes-y-sus-roles)
  - [Orquestación Multi-Agente](#orquestación-multi-agente)
- [Métricas Monitoreadas](#métricas-monitoreadas)
- [Cómo Funciona el Código](#cómo-funciona-el-código)
- [Resultados de Pruebas y Análisis](#resultados-de-pruebas-y-análisis)
  - [Configuraciones de Prueba](#configuraciones-de-prueba)
  - [Resultados](#resultados)
  - [Conclusión](#conclusión)
- [Archivos Generados](#archivos-generados)
- [Referencias](#referencias)
- [Cómo Ejecutar el Código](#cómo-ejecutar-el-código)
- [Conclusión](#conclusión-1)

---

## Descripción del Proyecto

Este proyecto utiliza el marco de trabajo OpenAI Swarm para simular un entorno multi-agente donde varios agentes especializados colaboran para desarrollar un marco político óptimo. El enfoque principal es explorar qué tipo de políticas—de tendencia izquierdista o derechista—maximizan los objetivos colectivos de equidad, igualdad, economía y progreso tecnológico.

## Objetivos

- **Objetivo Principal**: Determinar qué políticas (de tendencia izquierdista o derechista) son más efectivas en maximizar la equidad, igualdad, economía y progreso tecnológico.
- Desarrollar un marco político integral mediante la colaboración multi-agente.
- Analizar el impacto de diferentes tendencias políticas en las métricas de evolución social.
- Utilizar agentes de IA para simular discusiones de expertos y desarrollo de políticas.

## Arquitectura de Alto Nivel

### Agentes y sus Roles

El sistema comprende múltiples agentes especializados, cada uno representando a un experto en un dominio particular. A continuación, se presenta una lista de los agentes y sus roles:

1. **Director**: Lidera el proceso de desarrollo, sintetiza ideas y toma decisiones finales.
2. **Estratega Económico**: Propone y evalúa políticas económicas para un crecimiento sostenible.
3. **Defensor de la Igualdad**: Asegura que las políticas promuevan oportunidades iguales y reduzcan disparidades.
4. **Árbitro de Equidad**: Se enfoca en la implementación de políticas justas y equitativas.
5. **Científico Político**: Analiza marcos dentro de teorías políticas existentes.
6. **Futurista**: Considera tendencias e impactos sociales a largo plazo.
7. **Científico Ambiental**: Garantiza la sostenibilidad ambiental en las políticas.
8. **Ético**: Evalúa las implicaciones éticas de los marcos propuestos.
9. **Científico de Datos**: Proporciona conocimientos basados en datos utilizando métodos cuantitativos.
10. **Planificador Urbano**: Considera el impacto en entornos urbanos e infraestructura.
11. **Especialista en Educación**: Se enfoca en el rol de la educación en la sociedad.
12. **Experto en Políticas de Salud**: Aborda necesidades de salud y bienestar social.
13. **Defensor de Derechos Laborales**: Promueve prácticas laborales justas y derechos de los trabajadores.
14. **Experto en Relaciones Internacionales**: Considera interacciones e impactos globales.
15. **Antropólogo Cultural**: Examina factores culturales dentro de la sociedad.
16. **Especialista en IA y Automatización**: Explora el impacto de la IA y tecnologías de automatización.
17. **Evaluador de Métricas**: Evalúa la efectividad de las políticas utilizando métricas predefinidas.

### Orquestación Multi-Agente

Los agentes interactúan en un entorno simulado orquestado por el marco OpenAI Swarm. El proceso involucra:

- **Intercambio de Mensajes**: Los agentes se comunican mediante mensajes, proponiendo ideas y brindando retroalimentación.
- **Llamadas a Funciones**: Los agentes pueden invocar funciones, incluyendo transferir control a otros agentes o evaluar el marco.
- **Compartición de Contexto**: Los agentes comparten un diccionario común `context_variables` para almacenar propuestas, decisiones, métricas y la tendencia política actual.
- **Ciclo de Evaluación**: El `Evaluador de Métricas` evalúa el estado actual basado en propuestas y decisiones, actualizando las métricas y la tendencia política en consecuencia.
- **Resumido**: Se generan resúmenes periódicos para condensar la conversación, ayudando a manejar simulaciones largas.

## Métricas Monitorizadas

La efectividad del marco político se evalúa utilizando las siguientes métricas (que varían de 0 a 1, siendo 1 el resultado más deseable):

1. **Economía**: Impacto en el crecimiento económico y sostenibilidad.
2. **Equidad**: Promoción de equidad y protección de los derechos del consumidor.
3. **Igualdad**: Medidas para asegurar oportunidades iguales y reducir disparidades.
4. **Progreso Tecnológico**: Fomento de la innovación tecnológica y supervisión.

La tendencia política también se mide en una escala de -1 a 1 (-1 siendo extrema izquierda, 0 neutral, +1 extrema derecha).

Estas métricas se actualizan después de cada ciclo de evaluación, permitiendo a los agentes ajustar sus propuestas y decisiones en consecuencia.

## Cómo Funciona el Código

1. **Inicialización**:
   - Carga variables de entorno e inicializa el cliente de OpenAI.
   - Configura agentes con sus respectivos roles e instrucciones.
   - Define funciones de transferencia para la comunicación entre agentes.

2. **Bucle Principal**:
   - Se ejecuta por un número específico de turnos (`MAX_TURNS`).
   - El agente `Director` inicia la conversación con un mensaje inicial.
   - Los agentes interactúan intercambiando mensajes e invocando funciones.
   - El `Evaluador de Métricas` evalúa periódicamente el marco, actualizando métricas y tendencia política.

3. **Resumido**:
   - Cada 10, 100 y 1000 turnos, se resume la conversación para mantenerla manejable.
   - Los resúmenes se escriben en `summary.txt`.

4. **Finalización**:
   - Después de la simulación, se generan resúmenes y métricas finales.
   - Los resultados se guardan en archivos de salida y se visualizan mediante gráficos.

## Resultados de Pruebas y Análisis

### Configuraciones de Prueba

El sistema se probó bajo diferentes configuraciones para observar cómo el grado de libertad y creatividad (`OPENAI_TEMPERATURE`) y el número de turnos afectan los resultados.

1. **Prueba 1**: `Turnos = 500`, `Temperatura = 0.7`
2. **Prueba 2**: `Turnos = 300`, `Temperatura = 0.0`
3. **Prueba 3**: `Turnos = 1000`, `Temperatura = 1`

### Resultados

#### Prueba 1: Turnos = 500, Temperatura = 0.7

- **Métricas Finales**:
  - Economía: 0.7
  - Equidad: 0.6
  - Igualdad: 0.5
  - Progreso Tecnológico: 0.8
- **Tendencia Política Final**: **0.5** (Moderada hacia la derecha)
- **Promedio de Tendencia Política**: **0.294**
- **Desviación Estándar**: 0.362

**Resumen**:
Los agentes desarrollaron un marco que enfatiza el crecimiento económico mediante incentivos fiscales para startups e inversiones en infraestructura. Se fomentó el progreso tecnológico mediante mejoras en investigación y desarrollo. Se abordaron la equidad y la igualdad, pero obtuvieron puntuaciones más bajas, indicando un enfoque en aspectos económicos y tecnológicos sobre los programas sociales.

#### Prueba 2: Turnos = 300, Temperatura = 0.0

- **Métricas Finales**:
  - Economía: 0.7
  - Equidad: 0.8
  - Igualdad: 0.9
  - Progreso Tecnológico: 0.6
- **Tendencia Política Final**: **0.5** (Moderada hacia la derecha)
- **Promedio de Tendencia Política**: **0.084**
- **Desviación Estándar**: 0.390

**Resumen**:
El enfoque estuvo en políticas sociales como la expansión de la atención médica universal y el aumento de la financiación de la educación pública, lo que mejoró las métricas de equidad e igualdad. Sin embargo, la tendencia política permaneció ligeramente positiva, indicando que incluso con programas sociales, las políticas tenían elementos de derecha, posiblemente debido a estrategias como el apoyo a la participación del sector privado.

#### Prueba 3: Turnos = 1000, Temperatura = 1

- **Métricas Finales**:
  - Economía: 0.7
  - Equidad: 0.8
  - Igualdad: 0.9
  - Progreso Tecnológico: 0.9
- **Tendencia Política Final**: **0.2** (Moderada hacia la derecha)
- **Promedio de Tendencia Política**: **0.192**
- **Desviación Estándar**: 0.371

**Resumen**:
Se desarrolló un marco integral, destacando la tributación progresiva, ingreso básico universal (IBU) y significativas inversiones en tecnologías verdes. El avance tecnológico obtuvo una alta puntuación. La tendencia política fue moderadamente positiva, sugiriendo que, aunque se enfatizó la equidad social, las políticas aún tenían características de derecha, quizás debido a soluciones basadas en el mercado o incentivos para empresas privadas.

### Conclusión

Basado en las pruebas:

- **Políticas de Derecha**:
  - Consistentemente resultaron en puntajes más altos en todas las métricas, incluyendo equidad e igualdad.
  - Enfatizaron el crecimiento económico y el progreso tecnológico mediante incentivos para negocios e innovación.
  - Integraron programas sociales de una manera que se alinea con mecanismos de mercado.

- **Políticas de Izquierda**:
  - Aunque tradicionalmente asociadas con mayor equidad e igualdad, en estas simulaciones, las políticas que maximizaron todas las métricas tenían elementos moderados de derecha.

**Observación Final**:

- Un enfoque **moderadamente derechista** parece ser el más efectivo para balancear y maximizar la equidad, igualdad, economía y progreso tecnológico.
- Los valores positivos de tendencia política en todas las pruebas indican que las políticas que incorporan principios de derecha, como incentivos de mercado y participación del sector privado, fueron las más efectivas en lograr altas métricas en todas las áreas, probablemente debido al hecho de que la prosperidad económica que traen estas políticas es la única manera de financiar políticas de equidad e igualdad a largo plazo.
- Esto sugiere que integrar programas sociales con estrategias económicas que fomenten la innovación y el crecimiento conduce a un marco político holístico y efectivo.

**Nota sobre Sesgo del Modelo**:

- Las conclusiones iniciales generadas por el modelo o1-preview al analizar los resultados brutos fueron:

  > "Un enfoque moderado de tendencia izquierdista parece equilibrar y maximizar más efectivamente la equidad, igualdad, economía y progreso tecnológico."

- Esto fue afirmado a pesar de que los números indicaban claramente que las políticas moderadamente derechistas eran las de mejor desempeño. Después de resaltar esta discrepancia, el modelo proporcionó conclusiones más realistas, lo que sugiere que el modelo o1-preview puede tener un sesgo ideológico hacia la izquierda.

## Archivos Generados

- **`summary.txt`**: Contiene resúmenes periódicos de la conversación cada 10, 100 y 1000 turnos.
- **`results_<MAX_TURNS>_<TEMPERATURE>.txt`**: Almacena el marco político final, decisiones, métricas, tendencia política y resumen para cada configuración de prueba.
- **`political_leaning_over_time_<MAX_TURNS>_<TEMPERATURE>.png`**: Representación gráfica de la tendencia política a lo largo de la simulación.

## Referencias

- **Marco OpenAI Swarm**: Este proyecto utiliza el [OpenAI Swarm](https://github.com/openai/swarm) para la orquestación multi-agente.

## Cómo Ejecutar el Código

1. **Prerequisitos**:
   - Python 3.7 o superior
   - Clave API de OpenAI
   - Paquetes de Python requeridos: `openai`, `dotenv`, `matplotlib`, etc.

2. **Configuración**:
   - Clona el repositorio.
   - Crea un archivo `.env` con tu clave API de OpenAI:
     ```
     OPENAI_API_KEY=tu-clave-api
     ```
   - Instala las dependencias:
     ```
     pip install openai python-dotenv matplotlib
     pip install git+https://github.com/openai/swarm.git
     ```

3. **Configuración**:
   - Ajusta los parámetros en el archivo `.env` o dentro del script:
     - `OPENAI_TEMPERATURE`: Controla el grado de libertad y creatividad en las respuestas de los agentes.
     - `OPENAI_MAX_TOKENS`: Máximo de tokens por llamada API.
     - `MAX_TURNS`: Número de turnos para la simulación.

4. **Ejecuta el Script**:
   ```
   python optimal_politics_swarm.py
   ```

5. **Visualiza los Resultados**:
   - Los resúmenes y resultados se guardarán en los archivos de salida mencionados.
   - Los gráficos se mostrarán y guardarán en el directorio del proyecto.

## Conclusión

Este proyecto demuestra cómo un sistema de IA multi-agente puede simular el desarrollo de un marco político. Al analizar las interacciones y evaluar las métricas, concluimos que un enfoque **moderadamente derechista** tiende a maximizar la equidad, igualdad, economía y progreso tecnológico. Los valores positivos de tendencia política en todas las pruebas indican que las políticas que integran principios de derecha, como soluciones impulsadas por el mercado y incentivos al sector privado, equilibran efectivamente los objetivos sociales con el crecimiento económico. La integración de opiniones expertas diversas a través de agentes especializados proporciona una visión integral de los impactos de las políticas, mostrando el potencial de la IA en procesos de toma de decisiones complejos.
