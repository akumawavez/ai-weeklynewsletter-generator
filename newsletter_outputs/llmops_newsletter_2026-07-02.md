# Weekly LLMOps Newsletter — 2026-07-02

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

### 1. Building a Secure Kubernetes Platform for Autonomous AI Agents

**Company:** grab

**Industry:** Tech

**Relevance score:** 142

**grab / Tech** — Grab built Palana, a Kubernetes-native platform for running autonomous AI agents safely in production. As AI agents moved from experimental IDE plugins to long-running workloads that can access APIs, credentials, repositories, and internal services, Grab faced the challenge of providing teams with self-service agent deployment... — Tools: kubernetes,docker,monitoring,databases,orchestration,devops,security,guardrails,langchain,postgresql,redis,cache | Techniques: agent_based,multi_agent_systems,memory,harness_engineering,prompt_engineering

**Source:** https://engineering.grab.com/palana-part-1-secure-platform-for-ai-agents

---

### 2. Building a Production Data Agent for 90,000 Tables at Scale

**Company:** openai

**Industry:** Tech

**Relevance score:** 137

**openai / Tech** — OpenAI's data platform team built an internal data agent to help ~4,000 users navigate 1.5 exabytes of data across 90,000 datasets. The core challenge was not writing SQL queries but finding the right tables and understanding how to use them semantically, with analysts spending hours... — Tools: langchain,postgresql,redis,cache,pinecone,chromadb,qdrant,fastapi,spacy,monitoring,orchestration,databases,open_source,documentation | Techniques: embeddings,rag,semantic_search,vector_search,prompt_engineering,agent_based,memory,harness_engineering,chunking

**Source:** https://blog.bytebytego.com/p/how-openai-built-its-data-agent

---

### 3. Rapid AI Agent Development with Minimal Process Overhead

**Company:** gusto

**Industry:** HR

**Relevance score:** 132

**gusto / HR** — Gusto, a payroll and HR platform serving thousands of small businesses, rebuilt their application as an AI-powered agent platform called "Gusto Co-founder" in just 10 weeks using a team of four engineers and one designer. The problem they addressed was the extensive manual work business... — Tools: serverless,fastapi | Techniques: agent_based,prompt_engineering,evals,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=5FKBkUCaLa8

---

### 4. Conversational AI Shopping Assistant with Multi-Agent Architecture and Real-Time Grounding

**Company:** doordash

**Industry:** E-commerce

**Relevance score:** 132

**doordash / E-commerce** — DoorDash built a conversational AI shopping assistant called "Ask DoorDash" to help consumers discover restaurants and shop for groceries through natural language interactions. The system addresses the challenge of maintaining accurate grounding against rapidly changing local commerce data (menus, prices, inventory, ETAs) while providing personalized... — Tools: kubernetes,docker,monitoring,databases,api_gateway,microservices,cicd,scaling,serverless,devops,orchestration,continuous_deployment,continuous_integration,open_source,documentation,guardrails,reliability,scalability,cache,langchain | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,multi_agent_systems,agent_based,memory,latency_optimization,cost_optimization,evals,a2a,mcp

**Source:** https://careersatdoordash.com/blog/building-doordash-assistant-an-engineering-overview/

---

### 5. Building Production Agent Infrastructure with Claude Managed Agents

**Company:** anthropic_/_various

**Industry:** Tech

**Relevance score:** 132

**anthropic_/_various / Tech** — Anthropic introduced Claude Managed Agents, a platform designed to address the infrastructure bottlenecks that prevent organizations from deploying increasingly capable AI agents at scale. The platform tackles key challenges including context management, memory, reliability, security, and observability that developers face when building production agent systems... — Tools: kubernetes,docker,monitoring,api_gateway,microservices,serverless,orchestration,security,guardrails,reliability,scalability | Techniques: prompt_engineering,multi_agent_systems,memory,human_in_the_loop,error_handling

**Source:** https://www.youtube.com/watch?v=zenIB7XLZxQ

---

### 6. Enterprise AI Adoption Patterns and Production Agent Deployment at Scale

**Company:** mongodb

**Industry:** Tech

**Relevance score:** 132

**mongodb / Tech** — MongoDB's CEO shares insights from conversations with over 10 customers weekly across frontier labs, AI-native startups, and large enterprises, revealing different AI adoption patterns and production deployment challenges. While frontier labs use MongoDB for training data and inference layers, and AI-native companies like ElevenLabs achieve... — Tools: langchain,databases,open_source,documentation,monitoring,guardrails,compliance,security | Techniques: rag,embeddings,vector_search,semantic_search,agent_based,multi_agent_systems,memory,human_in_the_loop,cost_optimization,latency_optimization,prompt_engineering

**Source:** https://www.youtube.com/watch?v=k4l-rtwezVg

