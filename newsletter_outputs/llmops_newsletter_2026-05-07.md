# Weekly LLMOps Newsletter — 2026-05-07

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Industry News

### 1. Building an AI-Powered Slack Agent with MCP Standardization

**Company:** duolingo

**Industry:** Education

**Relevance score:** 137

**duolingo / Education** — Duolingo developed an AI-powered Slack bot to democratize access to their Model Context Protocol (MCP) infrastructure after discovering that manual MCP server setup was too complex for widespread adoption. The journey began with individual engineers connecting MCP servers to local editors in late 2024, evolved... — Tools: fastapi,docker,monitoring,security,guardrails,open_source,documentation,cicd,orchestration,postgresql | Techniques: mcp,prompt_engineering,human_in_the_loop,multi_agent_systems,agent_based,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=5sb9iA2v78g

---

### 2. Agentic Workflow Automation for Financial Operations

**Company:** ramp

**Industry:** Finance

**Relevance score:** 132

**ramp / Finance** — Ramp, a finance automation platform serving over 50,000 customers, built a comprehensive suite of AI agents to automate manual financial workflows including expense policy enforcement, accounting classification, and invoice processing. The company evolved from building hundreds of isolated agents to consolidating around a single agent... — Tools: langchain,fastapi,docker,kubernetes,monitoring,cicd,continuous_integration,continuous_deployment,open_source,documentation,guardrails,reliability,scalability,postgresql,cache,orchestration | Techniques: agent_based,multi_agent_systems,prompt_engineering,human_in_the_loop,few_shot,evals,token_optimization,error_handling,cost_optimization

**Source:** https://www.youtube.com/watch?v=NMs8C2_3M0w

---

### 3. Open-Source Agent Orchestration Platform for Multi-Agent Business Automation

**Company:** paperclip

**Industry:** Tech

**Relevance score:** 132

**paperclip / Tech** — Paperclip is an open-source agent orchestration platform designed to manage AI agents in production environments for business automation. The platform addresses the challenge of coordinating multiple AI agents across different organizational functions by providing a centralized control plane with organizational hierarchies, task management, quality assurance... — Tools: docker,orchestration,open_source,documentation,cicd,continuous_integration,fastapi,crewai,postgresql | Techniques: prompt_engineering,multi_agent_systems,agent_based,human_in_the_loop,system_prompts

**Source:** https://www.youtube.com/watch?v=h403btjldDQ

---

### 4. Platform Engineering for AI: Scaling Multi-Agentic Systems with MCP

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 132

**linkedin / Tech** — LinkedIn faced the challenge of moving AI agents from siloed proof-of-concepts to production-scale systems that could serve thousands of developers. The company developed a unified platform engineering approach that treats AI agents as a first-class execution model, comparable to microservices infrastructure. The solution involved building... — Tools: kubernetes,docker,monitoring,cicd,orchestration,security,guardrails,documentation,open_source,fastapi,postgresql,cache,devops,continuous_integration,continuous_deployment,reliability,scalability,compliance | Techniques: agent_based,multi_agent_systems,prompt_engineering,rag,embeddings,semantic_search,human_in_the_loop,evals,system_prompts,mcp,error_handling

**Source:** https://www.infoq.com/podcasts/platform-engineering-scaling-agents/

---

### 5. Grassroots AI Skills Marketplace: Scaling AI Capabilities Through Bottom-Up Engineering

**Company:** uber

**Industry:** Tech

**Relevance score:** 132

**uber / Tech** — Uber faced the common challenge of scaling AI adoption across a large engineering organization with 200+ microservices and thousands of engineers. Rather than implementing a top-down enterprise AI mandate, Uber enabled organic growth through a grassroots approach where a single engineer created an internal "Agentic... — Tools: cicd,microservices,continuous_deployment,continuous_integration,devops,orchestration,guardrails,reliability,scalability,documentation | Techniques: prompt_engineering,agent_based,multi_agent_systems,human_in_the_loop,evals,error_handling

**Source:** https://medium.com/activated-thinker/how-uber-secretly-scaled-ai-from-2-to-500-skills-in-5-months-without-a-strategy-25ff894c0f9c

---

### 6. Multi-Agent Research and Intelligence Platform for Pharmaceutical Data Integration

**Company:** madrigal

**Industry:** Healthcare

