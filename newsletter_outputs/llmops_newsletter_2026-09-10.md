# Weekly LLMOps Newsletter — 2026-09-10

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Research Highlights

### 1. Semantic Retrieval and Ranking for Follows Recommendations

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 132

**linkedin / Tech** — LinkedIn rebuilt its Follows Recommendation system for the MyNetwork tab and Home Feed to address popularity bias, weak discovery of less-known creators, and cold-start recommendations for new members. The production pipeline converts member and creator profile information into narrative prompts, encodes both sides with a... — Tools: open_source,scalability | Techniques: embeddings,fine_tuning,prompt_engineering,semantic_search,vector_search,model_optimization,latency_optimization,evals

**Source:** https://www.linkedin.com/blog/engineering/ai/rebuilding-linkedins-follows-recommendations-with-llm-based-semantic-retrieval-and-ranking?utm_source=substack&utm_medium=email

---

### 2. Multi-Agent AI Contact Center Platform Serving 30 Million Subscribers

**Company:** lg_u+

**Industry:** Telecommunications

**Relevance score:** 132

**lg_u+ / Telecommunications** — LG U+ built a comprehensive AI Contact Center platform to handle customer service for 30 million subscribers across 17 contact centers with 4,500 human agents processing 150,000 calls daily. The solution includes customer-facing chatbots and voice bots for self-service, real-time AI advisors that assist human... — Tools: vllm,monitoring,open_source | Techniques: rag,embeddings,fine_tuning,prompt_engineering,reranking,few_shot,semantic_search,vector_search,multi_agent_systems,agent_based,harness_engineering,memory,human_in_the_loop,latency_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=eaSINaHBVf0

---

### 3. Reducing Coding-Agent Token Costs with Declarative Model Routing

**Company:** spotify

**Industry:** Tech

**Relevance score:** 127

**spotify / Tech** — Spotify used Portal's AiKA Modes and a Claude Code plugin called shunt to route predictable, I/O-heavy coding tasks from Claude Code to Gemini 2.5 Flash. Two ephemeral, declarative agents handled large-file analysis and boilerplate code generation, while Claude Code remained responsible for targeted reads, editing... — Techniques: agent_based,prompt_engineering,token_optimization,cost_optimization,latency_optimization,mcp,evals

**Source:** https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90

---

## Industry News

### 1. Operationalizing Enterprise Agents for Legal Work and Customer Experience

**Company:** harvey_/_sierra

**Industry:** Tech

**Relevance score:** 137

**harvey_/_sierra / Tech** — Harvey and Sierra illustrate two production approaches to enterprise GenAI: Harvey applies LLMs to high-volume legal workflows such as diligence, document extraction, drafting, and collaborative review, while Sierra deploys customer-service agents that retrieve business context and take actions across operational systems. Both companies have moved... — Tools: monitoring,databases,api_gateway,scalability,reliability,guardrails,security,compliance | Techniques: rag,fine_tuning,model_optimization,agent_based,memory,human_in_the_loop,latency_optimization,error_handling,evals

**Source:** https://www.youtube.com/watch?v=Bj2BRrAiOy4

---

### 2. AI-Powered Citizen Inquiry Automation with Ticketing System Integration

**Company:** city_of_munich

**Industry:** Government

**Relevance score:** 137

**city_of_munich / Government** — The City of Munich IT department developed an AI-powered system to automate citizen inquiries through their Zammad ticketing platform, initially targeting the driver's licensing authority which handles approximately 16,000 requests annually. The solution uses a RAG-based architecture combining LLM-driven ticket classification, automated response generation from... — Tools: kubernetes,docker,langchain,postgresql,fastapi,chromadb | Techniques: rag,prompt_engineering,embeddings,few_shot,semantic_search,vector_search,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=9Sfxy2nmUU0

---

### 3. Building a Managed Software Factory with Agentic AI

**Company:** uber

**Industry:** Tech

**Relevance score:** 132

