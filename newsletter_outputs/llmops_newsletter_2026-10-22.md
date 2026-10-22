# Weekly LLMOps Newsletter — 2026-10-22

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Research Highlights

### 1. Multi-Agent AI Contact Center Platform Serving 30 Million Subscribers

**Company:** lg_u+

**Industry:** Telecommunications

**Relevance score:** 132

**lg_u+ / Telecommunications** — LG U+ built a comprehensive AI Contact Center platform to handle customer service for 30 million subscribers across 17 contact centers with 4,500 human agents processing 150,000 calls daily. The solution includes customer-facing chatbots and voice bots for self-service, real-time AI advisors that assist human... — Tools: vllm,monitoring,open_source | Techniques: rag,embeddings,fine_tuning,prompt_engineering,reranking,few_shot,semantic_search,vector_search,multi_agent_systems,agent_based,harness_engineering,memory,human_in_the_loop,latency_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=eaSINaHBVf0

---

### 2. Trace-Driven Cost, Quality, and Security Optimization for Coding Agents

**Company:** databricks

**Industry:** Tech

**Relevance score:** 127

**databricks / Tech** — Databricks deployed Unity Gateway as a centralized AI gateway for its engineering coding agents, using it to enforce budgets and security policies, collect agent traces, and provide flexibility across proprietary and open models and agent harnesses. Databricks then analyzed those traces with Genie and built... — Tools: api_gateway,monitoring,guardrails,security,open_source,reliability,scalability | Techniques: mcp,multi_agent_systems,agent_based,harness_engineering,model_optimization,token_optimization,cost_optimization,error_handling,evals

**Source:** https://www.youtube.com/watch?v=8mylEGP37bw

---

### 3. Simulation-Driven Testing and Continuous Improvement for Multi-Turn AI Agents

**Company:** arklex

**Industry:** Tech

**Relevance score:** 127

**arklex / Tech** — Arklex applies LLM-based user simulation to the testing and improvement of production-oriented AI agents, addressing the limits of manual testing and static single-turn benchmarks. Synthetic users are generated from personas, goals, agent capabilities, and contextual knowledge, then used to exercise conversational and workflow agents through... — Tools: cicd,continuous_integration,continuous_deployment,databases,open_source,compliance,reliability,scalability | Techniques: rag,prompt_engineering,fine_tuning,multi_agent_systems,agent_based,human_in_the_loop,fallback_strategies,error_handling,evals

**Source:** https://www.infoq.com/presentations/ai-agent-testing-evaluation/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations

---

### 4. AI-Native Investment Research with Governed Per-Query Data Purchasing

**Company:** heurist_finance

**Industry:** Finance

**Relevance score:** 127

**heurist_finance / Finance** — Heurist Finance built a production investment-research workbench for retail investors that combines portfolio-aware analysis, premium market data, financial research, scenario analysis, and monitoring in a conversational interface. Its agents are orchestrated with Strands and Anthropic Claude on Amazon Bedrock, while Amazon Bedrock AgentCore provides identity... — Tools: databases,postgresql,monitoring,guardrails,security,compliance | Techniques: agent_based,memory,error_handling,cost_optimization

**Source:** https://aws.amazon.com/blogs/machine-learning/how-heurist-finance-built-an-ai-native-investment-workbench-on-amazon-bedrock-agentcore/

---

## Industry News

### 1. A Shared Production Platform for Governed Enterprise Agents

**Company:** wood_mackenzie

**Industry:** Energy

**Relevance score:** 137

**wood_mackenzie / Energy** — Wood Mackenzie built APEX (Agentic Platform for Energy eXperience), a shared platform on Amazon Bedrock AgentCore, to move multiple agentic AI applications from prototypes into governed production. APEX centralizes runtime hosting, identity and entitlements, tool connectivity, memory, retrieval, guardrails, observability, evaluation, and generative user interfaces... — Tools: serverless,api_gateway,security,compliance,guardrails,reliability,scalability,cicd,continuous_deployment,open_source,databases | Techniques: rag,vector_search,mcp,a2a,agent_based,memory,human_in_the_loop,cost_optimization,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/a-shared-agentic-platform-for-wood-mackenzie-on-amazon-bedrock-agentcore/