**Relevance score:** 132

**madrigal / Healthcare** — Madrigal Pharmaceuticals built an enterprise multi-agent platform to integrate, search, and synthesize information from diverse pharmaceutical datasets scattered across structured systems, unstructured documents, and external sources. Using LangChain's DeepAgents framework and LangSmith for observability, evaluation, and deployment, they created a modular skills-based architecture where specialized... — Tools: langchain,cicd,orchestration,monitoring,databases,api_gateway,microservices,security,compliance,guardrails,scalability | Techniques: rag,multi_agent_systems,agent_based,prompt_engineering,semantic_search,vector_search,evals,error_handling,latency_optimization

**Source:** https://www.langchain.com/blog/customers-madrigal

---

### 7. Automating Workflows with AI Agents Across the Organization

**Company:** notion

**Industry:** Tech

**Relevance score:** 132

**notion / Tech** — Notion implemented Custom Agents across their organization to automate repetitive workflows and reduce manual busywork. The company faced challenges with knowledge accessibility, manual triage of product feedback, and time-consuming repetitive tasks across multiple teams. By deploying domain-specific AI agents that integrate with Slack, their knowledge... — Tools: langchain,documentation,security,crewai | Techniques: rag,prompt_engineering,multi_agent_systems,agent_based,semantic_search

**Source:** https://www.notion.com/blog/how-notion-uses-custom-agents

---

### 8. Multi-Agent AI System for Investment Thesis Validation Using Devil's Advocate

**Company:** linqalpha

**Industry:** Finance

**Relevance score:** 127

**linqalpha / Finance** — LinqAlpha, a Boston-based AI platform serving over 170 institutional investors, developed Devil's Advocate, an AI agent that systematically pressure-tests investment theses by identifying blind spots and generating evidence-based counterarguments. The system addresses the challenge of confirmation bias in investment research by automating the manual process... — Tools: databases,api_gateway,microservices,orchestration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,postgresql,redis,cache,elasticsearch | Techniques: multi_agent_systems,prompt_engineering,rag,embeddings,semantic_search,vector_search,agent_based,chunking,system_prompts

**Source:** https://aws.amazon.com/blogs/machine-learning/how-linqalpha-assesses-investment-theses-using-devils-advocate-on-amazon-bedrock?tag=soumet-20

---

### 9. Extreme Harness Engineering: Building Production Software with Zero Human-Written Code

**Company:** openai

**Industry:** Tech

**Relevance score:** 127

**openai / Tech** — OpenAI's Frontier Product Exploration team conducted a five-month experiment building an internal beta product with zero manually written code, generating over 1 million lines of code across thousands of PRs while processing approximately 1 billion tokens per day. The team developed "Symphony," an Elixir-based orchestration... — Tools: docker,monitoring,cicd,orchestration,continuous_integration,continuous_deployment,open_source,documentation,reliability,scalability,fastapi,postgresql,elasticsearch,guardrails | Techniques: prompt_engineering,multi_agent_systems,agent_based,human_in_the_loop,error_handling,evals

**Source:** https://www.latent.space/p/harness-eng

---

### 10. Building Production-Scale Voice AI with Multi-Model Pipelines and Deployment Infrastructure

**Company:** elevenlabs

**Industry:** Tech

**Relevance score:** 127

**elevenlabs / Tech** — ElevenLabs, founded by Mati and his co-founder from Poland, built frontier voice AI models to solve audio generation, transcription, and translation problems at scale. Starting in 2022 with text-to-speech models trained on modest compute budgets, they evolved a cascaded architecture combining speech-to-text, LLMs, and text-to-speech... — Tools: fastapi,monitoring,databases,api_gateway,microservices,open_source,documentation,guardrails,reliability,scalability,pytorch,tensorflow | Techniques: fine_tuning,model_optimization,knowledge_distillation,latency_optimization,few_shot,prompt_engineering,multi_agent_systems,agent_based,human_in_the_loop,error_handling,evals

**Source:** https://www.youtube.com/watch?v=TnL10oBZc6U

---

### 11. Multi-Agent System for Interview Analysis and Report Generation at Scale

**Company:** listenlabs

**Industry:** Tech

**Relevance score:** 127

