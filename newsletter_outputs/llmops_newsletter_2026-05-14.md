# Weekly LLMOps Newsletter — 2026-05-14

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Industry News

### 1. AI-Powered Search and Agent Automation for Digital Asset Management

**Company:** bynder

**Industry:** Media & Entertainment

**Relevance score:** 152

**bynder / Media & Entertainment** — Bynder, a digital asset management platform serving retail and CPG customers, faced significant operational bottlenecks as users had to manually tag and categorize all uploaded content for searchability. To address this, Bynder built AI search capabilities and four types of configurable AI agents using AWS... — Tools: postgresql,mysql,fastapi,elasticsearch,guardrails,microservices | Techniques: embeddings,prompt_engineering,semantic_search,vector_search,agent_based,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=Kyym50EgUOQ

---

### 2. Multi-Agent AI Platform for Life Insurance Sales Acceleration

**Company:** prudential

**Industry:** Insurance

**Relevance score:** 152

**prudential / Insurance** — Prudential developed "Just Ask," an AI-driven advisor assistant platform to address the complex, friction-heavy life insurance sales process that typically spans 8-10 weeks and involves navigating hundreds of products, regulatory requirements, and forms across different states. The company built a multi-agent system on AWS that... — Tools: redis,guardrails,monitoring,api_gateway,orchestration,databases,cache | Techniques: rag,embeddings,semantic_search,multi_agent_systems,agent_based,prompt_engineering,memory,human_in_the_loop,evals,reranking

**Source:** https://www.youtube.com/watch?v=g-YBqWv2kQ4

---

### 3. Building and Scaling AI Agents in Production for DevSecOps Automation

**Company:** datadog

**Industry:** Tech

**Relevance score:** 152

**datadog / Tech** — Datadog, an observability platform company, has deployed over a hundred AI agents in production to automate DevSecOps tasks, with plans to scale to thousands more. The agents include an SRE agent for autonomous alert investigation, a Dev agent for code generation and error fixes, and... — Tools: docker,kubernetes,monitoring,devops,orchestration,cicd,microservices,open_source,documentation,security,guardrails,fastapi | Techniques: agent_based,multi_agent_systems,prompt_engineering,mcp,a2a,evals,memory,harness_engineering

**Source:** https://www.youtube.com/watch?v=C3y3M_03Vco

---

### 4. AI-Powered Bug Routing System Using RAG and Multimodal Processing

**Company:** miro

**Industry:** Tech

**Relevance score:** 142

**miro / Tech** — Miro, serving over 95 million users globally, faced significant challenges with bug routing across nearly 100 engineering teams, resulting in an estimated 42 years of cumulative lost productivity annually due to misrouting and repeated reassignments. To address this, Miro partnered with AWS to develop BugManager... — Tools: kubernetes,elasticsearch | Techniques: rag,prompt_engineering,embeddings,vector_search,human_in_the_loop

**Source:** https://aws.amazon.com/blogs/machine-learning/how-miro-uses-amazon-bedrock-to-boost-software-bug-routing-accuracy-and-improve-time-to-resolution-from-days-to-hours/

---

### 5. Building Production Coding Agents with Pi Framework for Sales Process Automation

**Company:** tavon

**Industry:** Tech

**Relevance score:** 142

**tavon / Tech** — Tavon, a small European company building agents for organizations, developed a production-grade sales automation system using the Pi agent framework and OpenClaw. The system automates the processing of requests for proposals (RFPs) by monitoring email inboxes, routing messages to customer-specific agents, and generating draft responses... — Tools: open_source,security,databases | Techniques: prompt_engineering,multi_agent_systems,agent_based,harness_engineering,system_prompts,memory

**Source:** https://www.youtube.com/watch?v=vAIDdLKB6-w

---

### 6. Building a Production AI Code Review Agent with High Engineer Acceptance

**Company:** doordash

**Industry:** Tech

