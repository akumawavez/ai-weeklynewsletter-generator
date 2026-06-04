# Weekly LLMOps Newsletter — 2026-06-04

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Research Highlights

### 1. Training Low-Resource Language Models with Custom Tokenization and Kernel Optimization

**Company:** azercell

**Industry:** Telecommunications

**Relevance score:** 127

**azercell / Telecommunications** — Azercell Telecom, Azerbaijan's leading telecommunications provider, partnered with AWS Generative AI Innovation Center to build an Azerbaijani large language model for telecom use cases and customer-facing chatbots. The challenge was adapting foundation models to a morphologically rich, low-resource language with limited training data. Over six... — Tools: pytorch,triton,monitoring,open_source,scalability | Techniques: fine_tuning,token_optimization,model_optimization

**Source:** https://aws.amazon.com/blogs/machine-learning/training-azerbaijani-language-models-on-amazon-sagemaker-ai/

---

## Industry News

### 1. Building Self-Learning AI Agents for Site Reliability Engineering, Visual Asset Review, and Software Development

**Company:** cleric_/_puntt_/_tanagram

**Industry:** Tech

**Relevance score:** 152

**cleric_/_puntt_/_tanagram / Tech** — This case study presents three different production implementations of LLM-based agents: Cleric's self-learning SRE agent that automates on-call incident response, Puntt's visual asset review system for marketing materials compliance, and Tanagram's software factory approach for AI-assisted development. Cleric addresses the challenge of building trust in... — Tools: kubernetes,docker,monitoring,cicd,open_source,documentation | Techniques: agent_based,multi_agent_systems,prompt_engineering,evals,memory,harness_engineering,error_handling

**Source:** https://www.youtube.com/watch?v=iD50gwoce5w

---

### 2. Panel Discussion on AI Agents in Production: Security, Evaluation, and Infrastructure

**Company:** zenity_/_hetz_/_aidoc_/_band_/_mongodb

**Industry:** Tech

**Relevance score:** 147

