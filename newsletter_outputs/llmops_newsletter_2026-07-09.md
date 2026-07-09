# Weekly LLMOps Newsletter — 2026-07-09

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Research Highlights

### 1. AI Agents for Life Sciences R&D: Accelerating Drug Discovery with Context-Rich Data

**Company:** benchling

**Industry:** Healthcare

**Relevance score:** 132

**benchling / Healthcare** — Benchling, a 14-year-old platform for life sciences R&D data management, launched Benchling AI six months ago to bring intelligent agents to scientific workflows. The problem scientists face is the time-consuming nature of drug discovery, from initial experiments to FDA submissions, involving manual data entry, analysis... — Tools: fastapi,postgresql,monitoring,databases,open_source,documentation,security,compliance,guardrails | Techniques: rag,embeddings,prompt_engineering,multi_agent_systems,agent_based,harness_engineering,memory,human_in_the_loop,semantic_search,vector_search,chunking,system_prompts,evals

**Source:** https://www.youtube.com/watch?v=RjpTrffSMjE

---

## Industry News

### 1. Marketing Campaign Forecasting with Semantic Retrieval and RAG

**Company:** target

**Industry:** E-commerce

**Relevance score:** 137

**target / E-commerce** — Target's marketing teams needed to accurately forecast campaign performance before launch to optimize budget allocation and improve guest experiences. The company rebuilt their campaign similarity matching system using a RAG architecture that combines semantic embeddings, retrieval from historical campaign data, and LLM-based filtering and ranking... — Techniques: rag,embeddings,prompt_engineering,reranking,semantic_search,few_shot

**Source:** https://tech.target.com/blog/scaling-marketing-campaign-forecasting-ai

---

### 2. Conversational AI Shopping Assistant with Multi-Agent Architecture and Real-Time Grounding

**Company:** doordash

**Industry:** E-commerce

**Relevance score:** 132

**doordash / E-commerce** — DoorDash built a conversational AI shopping assistant called "Ask DoorDash" to help consumers discover restaurants and shop for groceries through natural language interactions. The system addresses the challenge of maintaining accurate grounding against rapidly changing local commerce data (menus, prices, inventory, ETAs) while providing personalized... — Tools: kubernetes,docker,monitoring,databases,api_gateway,microservices,cicd,scaling,serverless,devops,orchestration,continuous_deployment,continuous_integration,open_source,documentation,guardrails,reliability,scalability,cache,langchain | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,multi_agent_systems,agent_based,memory,latency_optimization,cost_optimization,evals,a2a,mcp

**Source:** https://careersatdoordash.com/blog/building-doordash-assistant-an-engineering-overview/

---

### 3. Building Production Agent Infrastructure with Claude Managed Agents

**Company:** anthropic_/_various

**Industry:** Tech

**Relevance score:** 132

**anthropic_/_various / Tech** — Anthropic introduced Claude Managed Agents, a platform designed to address the infrastructure bottlenecks that prevent organizations from deploying increasingly capable AI agents at scale. The platform tackles key challenges including context management, memory, reliability, security, and observability that developers face when building production agent systems... — Tools: kubernetes,docker,monitoring,api_gateway,microservices,serverless,orchestration,security,guardrails,reliability,scalability | Techniques: prompt_engineering,multi_agent_systems,memory,human_in_the_loop,error_handling

**Source:** https://www.youtube.com/watch?v=zenIB7XLZxQ

---

### 4. Enterprise AI Adoption Patterns and Production Agent Deployment at Scale

**Company:** mongodb

**Industry:** Tech

**Relevance score:** 132

**mongodb / Tech** — MongoDB's CEO shares insights from conversations with over 10 customers weekly across frontier labs, AI-native startups, and large enterprises, revealing different AI adoption patterns and production deployment challenges. While frontier labs use MongoDB for training data and inference layers, and AI-native companies like ElevenLabs achieve... — Tools: langchain,databases,open_source,documentation,monitoring,guardrails,compliance,security | Techniques: rag,embeddings,vector_search,semantic_search,agent_based,multi_agent_systems,memory,human_in_the_loop,cost_optimization,latency_optimization,prompt_engineering