**Relevance score:** 137

**doordash / Tech** — DoorDash built an AI code review agent to catch critical issues that humans systematically miss during pull request reviews, such as dangerous deletions, cross-boundary drift, and silent behavior changes. The system evolved through three major versions to arrive at a three-agent architecture: a "lead scout"... — Tools: fastapi,monitoring | Techniques: prompt_engineering,multi_agent_systems,agent_based,harness_engineering,cost_optimization,evals

**Source:** https://careersatdoordash.com/blog/doordash-built-an-ai-code-reviewer-engineers-actually-listen-to/

---

### 7. Building Custom Tracing Tools and Development Infrastructure for AI-Powered Meeting Notes

**Company:** granola

**Industry:** Tech

**Relevance score:** 137

**granola / Tech** — Granola, a meeting notes application that uses LLMs to generate summaries from real-time transcription, faced challenges in production with LLM behavior unpredictability, cost control, and feature testing. The company moved beyond simple one-shot LLM implementations by building custom internal tracing tools that provide complete visibility... — Tools: cicd,continuous_deployment,monitoring,databases | Techniques: prompt_engineering,cost_optimization,agent_based,harness_engineering,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=ON5LIT0M4do

---

### 8. Context Management and Memory Strategies for Production AI Agents

**Company:** arize

**Industry:** Tech

**Relevance score:** 137

**arize / Tech** — Arize built Alex, an AI agent designed to help users build AI applications by analyzing observability traces and span data from their platform. The team encountered significant context management challenges as conversations grew and data volumes multiplied, creating a vicious loop where the agent analyzing... — Tools: databases,monitoring | Techniques: prompt_engineering,memory,multi_agent_systems,agent_based,harness_engineering,token_optimization,evals

**Source:** https://www.youtube.com/watch?v=esY99nYXxR4

---

### 9. Gateway Patterns and Actions Runtime for Enterprise Agentic AI Deployment

**Company:** arcade.dev

**Industry:** Tech

**Relevance score:** 137

**arcade.dev / Tech** — Arcade.dev addresses the critical challenges of deploying AI agents in production enterprise environments by providing an actions runtime that separates reasoning from action execution. The company identifies fundamental security and governance problems with existing agent deployment patterns, particularly around authorization, tool quality, and observability. Their... — Tools: docker,api_gateway,security,compliance,guardrails,monitoring,databases,microservices,elasticsearch | Techniques: agent_based,multi_agent_systems,evals

**Source:** https://www.youtube.com/watch?v=gQhDwOGdE4E

---

### 10. Building an AI-Powered Slack Agent with MCP Standardization

**Company:** duolingo

**Industry:** Education

**Relevance score:** 137

**duolingo / Education** — Duolingo developed an AI-powered Slack bot to democratize access to their Model Context Protocol (MCP) infrastructure after discovering that manual MCP server setup was too complex for widespread adoption. The journey began with individual engineers connecting MCP servers to local editors in late 2024, evolved... — Tools: fastapi,docker,monitoring,security,guardrails,open_source,documentation,cicd,orchestration,postgresql | Techniques: mcp,prompt_engineering,human_in_the_loop,multi_agent_systems,agent_based,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=5sb9iA2v78g

---

### 11. Scaling LLM Production with Reinforcement Learning for Enterprise Agents

**Company:** adaptive_ml

**Industry:** Tech

**Relevance score:** 132

**adaptive_ml / Tech** — Adaptive ML addresses the challenge that 95% of GenAI pilots fail to reach production by advocating for reinforcement learning as the core post-training technique. The company argues that MVP solutions built on proprietary models or instruction fine-tuning lack systematic improvement mechanisms, whereas RL enables continuous... — Tools: llama_index,mistral,monitoring,open_source | Techniques: fine_tuning,few_shot,agent_based,multi_agent_systems,prompt_engineering,cost_optimization,latency_optimization,evals,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=X6NShR2ccOg