---

### 2. Grounded, Multi-Agent Enterprise AI at Global Scale

**Company:** qlik

**Industry:** Tech

**Relevance score:** 132

**qlik / Tech** — Qlik built Qlik Answers to let employees ask natural-language questions across structured analytics, documents, knowledge bases, glossaries, and automations while receiving sourced answers suitable for enterprise and regulated environments. The production architecture separates conversational entry, lightweight routing, answer planning, specialist agents, conversational analytics, retrieval, and... — Tools: orchestration,scaling,security,compliance,guardrails,reliability,scalability,databases | Techniques: rag,embeddings,reranking,multi_agent_systems,agent_based,human_in_the_loop,fallback_strategies,latency_optimization,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/how-qlik-built-grounded-enterprise-scale-ai-with-amazon-bedrock/

---

### 3. Industrializing Ontology-Grounded Agentic AI Across a Telecommunications Enterprise

**Company:** various

**Industry:** Telecommunications

**Relevance score:** 132

**various / Telecommunications** — EchoStar is moving from isolated AI proofs of concept toward persistent, secure, and scalable AI operations across telecommunications, technology, and corporate functions. Its approach combines cleaned and governed enterprise data, semantic models, metrics, ontologies, and knowledge graphs to ground agents in business context, while federated... — Tools: cicd,compliance,continuous_deployment,continuous_integration,devops,guardrails,monitoring,reliability,scalability,security | Techniques: agent_based,cost_optimization,error_handling,evals,harness_engineering,human_in_the_loop,rag,semantic_search,vector_search

**Source:** https://www.youtube.com/watch?v=S0876Xk3b4Y

---

### 4. Multichannel Customer-Service Agents with Model Routing and Production Evaluation

**Company:** ringg

**Industry:** Tech

**Relevance score:** 132

**ringg / Tech** — Ringg built a multichannel enterprise agent platform for voice, chat, WhatsApp, and web interactions, using OpenAI models, retrieval, tool orchestration, specialized subagents, and human escalation to automate customer-service workflows. The platform reportedly handles more than 7 million connected calls per month, resolves up to 65%... — Tools: monitoring,reliability,scalability | Techniques: rag,semantic_search,prompt_engineering,multi_agent_systems,agent_based,evals,cost_optimization,latency_optimization,fallback_strategies,token_optimization,human_in_the_loop

**Source:** https://openai.com/index/ringg/

---

### 5. Scaling Context-Aware Coding Agents with MCP Playbooks

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 132

**linkedin / Tech** — LinkedIn found that generic AI coding agents performed poorly against its large, mature codebase because they lacked internal architectural knowledge, procedural guidance, and reliable access to company systems. It built a local Model Context Protocol (MCP) server that exposes code search, documentation, operational systems, and... — Tools: monitoring,microservices,security,guardrails,reliability,scalability,open_source | Techniques: mcp,memory,agent_based,prompt_engineering,system_prompts,human_in_the_loop,token_optimization,error_handling,evals

**Source:** https://www.infoq.com/presentations/linkedin-context-engineering/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations

---

### 6. End-to-End Pretraining and Infrastructure Optimization for MAI-Base-2

**Company:** microsoft_ai

**Industry:** Tech

**Relevance score:** 127

**microsoft_ai / Tech** — Microsoft AI developed MAI-Base-2, an 80-billion-active-parameter, 2.8-trillion-total-parameter mixture-of-experts foundation model, by jointly optimizing data pipelines, model architecture, training algorithms, evaluation, and GPU infrastructure. The model was trained on 16,000 GB200 GPUs for 38 days, with reported 89% goodput and 21% average model-FLOPs utilization. Microsoft reports... — Tools: monitoring,scaling,scalability,reliability | Techniques: model_optimization,cost_optimization,evals

**Source:** https://microsoft.ai/news/frontier-pre-training-at-microsoft-ai

---

### 7. Slack-Based AI IT Help Desk with Retrieval and Ticket Automation

**Company:** shipstation

**Industry:** E-commerce

**Relevance score:** 127

