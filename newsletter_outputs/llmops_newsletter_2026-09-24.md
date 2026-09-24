# Weekly LLMOps Newsletter — 2026-09-24

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

### 2. Open Source LLM Infrastructure for Production AI: Building Sovereign, Customizable Intelligence

**Company:** nvidia

**Industry:** Tech

**Relevance score:** 122

**nvidia / Tech** — This panel discussion features leaders from NVIDIA, Prime Intellect, and RCAI discussing the infrastructure and operational challenges of deploying open source large language models in production environments. The conversation addresses the problem of enterprises lacking control, transparency, and cost predictability when using closed API models... — Tools: open_source,vllm,pytorch,langchain | Techniques: fine_tuning,reinforcement_learning,rlhf,model_optimization,cost_optimization,latency_optimization,agent_based,multi_agent_systems,harness_engineering,evals

**Source:** https://www.youtube.com/watch?v=FWMJQDH3iK0

---

### 3. Training Specialized Legal AI Models with Synthetic Data and KV Cache Compaction

**Company:** harvey_/_baseten

**Industry:** Legal

**Relevance score:** 122

**harvey_/_baseten / Legal** — Harvey, a legal AI company, partnered with Baseten's training team to develop specialized models for legal tasks like due diligence data room analysis. The core challenge was that frontier models failed at exhaustive document review and struggled with context windows far smaller than typical legal... — Tools: open_source,documentation,guardrails,reliability,scalability,pytorch,langchain,llama_index,chromadb,pinecone,qdrant | Techniques: fine_tuning,prompt_engineering,agent_based,multi_agent_systems,reinforcement_learning,rlhf,model_optimization,semantic_search,vector_search,token_optimization,cost_optimization,latency_optimization,harness_engineering,memory,chunking,evals

**Source:** https://www.youtube.com/watch?v=TU8kwE7z1qY

---

## Industry News

### 1. Operationalizing Enterprise Agents for Legal Work and Customer Experience

**Company:** harvey_/_sierra

**Industry:** Tech

**Relevance score:** 137

**harvey_/_sierra / Tech** — Harvey and Sierra illustrate two production approaches to enterprise GenAI: Harvey applies LLMs to high-volume legal workflows such as diligence, document extraction, drafting, and collaborative review, while Sierra deploys customer-service agents that retrieve business context and take actions across operational systems. Both companies have moved... — Tools: monitoring,databases,api_gateway,scalability,reliability,guardrails,security,compliance | Techniques: rag,fine_tuning,model_optimization,agent_based,memory,human_in_the_loop,latency_optimization,error_handling,evals

**Source:** https://www.youtube.com/watch?v=Bj2BRrAiOy4

---

### 2. Building a Managed Software Factory with Agentic AI

**Company:** uber

**Industry:** Tech

**Relevance score:** 132

**uber / Tech** — Uber built a comprehensive managed software factory powered by agentic AI to accelerate software development across thousands of engineers in 12 global tech sites. The solution consists of six core building blocks: a model gateway for secure API access with PII redaction, an MCP gateway... — Tools: kubernetes,docker,monitoring,cicd,scaling,microservices,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,guardrails,cache,spacy | Techniques: prompt_engineering,agent_based,multi_agent_systems,token_optimization,harness_engineering,human_in_the_loop,evals,few_shot,error_handling

**Source:** https://www.youtube.com/watch?v=17-YSUHo6Lk

---

### 3. Agentic AI for Healthcare Insurance Claims Processing with X12 Harness

**Company:** onlay

**Industry:** Healthcare

**Relevance score:** 127

**onlay / Healthcare** — Onlay has developed an agentic AI system to automate healthcare insurance claims processing workflows, addressing the complex multi-step patient journey from eligibility verification through to payment. The solution employs an execution layer that enables LLM agents to take actions across multiple systems including database queries... — Tools: databases,guardrails,documentation | Techniques: agent_based,multi_agent_systems,harness_engineering,memory,prompt_engineering,error_handling,cost_optimization,evals

**Source:** https://www.youtube.com/watch?v=UyyOoJmuATU

---

### 4. AI Agents in Software Development Lifecycle (SDLC) - Panel Discussion on Production Deployment

**Company:** overcut_/_hud

**Industry:** Tech

**Relevance score:** 127

**overcut_/_hud / Tech** — This panel discussion features representatives from Overcut and Hud discussing the practical implementation of AI agents throughout the software development lifecycle. The conversation addresses key challenges in deploying LLMs in production environments, including governance, quality assurance, context management, and cost optimization. Panelists share their experiences... — Tools: open_source,documentation,guardrails,monitoring,crewai | Techniques: agent_based,multi_agent_systems,prompt_engineering,few_shot,error_handling,cost_optimization,latency_optimization,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=25ecbeP5KR4

