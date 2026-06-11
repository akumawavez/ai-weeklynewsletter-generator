# Weekly LLMOps Newsletter — 2026-06-11

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Research Highlights

### 1. AI Agents for Life Sciences R&D: Accelerating Drug Discovery with Context-Rich Data

**Company:** benchling

**Industry:** Healthcare

**Relevance score:** 152

**benchling / Healthcare** — Benchling, a 14-year-old platform for life sciences R&D data management, launched Benchling AI six months ago to bring intelligent agents to scientific workflows. The problem scientists face is the time-consuming nature of drug discovery, from initial experiments to FDA submissions, involving manual data entry, analysis... — Tools: fastapi,postgresql,monitoring,databases,open_source,documentation,security,compliance,guardrails | Techniques: rag,embeddings,prompt_engineering,multi_agent_systems,agent_based,harness_engineering,memory,human_in_the_loop,semantic_search,vector_search,chunking,system_prompts,evals

**Source:** https://www.youtube.com/watch?v=RjpTrffSMjE

---

### 2. Hybrid Agent Architecture with Open-Source Workers and Frontier Advisors for Legal AI

**Company:** harvey

**Industry:** Legal

**Relevance score:** 122

**harvey / Legal** — Fireworks and Harvey partnered to explore cost-effective approaches to achieving frontier-level performance on legal AI tasks using the Legal Agent Benchmark (LAB). The team investigated two primary strategies: a hybrid agent harness combining an open-source GLM 5.1 worker model with Claude Opus 4.7 as a... — Tools: open_source | Techniques: fine_tuning,multi_agent_systems,cost_optimization,harness_engineering,instruction_tuning,agent_based,evals

**Source:** https://fireworks.ai/blog/open-source-agents-frontier-advisors

---

## Industry News

### 1. Platform-Driven AI Agent Orchestration for Large-Scale Engineering

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 149

**linkedin / Tech** — LinkedIn operates at massive scale with 1.3 billion members, 7,000 deployables, and 10,000+ repositories generating over a million PRs annually. To unlock engineering efficiency, LinkedIn built a comprehensive platform for AI agents that handles orchestration, tooling, context management, and evaluation. Rather than allowing fragmented implementations... — Tools: kubernetes,docker,monitoring,databases,api_gateway,microservices,cicd,orchestration,open_source,documentation,security,guardrails,reliability,scalability,langchain,crewai,redis,cache,elasticsearch | Techniques: agent_based,multi_agent_systems,mcp,prompt_engineering,rag,human_in_the_loop,memory,harness_engineering,few_shot,evals

**Source:** https://www.infoq.com/presentations/ai-multi-agentic-tools

---

### 2. Building a Production Data Agent for 90,000 Tables at Scale

**Company:** openai

**Industry:** Tech

**Relevance score:** 137

**openai / Tech** — OpenAI's data platform team built an internal data agent to help ~4,000 users navigate 1.5 exabytes of data across 90,000 datasets. The core challenge was not writing SQL queries but finding the right tables and understanding how to use them semantically, with analysts spending hours... — Tools: langchain,postgresql,redis,cache,pinecone,chromadb,qdrant,fastapi,spacy,monitoring,orchestration,databases,open_source,documentation | Techniques: embeddings,rag,semantic_search,vector_search,prompt_engineering,agent_based,memory,harness_engineering,chunking

**Source:** https://blog.bytebytego.com/p/how-openai-built-its-data-agent

---

### 3. Building Production AI Customer Support Agents with Multi-Agent Architecture and Human-in-the-Loop Design

**Company:** lorikeet

**Industry:** Tech

**Relevance score:** 137

**lorikeet / Tech** — Lorikeet is an AI customer support startup that evolved from building basic automation tools to creating sophisticated multi-agent systems for handling customer support at scale. The company developed two primary agents: a customer-facing concierge agent that handles support tickets across email, live chat, and voice... — Tools: langchain,monitoring,databases,api_gateway,guardrails,open_source | Techniques: multi_agent_systems,prompt_engineering,human_in_the_loop,agent_based,evals,system_prompts,error_handling,harness_engineering