---

### 12. Scaling AI Agents in Production for B2B Growth and Outreach

**Company:** clay

**Industry:** Tech

**Relevance score:** 132

**clay / Tech** — Clay, a creative tool for B2B growth and customer acquisition, scaled their AI agent infrastructure from early chat completion wrappers to operating 300 million agent runs per month. The company deployed multiple specialized agents across finding, closing, and growing customers, with individual agents running 10-30... — Tools: langchain,monitoring,open_source,documentation | Techniques: agent_based,prompt_engineering,few_shot,cost_optimization,harness_engineering,evals,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=cx6_tb6HCeY

---

### 13. AI Employee Agent Operating in Slack with Multi-Tool Integration

**Company:** viktor

**Industry:** Tech

**Relevance score:** 132

**viktor / Tech** — Viktor is an AI employee agent that operates directly within Slack, providing teams with access to over 3,000 integrations and company-wide context. The product evolved from early web agent experiments in 2023 through an email agent called Jace, ultimately launching as Viktor in February 2026... — Tools: fastapi,security,compliance | Techniques: multi_agent_systems,agent_based,memory,harness_engineering,prompt_engineering,human_in_the_loop,latency_optimization

**Source:** https://www.youtube.com/watch?v=ohKt066uFhg

---

### 14. Automating Workflows with AI Agents Across the Organization

**Company:** notion

**Industry:** Tech

**Relevance score:** 132

**notion / Tech** — Notion implemented Custom Agents across their organization to automate repetitive workflows and reduce manual busywork. The company faced challenges with knowledge accessibility, manual triage of product feedback, and time-consuming repetitive tasks across multiple teams. By deploying domain-specific AI agents that integrate with Slack, their knowledge... — Tools: langchain,documentation,security,crewai | Techniques: rag,prompt_engineering,multi_agent_systems,agent_based,semantic_search

**Source:** https://www.notion.com/blog/how-notion-uses-custom-agents

---

### 15. Multi-Agent Research and Intelligence Platform for Pharmaceutical Data Integration

**Company:** madrigal

**Industry:** Healthcare

**Relevance score:** 132

**madrigal / Healthcare** — Madrigal Pharmaceuticals built an enterprise multi-agent platform to integrate, search, and synthesize information from diverse pharmaceutical datasets scattered across structured systems, unstructured documents, and external sources. Using LangChain's DeepAgents framework and LangSmith for observability, evaluation, and deployment, they created a modular skills-based architecture where specialized... — Tools: langchain,cicd,orchestration,monitoring,databases,api_gateway,microservices,security,compliance,guardrails,scalability | Techniques: rag,multi_agent_systems,agent_based,prompt_engineering,semantic_search,vector_search,evals,error_handling,latency_optimization

**Source:** https://www.langchain.com/blog/customers-madrigal

---

### 16. Platform Engineering for AI: Scaling Multi-Agentic Systems with MCP

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 132

**linkedin / Tech** — LinkedIn faced the challenge of moving AI agents from siloed proof-of-concepts to production-scale systems that could serve thousands of developers. The company developed a unified platform engineering approach that treats AI agents as a first-class execution model, comparable to microservices infrastructure. The solution involved building... — Tools: kubernetes,docker,monitoring,cicd,orchestration,security,guardrails,documentation,open_source,fastapi,postgresql,cache,devops,continuous_integration,continuous_deployment,reliability,scalability,compliance | Techniques: agent_based,multi_agent_systems,prompt_engineering,rag,embeddings,semantic_search,human_in_the_loop,evals,system_prompts,mcp,error_handling

**Source:** https://www.infoq.com/podcasts/platform-engineering-scaling-agents/

---

## Cool Use Cases

### 1. AI-Powered Customer Feedback Analysis System for Container Shipping

**Company:** hapag-lloyd

**Industry:** Other

**Relevance score:** 137