**shipstation / E-commerce** — ShipStation built Deckhand, an AI IT help desk that operates in Slack and uses Amazon Bedrock AgentCore, Claude, retrieval-augmented generation, and Jira Service Management integrations to answer routine questions, interpret error screenshots, and create contextualized tickets when self-service is insufficient. The system indexes curated internal... — Tools: serverless,monitoring,databases,fastapi,open_source,security,guardrails,reliability | Techniques: rag,prompt_engineering,agent_based,human_in_the_loop,error_handling,fallback_strategies,mcp

**Source:** https://aws.amazon.com/blogs/machine-learning/how-shipstation-global-built-an-ai-it-help-desk-on-amazon-bedrock-agentcore/

---

### 8. Building Production-Grade Company Memory and Portable AI Infrastructure

**Company:** various

**Industry:** Tech

**Relevance score:** 127

**various / Tech** — Several AI companies are addressing different production challenges that emerge when LLM systems move beyond small prototypes: retrieval over rapidly changing enterprise data, strict customer-cloud deployment requirements, and the loss of organizational knowledge across disconnected tools. The proposed solutions combine event-based memory, entity graphs, raw-document... — Tools: databases,postgresql,security,compliance,reliability,scalability,open_source | Techniques: rag,embeddings,memory,semantic_search,vector_search,chunking,agent_based,human_in_the_loop,cost_optimization,evals

**Source:** https://www.youtube.com/watch?v=dS_VDa620VM

---

### 9. Conversational HVAC Diagnostics and Building Intelligence

**Company:** trane

**Industry:** Other

**Relevance score:** 127

**trane / Other** — Trane Technologies built a multi-agent conversational system that gives building operators, field technicians, service managers, and owners natural-language access to live HVAC telemetry, technical documentation, and operational tools. Using the Strands framework with Amazon Bedrock AgentCore, AgentCore Gateway, AgentCore Memory, CloudWatch observability, and Anthropic Claude... — Tools: monitoring,microservices,security,guardrails,reliability,scalability | Techniques: rag,semantic_search,agent_based,memory,mcp,system_prompts,human_in_the_loop,latency_optimization,cost_optimization,error_handling,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/how-trane-gets-building-insights-60x-faster-with-amazon-bedrock-agentcore/

---

### 10. Operating Identity-Aware Digital Employees at Enterprise Scale

**Company:** china_merchants_bank

**Industry:** Finance

**Relevance score:** 127

**china_merchants_bank / Finance** — China Merchants Bank describes an enterprise platform for operating more than 20,000 digital employee agents, 200 domain experts, and over 10,000 registered skills across employee-facing workflows. The approach treats agents as persistent production services rather than isolated model-and-tool demos: channel adapters normalize events, a harness... — Tools: kubernetes,monitoring,api_gateway,microservices,orchestration,security,compliance,guardrails,reliability,scalability | Techniques: mcp,human_in_the_loop,cost_optimization,error_handling,latency_optimization,harness_engineering,agent_based,multi_agent_systems,evals

**Source:** https://www.youtube.com/watch?v=KRuU_nhoMH0

---

### 11. Multi-Agent Open Finance Onboarding on Amazon Bedrock

**Company:** ninth_wave

**Industry:** Finance

**Relevance score:** 127

**ninth_wave / Finance** — Ninth Wave built Compass to reduce the specialist effort required to validate bank APIs, map fields to the Financial Data Exchange (FDX) standard, answer integration questions, and assess readiness for production connectivity. The production system uses a Strands Agents orchestrator on Amazon Bedrock AgentCore, seven... — Tools: monitoring,load_balancing,scaling,orchestration,cicd,continuous_integration,continuous_deployment,docker,security,compliance,guardrails,reliability,scalability | Techniques: rag,multi_agent_systems,agent_based,prompt_engineering,system_prompts

**Source:** https://aws.amazon.com/blogs/machine-learning/how-ninth-wave-built-ai-powered-open-finance-onboarding-on-amazon-bedrock/

---

### 12. Governed Self-Service AI Agents for a Regulated Insurance Broker

**Company:** mrh_trowe

**Industry:** Insurance

**Relevance score:** 127