**Source:** https://www.youtube.com/watch?v=eZj1xSiyd9U

---

### 4. Building Self-Learning AI Agents for Site Reliability Engineering, Visual Asset Review, and Software Development

**Company:** cleric_/_puntt_/_tanagram

**Industry:** Tech

**Relevance score:** 132

**cleric_/_puntt_/_tanagram / Tech** — This case study presents three different production implementations of LLM-based agents: Cleric's self-learning SRE agent that automates on-call incident response, Puntt's visual asset review system for marketing materials compliance, and Tanagram's software factory approach for AI-assisted development. Cleric addresses the challenge of building trust in... — Tools: kubernetes,docker,monitoring,cicd,open_source,documentation | Techniques: agent_based,multi_agent_systems,prompt_engineering,evals,memory,harness_engineering,error_handling

**Source:** https://www.youtube.com/watch?v=iD50gwoce5w

---

### 5. Multi-Company Panel on Building Production-Grade AI Agent Systems

**Company:** abridge_/_replit_/_hebbia

**Industry:** Tech

**Relevance score:** 132

**abridge_/_replit_/_hebbia / Tech** — This panel discussion features engineering leaders from Abridge, Replit, and Hebbia discussing their experiences building sophisticated AI agent systems at production scale. Abridge tackles clinical documentation by recording and summarizing doctor-patient conversations for over 250 healthcare systems, addressing challenges around clinical compliance and trust. Replit... — Tools: docker,kubernetes,monitoring,databases,api_gateway,load_balancing,microservices,cicd,scaling,serverless,devops,orchestration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,pytorch,tensorflow,cache,redis | Techniques: rag,prompt_engineering,few_shot,model_optimization,cost_optimization,latency_optimization,harness_engineering,agent_based,multi_agent_systems,chunking,evals

**Source:** https://www.youtube.com/watch?v=uC2m61JpyDs

---

### 6. Building Production-Ready Coding Agents with Skills and Observability

**Company:** langfuse_/_clickhouse

**Industry:** Tech

**Relevance score:** 132

**langfuse_/_clickhouse / Tech** — Langfuse, an open-source LLM observability platform, faced the challenge of helping thousands of users integrate their complex tracing and evaluation system into diverse codebases through 478+ pages of documentation. The team built a custom "skill" for coding agents (like Claude Code) that acts as an... — Tools: langchain,open_source,documentation,cicd,monitoring | Techniques: agent_based,prompt_engineering,rag,semantic_search,few_shot,evals,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=vNCY9kXXyDQ

---

### 7. AI-Powered Search and Agent Automation for Digital Asset Management

**Company:** bynder

**Industry:** Media & Entertainment

**Relevance score:** 132

**bynder / Media & Entertainment** — Bynder, a digital asset management platform serving retail and CPG customers, faced significant operational bottlenecks as users had to manually tag and categorize all uploaded content for searchability. To address this, Bynder built AI search capabilities and four types of configurable AI agents using AWS... — Tools: postgresql,mysql,fastapi,elasticsearch,guardrails,microservices | Techniques: embeddings,prompt_engineering,semantic_search,vector_search,agent_based,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=Kyym50EgUOQ

---

### 8. Multi-Agent AI Platform for Life Insurance Sales Acceleration

**Company:** prudential

**Industry:** Insurance

**Relevance score:** 132

**prudential / Insurance** — Prudential developed "Just Ask," an AI-driven advisor assistant platform to address the complex, friction-heavy life insurance sales process that typically spans 8-10 weeks and involves navigating hundreds of products, regulatory requirements, and forms across different states. The company built a multi-agent system on AWS that... — Tools: redis,guardrails,monitoring,api_gateway,orchestration,databases,cache | Techniques: rag,embeddings,semantic_search,multi_agent_systems,agent_based,prompt_engineering,memory,human_in_the_loop,evals,reranking