---

### 7. Building Self-Learning AI Agents for Site Reliability Engineering, Visual Asset Review, and Software Development

**Company:** cleric_/_puntt_/_tanagram

**Industry:** Tech

**Relevance score:** 132

**cleric_/_puntt_/_tanagram / Tech** — This case study presents three different production implementations of LLM-based agents: Cleric's self-learning SRE agent that automates on-call incident response, Puntt's visual asset review system for marketing materials compliance, and Tanagram's software factory approach for AI-assisted development. Cleric addresses the challenge of building trust in... — Tools: kubernetes,docker,monitoring,cicd,open_source,documentation | Techniques: agent_based,multi_agent_systems,prompt_engineering,evals,memory,harness_engineering,error_handling

**Source:** https://www.youtube.com/watch?v=iD50gwoce5w

---

### 8. Multi-Company Panel on Building Production-Grade AI Agent Systems

**Company:** abridge_/_replit_/_hebbia

**Industry:** Tech

**Relevance score:** 132

**abridge_/_replit_/_hebbia / Tech** — This panel discussion features engineering leaders from Abridge, Replit, and Hebbia discussing their experiences building sophisticated AI agent systems at production scale. Abridge tackles clinical documentation by recording and summarizing doctor-patient conversations for over 250 healthcare systems, addressing challenges around clinical compliance and trust. Replit... — Tools: docker,kubernetes,monitoring,databases,api_gateway,load_balancing,microservices,cicd,scaling,serverless,devops,orchestration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,pytorch,tensorflow,cache,redis | Techniques: rag,prompt_engineering,few_shot,model_optimization,cost_optimization,latency_optimization,harness_engineering,agent_based,multi_agent_systems,chunking,evals

**Source:** https://www.youtube.com/watch?v=uC2m61JpyDs

---

### 9. Platform-Driven AI Agent Orchestration for Large-Scale Engineering

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 129

**linkedin / Tech** — LinkedIn operates at massive scale with 1.3 billion members, 7,000 deployables, and 10,000+ repositories generating over a million PRs annually. To unlock engineering efficiency, LinkedIn built a comprehensive platform for AI agents that handles orchestration, tooling, context management, and evaluation. Rather than allowing fragmented implementations... — Tools: kubernetes,docker,monitoring,databases,api_gateway,microservices,cicd,orchestration,open_source,documentation,security,guardrails,reliability,scalability,langchain,crewai,redis,cache,elasticsearch | Techniques: agent_based,multi_agent_systems,mcp,prompt_engineering,rag,human_in_the_loop,memory,harness_engineering,few_shot,evals

**Source:** https://www.infoq.com/presentations/ai-multi-agentic-tools

---

### 10. Building Production-Grade Customer Experience Agents at Enterprise Scale

**Company:** sierra

**Industry:** Tech

**Relevance score:** 127

**sierra / Tech** — Sierra has built a comprehensive platform for deploying customer experience agents across sales, service, and loyalty touchpoints for Fortune 20 companies. The platform addresses the challenge of building reliable, low-latency conversational AI at enterprise scale by developing a modular architecture that orchestrates 10-15 different models... — Tools: monitoring,api_gateway,microservices,cicd,devops,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,postgresql,cache,langchain | Techniques: prompt_engineering,few_shot,model_optimization,error_handling,agent_based,harness_engineering,memory,latency_optimization,cost_optimization,fallback_strategies,system_prompts,mcp,a2a,evals,rag,fine_tuning,reranking

**Source:** https://www.youtube.com/watch?v=uCKhOmth2ms

---

### 11. Agentic AI for Title Operations Workflow Optimization

**Company:** rocket

**Industry:** Finance

**Relevance score:** 127

**rocket / Finance** — Rocket Close, a Detroit-based title agency within Rocket Companies, faced bottlenecks in title operations due to time-intensive state-specific examinations, manual research across fragmented systems, and complex local requirements that slowed mortgage processing. To address these challenges, they built Supercharger in collaboration with AWS—an agentic AI... — Tools: kubernetes,microservices,guardrails,compliance,monitoring,api_gateway,documentation,security | Techniques: rag,prompt_engineering,agent_based,multi_agent_systems,semantic_search,mcp,a2a

**Source:** https://aws.amazon.com/blogs/machine-learning/building-supercharger-how-rocket-close-optimized-title-operations-with-agentic-ai/

---

### 12. Agentic E-commerce Copilot for Merchant Store Management

**Company:** tiendanube_/_nuvemshop

**Industry:** E-commerce

**Relevance score:** 127

**tiendanube_/_nuvemshop / E-commerce** — Tiendanube/Nuvemshop, a Latin American e-commerce platform serving over 180,000 merchants, developed Lumi, an agentic copilot embedded directly into their merchant admin interface. The problem they addressed was enabling shop owners to manage their stores more efficiently through natural language interactions. Using LangChain as the foundational... — Tools: langchain | Techniques: agent_based,prompt_engineering