**listenlabs / Tech** — ListenLabs, a platform for analyzing user research at scale, built a sophisticated multi-agent system that processes hundreds to thousands of user interviews, surveys, and focus group feedback. The company evolved from basic retrieval-augmented generation to a complex architecture featuring three primary agents: a study creation... — Tools: postgresql,fastapi,langchain,open_source,monitoring,databases,orchestration,devops | Techniques: multi_agent_systems,prompt_engineering,evals,rag,embeddings,semantic_search,few_shot,chunking,system_prompts,human_in_the_loop,agent_based,error_handling,latency_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=YTTH-0XXEBE

---

### 12. Multi-Agent Architecture for Intelligent Advertising Media Planning

**Company:** spotify

**Industry:** Media & Entertainment

**Relevance score:** 127

**spotify / Media & Entertainment** — Spotify faced a structural problem where multiple advertising buying channels (Direct, Self-Serve, Programmatic) had fragmented workflow logic despite a consolidated backend, leading to duplicated decision-making and tech debt. They built Ads AI, a multi-agent system using Google's Agent Development Kit (ADK) and Vertex AI's Gemini... — Tools: orchestration,cache,postgresql,monitoring,api_gateway,microservices,databases,documentation | Techniques: multi_agent_systems,prompt_engineering,agent_based,few_shot,latency_optimization,cost_optimization,system_prompts

**Source:** https://engineering.atspotify.com/2026/02/our-multi-agent-architecture-for-smarter-advertising

---

### 13. Scaling AI Agents in Production: Building and Operating Hundreds of Autonomous Agents

**Company:** datadog

**Industry:** Tech

**Relevance score:** 127

**datadog / Tech** — Datadog shares lessons learned from building over 100 AI agents in production and preparing to scale to thousands more. The company deployed multiple production agents including Bits AI SRE for autonomous alert investigation, Bits AI Dev for code generation and error fixes, and security analysts... — Tools: docker,kubernetes,monitoring,api_gateway,microservices,cicd,serverless,devops,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,guardrails,reliability,scalability,fastapi,langchain | Techniques: agent_based,multi_agent_systems,prompt_engineering,evals,human_in_the_loop,latency_optimization,error_handling,mcp,a2a

**Source:** https://www.youtube.com/watch?v=Naty_iFtITM

---

### 14. Building Enterprise AI Agents with Code-First Approach for Trust and Auditability

**Company:** coinbase

**Industry:** Finance

**Relevance score:** 124

**coinbase / Finance** — Coinbase's Enterprise Applications and Architecture team established an Agentic AI Tiger Team over six weeks to standardize the development and deployment of enterprise AI agents for internal process automation. The team deliberately chose a code-first, high-code approach using LangGraph and LangChain over low-code tools to... — Tools: langchain,monitoring,cicd,orchestration,devops,documentation,compliance,guardrails,reliability,scalability | Techniques: agent_based,multi_agent_systems,human_in_the_loop,prompt_engineering,evals,error_handling

**Source:** https://www.coinbase.com/en-nl/blog/building-enterprise-AI-agents-at-Coinbase

---

### 15. Building Reliable LLM Workflows in Biotech Research

**Company:** moderna

**Industry:** Healthcare

**Relevance score:** 122

**moderna / Healthcare** — Moderna Therapeutics applies large language models primarily for document reformatting and regulatory submission preparation within their research organization, deliberately avoiding autonomous agents in favor of highly structured workflows. The team, led by Eric Maher in research data science, focuses on automating what they term "intellectual... — Tools: vllm,open_source,documentation,security,compliance,guardrails,sqlite,serverless | Techniques: fine_tuning,prompt_engineering,rag,embeddings,few_shot,error_handling,human_in_the_loop,cost_optimization,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=GvCFFvMw2uo

---

## Cool Use Cases

### 1. Building Custom Agents at Scale: Notion's Multi-Year Journey to Production-Ready Agentic Workflows

**Company:** notion

**Industry:** Tech

**Relevance score:** 137