**Source:** https://www.youtube.com/watch?v=g-YBqWv2kQ4

---

### 9. Building and Scaling AI Agents in Production for DevSecOps Automation

**Company:** datadog

**Industry:** Tech

**Relevance score:** 132

**datadog / Tech** — Datadog, an observability platform company, has deployed over a hundred AI agents in production to automate DevSecOps tasks, with plans to scale to thousands more. The agents include an SRE agent for autonomous alert investigation, a Dev agent for code generation and error fixes, and... — Tools: docker,kubernetes,monitoring,devops,orchestration,cicd,microservices,open_source,documentation,security,guardrails,fastapi | Techniques: agent_based,multi_agent_systems,prompt_engineering,mcp,a2a,evals,memory,harness_engineering

**Source:** https://www.youtube.com/watch?v=C3y3M_03Vco

---

### 10. Agentic Workflow Automation for Financial Operations

**Company:** ramp

**Industry:** Finance

**Relevance score:** 132

**ramp / Finance** — Ramp, a finance automation platform serving over 50,000 customers, built a comprehensive suite of AI agents to automate manual financial workflows including expense policy enforcement, accounting classification, and invoice processing. The company evolved from building hundreds of isolated agents to consolidating around a single agent... — Tools: langchain,fastapi,docker,kubernetes,monitoring,cicd,continuous_integration,continuous_deployment,open_source,documentation,guardrails,reliability,scalability,postgresql,cache,orchestration | Techniques: agent_based,multi_agent_systems,prompt_engineering,human_in_the_loop,few_shot,evals,token_optimization,error_handling,cost_optimization

**Source:** https://www.youtube.com/watch?v=NMs8C2_3M0w

---

### 11. Building Multilingual AI Agents with Translation Pipelines

**Company:** boundary

**Industry:** Tech

**Relevance score:** 127

**boundary / Tech** — The case study demonstrates how to build production-ready multilingual AI agents that serve users speaking different languages. The core problem is that when AI pipelines are designed primarily in English with extensive prompts, tool definitions, and business logic, they tend to produce English responses even... — Tools: fastapi | Techniques: prompt_engineering,few_shot,agent_based,evals,latency_optimization,error_handling

**Source:** https://www.youtube.com/watch?v=-gFdtc-HbOY

---

### 12. Feature Flags as LLMOps Infrastructure for Agentic Development Teams

**Company:** boundary

**Industry:** Tech

**Relevance score:** 127

**boundary / Tech** — This discussion explores how feature flags serve as critical infrastructure for teams deploying AI agents to production at scale. The problem addressed is that agentic systems can generate and ship code at extremely high velocity, creating bottlenecks in traditional deployment pipelines and making it difficult... — Tools: cicd,monitoring,databases,devops,continuous_deployment,continuous_integration,fastapi,postgresql | Techniques: agent_based,multi_agent_systems,harness_engineering,evals,human_in_the_loop,latency_optimization,cost_optimization,error_handling

**Source:** https://www.youtube.com/watch?v=gRqb7R4Pcrs

---

### 13. Panel Discussion on AI Agents in Production: Security, Evaluation, and Infrastructure

**Company:** zenity_/_hetz_/_aidoc_/_band_/_mongodb

**Industry:** Tech

**Relevance score:** 127