---

### 5. AI-Powered Citizen Inquiry Automation with Ticketing System Integration

**Company:** city_of_munich

**Industry:** Government

**Relevance score:** 127

**city_of_munich / Government** — The City of Munich IT department developed an AI-powered system to automate citizen inquiries through their Zammad ticketing platform, initially targeting the driver's licensing authority which handles approximately 16,000 requests annually. The solution uses a RAG-based architecture combining LLM-driven ticket classification, automated response generation from... — Tools: kubernetes,docker,langchain,postgresql,fastapi,chromadb | Techniques: rag,prompt_engineering,embeddings,few_shot,semantic_search,vector_search,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=9Sfxy2nmUU0

---

### 6. Building an Agentic Software Factory for High-Velocity Development

**Company:** openai

**Industry:** Tech

**Relevance score:** 122

**openai / Tech** — OpenAI has reorganized much of its internal software development and knowledge work around Codex and ChatGPT Work, using long-running coding agents, role-specific skills, broad enterprise context, automated testing, agentic code review, monitored deployment, performance analysis, and incident-response assistance. The reported result is rapid adoption across... — Tools: cicd,continuous_integration,continuous_deployment,devops,monitoring,reliability,scalability,documentation,orchestration | Techniques: agent_based,harness_engineering,human_in_the_loop,error_handling,latency_optimization,evals

**Source:** https://newsletter.pragmaticengineer.com/p/openai-software-factory

---

### 7. Designing Persistent, Multi-Agent Workflows for Grok Bot

**Company:** x_ai

**Industry:** Tech

**Relevance score:** 122

**x_ai / Tech** — X AI designed Grok Bot as a persistent-agent product rather than a collection of disposable chat sessions. Bots retain role-specific memory, tools, routines, and durable artifacts; they can browse the web, manipulate files, run software in an isolated computer environment, coordinate with other Bots, and... — Techniques: multi_agent_systems,agent_based,memory,human_in_the_loop

**Source:** https://x.ai/news/designing-grok-bot

---

### 8. Multi-Agent Automation for Feature-Flag Cleanup

**Company:** doordash

**Industry:** Tech

**Relevance score:** 122

**doordash / Tech** — DoorDash built a two-phase, human-in-the-loop multi-agent LLM system to remove stale feature flags, or dynamic values, from repositories and produce merge-ready pull requests. The system combines Jira intake, live rollout-state queries through MCP, repository-wide semantic code analysis, isolated parallel git worktrees, and deterministic build, test... — Tools: orchestration,scalability,reliability,guardrails,cicd | Techniques: multi_agent_systems,agent_based,human_in_the_loop,mcp,error_handling,fallback_strategies,cost_optimization,latency_optimization,evals

**Source:** https://careersatdoordash.com/blog/automating-feature-flag-cleanup-at-scale-with-a-multi-agent-llm-system/

---

### 9. Transitioning from Traditional Tech Company to AI-Native Digital Health Platform

**Company:** maven_clinic

**Industry:** Healthcare

**Relevance score:** 122

**maven_clinic / Healthcare** — Maven Clinic, the largest digital health platform focused on women and families, describes their two-year journey transforming from a traditional technology company to an AI-native organization. The company built Maven Intelligence, an orchestration layer that enables AI across all their products. Their transformation focused on... — Tools: documentation,monitoring,guardrails,reliability | Techniques: prompt_engineering,error_handling,evals,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=WJRdLNhrsLQ

---

### 10. Building Scalable AI Agents for Go-to-Market Automation at Production Scale

**Company:** unify

**Industry:** Tech

**Relevance score:** 122

**unify / Tech** — UniFi developed an AI agent platform that automates go-to-market research and outreach for sales teams, powering $900 million in pipeline. The company evolved from running millions of asynchronous web research agents to launching a chat-based interface where sales reps interact with agents that can write... — Tools: langchain,postgresql,docker,monitoring,security,cache | Techniques: prompt_engineering,agent_based,multi_agent_systems,memory,harness_engineering,cost_optimization,latency_optimization,few_shot,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=6898VdRtKDE

---

### 11. Multi-Agent AI Platform for Streaming Media Analytics and Content Production

**Company:** mbc_shahid

**Industry:** Media & Entertainment

**Relevance score:** 122