**zenity_/_hetz_/_aidoc_/_band_/_mongodb / Tech** — This panel discussion brings together practitioners from multiple companies to discuss the challenges and best practices of deploying AI agents in production environments. The panelists, representing companies like aidoc (medical AI), Zenity (AI agent security), Band (agent communication infrastructure), and MongoDB (data layer for AI... — Tools: monitoring,databases,microservices,security,guardrails,langchain,chromadb,pinecone,qdrant,postgresql,mysql,sqlite,redis,cache | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,model_optimization,fine_tuning,multi_agent_systems,agent_based,memory,evals

**Source:** https://www.youtube.com/watch?v=BQ6aIRYYwh4

---

### 3. Agent Identity and Access Management for Production AI Systems

**Company:** uber

**Industry:** Tech

**Relevance score:** 142

**uber / Tech** — Uber faced critical challenges in implementing production AI agents at scale, specifically around identity attribution and audit trails when agents acted on behalf of users across multi-hop workflows. Traditional identity models designed for humans and workloads couldn't adequately describe agency relationships or preserve provenance across... — Tools: kubernetes,monitoring,security,guardrails,databases,microservices,api_gateway,devops,orchestration,scalability | Techniques: multi_agent_systems,agent_based,prompt_engineering,mcp

**Source:** https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/

---

### 4. Building Custom Cloud Agent Infrastructure for Legal AI at Scale

**Company:** harvey

**Industry:** Legal

**Relevance score:** 137

**harvey / Legal** — Harvey, a legal AI company, built their own custom cloud agent infrastructure to support complex legal tasks that require processing hundreds of thousands of documents. The company identified three critical requirements that existing managed agent runtimes from frontier labs and cloud providers couldn't meet: multi-model... — Tools: open_source,security,compliance,guardrails,orchestration | Techniques: agent_based,multi_agent_systems,cost_optimization,harness_engineering,latency_optimization,error_handling,fallback_strategies

**Source:** https://x.com/gabepereyra/status/2061449144074444925

---

### 5. Building Production AI Customer Support Agents with Multi-Agent Architecture and Human-in-the-Loop Design

**Company:** lorikeet

**Industry:** Tech

**Relevance score:** 137

**lorikeet / Tech** — Lorikeet is an AI customer support startup that evolved from building basic automation tools to creating sophisticated multi-agent systems for handling customer support at scale. The company developed two primary agents: a customer-facing concierge agent that handles support tickets across email, live chat, and voice... — Tools: langchain,monitoring,databases,api_gateway,guardrails,open_source | Techniques: multi_agent_systems,prompt_engineering,human_in_the_loop,agent_based,evals,system_prompts,error_handling,harness_engineering

**Source:** https://www.youtube.com/watch?v=eZj1xSiyd9U

---

### 6. Autonomous Security Investigation Agent at Scale

**Company:** wiz

**Industry:** Tech

**Relevance score:** 132

**wiz / Tech** — Wiz developed an autonomous agent called AutoAgent to conduct daily security threat investigations at massive scale, handling over 3,000 investigations per day. The system addresses the challenge of security event investigation in cloud environments, where the investigative path is unpredictable and context can explode to... — Techniques: agent_based,multi_agent_systems,prompt_engineering,memory,harness_engineering,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=sGj_ZFLX-VE

---

### 7. Building Alex: An Agent-First AI Engineering Assistant with Production-Grade LLMOps

**Company:** alyx

**Industry:** Tech

**Relevance score:** 132

**alyx / Tech** — Arize built Alex, an AI engineering agent that handles complex workflows like tracing, evaluation, and playground interaction within their observability platform. The team encountered significant challenges with task completion, context management, testing non-deterministic behavior, and debugging in production. They solved these through enforced planning with... — Tools: langchain,cicd,monitoring,orchestration,open_source,documentation | Techniques: prompt_engineering,agent_based,multi_agent_systems,harness_engineering,memory,few_shot,error_handling,token_optimization

**Source:** https://www.youtube.com/watch?v=cyzeZ52HX9c

---

### 8. Building Production-Ready Coding Agents with Skills and Observability

**Company:** langfuse_/_clickhouse

**Industry:** Tech

**Relevance score:** 132

**langfuse_/_clickhouse / Tech** — Langfuse, an open-source LLM observability platform, faced the challenge of helping thousands of users integrate their complex tracing and evaluation system into diverse codebases through 478+ pages of documentation. The team built a custom "skill" for coding agents (like Claude Code) that acts as an... — Tools: langchain,open_source,documentation,cicd,monitoring | Techniques: agent_based,prompt_engineering,rag,semantic_search,few_shot,evals,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=vNCY9kXXyDQ

---

### 9. AI-Powered Search and Agent Automation for Digital Asset Management

**Company:** bynder

**Industry:** Media & Entertainment

**Relevance score:** 132

**bynder / Media & Entertainment** — Bynder, a digital asset management platform serving retail and CPG customers, faced significant operational bottlenecks as users had to manually tag and categorize all uploaded content for searchability. To address this, Bynder built AI search capabilities and four types of configurable AI agents using AWS... — Tools: postgresql,mysql,fastapi,elasticsearch,guardrails,microservices | Techniques: embeddings,prompt_engineering,semantic_search,vector_search,agent_based,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=Kyym50EgUOQ

---

### 10. Multi-Agent AI Platform for Life Insurance Sales Acceleration

**Company:** prudential

**Industry:** Insurance

**Relevance score:** 132

**prudential / Insurance** — Prudential developed "Just Ask," an AI-driven advisor assistant platform to address the complex, friction-heavy life insurance sales process that typically spans 8-10 weeks and involves navigating hundreds of products, regulatory requirements, and forms across different states. The company built a multi-agent system on AWS that... — Tools: redis,guardrails,monitoring,api_gateway,orchestration,databases,cache | Techniques: rag,embeddings,semantic_search,multi_agent_systems,agent_based,prompt_engineering,memory,human_in_the_loop,evals,reranking

**Source:** https://www.youtube.com/watch?v=g-YBqWv2kQ4

---

### 11. Building and Scaling AI Agents in Production for DevSecOps Automation

**Company:** datadog

**Industry:** Tech

**Relevance score:** 132

**datadog / Tech** — Datadog, an observability platform company, has deployed over a hundred AI agents in production to automate DevSecOps tasks, with plans to scale to thousands more. The agents include an SRE agent for autonomous alert investigation, a Dev agent for code generation and error fixes, and... — Tools: docker,kubernetes,monitoring,devops,orchestration,cicd,microservices,open_source,documentation,security,guardrails,fastapi | Techniques: agent_based,multi_agent_systems,prompt_engineering,mcp,a2a,evals,memory,harness_engineering

**Source:** https://www.youtube.com/watch?v=C3y3M_03Vco

---

### 12. Agentic Workflow Automation for Financial Operations

**Company:** ramp

**Industry:** Finance

**Relevance score:** 132

**ramp / Finance** — Ramp, a finance automation platform serving over 50,000 customers, built a comprehensive suite of AI agents to automate manual financial workflows including expense policy enforcement, accounting classification, and invoice processing. The company evolved from building hundreds of isolated agents to consolidating around a single agent... — Tools: langchain,fastapi,docker,kubernetes,monitoring,cicd,continuous_integration,continuous_deployment,open_source,documentation,guardrails,reliability,scalability,postgresql,cache,orchestration | Techniques: agent_based,multi_agent_systems,prompt_engineering,human_in_the_loop,few_shot,evals,token_optimization,error_handling,cost_optimization

**Source:** https://www.youtube.com/watch?v=NMs8C2_3M0w

---

### 13. Building Production AI Agents with Temporal-Based Workflow Orchestration

**Company:** retool

**Industry:** Tech

**Relevance score:** 129

**retool / Tech** — Retool transformed their existing Temporal-based workflow engine into a full agent orchestration platform to address the challenges of running production AI agents at enterprise scale. The company recognized that key agent challenges—durable execution for long-running processes, context management, unreliable tool calls, human-in-the-loop approval, and observability—mapped... — Tools: monitoring,databases,orchestration,devops,security,guardrails,reliability,scalability | Techniques: human_in_the_loop,agent_based,harness_engineering,error_handling,latency_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=zBliFZMJYyY

---

### 14. Scaling Agentic Workflows with Temporal Cloud: Platform Engineering for Production LLM Systems

**Company:** openai

**Industry:** Tech

**Relevance score:** 129

**openai / Tech** — OpenAI faced scalability challenges when their image generation service went viral, with synchronous request-response flows unable to handle the massive demand and resulting in rate limits and poor user experience. They addressed this by adopting Temporal Cloud for durable workflow orchestration and building a comprehensive... — Tools: kubernetes,docker,monitoring,databases,api_gateway,microservices,cicd,scaling,devops,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,guardrails,reliability,scalability,fastapi,postgresql | Techniques: agent_based,multi_agent_systems,error_handling,latency_optimization,cost_optimization,fallback_strategies

**Source:** https://www.youtube.com/watch?v=JOLu1E-hKC4

---

### 15. Real-time Clinical Audio Processing with Agentic Workflows

**Company:** abridge

**Industry:** Healthcare

**Relevance score:** 127

**abridge / Healthcare** — Abridge built a system for real-time clinical audio processing that records conversations between clinicians and patients, transcribing and analyzing them to drive healthcare products. The problem involved handling high-stakes healthcare data with strict durability and latency requirements, needing to process audio in real-time and make... — Tools: monitoring,orchestration,microservices,api_gateway,open_source,reliability,scalability | Techniques: agent_based,multi_agent_systems,harness_engineering,memory,error_handling,latency_optimization

**Source:** https://www.youtube.com/watch?v=ZybCTJLukyk

---

### 16. Building an AI-Powered Slack Agent with MCP Standardization

**Company:** duolingo

**Industry:** Education

**Relevance score:** 127

**duolingo / Education** — Duolingo developed an AI-powered Slack bot to democratize access to their Model Context Protocol (MCP) infrastructure after discovering that manual MCP server setup was too complex for widespread adoption. The journey began with individual engineers connecting MCP servers to local editors in late 2024, evolved... — Tools: fastapi,docker,monitoring,security,guardrails,open_source,documentation,cicd,orchestration,postgresql | Techniques: mcp,prompt_engineering,human_in_the_loop,multi_agent_systems,agent_based,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=5sb9iA2v78g

---

### 17. Workflow Simulator for Testing Flight Integration Connectors

**Company:** agoda

**Industry:** E-commerce

**Relevance score:** 122

**agoda / E-commerce** — Agoda faced challenges testing supplier connectors for their flight booking platform, where traditional end-to-end testing required spinning up full production-like stacks, causing late bug discovery and slow iteration cycles. They built a Workflow Simulator that validates supplier connectors by simulating the surrounding ecosystem, enabling engineers...

**Source:** https://medium.com/agoda-engineering/how-agoda-simulates-booking-flows-to-test-flight-integrations-204ec4f2e128

---

### 18. Multi-Cloud LLM Infrastructure Evolution at Scale

**Company:** slack

**Industry:** Tech

**Relevance score:** 122

**slack / Tech** — Slack evolved their production LLM infrastructure through four distinct phases over three years (2023-2026) to serve AI features to millions of enterprise users. Starting with AWS SageMaker's managed infrastructure, they migrated to Amazon Bedrock for operational simplicity and faster model access, then adopted hybrid provisioned/on-demand... — Tools: monitoring,api_gateway,load_balancing,microservices,scaling,devops,orchestration,security,compliance,guardrails,reliability,scalability | Techniques: prompt_engineering,latency_optimization,cost_optimization,fallback_strategies,a2a,evals

**Source:** https://slack.engineering/slack-ai-the-path-to-multi-cloud/

---

### 19. AI-Driven Enzyme Design for Advanced Plastic Recycling

**Company:** rhea’s_factory

**Industry:** Energy

**Relevance score:** 122

**rhea’s_factory / Energy** — Rhea's Factory is developing enzymatic plastic recycling technology that uses AI and protein language models to design novel enzymes capable of breaking down polymers to their original monomer building blocks. The traditional plastic recycling process only allows materials to be recycled two to three times... — Tools: guardrails,open_source,pytorch,tensorflow | Techniques: embeddings,multi_agent_systems,agent_based,prompt_engineering,human_in_the_loop,cost_optimization,latency_optimization

**Source:** https://www.youtube.com/watch?v=huFaei-6Z4g

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

**Relevance score:** 127

**notion / Tech** — Notion, a knowledge work platform serving enterprise customers, spent multiple years (2022-2026) iterating through four to five complete rebuilds of their agent infrastructure before shipping Custom Agents to production. The core problem was enabling users to automate complex workflows across their workspaces while maintaining enterprise-grade... — Tools: langchain,postgresql,sqlite,elasticsearch,fastapi,docker,kubernetes,cicd,monitoring,databases,api_gateway,microservices,orchestration,open_source,documentation,security,guardrails,reliability,scalability,cache | Techniques: agent_based,multi_agent_systems,prompt_engineering,few_shot,rag,embeddings,fine_tuning,evals,reranking,semantic_search,vector_search,human_in_the_loop,cost_optimization,latency_optimization,system_prompts,mcp,chunking,error_handling,a2a

**Source:** https://www.latent.space/p/notion

---

## Tools & Infrastructure

### 1. Orchestrating Fleet-Scale AI Coding Agents with Temporal Workflows

**Company:** macroscope

**Industry:** Tech

**Relevance score:** 137

**macroscope / Tech** — Macroscope, a software development intelligence platform founded by former Twitter executives, built two production LLM systems powered by Temporal workflows: their core code understanding and review platform, and Murmur, a fleet orchestration system for AI coding agents. The core Macroscope product uses LLMs to automatically... — Tools: docker,kubernetes,cicd,orchestration,monitoring,devops,microservices,postgresql,redis,fastapi,pytorch | Techniques: agent_based,multi_agent_systems,harness_engineering,prompt_engineering,error_handling,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=iv3kfcXFS7w

---

### 2. Building Agentic Spreadsheet Automation from Process Mining to Production

**Company:** ramp

**Industry:** Finance

**Relevance score:** 127

**ramp / Finance** — Ramp developed an agentic spreadsheet editor called Ramp Sheets to automate complex finance workflows, starting from an internal process mining project that converted Loom videos of finance tasks into automation pipelines. The team evolved from black-box Python code generation to transparent spreadsheet-native operations using around... — Tools: docker,monitoring,databases,api_gateway,microservices,cicd,open_source,fastapi,pytorch,redis,cache | Techniques: agent_based,prompt_engineering,few_shot,harness_engineering,memory,multi_agent_systems,evals,human_in_the_loop,latency_optimization,token_optimization

**Source:** https://www.youtube.com/watch?v=trEM9OKr5Sc

---

### 3. AI-Powered Workflow Assistant for Seismic Data Processing

**Company:** halliburton

**Industry:** Energy

**Relevance score:** 127

**halliburton / Energy** — Halliburton partnered with AWS Generative AI Innovation Center to develop an AI-powered assistant for their Seismic Engine, a cloud-native application for seismic data processing. The traditional workflow creation process required manual configuration of approximately 100 specialized tools, which was time-consuming and required deep expertise. The... — Tools: langchain,fastapi,elasticsearch,databases,serverless,api_gateway,monitoring,orchestration | Techniques: rag,prompt_engineering,agent_based,semantic_search,vector_search

**Source:** https://aws.amazon.com/blogs/machine-learning/halliburton-enhances-seismic-workflow-creation-with-amazon-bedrock-and-generative-ai/

---