**notion / Tech** — Notion, a knowledge work platform serving enterprise customers, spent multiple years (2022-2026) iterating through four to five complete rebuilds of their agent infrastructure before shipping Custom Agents to production. The core problem was enabling users to automate complex workflows across their workspaces while maintaining enterprise-grade... — Tools: langchain,postgresql,sqlite,elasticsearch,fastapi,docker,kubernetes,cicd,monitoring,databases,api_gateway,microservices,orchestration,open_source,documentation,security,guardrails,reliability,scalability,cache | Techniques: agent_based,multi_agent_systems,prompt_engineering,few_shot,rag,embeddings,fine_tuning,evals,reranking,semantic_search,vector_search,human_in_the_loop,cost_optimization,latency_optimization,system_prompts,mcp,chunking,error_handling,a2a

**Source:** https://www.latent.space/p/notion

---

### 2. Hyper-Personalized Merchandising Through Hybrid LLM and Deep Learning Systems

**Company:** doordash

**Industry:** E-commerce

**Relevance score:** 132

**doordash / E-commerce** — DoorDash faced the challenge of personalizing experiences across a massive, diverse catalog spanning restaurants, grocery, retail, and other local commerce categories for millions of users with rapidly shifting intents. Traditional collaborative filtering and deep learning approaches could not adapt quickly enough to short-lived, high-context moments... — Tools: langchain,llama_index,pinecone,chromadb,qdrant,fastapi,postgresql,redis,cache,elasticsearch,monitoring,databases,api_gateway,microservices,orchestration,open_source,documentation | Techniques: rag,embeddings,fine_tuning,prompt_engineering,few_shot,semantic_search,vector_search,agent_based,multi_agent_systems,human_in_the_loop,latency_optimization,cost_optimization,chunking,evals,reranking

**Source:** https://www.infoq.com/presentations/llm-personalization/

---

### 3. Multi-Agent AI SRE System for Automated Incident Response and Root Cause Analysis

**Company:** opsworker.ai

**Industry:** Tech

**Relevance score:** 132

**opsworker.ai / Tech** — OpsWorker.ai developed a multi-agent AI SRE (Site Reliability Engineering) system to address the challenge of investigating and resolving complex system incidents in modern cloud-native environments. Traditional SRE automation relies on simple rules and alerts, but struggles with the complexity and data volume of Kubernetes-based microservices... — Tools: kubernetes,monitoring,orchestration,devops,scaling,microservices,databases,api_gateway,cicd,continuous_deployment,open_source,documentation,reliability,scalability,postgresql,mysql,redis,cache,elasticsearch | Techniques: multi_agent_systems,agent_based,prompt_engineering,error_handling,latency_optimization,human_in_the_loop

**Source:** https://www.opsworker.ai/blog/what-is-an-ai-sre-agent-and-how-we-implement-an-ai-sre-agent-at-opsworker-ai-multi-agent-logic/

---

### 4. Agent-Driven Development for AI Research Using GitHub Copilot CLI

**Company:** github

**Industry:** Tech

**Relevance score:** 127

**github / Tech** — Tyler McGoffin, a senior applied researcher on GitHub's Copilot Applied Science team, faced the challenge of analyzing hundreds of thousands of lines of code in agent trajectory files from evaluation benchmarks like TerminalBench2 and SWEBench-Pro. He developed 'eval-agents', a tool built primarily using GitHub Copilot... — Tools: cicd,documentation,open_source,devops,continuous_integration,continuous_deployment | Techniques: prompt_engineering,agent_based,multi_agent_systems,evals

**Source:** https://github.blog/ai-and-ml/github-copilot/agent-driven-development-in-copilot-applied-science/

---

### 5. Multi-Agent Orchestration for Enterprise Conversational AI

**Company:** atlassian

**Industry:** Tech

**Relevance score:** 124

