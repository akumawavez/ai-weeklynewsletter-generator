# Weekly LLMOps Newsletter — 2026-08-27

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Research Highlights

### 1. Multi-Agent AI Contact Center Platform Serving 30 Million Subscribers

**Company:** lg_u+

**Industry:** Telecommunications

**Relevance score:** 142

**lg_u+ / Telecommunications** — LG U+ built a comprehensive AI Contact Center platform to handle customer service for 30 million subscribers across 17 contact centers with 4,500 human agents processing 150,000 calls daily. The solution includes customer-facing chatbots and voice bots for self-service, real-time AI advisors that assist human... — Tools: vllm,monitoring,open_source | Techniques: rag,embeddings,fine_tuning,prompt_engineering,reranking,few_shot,semantic_search,vector_search,multi_agent_systems,agent_based,harness_engineering,memory,human_in_the_loop,latency_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=eaSINaHBVf0

---

### 2. Engineering Reliable Multi-Agent LLM Systems by Starting Simple

**Company:** anthropic

**Industry:** Tech

**Relevance score:** 137

**anthropic / Tech** — Anthropic’s enterprise implementation work indicates that production agent performance depends on the combination of the model and its harness rather than on model intelligence alone. The recommended approach is to establish a strong single-agent baseline, isolate failure modes, and add multi-agent complexity only when context... — Techniques: multi_agent_systems,agent_based,harness_engineering,prompt_engineering,system_prompts,mcp,evals,cost_optimization,latency_optimization

**Source:** https://www.youtube.com/watch?v=IPu3HwtQb18

---

### 3. Safe Deployment of Clinical Conversational AI Through Simulation-Based Testing

**Company:** ufonia

**Industry:** Healthcare

**Relevance score:** 132

**ufonia / Healthcare** — Ufonia developed a comprehensive LLMOps framework for deploying Dora, a clinical conversational AI agent that conducts real medical conversations with patients across UK and US healthcare settings. The company built a simulation-based testing framework called Matrix that uses LLM-based patient simulators and automated judges to... — Techniques: prompt_engineering,few_shot,agent_based,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=McknwOzbmyg

---

### 4. AI-Powered Content Moderation Platform for Real-Time Marketplace Safety

**Company:** doordash

**Industry:** E-commerce

**Relevance score:** 132

**doordash / E-commerce** — DoorDash built SafeChat, an AI-powered safety system to moderate over 4 million daily messages exchanged between consumers, Dashers, and merchants in their marketplace. The solution employs a hybrid architecture with a fast, cheap internal classifier filtering obviously safe messages (90%+ of traffic) followed by LLM-based... — Tools: fastapi,monitoring,orchestration,microservices,scalability,reliability | Techniques: prompt_engineering,model_optimization,cost_optimization,latency_optimization,fallback_strategies,evals

**Source:** https://www.infoq.com/presentations/doordash-llm-ai-moderation-platform/

---

### 5. Open Source LLM Infrastructure for Production AI: Building Sovereign, Customizable Intelligence

**Company:** nvidia

**Industry:** Tech

**Relevance score:** 132

**nvidia / Tech** — This panel discussion features leaders from NVIDIA, Prime Intellect, and RCAI discussing the infrastructure and operational challenges of deploying open source large language models in production environments. The conversation addresses the problem of enterprises lacking control, transparency, and cost predictability when using closed API models... — Tools: open_source,vllm,pytorch,langchain | Techniques: fine_tuning,reinforcement_learning,rlhf,model_optimization,cost_optimization,latency_optimization,agent_based,multi_agent_systems,harness_engineering,evals

**Source:** https://www.youtube.com/watch?v=FWMJQDH3iK0

---

## Industry News

### 1. Building a Managed Software Factory with Agentic AI

**Company:** uber

**Industry:** Tech

**Relevance score:** 152

**uber / Tech** — Uber built a comprehensive managed software factory powered by agentic AI to accelerate software development across thousands of engineers in 12 global tech sites. The solution consists of six core building blocks: a model gateway for secure API access with PII redaction, an MCP gateway... — Tools: kubernetes,docker,monitoring,cicd,scaling,microservices,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,guardrails,cache,spacy | Techniques: prompt_engineering,agent_based,multi_agent_systems,token_optimization,harness_engineering,human_in_the_loop,evals,few_shot,error_handling

**Source:** https://www.youtube.com/watch?v=17-YSUHo6Lk

---

### 2. Agentic AI for Healthcare Insurance Claims Processing with X12 Harness

**Company:** onlay

**Industry:** Healthcare

**Relevance score:** 147