**zenity_/_hetz_/_aidoc_/_band_/_mongodb / Tech** — This panel discussion brings together practitioners from multiple companies to discuss the challenges and best practices of deploying AI agents in production environments. The panelists, representing companies like aidoc (medical AI), Zenity (AI agent security), Band (agent communication infrastructure), and MongoDB (data layer for AI... — Tools: monitoring,databases,microservices,security,guardrails,langchain,chromadb,pinecone,qdrant,postgresql,mysql,sqlite,redis,cache | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,model_optimization,fine_tuning,multi_agent_systems,agent_based,memory,evals

**Source:** https://www.youtube.com/watch?v=BQ6aIRYYwh4

---

### 14. Building an AI-Powered Slack Agent with MCP Standardization

**Company:** duolingo

**Industry:** Education

**Relevance score:** 127

**duolingo / Education** — Duolingo developed an AI-powered Slack bot to democratize access to their Model Context Protocol (MCP) infrastructure after discovering that manual MCP server setup was too complex for widespread adoption. The journey began with individual engineers connecting MCP servers to local editors in late 2024, evolved... — Tools: fastapi,docker,monitoring,security,guardrails,open_source,documentation,cicd,orchestration,postgresql | Techniques: mcp,prompt_engineering,human_in_the_loop,multi_agent_systems,agent_based,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=5sb9iA2v78g

---

### 15. Building Trustworthy AI Agents for Automated Expense Management

**Company:** ramp

**Industry:** Finance

**Relevance score:** 124

**ramp / Finance** — Ramp built and deployed a suite of LLM-backed agents to automate expense management workflows, focusing specifically on expense approval processes that traditionally required manual manager review. The solution emphasizes transparency through explicit reasoning and citations, implements escape hatches for uncertain decisions, enables collaborative context refinement... — Tools: guardrails,documentation | Techniques: prompt_engineering,human_in_the_loop,agent_based,evals,error_handling,fallback_strategies

**Source:** https://builders.ramp.com/post/how-to-build-agents-users-can-trust

---

### 16. AI Agent for Automated Merchant Classification Correction

**Company:** ramp

**Industry:** Finance

**Relevance score:** 124

**ramp / Finance** — Ramp, a corporate card and expense management platform, faced a scaling challenge with incorrect merchant classifications that frustrated customers and required hours of manual intervention from support and engineering teams. The company built an AI agent using LLMs combined with RAG, embeddings, OLAP queries, and... — Tools: guardrails | Techniques: rag,embeddings,prompt_engineering,agent_based,error_handling,evals

**Source:** https://builders.ramp.com/post/fixing-merchant-classifications-with-ai

---

### 17. Self-Service Data Analytics with Claude-Powered Agents

**Company:** anthropic

**Industry:** Tech

**Relevance score:** 122

**anthropic / Tech** — Anthropic deployed Claude-powered analytics agents to automate 95% of business analytics queries with approximately 95% aggregate accuracy, enabling their data science team to focus on strategic work rather than ad-hoc requests. The system addresses three critical failure modes in analytics agents—concept-to-entity ambiguity, data staleness, and... — Tools: documentation,guardrails,monitoring | Techniques: prompt_engineering,rag,embeddings,semantic_search,agent_based,human_in_the_loop,evals

**Source:** https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude

---

### 18. Building a Custom Background Coding Agent with Cloud-Based Sandboxes

**Company:** ramp

**Industry:** Finance

**Relevance score:** 122

**ramp / Finance** — Ramp built Inspect, a custom background coding agent that writes and verifies code in isolated cloud-based environments. The system addresses the need for faster, more powerful development workflows by running sessions in sandboxed VMs on Modal with full development environments, integrated with production tools like... — Tools: docker,kubernetes,monitoring,databases,api_gateway,microservices,cicd,scaling,serverless,devops,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,guardrails,reliability,scalability,fastapi,postgresql,sqlite,redis,cache | Techniques: prompt_engineering,agent_based,multi_agent_systems,latency_optimization,cost_optimization,system_prompts,mcp

**Source:** https://builders.ramp.com/post/why-we-built-our-background-agent

---

### 19. One-Click Simulation and Evaluation Platform for Support Chatbots

**Company:** doordash

**Industry:** E-commerce

**Relevance score:** 122

**doordash / E-commerce** — DoorDash built a comprehensive simulation and evaluation platform to address bottlenecks in their LLM-powered support chatbot development cycle. Previously, validation required deploying changes to 1% of live traffic and manually reviewing transcripts—a process that took hours to weeks and struggled to catch long-tail edge cases... — Tools: fastapi,monitoring,microservices | Techniques: prompt_engineering,evals,few_shot,system_prompts

**Source:** https://careersatdoordash.com/blog/doordashs-one-click-simulation-and-evaluation-platform-for-support-chatbots/

---

## Cool Use Cases

### 1. AI-Powered Customer Feedback Analysis System for Container Shipping

**Company:** hapag-lloyd

**Industry:** Other

**Relevance score:** 127

**hapag-lloyd / Other** — Hapag-Lloyd, a global container shipping company, transformed their manual and time-consuming customer feedback analysis process into an automated AI-powered system using Amazon Bedrock. Previously, product managers spent hours or days manually categorizing sentiment and themes from hundreds of feedback comments exported as CSV files. The... — Tools: langchain,elasticsearch,monitoring,serverless,orchestration,open_source,guardrails | Techniques: embeddings,rag,prompt_engineering,multi_agent_systems,agent_based,semantic_search

**Source:** https://aws.amazon.com/blogs/machine-learning/how-hapag-lloyd-uses-amazon-bedrock-to-transform-customer-feedback-into-actionable-insights/

---

### 2. Building Custom Agents at Scale: Notion's Multi-Year Journey to Production-Ready Agentic Workflows

**Company:** notion

**Industry:** Tech

**Relevance score:** 127

**notion / Tech** — Notion, a knowledge work platform serving enterprise customers, spent multiple years (2022-2026) iterating through four to five complete rebuilds of their agent infrastructure before shipping Custom Agents to production. The core problem was enabling users to automate complex workflows across their workspaces while maintaining enterprise-grade... — Tools: langchain,postgresql,sqlite,elasticsearch,fastapi,docker,kubernetes,cicd,monitoring,databases,api_gateway,microservices,orchestration,open_source,documentation,security,guardrails,reliability,scalability,cache | Techniques: agent_based,multi_agent_systems,prompt_engineering,few_shot,rag,embeddings,fine_tuning,evals,reranking,semantic_search,vector_search,human_in_the_loop,cost_optimization,latency_optimization,system_prompts,mcp,chunking,error_handling,a2a

**Source:** https://www.latent.space/p/notion

---

## Tools & Infrastructure

### 1. Building Agentic Spreadsheet Automation from Process Mining to Production

**Company:** ramp

**Industry:** Finance

**Relevance score:** 127

**ramp / Finance** — Ramp developed an agentic spreadsheet editor called Ramp Sheets to automate complex finance workflows, starting from an internal process mining project that converted Loom videos of finance tasks into automation pipelines. The team evolved from black-box Python code generation to transparent spreadsheet-native operations using around... — Tools: docker,monitoring,databases,api_gateway,microservices,cicd,open_source,fastapi,pytorch,redis,cache | Techniques: agent_based,prompt_engineering,few_shot,harness_engineering,memory,multi_agent_systems,evals,human_in_the_loop,latency_optimization,token_optimization

**Source:** https://www.youtube.com/watch?v=trEM9OKr5Sc

---

### 2. AI-Powered Workflow Assistant for Seismic Data Processing

**Company:** halliburton

**Industry:** Energy

**Relevance score:** 127

**halliburton / Energy** — Halliburton partnered with AWS Generative AI Innovation Center to develop an AI-powered assistant for their Seismic Engine, a cloud-native application for seismic data processing. The traditional workflow creation process required manual configuration of approximately 100 specialized tools, which was time-consuming and required deep expertise. The... — Tools: langchain,fastapi,elasticsearch,databases,serverless,api_gateway,monitoring,orchestration | Techniques: rag,prompt_engineering,agent_based,semantic_search,vector_search

**Source:** https://aws.amazon.com/blogs/machine-learning/halliburton-enhances-seismic-workflow-creation-with-amazon-bedrock-and-generative-ai/

---