**Source:** https://www.youtube.com/watch?v=k4l-rtwezVg

---

### 5. Platform-Driven AI Agent Orchestration for Large-Scale Engineering

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 129

**linkedin / Tech** — LinkedIn operates at massive scale with 1.3 billion members, 7,000 deployables, and 10,000+ repositories generating over a million PRs annually. To unlock engineering efficiency, LinkedIn built a comprehensive platform for AI agents that handles orchestration, tooling, context management, and evaluation. Rather than allowing fragmented implementations... — Tools: kubernetes,docker,monitoring,databases,api_gateway,microservices,cicd,orchestration,open_source,documentation,security,guardrails,reliability,scalability,langchain,crewai,redis,cache,elasticsearch | Techniques: agent_based,multi_agent_systems,mcp,prompt_engineering,rag,human_in_the_loop,memory,harness_engineering,few_shot,evals

**Source:** https://www.infoq.com/presentations/ai-multi-agentic-tools

---

### 6. LLM-Powered Spark SQL Plan Analysis for Performance Optimization

**Company:** expedia

**Industry:** Tech

**Relevance score:** 127

**expedia / Tech** — Expedia Group developed an automated, LLM-powered workflow to analyze Apache Spark SQL execution plans and identify performance bottlenecks in long-running data processing jobs. The system uses structured prompting with an open-source Spark MCP server to detect specific anti-patterns such as missing broadcast joins, skewed partitions... — Tools: open_source,documentation | Techniques: prompt_engineering,cost_optimization,latency_optimization,mcp

**Source:** https://medium.com/expedia-group-tech/using-llms-to-analyze-spark-sql-plans-a-practical-approach-to-debugging-long-running-jobs-35eace7eeec4

---

### 7. Building Production-Grade Customer Experience Agents at Enterprise Scale

**Company:** sierra

**Industry:** Tech

**Relevance score:** 127

**sierra / Tech** — Sierra has built a comprehensive platform for deploying customer experience agents across sales, service, and loyalty touchpoints for Fortune 20 companies. The platform addresses the challenge of building reliable, low-latency conversational AI at enterprise scale by developing a modular architecture that orchestrates 10-15 different models... — Tools: monitoring,api_gateway,microservices,cicd,devops,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,postgresql,cache,langchain | Techniques: prompt_engineering,few_shot,model_optimization,error_handling,agent_based,harness_engineering,memory,latency_optimization,cost_optimization,fallback_strategies,system_prompts,mcp,a2a,evals,rag,fine_tuning,reranking

**Source:** https://www.youtube.com/watch?v=uCKhOmth2ms

---

### 8. Agentic AI for Title Operations Workflow Optimization

**Company:** rocket

**Industry:** Finance

**Relevance score:** 127

**rocket / Finance** — Rocket Close, a Detroit-based title agency within Rocket Companies, faced bottlenecks in title operations due to time-intensive state-specific examinations, manual research across fragmented systems, and complex local requirements that slowed mortgage processing. To address these challenges, they built Supercharger in collaboration with AWS—an agentic AI... — Tools: kubernetes,microservices,guardrails,compliance,monitoring,api_gateway,documentation,security | Techniques: rag,prompt_engineering,agent_based,multi_agent_systems,semantic_search,mcp,a2a

**Source:** https://aws.amazon.com/blogs/machine-learning/building-supercharger-how-rocket-close-optimized-title-operations-with-agentic-ai/

---

### 9. Agentic E-commerce Copilot for Merchant Store Management

**Company:** tiendanube_/_nuvemshop

**Industry:** E-commerce

**Relevance score:** 127

**tiendanube_/_nuvemshop / E-commerce** — Tiendanube/Nuvemshop, a Latin American e-commerce platform serving over 180,000 merchants, developed Lumi, an agentic copilot embedded directly into their merchant admin interface. The problem they addressed was enabling shop owners to manage their stores more efficiently through natural language interactions. Using LangChain as the foundational... — Tools: langchain | Techniques: agent_based,prompt_engineering