**uber / Tech** — Uber built a comprehensive managed software factory powered by agentic AI to accelerate software development across thousands of engineers in 12 global tech sites. The solution consists of six core building blocks: a model gateway for secure API access with PII redaction, an MCP gateway... — Tools: kubernetes,docker,monitoring,cicd,scaling,microservices,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,guardrails,cache,spacy | Techniques: prompt_engineering,agent_based,multi_agent_systems,token_optimization,harness_engineering,human_in_the_loop,evals,few_shot,error_handling

**Source:** https://www.youtube.com/watch?v=17-YSUHo6Lk

---

### 4. Building Scalable AI Agents for Go-to-Market Automation at Production Scale

**Company:** unify

**Industry:** Tech

**Relevance score:** 132

**unify / Tech** — UniFi developed an AI agent platform that automates go-to-market research and outreach for sales teams, powering $900 million in pipeline. The company evolved from running millions of asynchronous web research agents to launching a chat-based interface where sales reps interact with agents that can write... — Tools: langchain,postgresql,docker,monitoring,security,cache | Techniques: prompt_engineering,agent_based,multi_agent_systems,memory,harness_engineering,cost_optimization,latency_optimization,few_shot,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=6898VdRtKDE

---

### 5. Multi-Agent AI Platform for Streaming Media Analytics and Content Production

**Company:** mbc_shahid

**Industry:** Media & Entertainment

**Relevance score:** 132