**hapag-lloyd / Other** — Hapag-Lloyd, a global container shipping company, transformed their manual and time-consuming customer feedback analysis process into an automated AI-powered system using Amazon Bedrock. Previously, product managers spent hours or days manually categorizing sentiment and themes from hundreds of feedback comments exported as CSV files. The... — Tools: langchain,elasticsearch,monitoring,serverless,orchestration,open_source,guardrails | Techniques: embeddings,rag,prompt_engineering,multi_agent_systems,agent_based,semantic_search

**Source:** https://aws.amazon.com/blogs/machine-learning/how-hapag-lloyd-uses-amazon-bedrock-to-transform-customer-feedback-into-actionable-insights/

---

### 2. Building Custom Agents at Scale: Notion's Multi-Year Journey to Production-Ready Agentic Workflows

**Company:** notion

**Industry:** Tech

**Relevance score:** 137

**notion / Tech** — Notion, a knowledge work platform serving enterprise customers, spent multiple years (2022-2026) iterating through four to five complete rebuilds of their agent infrastructure before shipping Custom Agents to production. The core problem was enabling users to automate complex workflows across their workspaces while maintaining enterprise-grade... — Tools: langchain,postgresql,sqlite,elasticsearch,fastapi,docker,kubernetes,cicd,monitoring,databases,api_gateway,microservices,orchestration,open_source,documentation,security,guardrails,reliability,scalability,cache | Techniques: agent_based,multi_agent_systems,prompt_engineering,few_shot,rag,embeddings,fine_tuning,evals,reranking,semantic_search,vector_search,human_in_the_loop,cost_optimization,latency_optimization,system_prompts,mcp,chunking,error_handling,a2a

**Source:** https://www.latent.space/p/notion

---

### 3. Production Skills Framework for Agentic LLM Workflows

**Company:** workos

**Industry:** Tech

**Relevance score:** 132

**workos / Tech** — WorkOS developed a comprehensive approach to productionizing LLM workflows through "skills" - reusable, composable units of work that encapsulate specific tasks, constraints, and domain knowledge in markdown files with optional scripts. The problem addressed was the repetitive nature of LLM interactions where context must be... — Tools: langchain,fastapi,documentation,cicd,open_source,crewai | Techniques: prompt_engineering,agent_based,multi_agent_systems,system_prompts,evals,few_shot,memory,chunking

**Source:** https://www.youtube.com/watch?v=pFsfax19yOM

---

### 4. Production Agent Observability and Monitoring Platform

**Company:** raindrop

**Industry:** Tech

**Relevance score:** 132

**raindrop / Tech** — Raindrop addresses the challenge of monitoring and debugging AI agents in production environments where traditional testing and evaluation approaches fall short. As agents become more complex with multiple tools, memory sources, and sub-agents, the combinatorial explosion of possible behaviors makes comprehensive testing impractical. Raindrop provides... — Tools: monitoring,open_source,documentation,guardrails,reliability,langchain,fastapi | Techniques: prompt_engineering,few_shot,agent_based,multi_agent_systems,error_handling,latency_optimization,cost_optimization,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=-aM2EDTiaMs

---

### 5. Multi-Agent AI SRE System for Automated Incident Response and Root Cause Analysis

**Company:** opsworker.ai

**Industry:** Tech

**Relevance score:** 132

**opsworker.ai / Tech** — OpsWorker.ai developed a multi-agent AI SRE (Site Reliability Engineering) system to address the challenge of investigating and resolving complex system incidents in modern cloud-native environments. Traditional SRE automation relies on simple rules and alerts, but struggles with the complexity and data volume of Kubernetes-based microservices... — Tools: kubernetes,monitoring,orchestration,devops,scaling,microservices,databases,api_gateway,cicd,continuous_deployment,open_source,documentation,reliability,scalability,postgresql,mysql,redis,cache,elasticsearch | Techniques: multi_agent_systems,agent_based,prompt_engineering,error_handling,latency_optimization,human_in_the_loop