**Source:** https://x.com/tadeodonegana/status/2065113803398717909

---

### 10. AI Chatbots for Customer Service: Production Lessons from 90 Days

**Company:** edsdev

**Industry:** Tech

**Relevance score:** 127

**edsdev / Tech** — EdsDev deployed multiple customer service chatbots for clients and shares production insights after 90 days of operation. The problem addressed was handling customer service inquiries at scale while maintaining quality and satisfaction. Their solution combined RAG-based retrieval systems with LLMs (primarily Claude 3.5 Sonnet and... — Tools: langchain,monitoring | Techniques: rag,embeddings,reranking,prompt_engineering,semantic_search,vector_search,chunking,error_handling,human_in_the_loop,agent_based,evals

**Source:** https://edsdev.ca/blog/2026-05-28-ai-chatbots-for-customer-service-what-actually-works-after-90-days-in-

---

### 11. Building a Production Data Agent for 90,000 Tables at Scale

**Company:** openai

**Industry:** Tech

**Relevance score:** 127

**openai / Tech** — OpenAI's data platform team built an internal data agent to help ~4,000 users navigate 1.5 exabytes of data across 90,000 datasets. The core challenge was not writing SQL queries but finding the right tables and understanding how to use them semantically, with analysts spending hours... — Tools: langchain,postgresql,redis,cache,pinecone,chromadb,qdrant,fastapi,spacy,monitoring,orchestration,databases,open_source,documentation | Techniques: embeddings,rag,semantic_search,vector_search,prompt_engineering,agent_based,memory,harness_engineering,chunking

**Source:** https://blog.bytebytego.com/p/how-openai-built-its-data-agent

---

### 12. Building Production AI Customer Support Agents with Multi-Agent Architecture and Human-in-the-Loop Design

**Company:** lorikeet

**Industry:** Tech

**Relevance score:** 127

**lorikeet / Tech** — Lorikeet is an AI customer support startup that evolved from building basic automation tools to creating sophisticated multi-agent systems for handling customer support at scale. The company developed two primary agents: a customer-facing concierge agent that handles support tickets across email, live chat, and voice... — Tools: langchain,monitoring,databases,api_gateway,guardrails,open_source | Techniques: multi_agent_systems,prompt_engineering,human_in_the_loop,agent_based,evals,system_prompts,error_handling,harness_engineering

**Source:** https://www.youtube.com/watch?v=eZj1xSiyd9U

---

### 13. Building an AI-Powered Slack Agent with MCP Standardization

**Company:** duolingo

**Industry:** Education

**Relevance score:** 127

**duolingo / Education** — Duolingo developed an AI-powered Slack bot to democratize access to their Model Context Protocol (MCP) infrastructure after discovering that manual MCP server setup was too complex for widespread adoption. The journey began with individual engineers connecting MCP servers to local editors in late 2024, evolved... — Tools: fastapi,docker,monitoring,security,guardrails,open_source,documentation,cicd,orchestration,postgresql | Techniques: mcp,prompt_engineering,human_in_the_loop,multi_agent_systems,agent_based,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=5sb9iA2v78g

---

### 14. Building LangSmith Engine: An Autonomous Agent for Agent Debugging and Improvement

**Company:** langchain

**Industry:** Tech

**Relevance score:** 122

**langchain / Tech** — LangChain developed LangSmith Engine, an autonomous agent that continuously monitors production agent traces, identifies failures, clusters them into actionable issues, and proposes code fixes. The problem was the manual, time-intensive process of agent debugging where engineers had to manually review traces, identify patterns, write fixes... — Tools: langchain,docker,monitoring,databases,cicd,continuous_integration,continuous_deployment,open_source,documentation,guardrails,fastapi,postgresql | Techniques: agent_based,multi_agent_systems,prompt_engineering,memory,evals,cost_optimization,latency_optimization,error_handling,human_in_the_loop,few_shot,system_prompts

**Source:** https://www.youtube.com/watch?v=YqjR4vQwbTc

---

### 15. Second-Order Automation: Multi-Agent System for Finance Workflow Generation

**Company:** ramp

**Industry:** Finance

**Relevance score:** 122

**ramp / Finance** — Ramp built a two-agent system to automate finance and accounting workflows, addressing the challenge that their original finance agent required extensive manual prompt engineering for each use. The solution consists of an "Architect" agent that watches screen recordings of accountants performing tasks and automatically generates... — Tools: fastapi | Techniques: prompt_engineering,multi_agent_systems,agent_based,system_prompts,error_handling

**Source:** https://x.com/RampLabs/status/1973768224253632953

---

### 16. Building a Secure Kubernetes Platform for Autonomous AI Agents

**Company:** grab

**Industry:** Tech

**Relevance score:** 122

**grab / Tech** — Grab built Palana, a Kubernetes-native platform for running autonomous AI agents safely in production. As AI agents moved from experimental IDE plugins to long-running workloads that can access APIs, credentials, repositories, and internal services, Grab faced the challenge of providing teams with self-service agent deployment... — Tools: kubernetes,docker,monitoring,databases,orchestration,devops,security,guardrails,langchain,postgresql,redis,cache | Techniques: agent_based,multi_agent_systems,memory,harness_engineering,prompt_engineering

**Source:** https://engineering.grab.com/palana-part-1-secure-platform-for-ai-agents

---

### 17. Building Kepler: An AI Data Analyst Agent for Internal Data Exploration

**Company:** openai

**Industry:** Tech

**Relevance score:** 122

**openai / Tech** — OpenAI built Kepler, an internal AI-powered data analyst agent, to solve the problem of answering data questions across 600+ petabytes of data and 70,000 datasets. The agent uses LLMs with Model Context Protocol (MCP), automated code crawling, RAG-based retrieval, and semantic memory to provide contextualized... — Tools: langchain,databases,cache,security,compliance | Techniques: rag,embeddings,prompt_engineering,semantic_search,agent_based,memory,evals,mcp

**Source:** https://www.infoq.com/presentations/data-aware-ai-agents/

---

### 18. Frontier Intelligence Platform: Microsoft's Multi-Model Harness Strategy for Enterprise AI

**Company:** microsoft

**Industry:** Tech

**Relevance score:** 122

**microsoft / Tech** — This case study captures Microsoft CEO Satya Nadella's comprehensive vision for deploying LLMs in production at enterprise scale, presented at Microsoft Build 2026. The core problem addressed is enabling every company to operate at the "frontier" of AI capabilities while maintaining independence and value capture... — Tools: monitoring,databases,orchestration,open_source,guardrails,scalability,cicd,devops,microservices,security,compliance,redis,cache | Techniques: multi_agent_systems,agent_based,prompt_engineering,reinforcement_learning,rlhf,few_shot,evals,token_optimization,model_optimization,harness_engineering,human_in_the_loop

**Source:** https://www.latent.space/p/satya-2026

---

## Cool Use Cases

### 1. Building Production-Scale Voice and Multi-Modal Customer Experience Agents

**Company:** sierra

**Industry:** Tech

**Relevance score:** 142

**sierra / Tech** — Sierra has built an enterprise agent platform serving most of the Fortune 20 companies, focusing on customer experience across sales, service, and loyalty touchpoints. The platform addresses the challenge of building reliable, low-latency conversational agents that can handle complex customer interactions across voice and chat... — Tools: monitoring,api_gateway,microservices,cicd,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,postgresql,cache,langchain | Techniques: prompt_engineering,few_shot,semantic_search,vector_search,model_optimization,token_optimization,error_handling,multi_agent_systems,agent_based,harness_engineering,memory,latency_optimization,cost_optimization,fallback_strategies,system_prompts,mcp,a2a,evals,fine_tuning,reranking,rag,embeddings,reinforcement_learning

**Source:** https://www.youtube.com/watch?v=uCKhOmth2ms

---

### 2. Agent Memory System for Personalized Food Ordering and Discovery

**Company:** doordash

**Industry:** E-commerce

**Relevance score:** 127

**doordash / E-commerce** — DoorDash built an agent memory system to power their Ask DoorDash conversational ordering experience, addressing the challenge of enabling AI agents to maintain persistent, structured understanding of user preferences across sessions. The solution connects their long-term memory platform with live agents through a three-layer architecture... — Tools: llama_index,langchain,pinecone,chromadb,qdrant,postgresql,redis,cache,fastapi,monitoring | Techniques: embeddings,vector_search,semantic_search,rag,prompt_engineering,memory,agent_based,multi_agent_systems,chunking

**Source:** https://careersatdoordash.com/blog/building-ask-doordash-part-two-intelligence/

---

### 3. AI-Powered Customer Feedback Analysis System for Container Shipping

**Company:** hapag-lloyd

**Industry:** Other

**Relevance score:** 127

**hapag-lloyd / Other** — Hapag-Lloyd, a global container shipping company, transformed their manual and time-consuming customer feedback analysis process into an automated AI-powered system using Amazon Bedrock. Previously, product managers spent hours or days manually categorizing sentiment and themes from hundreds of feedback comments exported as CSV files. The... — Tools: langchain,elasticsearch,monitoring,serverless,orchestration,open_source,guardrails | Techniques: embeddings,rag,prompt_engineering,multi_agent_systems,agent_based,semantic_search

**Source:** https://aws.amazon.com/blogs/machine-learning/how-hapag-lloyd-uses-amazon-bedrock-to-transform-customer-feedback-into-actionable-insights/

---

### 4. Building Custom Agents at Scale: Notion's Multi-Year Journey to Production-Ready Agentic Workflows

**Company:** notion

**Industry:** Tech

**Relevance score:** 127

**notion / Tech** — Notion, a knowledge work platform serving enterprise customers, spent multiple years (2022-2026) iterating through four to five complete rebuilds of their agent infrastructure before shipping Custom Agents to production. The core problem was enabling users to automate complex workflows across their workspaces while maintaining enterprise-grade... — Tools: langchain,postgresql,sqlite,elasticsearch,fastapi,docker,kubernetes,cicd,monitoring,databases,api_gateway,microservices,orchestration,open_source,documentation,security,guardrails,reliability,scalability,cache | Techniques: agent_based,multi_agent_systems,prompt_engineering,few_shot,rag,embeddings,fine_tuning,evals,reranking,semantic_search,vector_search,human_in_the_loop,cost_optimization,latency_optimization,system_prompts,mcp,chunking,error_handling,a2a

**Source:** https://www.latent.space/p/notion

---

## Tools & Infrastructure

### 1. Production AI Framework for Retail Banking Chatbot

**Company:** databricks

**Industry:** Finance

**Relevance score:** 132

**databricks / Finance** — A retail banking institution was struggling with a chatbot that failed to scale from demo to production, receiving 20,000 customer calls per month with 60% being simple queries that could be automated. The organization had spent $85K over 6 months on a failed POC that... — Tools: crewai,langchain,monitoring,databases,api_gateway,orchestration,guardrails,documentation,open_source | Techniques: rag,embeddings,prompt_engineering,multi_agent_systems,agent_based,human_in_the_loop,error_handling,fallback_strategies,evals,semantic_search,vector_search

**Source:** https://www.youtube.com/watch?v=ObTPqBGsEbA

---

### 2. Scaling Multimodal AI for Autonomous Trucking with Ray

**Company:** torc_robotics

**Industry:** Automotive

**Relevance score:** 122

**torc_robotics / Automotive** — Torc Robotics, a company developing autonomous semi-truck technology with over 20 years of experience in safety-critical self-driving applications, faced significant challenges in scaling their multimodal AI workloads for their AV 3.0 architecture. The company needed to handle massive amounts of diverse sensor data including camera... — Tools: kubernetes,docker,monitoring,databases,microservices,scaling,serverless,devops,orchestration,open_source,scalability,pytorch,fastapi,redis,cache | Techniques: reinforcement_learning,model_optimization,latency_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=8UFDsr6B6BY

---