**Source:** https://x.com/tadeodonegana/status/2065113803398717909

---

### 13. AI Chatbots for Customer Service: Production Lessons from 90 Days

**Company:** edsdev

**Industry:** Tech

**Relevance score:** 127

**edsdev / Tech** — EdsDev deployed multiple customer service chatbots for clients and shares production insights after 90 days of operation. The problem addressed was handling customer service inquiries at scale while maintaining quality and satisfaction. Their solution combined RAG-based retrieval systems with LLMs (primarily Claude 3.5 Sonnet and... — Tools: langchain,monitoring | Techniques: rag,embeddings,reranking,prompt_engineering,semantic_search,vector_search,chunking,error_handling,human_in_the_loop,agent_based,evals

**Source:** https://edsdev.ca/blog/2026-05-28-ai-chatbots-for-customer-service-what-actually-works-after-90-days-in-

---

### 14. Panel Discussion on AI Agents in Production: Security, Evaluation, and Infrastructure

**Company:** zenity_/_hetz_/_aidoc_/_band_/_mongodb

**Industry:** Tech

**Relevance score:** 127

**zenity_/_hetz_/_aidoc_/_band_/_mongodb / Tech** — This panel discussion brings together practitioners from multiple companies to discuss the challenges and best practices of deploying AI agents in production environments. The panelists, representing companies like aidoc (medical AI), Zenity (AI agent security), Band (agent communication infrastructure), and MongoDB (data layer for AI... — Tools: monitoring,databases,microservices,security,guardrails,langchain,chromadb,pinecone,qdrant,postgresql,mysql,sqlite,redis,cache | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,model_optimization,fine_tuning,multi_agent_systems,agent_based,memory,evals

**Source:** https://www.youtube.com/watch?v=BQ6aIRYYwh4

---

### 15. Building Production AI Customer Support Agents with Multi-Agent Architecture and Human-in-the-Loop Design

**Company:** lorikeet

**Industry:** Tech

**Relevance score:** 127

**lorikeet / Tech** — Lorikeet is an AI customer support startup that evolved from building basic automation tools to creating sophisticated multi-agent systems for handling customer support at scale. The company developed two primary agents: a customer-facing concierge agent that handles support tickets across email, live chat, and voice... — Tools: langchain,monitoring,databases,api_gateway,guardrails,open_source | Techniques: multi_agent_systems,prompt_engineering,human_in_the_loop,agent_based,evals,system_prompts,error_handling,harness_engineering

**Source:** https://www.youtube.com/watch?v=eZj1xSiyd9U

---

### 16. Building an AI-Powered Slack Agent with MCP Standardization

**Company:** duolingo

**Industry:** Education

**Relevance score:** 127

**duolingo / Education** — Duolingo developed an AI-powered Slack bot to democratize access to their Model Context Protocol (MCP) infrastructure after discovering that manual MCP server setup was too complex for widespread adoption. The journey began with individual engineers connecting MCP servers to local editors in late 2024, evolved... — Tools: fastapi,docker,monitoring,security,guardrails,open_source,documentation,cicd,orchestration,postgresql | Techniques: mcp,prompt_engineering,human_in_the_loop,multi_agent_systems,agent_based,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=5sb9iA2v78g

---

### 17. Building Trustworthy AI Agents for Automated Expense Management

**Company:** ramp

**Industry:** Finance

**Relevance score:** 124

**ramp / Finance** — Ramp built and deployed a suite of LLM-backed agents to automate expense management workflows, focusing specifically on expense approval processes that traditionally required manual manager review. The solution emphasizes transparency through explicit reasoning and citations, implements escape hatches for uncertain decisions, enables collaborative context refinement... — Tools: guardrails,documentation | Techniques: prompt_engineering,human_in_the_loop,agent_based,evals,error_handling,fallback_strategies

**Source:** https://builders.ramp.com/post/how-to-build-agents-users-can-trust

---

### 18. AI Agent for Automated Merchant Classification Correction

**Company:** ramp

**Industry:** Finance

**Relevance score:** 124

**ramp / Finance** — Ramp, a corporate card and expense management platform, faced a scaling challenge with incorrect merchant classifications that frustrated customers and required hours of manual intervention from support and engineering teams. The company built an AI agent using LLMs combined with RAG, embeddings, OLAP queries, and... — Tools: guardrails | Techniques: rag,embeddings,prompt_engineering,agent_based,error_handling,evals

**Source:** https://builders.ramp.com/post/fixing-merchant-classifications-with-ai

---

### 19. AI-Powered Consent Education Tool for Preventing Gender-Based Violence

**Company:** override

**Industry:** Other

**Relevance score:** 122

**override / Other** — Override Labs developed "Is This Okay?" (ITO), a nonprofit AI chatbot designed to prevent sexual assault among high school-aged teenagers by providing judgment-free guidance on sexually ambiguous scenarios. The product uses Claude LLM with carefully designed system prompts incorporating motivational interviewing techniques, hard-coded risk classification... — Tools: postgresql | Techniques: prompt_engineering,system_prompts,evals

**Source:** https://www.youtube.com/watch?v=P51t3JJCag8

---

## Cool Use Cases

### 1. Agent Memory System for Personalized Food Ordering and Discovery

**Company:** doordash

**Industry:** E-commerce

**Relevance score:** 127

**doordash / E-commerce** — DoorDash built an agent memory system to power their Ask DoorDash conversational ordering experience, addressing the challenge of enabling AI agents to maintain persistent, structured understanding of user preferences across sessions. The solution connects their long-term memory platform with live agents through a three-layer architecture... — Tools: llama_index,langchain,pinecone,chromadb,qdrant,postgresql,redis,cache,fastapi,monitoring | Techniques: embeddings,vector_search,semantic_search,rag,prompt_engineering,memory,agent_based,multi_agent_systems,chunking

**Source:** https://careersatdoordash.com/blog/building-ask-doordash-part-two-intelligence/

---

### 2. AI-Powered Customer Feedback Analysis System for Container Shipping

**Company:** hapag-lloyd

**Industry:** Other

**Relevance score:** 127

**hapag-lloyd / Other** — Hapag-Lloyd, a global container shipping company, transformed their manual and time-consuming customer feedback analysis process into an automated AI-powered system using Amazon Bedrock. Previously, product managers spent hours or days manually categorizing sentiment and themes from hundreds of feedback comments exported as CSV files. The... — Tools: langchain,elasticsearch,monitoring,serverless,orchestration,open_source,guardrails | Techniques: embeddings,rag,prompt_engineering,multi_agent_systems,agent_based,semantic_search

**Source:** https://aws.amazon.com/blogs/machine-learning/how-hapag-lloyd-uses-amazon-bedrock-to-transform-customer-feedback-into-actionable-insights/

---

### 3. Building Custom Agents at Scale: Notion's Multi-Year Journey to Production-Ready Agentic Workflows

**Company:** notion

**Industry:** Tech

**Relevance score:** 127

**notion / Tech** — Notion, a knowledge work platform serving enterprise customers, spent multiple years (2022-2026) iterating through four to five complete rebuilds of their agent infrastructure before shipping Custom Agents to production. The core problem was enabling users to automate complex workflows across their workspaces while maintaining enterprise-grade... — Tools: langchain,postgresql,sqlite,elasticsearch,fastapi,docker,kubernetes,cicd,monitoring,databases,api_gateway,microservices,orchestration,open_source,documentation,security,guardrails,reliability,scalability,cache | Techniques: agent_based,multi_agent_systems,prompt_engineering,few_shot,rag,embeddings,fine_tuning,evals,reranking,semantic_search,vector_search,human_in_the_loop,cost_optimization,latency_optimization,system_prompts,mcp,chunking,error_handling,a2a

**Source:** https://www.latent.space/p/notion

---

## Tools & Infrastructure

### 1. Kubernetes-Native Secure Execution Platform for Autonomous AI Agents

**Company:** grab

**Industry:** Tech

**Relevance score:** 137

**grab / Tech** — Grab, Southeast Asia's leading superapp, developed Palana, a Kubernetes-native secure execution platform designed to enable autonomous AI agents to operate in production environments while maintaining strict isolation, identity, and auditability controls. The platform addresses the fundamental challenge of allowing AI agents to perform useful work... — Tools: kubernetes,docker,monitoring,databases,api_gateway,microservices,cicd,devops,orchestration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,redis,cache | Techniques: agent_based,multi_agent_systems,prompt_engineering,human_in_the_loop

**Source:** https://engineering.grab.com/part-2-palana-architecture

---

### 2. Production AI Framework for Retail Banking Chatbot

**Company:** databricks

**Industry:** Finance

**Relevance score:** 132

**databricks / Finance** — A retail banking institution was struggling with a chatbot that failed to scale from demo to production, receiving 20,000 customer calls per month with 60% being simple queries that could be automated. The organization had spent $85K over 6 months on a failed POC that... — Tools: crewai,langchain,monitoring,databases,api_gateway,orchestration,guardrails,documentation,open_source | Techniques: rag,embeddings,prompt_engineering,multi_agent_systems,agent_based,human_in_the_loop,error_handling,fallback_strategies,evals,semantic_search,vector_search

**Source:** https://www.youtube.com/watch?v=ObTPqBGsEbA

---