**mbc_shahid / Media & Entertainment** — MBC Shahid, the leading Arabic streaming platform in the MENA region with 35 million monthly active users, evolved from traditional BI dashboards to AI-powered data products through a three-season journey. The company built multiple production LLM applications using Databricks, including Enigma (a conversational analytics platform... — Tools: langchain,chromadb,pinecone,qdrant,fastapi,postgresql,redis,cache,monitoring,databases,api_gateway,orchestration,open_source,documentation,compliance,wandb | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,multi_agent_systems,agent_based,cost_optimization,human_in_the_loop,few_shot,evals

**Source:** https://www.youtube.com/watch?v=cA_HTWEhTtM

---

### 12. Multi-Agent Orchestration for Enterprise Sales with Amazon Bedrock AgentCore

**Company:** aws

**Industry:** Tech

**Relevance score:** 122

**aws / Tech** — AWS Sales faced an agent proliferation challenge with over 20 domain-specific AI agents deployed globally, forcing sales representatives to manually navigate between systems and manage context across fragmented conversations. To address this, AWS built Field Advisor on Amazon Bedrock AgentCore, creating a unified conversational interface... — Tools: microservices,orchestration,monitoring,guardrails,langchain,fastapi,cache | Techniques: multi_agent_systems,agent_based,prompt_engineering,memory,human_in_the_loop,rag,semantic_search,embeddings,token_optimization,error_handling,latency_optimization

**Source:** https://aws.amazon.com/blogs/machine-learning/powering-agentic-ai-sales-strategy-with-amazon-bedrock-agentcore/

---

### 13. Agentic Workflow Automation for Financial Operations

**Company:** ramp

**Industry:** Finance

**Relevance score:** 122

**ramp / Finance** — Ramp, a finance automation platform serving over 50,000 customers, built a comprehensive suite of AI agents to automate manual financial workflows including expense policy enforcement, accounting classification, and invoice processing. The company evolved from building hundreds of isolated agents to consolidating around a single agent... — Tools: langchain,fastapi,docker,kubernetes,monitoring,cicd,continuous_integration,continuous_deployment,open_source,documentation,guardrails,reliability,scalability,postgresql,cache,orchestration | Techniques: agent_based,multi_agent_systems,prompt_engineering,human_in_the_loop,few_shot,evals,token_optimization,error_handling,cost_optimization

**Source:** https://www.youtube.com/watch?v=NMs8C2_3M0w

---

## Cool Use Cases

### 1. Building Production-Scale Voice and Multi-Modal Customer Experience Agents

**Company:** sierra

**Industry:** Tech

**Relevance score:** 132

**sierra / Tech** — Sierra has built an enterprise agent platform serving most of the Fortune 20 companies, focusing on customer experience across sales, service, and loyalty touchpoints. The platform addresses the challenge of building reliable, low-latency conversational agents that can handle complex customer interactions across voice and chat... — Tools: monitoring,api_gateway,microservices,cicd,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,postgresql,cache,langchain | Techniques: prompt_engineering,few_shot,semantic_search,vector_search,model_optimization,token_optimization,error_handling,multi_agent_systems,agent_based,harness_engineering,memory,latency_optimization,cost_optimization,fallback_strategies,system_prompts,mcp,a2a,evals,fine_tuning,reranking,rag,embeddings,reinforcement_learning

**Source:** https://www.youtube.com/watch?v=uCKhOmth2ms

---

### 2. Production Paid Media Agent for Cross-Channel Campaign Operations

**Company:** langchain

**Industry:** Tech

**Relevance score:** 122

**langchain / Tech** — LangChain built a long-running paid media agent to help a small marketing team scale from organic growth to five paid advertising channels while managing fragmented campaign data, experiments, and optimization work. The agent runs in Slack and on a weekly schedule, combines advertising-platform data with... — Tools: langchain,databases,orchestration,open_source,security,guardrails,reliability,scalability | Techniques: prompt_engineering,system_prompts,multi_agent_systems,agent_based,human_in_the_loop,mcp,token_optimization,cost_optimization,latency_optimization,error_handling,evals

**Source:** https://www.langchain.com/blog/paid-media-agent

---

## Tools & Infrastructure

### 1. Multi-Agent Customer Support System for Sports Betting

**Company:** fanatics_betting

**Industry:** Media & Entertainment

**Relevance score:** 127

**fanatics_betting / Media & Entertainment** — Fanatics Betting and Gaming built a multi-agent AI customer support system on AWS to handle the complexity of sports betting customer service, where state-specific regulations, high-traffic events, and responsible gaming requirements create unique challenges. The system uses specialized agents orchestrated through Amazon EKS and Amazon... — Tools: kubernetes,databases,orchestration,guardrails,scalability,microservices,monitoring,api_gateway,compliance,security | Techniques: multi_agent_systems,rag,embeddings,prompt_engineering,semantic_search,vector_search,agent_based,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/how-fanatics-betting-and-gaming-built-a-multi-agent-customer-support-system/

---

### 2. AI-Powered CLI App Generation with Multi-Agent and Skills-Based Workflows

**Company:** wix

**Industry:** Tech

**Relevance score:** 122

**wix / Tech** — Wix built an AI app builder that enables users to generate CLI applications containing dashboard pages, backend services, site plugins, CMS collections, APIs, and other extensions, while allowing them to inspect, edit, preview, validate, and export the resulting code. The initial architecture used specialized agents... — Tools: open_source,documentation | Techniques: multi_agent_systems,agent_based,prompt_engineering,system_prompts,mcp,error_handling,latency_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=7HNaxSUPUTA

---

### 3. Evolution of AI Agent Architectures and Evaluation Strategies Across Model Generations

**Company:** braintrust

**Industry:** Tech

**Relevance score:** 122

**braintrust / Tech** — This presentation by Braintrust's Field CTO examines the challenge of maintaining AI applications through rapid generational shifts in foundation models. The problem is that each major model advancement requires significant re-architecting of AI systems, and traditional evaluation approaches become inadequate as architectures evolve from simple... — Tools: langchain,llama_index,monitoring,orchestration,documentation | Techniques: rag,prompt_engineering,agent_based,multi_agent_systems,memory,error_handling,few_shot,evals

**Source:** https://www.youtube.com/watch?v=nxokqOq1imY

---

### 4. Agentic AI for Aircraft In-Flight Entertainment Diagnostics at Scale

**Company:** panasonic_avionics_corporation

**Industry:** Other

**Relevance score:** 122

**panasonic_avionics_corporation / Other** — Panasonic Avionics Corporation faced significant challenges in diagnosing issues across its global fleet of in-flight entertainment and connectivity (IFEC) systems, where manual correlation of logs, metrics, and tickets across thousands of unique configurations took hours and required deep institutional knowledge. Working with AWS and the... — Tools: langchain,postgresql,orchestration,open_source,monitoring | Techniques: multi_agent_systems,agent_based,semantic_search,embeddings,prompt_engineering,human_in_the_loop

**Source:** https://aws.amazon.com/blogs/machine-learning/accelerating-aircraft-ifec-diagnostics-with-agentic-ai-on-aws/

---

### 5. Production AI and Trust in High-Stakes Government, Travel, and Healthcare Applications

**Company:** oracle_/_ca_dmv_/_tripadvisor

**Industry:** Government

**Relevance score:** 122

**oracle_/_ca_dmv_/_tripadvisor / Government** — This panel discussion brings together AI leaders from California DMV, Tripadvisor, and Oracle Health to explore the challenges of deploying LLM-based systems in production environments where failures have serious consequences. The panelists discuss how they ensure trust and reliability when deploying AI agents and GenAI... — Tools: monitoring,guardrails,langchain,crewai,postgresql,redis,chromadb,pinecone,wandb | Techniques: multi_agent_systems,agent_based,human_in_the_loop,memory,harness_engineering,prompt_engineering,embeddings

**Source:** https://www.youtube.com/watch?v=hXk-Ahocp04

---

### 6. Production LLM Systems: RAG Evaluation, Voice Agent Turn Detection, and Digital Persona Training

**Company:** various

**Industry:** Tech

**Relevance score:** 122

**various / Tech** — This case study presents three distinct production LLM implementations. Deep Verified built a self-hosted RAG platform for regulated fintech environments with comprehensive evaluation frameworks measuring answer accuracy, retrieval accuracy, latency, and observability over time. Alex AI developed a conversational voice agent for recruiting that solves... — Tools: langchain,postgresql,redis,chromadb,pinecone,qdrant,monitoring,databases,api_gateway,docker,kubernetes | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,agent_based,latency_optimization,evals,chunking

**Source:** https://www.youtube.com/watch?v=Wgud1JJNLfs

---

### 7. Production AI Deployment: Lessons from Real-World Agentic AI Systems

**Company:** databricks_/_various

**Industry:** Healthcare

**Relevance score:** 122

**databricks_/_various / Healthcare** — This case study presents lessons learned from deploying generative AI applications in production, with a specific focus on Flo Health's implementation of a women's health chatbot on the Databricks platform. The presentation addresses common failure points in GenAI projects including poor constraint definition, over-reliance on... — Tools: monitoring,cicd,devops,orchestration,continuous_deployment,continuous_integration,open_source,guardrails,reliability,scalability,langchain,llama_index,databases,api_gateway,microservices,scaling,postgresql | Techniques: rag,fine_tuning,prompt_engineering,few_shot,agent_based,multi_agent_systems,human_in_the_loop,latency_optimization,cost_optimization,system_prompts,evals,token_optimization,error_handling,instruction_tuning

**Source:** https://www.youtube.com/watch?v=mMQq-KDKEbA

---