**Source:** https://www.opsworker.ai/blog/what-is-an-ai-sre-agent-and-how-we-implement-an-ai-sre-agent-at-opsworker-ai-multi-agent-logic/

---

## Tools & Infrastructure

### 1. Building Agentic Spreadsheet Automation from Process Mining to Production

**Company:** ramp

**Industry:** Finance

**Relevance score:** 147

**ramp / Finance** — Ramp developed an agentic spreadsheet editor called Ramp Sheets to automate complex finance workflows, starting from an internal process mining project that converted Loom videos of finance tasks into automation pipelines. The team evolved from black-box Python code generation to transparent spreadsheet-native operations using around... — Tools: docker,monitoring,databases,api_gateway,microservices,cicd,open_source,fastapi,pytorch,redis,cache | Techniques: agent_based,prompt_engineering,few_shot,harness_engineering,memory,multi_agent_systems,evals,human_in_the_loop,latency_optimization,token_optimization

**Source:** https://www.youtube.com/watch?v=trEM9OKr5Sc

---

### 2. AI-Powered Workflow Assistant for Seismic Data Processing

**Company:** halliburton

**Industry:** Energy

**Relevance score:** 147

**halliburton / Energy** — Halliburton partnered with AWS Generative AI Innovation Center to develop an AI-powered assistant for their Seismic Engine, a cloud-native application for seismic data processing. The traditional workflow creation process required manual configuration of approximately 100 specialized tools, which was time-consuming and required deep expertise. The... — Tools: langchain,fastapi,elasticsearch,databases,serverless,api_gateway,monitoring,orchestration | Techniques: rag,prompt_engineering,agent_based,semantic_search,vector_search

**Source:** https://aws.amazon.com/blogs/machine-learning/halliburton-enhances-seismic-workflow-creation-with-amazon-bedrock-and-generative-ai/

---

### 3. Multi-Agent AI Architecture for Site Reliability Engineering in Cloud-Native Infrastructure

**Company:** komodor

**Industry:** Tech

**Relevance score:** 132

**komodor / Tech** — Komodor introduced Klaudia AI, a multi-agent architecture designed to address the complexity of modern cloud-native infrastructure incident management. The problem stems from contemporary systems running hundreds of microservices across multi-cloud environments where symptoms appear in one place while root causes exist elsewhere, making single-agent AI... — Tools: kubernetes,docker,monitoring,databases,api_gateway,microservices,orchestration,devops,open_source,documentation,security,guardrails,reliability,scalability,vllm,postgresql,redis,langchain,pinecone,qdrant,wandb | Techniques: rag,embeddings,multi_agent_systems,agent_based,semantic_search,vector_search,prompt_engineering,error_handling,human_in_the_loop,evals

**Source:** https://komodor.com/blog/multi-agent-ai-sre-has-landed-and-its-built-for-your-most-complex-stacks/

---

### 4. Cognitive Memory Agent: Building Stateful AI Agents with Multi-Layer Memory Architecture

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 132

**linkedin / Tech** — LinkedIn developed the Cognitive Memory Agent (CMA), a horizontal memory platform designed to enable stateful and context-aware AI agents at scale, initially deployed within their Hiring Assistant product. The problem addressed was that delivering truly agentic experiences required more than capable models—agents needed domain intelligence... — Tools: langchain,chromadb,pinecone,qdrant,postgresql,redis,cache,microservices,monitoring,scalability,open_source,documentation,security,guardrails,databases,orchestration | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,multi_agent_systems,agent_based,human_in_the_loop,latency_optimization,cost_optimization,chunking,system_prompts,evals

**Source:** https://www.linkedin.com/blog/engineering/ai/the-linkedin-generative-ai-application-tech-stack-personalization-with-cognitive-memory-agent

---