**onlay / Healthcare** — Onlay has developed an agentic AI system to automate healthcare insurance claims processing workflows, addressing the complex multi-step patient journey from eligibility verification through to payment. The solution employs an execution layer that enables LLM agents to take actions across multiple systems including database queries... — Tools: databases,guardrails,documentation | Techniques: agent_based,multi_agent_systems,harness_engineering,memory,prompt_engineering,error_handling,cost_optimization,evals

**Source:** https://www.youtube.com/watch?v=UyyOoJmuATU

---

### 3. AI Agents in Software Development Lifecycle (SDLC) - Panel Discussion on Production Deployment

**Company:** overcut_/_hud

**Industry:** Tech

**Relevance score:** 147

**overcut_/_hud / Tech** — This panel discussion features representatives from Overcut and Hud discussing the practical implementation of AI agents throughout the software development lifecycle. The conversation addresses key challenges in deploying LLMs in production environments, including governance, quality assurance, context management, and cost optimization. Panelists share their experiences... — Tools: open_source,documentation,guardrails,monitoring,crewai | Techniques: agent_based,multi_agent_systems,prompt_engineering,few_shot,error_handling,cost_optimization,latency_optimization,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=25ecbeP5KR4

---

### 4. Multi-Agent Automation for Feature-Flag Cleanup

**Company:** doordash

**Industry:** Tech

**Relevance score:** 142

**doordash / Tech** — DoorDash built a two-phase, human-in-the-loop multi-agent LLM system to remove stale feature flags, or dynamic values, from repositories and produce merge-ready pull requests. The system combines Jira intake, live rollout-state queries through MCP, repository-wide semantic code analysis, isolated parallel git worktrees, and deterministic build, test... — Tools: orchestration,scalability,reliability,guardrails,cicd | Techniques: multi_agent_systems,agent_based,human_in_the_loop,mcp,error_handling,fallback_strategies,cost_optimization,latency_optimization,evals

**Source:** https://careersatdoordash.com/blog/automating-feature-flag-cleanup-at-scale-with-a-multi-agent-llm-system/

---

### 5. Transitioning from Traditional Tech Company to AI-Native Digital Health Platform

**Company:** maven_clinic

**Industry:** Healthcare

**Relevance score:** 142

**maven_clinic / Healthcare** — Maven Clinic, the largest digital health platform focused on women and families, describes their two-year journey transforming from a traditional technology company to an AI-native organization. The company built Maven Intelligence, an orchestration layer that enables AI across all their products. Their transformation focused on... — Tools: documentation,monitoring,guardrails,reliability | Techniques: prompt_engineering,error_handling,evals,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=WJRdLNhrsLQ

---

### 6. Token Ops: Runaway Token Governance for AI Agents

**Company:** microsoft

**Industry:** Tech

**Relevance score:** 137

**microsoft / Tech** — This presentation addresses the challenge of uncontrolled token consumption in AI agent systems, where organizations struggle to trace and manage escalating costs from model calls. The speakers introduce Token Ops, an out-of-band governance platform that manages costs at the agent run level rather than just... — Tools: langchain,open_source,monitoring,orchestration | Techniques: multi_agent_systems,agent_based,prompt_engineering,rag,cost_optimization,token_optimization,system_prompts,evals

**Source:** https://www.youtube.com/watch?v=GJX19pNhmSw

---

### 7. AI-Powered Citizen Inquiry Automation with Ticketing System Integration

**Company:** city_of_munich

**Industry:** Government

**Relevance score:** 137

**city_of_munich / Government** — The City of Munich IT department developed an AI-powered system to automate citizen inquiries through their Zammad ticketing platform, initially targeting the driver's licensing authority which handles approximately 16,000 requests annually. The solution uses a RAG-based architecture combining LLM-driven ticket classification, automated response generation from... — Tools: kubernetes,docker,langchain,postgresql,fastapi,chromadb | Techniques: rag,prompt_engineering,embeddings,few_shot,semantic_search,vector_search,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=9Sfxy2nmUU0

---

### 8. Auto-Generated Codebase Documentation and Intelligence at Scale

**Company:** cognition

**Industry:** Tech

**Relevance score:** 132

**cognition / Tech** — Cognition developed DeepWiki, a system that automatically generates comprehensive documentation for code repositories, initially built to help their AI coding agent Devin understand codebases better. The system addresses the challenge of creating high-quality, scalable documentation for repositories ranging from small projects to enterprise codebases with... — Tools: langchain,cache | Techniques: rag,prompt_engineering,agent_based,multi_agent_systems,semantic_search,few_shot,cost_optimization,latency_optimization,harness_engineering,evals