**atlassian / Tech** — Atlassian evolved Rovo Chat, their conversational AI assistant for enterprise knowledge retrieval and workflow automation, from a single-agent RAG architecture to a hierarchical multi-agent orchestration system. The problem was that a single agent struggled to reliably handle diverse tasks and tools across different domains (Jira... — Tools: llama_index,langchain,monitoring | Techniques: multi_agent_systems,agent_based,rag,prompt_engineering,few_shot,semantic_search,vector_search,latency_optimization,error_handling,system_prompts,evals

**Source:** https://www.atlassian.com/blog/atlassian-engineering/how-rovo-embraces-multi-agent-orchestration

---

### 6. AI-Powered Multi-Agent Decision Support System for Strategic Business Decisions

**Company:** coinbase

**Industry:** Finance

**Relevance score:** 124

**coinbase / Finance** — Coinbase developed RAPID-D, an internal AI-powered decision support tool designed to augment their existing RAPID (Recommender, Agree, Perform, Input, Decider) decision-making framework. The system addresses the challenge of cognitive bias and unseen risks in critical strategic decisions by deploying a multi-agent architecture where specialized AI... — Tools: fastapi,monitoring,documentation | Techniques: multi_agent_systems,prompt_engineering,rag,semantic_search,human_in_the_loop,error_handling,evals

**Source:** https://www.coinbase.com/en-nl/blog/making-smarter-decisions-faster-with-AI-at-Coinbase

---

## Tools & Infrastructure

### 1. Cognitive Memory Agent: Building Stateful AI Agents with Multi-Layer Memory Architecture

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 132

**linkedin / Tech** — LinkedIn developed the Cognitive Memory Agent (CMA), a horizontal memory platform designed to enable stateful and context-aware AI agents at scale, initially deployed within their Hiring Assistant product. The problem addressed was that delivering truly agentic experiences required more than capable models—agents needed domain intelligence... — Tools: langchain,chromadb,pinecone,qdrant,postgresql,redis,cache,microservices,monitoring,scalability,open_source,documentation,security,guardrails,databases,orchestration | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,multi_agent_systems,agent_based,human_in_the_loop,latency_optimization,cost_optimization,chunking,system_prompts,evals

**Source:** https://www.linkedin.com/blog/engineering/ai/the-linkedin-generative-ai-application-tech-stack-personalization-with-cognitive-memory-agent

---

### 2. Multi-Agent AI Architecture for Site Reliability Engineering in Cloud-Native Infrastructure

**Company:** komodor

**Industry:** Tech

**Relevance score:** 132

**komodor / Tech** — Komodor introduced Klaudia AI, a multi-agent architecture designed to address the complexity of modern cloud-native infrastructure incident management. The problem stems from contemporary systems running hundreds of microservices across multi-cloud environments where symptoms appear in one place while root causes exist elsewhere, making single-agent AI... — Tools: kubernetes,docker,monitoring,databases,api_gateway,microservices,orchestration,devops,open_source,documentation,security,guardrails,reliability,scalability,vllm,postgresql,redis,langchain,pinecone,qdrant,wandb | Techniques: rag,embeddings,multi_agent_systems,agent_based,semantic_search,vector_search,prompt_engineering,error_handling,human_in_the_loop,evals

**Source:** https://komodor.com/blog/multi-agent-ai-sre-has-landed-and-its-built-for-your-most-complex-stacks/

---

### 3. Building Production Data Agents with Long-Running Context and Iterative Workflows

**Company:** hex

**Industry:** Tech

**Relevance score:** 127

**hex / Tech** — Hex, a data analytics platform, evolved from single-shot text-to-SQL features to building sophisticated multi-agent systems that operate across entire data notebooks and conversational threads. The company faced challenges with model context limitations, tool proliferation, and evaluation of iterative data work that doesn't lend itself to... — Tools: langchain,postgresql,monitoring,orchestration,databases | Techniques: agent_based,prompt_engineering,rag,embeddings,semantic_search,few_shot,human_in_the_loop,error_handling,multi_agent_systems,evals,system_prompts,mcp

**Source:** https://www.youtube.com/watch?v=Xyh1EqcjGME

---

### 4. Production AI Deployment: Lessons from Real-World Agentic AI Systems

**Company:** databricks_/_various

**Industry:** Healthcare

**Relevance score:** 122

**databricks_/_various / Healthcare** — This case study presents lessons learned from deploying generative AI applications in production, with a specific focus on Flo Health's implementation of a women's health chatbot on the Databricks platform. The presentation addresses common failure points in GenAI projects including poor constraint definition, over-reliance on... — Tools: monitoring,cicd,devops,orchestration,continuous_deployment,continuous_integration,open_source,guardrails,reliability,scalability,langchain,llama_index,databases,api_gateway,microservices,scaling,postgresql | Techniques: rag,fine_tuning,prompt_engineering,few_shot,agent_based,multi_agent_systems,human_in_the_loop,latency_optimization,cost_optimization,system_prompts,evals,token_optimization,error_handling,instruction_tuning

**Source:** https://www.youtube.com/watch?v=mMQq-KDKEbA

---