**mbc_shahid / Media & Entertainment** — MBC Shahid, the leading Arabic streaming platform in the MENA region with 35 million monthly active users, evolved from traditional BI dashboards to AI-powered data products through a three-season journey. The company built multiple production LLM applications using Databricks, including Enigma (a conversational analytics platform... — Tools: langchain,chromadb,pinecone,qdrant,fastapi,postgresql,redis,cache,monitoring,databases,api_gateway,orchestration,open_source,documentation,compliance,wandb | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,multi_agent_systems,agent_based,cost_optimization,human_in_the_loop,few_shot,evals

**Source:** https://www.youtube.com/watch?v=cA_HTWEhTtM

---

### 6. Agentic AI for Healthcare Insurance Claims Processing with X12 Harness

**Company:** onlay

**Industry:** Healthcare

**Relevance score:** 127

**onlay / Healthcare** — Onlay has developed an agentic AI system to automate healthcare insurance claims processing workflows, addressing the complex multi-step patient journey from eligibility verification through to payment. The solution employs an execution layer that enables LLM agents to take actions across multiple systems including database queries... — Tools: databases,guardrails,documentation | Techniques: agent_based,multi_agent_systems,harness_engineering,memory,prompt_engineering,error_handling,cost_optimization,evals

**Source:** https://www.youtube.com/watch?v=UyyOoJmuATU

---

### 7. AI Agents in Software Development Lifecycle (SDLC) - Panel Discussion on Production Deployment

**Company:** overcut_/_hud

**Industry:** Tech

**Relevance score:** 127

**overcut_/_hud / Tech** — This panel discussion features representatives from Overcut and Hud discussing the practical implementation of AI agents throughout the software development lifecycle. The conversation addresses key challenges in deploying LLMs in production environments, including governance, quality assurance, context management, and cost optimization. Panelists share their experiences... — Tools: open_source,documentation,guardrails,monitoring,crewai | Techniques: agent_based,multi_agent_systems,prompt_engineering,few_shot,error_handling,cost_optimization,latency_optimization,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=25ecbeP5KR4

---

### 8. UK-Sovereign AI Platform with Self-Hosted LLMs and 50+ Specialized Agents

**Company:** oneadvanced

**Industry:** Tech

**Relevance score:** 127

**oneadvanced / Tech** — OneAdvanced, a UK-based enterprise software provider serving over 10,000 customers in regulated industries including healthcare, legal, and public sector, needed to deploy AI capabilities while ensuring strict UK data sovereignty requirements. The company built a production AI solution by self-hosting Llama 4 Maverick and Llama... — Tools: vllm,postgresql,docker,microservices,guardrails,documentation,security,compliance,databases,monitoring | Techniques: rag,embeddings,prompt_engineering,multi_agent_systems,agent_based,semantic_search,vector_search,chunking,system_prompts,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/how-oneadvanced-deployed-over-50-ai-agents-on-uk-sovereign-aws/

---

### 9. Building Long-Horizon Autonomous Agents for Complex Accounting Work

**Company:** basis

**Industry:** Finance

**Relevance score:** 127

**basis / Finance** — Basis, a unicorn AI company, has developed autonomous agents capable of completing complex, multi-hour accounting tasks such as preparing entire tax returns end-to-end. The company addresses fundamental challenges in building long-horizon agents that operate reliably over extended periods, including managing context windows, ensuring process adherence... — Tools: open_source,documentation | Techniques: agent_based,multi_agent_systems,prompt_engineering,harness_engineering,human_in_the_loop,system_prompts,evals

**Source:** https://www.youtube.com/watch?v=54pwkcp48Lg

---

### 10. Scaling Generative AI in Large Industrial Enterprise Through Platform Architecture

**Company:** omv

**Industry:** Energy

**Relevance score:** 127

**omv / Energy** — OMV, Austria's largest industrial company operating across chemicals, fuels, and plastics sectors, faced the challenge of scaling generative AI across highly heterogeneous business divisions with 140+ use case demands from business units. The company implemented a federated platform approach centered on a central AI platform... — Tools: langchain,llama_index,chromadb,pinecone,qdrant,fastapi,microservices,api_gateway,documentation,orchestration,open_source | Techniques: rag,embeddings,reranking,prompt_engineering,agent_based,multi_agent_systems

**Source:** https://www.youtube.com/watch?v=c8KP7I7x6f8

---

### 11. Deploying AI Agents in High-Risk Finance and Legal Operations

**Company:** circle_/_wells_fargo_/_mayfield

**Industry:** Finance

**Relevance score:** 127

**circle_/_wells_fargo_/_mayfield / Finance** — Circle and Wells Fargo discuss their approaches to deploying AI agents in high-stakes finance and legal environments where the cost of failure is substantial. The organizations emphasize the critical importance of verifiability, auditability, and rigorous evaluation frameworks when implementing agents for tasks like SOX compliance... — Tools: langchain,crewai,documentation,security,compliance,guardrails | Techniques: agent_based,multi_agent_systems,evals,human_in_the_loop,harness_engineering,a2a,reinforcement_learning

**Source:** https://www.youtube.com/watch?v=elptCI-FSCA

---

### 12. Designing Persistent, Multi-Agent Workflows for Grok Bot

**Company:** x_ai

**Industry:** Tech

**Relevance score:** 122

**x_ai / Tech** — X AI designed Grok Bot as a persistent-agent product rather than a collection of disposable chat sessions. Bots retain role-specific memory, tools, routines, and durable artifacts; they can browse the web, manipulate files, run software in an isolated computer environment, coordinate with other Bots, and... — Techniques: multi_agent_systems,agent_based,memory,human_in_the_loop

**Source:** https://x.ai/news/designing-grok-bot

---

### 13. Multi-Agent Automation for Feature-Flag Cleanup

**Company:** doordash

**Industry:** Tech

**Relevance score:** 122

**doordash / Tech** — DoorDash built a two-phase, human-in-the-loop multi-agent LLM system to remove stale feature flags, or dynamic values, from repositories and produce merge-ready pull requests. The system combines Jira intake, live rollout-state queries through MCP, repository-wide semantic code analysis, isolated parallel git worktrees, and deterministic build, test... — Tools: orchestration,scalability,reliability,guardrails,cicd | Techniques: multi_agent_systems,agent_based,human_in_the_loop,mcp,error_handling,fallback_strategies,cost_optimization,latency_optimization,evals

**Source:** https://careersatdoordash.com/blog/automating-feature-flag-cleanup-at-scale-with-a-multi-agent-llm-system/

---

### 14. Transitioning from Traditional Tech Company to AI-Native Digital Health Platform

**Company:** maven_clinic

**Industry:** Healthcare

**Relevance score:** 122

**maven_clinic / Healthcare** — Maven Clinic, the largest digital health platform focused on women and families, describes their two-year journey transforming from a traditional technology company to an AI-native organization. The company built Maven Intelligence, an orchestration layer that enables AI across all their products. Their transformation focused on... — Tools: documentation,monitoring,guardrails,reliability | Techniques: prompt_engineering,error_handling,evals,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=WJRdLNhrsLQ

---

### 15. Enterprise-Scale Agentic Engineering: Building LLM Infrastructure and Tooling for 250+ Engineering Teams

**Company:** zalando

**Industry:** E-commerce

**Relevance score:** 122

**zalando / E-commerce** — Zalando, a major e-commerce company, shares their 2.5-year journey implementing agentic engineering and LLMOps practices across 250+ engineering teams. The company built a comprehensive LLM infrastructure starting with a LiteLLM-based API proxy deployed in January 2024, complemented by chat UIs, CLI tools, and coding agents... — Tools: kubernetes,docker,api_gateway,monitoring,cicd,orchestration,devops,open_source,documentation,security,guardrails,langchain,fastapi,scalability,reliability,cache,microservices | Techniques: prompt_engineering,agent_based,multi_agent_systems,cost_optimization,latency_optimization,evals,mcp,token_optimization

**Source:** https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html

---

### 16. Enterprise Sales Intelligence Agent: From Prototype to Production

**Company:** postman

**Industry:** Tech

**Relevance score:** 122

**postman / Tech** — Postman developed an enterprise sales intelligence agent to address context loss and information handoff challenges across their sales organization, which relied on multiple disconnected systems throughout the sales lifecycle. Starting with a hackathon that produced numerous prototypes, they identified a win-loss analysis agent as most... — Tools: guardrails,microservices | Techniques: prompt_engineering,multi_agent_systems,agent_based,human_in_the_loop,cost_optimization,evals

**Source:** https://www.youtube.com/watch?v=gjGAnb0if28

---

## Cool Use Cases

### 1. Building Production-Scale Voice and Multi-Modal Customer Experience Agents

**Company:** sierra

**Industry:** Tech

**Relevance score:** 132

**sierra / Tech** — Sierra has built an enterprise agent platform serving most of the Fortune 20 companies, focusing on customer experience across sales, service, and loyalty touchpoints. The platform addresses the challenge of building reliable, low-latency conversational agents that can handle complex customer interactions across voice and chat... — Tools: monitoring,api_gateway,microservices,cicd,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,postgresql,cache,langchain | Techniques: prompt_engineering,few_shot,semantic_search,vector_search,model_optimization,token_optimization,error_handling,multi_agent_systems,agent_based,harness_engineering,memory,latency_optimization,cost_optimization,fallback_strategies,system_prompts,mcp,a2a,evals,fine_tuning,reranking,rag,embeddings,reinforcement_learning

**Source:** https://www.youtube.com/watch?v=uCKhOmth2ms

---

### 2. Building Shared Memory for AI Agents with Notion-Backed Persistence

**Company:** notion

**Industry:** Tech

**Relevance score:** 122

**notion / Tech** — Notion developed Lore, an open-source system for shared, persistent memory for AI agents, to address the problem of tribal knowledge and experiential learning being lost across agent sessions. The solution uses Notion as a backing store with five interconnected databases (Projects, Topics, Memories, Entities, Facts)... — Tools: open_source,documentation | Techniques: memory,multi_agent_systems,agent_based,rag,semantic_search,evals

**Source:** https://www.notion.com/blog/building-shared-memory-for-ai-agents-in-notion

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