**Source:** https://www.youtube.com/watch?v=u8Im0l_vwqM

---

### 9. Context Engine for Production Agent Systems

**Company:** unblocked

**Industry:** Tech

**Relevance score:** 132

**unblocked / Tech** — Unblocked addresses the critical challenge of deploying AI agents in production environments where they make confidently wrong decisions due to missing organizational context. While modern frameworks and cloud infrastructure have made building agents technically trivial, agents deployed without human oversight lack access to the institutional... — Tools: langchain,fastapi,monitoring,databases,orchestration,open_source,documentation,serverless | Techniques: prompt_engineering,agent_based,multi_agent_systems,system_prompts,mcp,error_handling,semantic_search

**Source:** https://www.youtube.com/watch?v=HvMyYLTfvhg

---

### 10. Building a Cloud Agent Platform for Scalable AI-Powered Development Workflows

**Company:** warp

**Industry:** Tech

**Relevance score:** 132

**warp / Tech** — Warp, a developer tools company that evolved from a terminal application into an agentic development environment, built a cloud agent platform to enable AI agents to perform long-running, complex development tasks beyond what's possible on local machines. The platform abstracts infrastructure complexity by providing flexible... — Tools: docker,kubernetes,api_gateway,microservices,cicd,orchestration,open_source,documentation | Techniques: prompt_engineering,multi_agent_systems,agent_based,harness_engineering,human_in_the_loop,semantic_search

**Source:** https://www.youtube.com/watch?v=L173Z8DpaJg

---

### 11. Building Scalable AI Agents for Go-to-Market Automation at Production Scale

**Company:** unify

**Industry:** Tech

**Relevance score:** 132

**unify / Tech** — UniFi developed an AI agent platform that automates go-to-market research and outreach for sales teams, powering $900 million in pipeline. The company evolved from running millions of asynchronous web research agents to launching a chat-based interface where sales reps interact with agents that can write... — Tools: langchain,postgresql,docker,monitoring,security,cache | Techniques: prompt_engineering,agent_based,multi_agent_systems,memory,harness_engineering,cost_optimization,latency_optimization,few_shot,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=6898VdRtKDE

---

### 12. Multi-Agent AI Platform for Streaming Media Analytics and Content Production

**Company:** mbc_shahid

**Industry:** Media & Entertainment

**Relevance score:** 132