**mrh_trowe / Insurance** — MRH Trowe needed to give employees practical access to generative AI without exposing sensitive insurance and client information through unmanaged tools. It deployed a centrally governed platform combining LibreChat, Strands Agents, Amazon Bedrock AgentCore, AWS networking and identity controls, and multiple storage and retrieval services... — Tools: databases,api_gateway,microservices,serverless,scaling,open_source,security,compliance,reliability,scalability,orchestration,monitoring,postgresql,redis,cache | Techniques: rag,embeddings,semantic_search,vector_search,agent_based,cost_optimization,token_optimization

**Source:** https://aws.amazon.com/blogs/machine-learning/how-mrh-trowe-enabled-secure-self-service-ai-agents-in-financial-services/

---

### 13. Operationalizing Enterprise Agents for Legal Work and Customer Experience

**Company:** harvey_/_sierra

**Industry:** Tech

**Relevance score:** 127

**harvey_/_sierra / Tech** — Harvey and Sierra illustrate two production approaches to enterprise GenAI: Harvey applies LLMs to high-volume legal workflows such as diligence, document extraction, drafting, and collaborative review, while Sierra deploys customer-service agents that retrieve business context and take actions across operational systems. Both companies have moved... — Tools: monitoring,databases,api_gateway,scalability,reliability,guardrails,security,compliance | Techniques: rag,fine_tuning,model_optimization,agent_based,memory,human_in_the_loop,latency_optimization,error_handling,evals

**Source:** https://www.youtube.com/watch?v=Bj2BRrAiOy4

---

## Cool Use Cases

### 1. Scaling a Company-Wide GenAI Platform with Gateways, Open Models, and Agent Infrastructure

**Company:** doordash

**Industry:** E-commerce

**Relevance score:** 132

**doordash / E-commerce** — DoorDash built an internal GenAI platform to help thousands of employees and product teams deploy LLM-powered automation, recommendations, personalization, and agents while balancing accuracy, latency, cost, velocity, and accountability. The platform evolved from an API-first LLM Gateway with provider abstraction, fallbacks, cost attribution, logging, and... — Tools: api_gateway,monitoring,open_source,security,guardrails,reliability,scalability,vllm,documentation | Techniques: fine_tuning,model_optimization,prompt_engineering,error_handling,fallback_strategies,latency_optimization,cost_optimization,human_in_the_loop,agent_based,mcp,a2a,evals,system_prompts

**Source:** https://www.infoq.com/presentations/doordash-genai-platform-architecture/

---

### 2. Multi-Agent Database Operations and Proactive Incident Diagnosis

**Company:** cornerstone_on_demand

**Industry:** HR

**Relevance score:** 132

**cornerstone_on_demand / HR** — CornerStone On Demand built Orion AI to reduce the manual effort involved in diagnosing database incidents, managing database lifecycles, and coordinating DataOps and SRE workflows. The production system uses Amazon Bedrock, Strands Agents, specialized domain agents, hybrid keyword and semantic routing, MCP and API-based tool... — Tools: monitoring,databases,open_source,security,guardrails,cache,reliability,orchestration | Techniques: multi_agent_systems,agent_based,rag,embeddings,semantic_search,memory,human_in_the_loop,fallback_strategies,latency_optimization,system_prompts,mcp,token_optimization

**Source:** https://aws.amazon.com/blogs/machine-learning/how-cornerstone-ondemand-cut-database-diagnosis-by-78-with-amazon-bedrock/

---

### 3. On-Premises Agentic Troubleshooting for Disaster Recovery Operations

**Company:** hpe_zerto

**Industry:** Tech

**Relevance score:** 127

**hpe_zerto / Tech** — HPE Zerto built an agentic troubleshooting assistant embedded in its on-premises disaster recovery management product to help operators investigate alerts, configuration problems, replication failures, SLA risks, and recovery readiness issues without manually assembling context from multiple dashboards and knowledge sources. The system uses locally hosted... — Tools: monitoring,databases,serverless,security,compliance,guardrails,reliability,scalability | Techniques: rag,semantic_search,multi_agent_systems,agent_based,mcp,evals,system_prompts,token_optimization,latency_optimization,cost_optimization

**Source:** https://aws.amazon.com/blogs/machine-learning/how-hpe-zerto-built-an-agentic-troubleshooting-system-with-amazon-bedrock/

---

## Tools & Infrastructure

### 1. Governed AI Enablement for a Banking Internal Developer Platform