**mbc_shahid / Media & Entertainment** — MBC Shahid, the leading Arabic streaming platform in the MENA region with 35 million monthly active users, evolved from traditional BI dashboards to AI-powered data products through a three-season journey. The company built multiple production LLM applications using Databricks, including Enigma (a conversational analytics platform... — Tools: langchain,chromadb,pinecone,qdrant,fastapi,postgresql,redis,cache,monitoring,databases,api_gateway,orchestration,open_source,documentation,compliance,wandb | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,multi_agent_systems,agent_based,cost_optimization,human_in_the_loop,few_shot,evals

**Source:** https://www.youtube.com/watch?v=cA_HTWEhTtM

---

## Cool Use Cases

### 1. Building an Always-On Agentic Teammate for Platform Engineering

**Company:** melio

**Industry:** Finance

**Relevance score:** 137

**melio / Finance** — Melio, a fintech company operating in the payments space, embarked on a journey to implement an always-on AI agent as a digital teammate working alongside their engineering teams. After initially exploring and piloting commercial solutions like Devin (similar to OpenClaw) for approximately two months, the... — Tools: kubernetes,docker,fastapi,cicd,open_source,documentation,security | Techniques: prompt_engineering,mcp,agent_based,multi_agent_systems,harness_engineering

**Source:** https://www.youtube.com/watch?v=N2TNOpWaImY

---

### 2. From Fine-Tuning to Agentic RAG: Reducing Technical Debt in Conversational AI for Auto Lease Buyouts

**Company:** lease_end

**Industry:** Automotive

**Relevance score:** 132

**lease_end / Automotive** — Lease End built an LLM-based conversational application in late 2024 to help customers nearing the end of their auto lease connect with sales teams via text messages. Initially, the system used a RAG-based workflow with fine-tuned models for intent classification across six categories, which generated... — Tools: langchain,fastapi,chromadb,pinecone,qdrant,postgresql,mysql,sqlite,redis | Techniques: rag,fine_tuning,prompt_engineering,agent_based,few_shot,semantic_search,vector_search,cost_optimization,latency_optimization,system_prompts,evals

**Source:** https://www.youtube.com/watch?v=4loPnxvWWhg

---

## Tools & Infrastructure

### 1. Multi-Agent Customer Support System for Sports Betting

**Company:** fanatics_betting

**Industry:** Media & Entertainment

**Relevance score:** 147

**fanatics_betting / Media & Entertainment** — Fanatics Betting and Gaming built a multi-agent AI customer support system on AWS to handle the complexity of sports betting customer service, where state-specific regulations, high-traffic events, and responsible gaming requirements create unique challenges. The system uses specialized agents orchestrated through Amazon EKS and Amazon... — Tools: kubernetes,databases,orchestration,guardrails,scalability,microservices,monitoring,api_gateway,compliance,security | Techniques: multi_agent_systems,rag,embeddings,prompt_engineering,semantic_search,vector_search,agent_based,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/how-fanatics-betting-and-gaming-built-a-multi-agent-customer-support-system/

---

### 2. AI-Powered CLI App Generation with Multi-Agent and Skills-Based Workflows

**Company:** wix

**Industry:** Tech

**Relevance score:** 142

**wix / Tech** — Wix built an AI app builder that enables users to generate CLI applications containing dashboard pages, backend services, site plugins, CMS collections, APIs, and other extensions, while allowing them to inspect, edit, preview, validate, and export the resulting code. The initial architecture used specialized agents... — Tools: open_source,documentation | Techniques: multi_agent_systems,agent_based,prompt_engineering,system_prompts,mcp,error_handling,latency_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=7HNaxSUPUTA

---

### 3. Evolution of AI Agent Architectures and Evaluation Strategies Across Model Generations

**Company:** braintrust

**Industry:** Tech

**Relevance score:** 142

**braintrust / Tech** — This presentation by Braintrust's Field CTO examines the challenge of maintaining AI applications through rapid generational shifts in foundation models. The problem is that each major model advancement requires significant re-architecting of AI systems, and traditional evaluation approaches become inadequate as architectures evolve from simple... — Tools: langchain,llama_index,monitoring,orchestration,documentation | Techniques: rag,prompt_engineering,agent_based,multi_agent_systems,memory,error_handling,few_shot,evals

**Source:** https://www.youtube.com/watch?v=nxokqOq1imY

---

### 4. Agentic AI for Aircraft In-Flight Entertainment Diagnostics at Scale

**Company:** panasonic_avionics_corporation

**Industry:** Other

**Relevance score:** 142

**panasonic_avionics_corporation / Other** — Panasonic Avionics Corporation faced significant challenges in diagnosing issues across its global fleet of in-flight entertainment and connectivity (IFEC) systems, where manual correlation of logs, metrics, and tickets across thousands of unique configurations took hours and required deep institutional knowledge. Working with AWS and the... — Tools: langchain,postgresql,orchestration,open_source,monitoring | Techniques: multi_agent_systems,agent_based,semantic_search,embeddings,prompt_engineering,human_in_the_loop

**Source:** https://aws.amazon.com/blogs/machine-learning/accelerating-aircraft-ifec-diagnostics-with-agentic-ai-on-aws/

---

### 5. Production AI and Trust in High-Stakes Government, Travel, and Healthcare Applications

**Company:** oracle_/_ca_dmv_/_tripadvisor

**Industry:** Government

**Relevance score:** 132

**oracle_/_ca_dmv_/_tripadvisor / Government** — This panel discussion brings together AI leaders from California DMV, Tripadvisor, and Oracle Health to explore the challenges of deploying LLM-based systems in production environments where failures have serious consequences. The panelists discuss how they ensure trust and reliability when deploying AI agents and GenAI... — Tools: monitoring,guardrails,langchain,crewai,postgresql,redis,chromadb,pinecone,wandb | Techniques: multi_agent_systems,agent_based,human_in_the_loop,memory,harness_engineering,prompt_engineering,embeddings

**Source:** https://www.youtube.com/watch?v=hXk-Ahocp04

---

### 6. Production LLM Systems: RAG Evaluation, Voice Agent Turn Detection, and Digital Persona Training

**Company:** various

**Industry:** Tech

**Relevance score:** 132

**various / Tech** — This case study presents three distinct production LLM implementations. Deep Verified built a self-hosted RAG platform for regulated fintech environments with comprehensive evaluation frameworks measuring answer accuracy, retrieval accuracy, latency, and observability over time. Alex AI developed a conversational voice agent for recruiting that solves... — Tools: langchain,postgresql,redis,chromadb,pinecone,qdrant,monitoring,databases,api_gateway,docker,kubernetes | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,agent_based,latency_optimization,evals,chunking

**Source:** https://www.youtube.com/watch?v=Wgud1JJNLfs

---