**Company:** dkb

**Industry:** Finance

**Relevance score:** 137

**dkb / Finance** — DKB, a German online bank serving approximately five million customers, is adapting its internal platform and platform-experience practices for AI-assisted software development. The discussion describes using AI and agentic tooling to improve documentation, analyze infrastructure and repositories, answer first-line developer questions, interpret logs, and generate... — Tools: kubernetes,monitoring,security,compliance,guardrails,reliability,scalability,orchestration,devops,cicd,continuous_integration,continuous_deployment,open_source,documentation | Techniques: agent_based,mcp,evals,human_in_the_loop,cost_optimization,error_handling

**Source:** https://www.infoq.com/presentations/ai-platform-engineering-roundtable/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering-presentations

---

### 2. Scaling a Production AI Agent for API Development

**Company:** postman

**Industry:** Tech

**Relevance score:** 132

**postman / Tech** — Postman built Agent Mode to let developers use an AI agent across API testing, documentation, discovery, and implementation within a mature product used by a global developer community. The production challenge was less about model access than about translating interface-oriented product behavior into reliable agent... — Tools: monitoring,databases,security,compliance,guardrails,reliability,scalability | Techniques: rag,embeddings,semantic_search,vector_search,prompt_engineering,system_prompts,model_optimization,agent_based,harness_engineering,human_in_the_loop,latency_optimization,cost_optimization,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/how-postman-runs-agent-mode-for-40-million-developers-on-amazon-bedrock/

---

### 3. Enterprise Context and Grounded Agentic Workflows for Genie1

**Company:** databricks

**Industry:** Tech

**Relevance score:** 132

**databricks / Tech** — Databricks built Genie1 as a general-purpose enterprise AI co-worker that can answer business questions, explore governed data, execute analyses, and interact with workplace systems. The central challenge is that capable language models lack organization-specific definitions, data relationships, permissions, and operational context. Genie1 addresses this by... — Tools: databases,security,compliance,guardrails,reliability,scalability | Techniques: rag,embeddings,semantic_search,vector_search,reranking,knowledge_distillation,prompt_engineering,token_optimization,multi_agent_systems,agent_based,memory,mcp,latency_optimization,cost_optimization,evals,error_handling

**Source:** https://www.youtube.com/watch?v=eTZc0JBj2AY

---

### 4. Healthcare Voice Scheduling Agent with Progressive Authentication and Latency Masking

**Company:** natera

**Industry:** Healthcare

**Relevance score:** 132

**natera / Healthcare** — Natera replaced a container-based voice scheduling workflow with a production voice agent for mobile phlebotomy appointments, using Amazon Bedrock AgentCore Runtime and Memory, Amazon Bedrock foundation models, retrieval-augmented generation, and integrations with telephony, identity, vendor, and scheduling services. The architecture uses a dual-WebSocket bridge, event-driven... — Tools: serverless,monitoring,databases,microservices,orchestration,security,guardrails,reliability,scalability | Techniques: rag,embeddings,prompt_engineering,semantic_search,memory,latency_optimization,fallback_strategies,chunking,system_prompts,human_in_the_loop,error_handling,agent_based,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/nateras-intelligent-appointment-scheduling-with-amazon-bedrock-agentcore/

---

### 5. Automating Scheduled Mobile Commerce Updates with Multi-Agent Workflows

**Company:** reactiv

**Industry:** E-commerce

**Relevance score:** 127

**reactiv / E-commerce** — Reactiv, a mobile commerce platform for Shopify merchants, used Amazon Bedrock AgentCore and the Strands Agents SDK to automate recurring mobile-app updates that previously required substantial manual configuration. A scheduled, three-agent workflow uses EventBridge, Lambda, Redshift text-to-SQL queries, MCP-hosted configuration tools, persistent per-merchant memory, and... — Tools: docker,databases,serverless,orchestration,security,guardrails,reliability,scalability | Techniques: multi_agent_systems,agent_based,memory,mcp,human_in_the_loop,latency_optimization,cost_optimization

**Source:** https://aws.amazon.com/blogs/machine-learning/how-reactiv-automates-mobile-commerce-80-faster-with-amazon-bedrock-agentcore/

---
