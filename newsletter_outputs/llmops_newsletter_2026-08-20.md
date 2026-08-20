# Weekly LLMOps Newsletter — 2026-08-20

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Research Highlights

### 1. Training and Deploying Create 2: A Stylistically Diverse Image Foundation Model

**Company:** krea

**Industry:** Media & Entertainment

**Relevance score:** 142

**krea / Media & Entertainment** — Krea developed and open-sourced Create 2, an image foundation model designed to prioritize stylistic diversity and faster generation over the mode-collapsed outputs of competitors. The team addressed the challenge of creative professionals needing diverse visual exploration tools rather than consistently safe but homogeneous results. Their... — Tools: pytorch,spacy,chromadb,pinecone | Techniques: fine_tuning,prompt_engineering,reinforcement_learning,rlhf,embeddings,semantic_search

**Source:** https://www.youtube.com/watch?v=-tviRdpmHvs

---

### 2. Multi-Agent AI Contact Center Platform Serving 30 Million Subscribers

**Company:** lg_u+

**Industry:** Telecommunications

**Relevance score:** 142

**lg_u+ / Telecommunications** — LG U+ built a comprehensive AI Contact Center platform to handle customer service for 30 million subscribers across 17 contact centers with 4,500 human agents processing 150,000 calls daily. The solution includes customer-facing chatbots and voice bots for self-service, real-time AI advisors that assist human... — Tools: vllm,monitoring,open_source | Techniques: rag,embeddings,fine_tuning,prompt_engineering,reranking,few_shot,semantic_search,vector_search,multi_agent_systems,agent_based,harness_engineering,memory,human_in_the_loop,latency_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=eaSINaHBVf0

---

### 3. Scaling Agentic AI Infrastructure for Production ML Workflows

**Company:** linkedin

**Industry:** Tech

**Relevance score:** 137

**linkedin / Tech** — LinkedIn's AI platforms team developed an agentic platform to automate complex machine learning tasks including migrating 400+ TensorFlow models to PyTorch, optimizing cluster performance, and conducting autonomous research experiments. The platform uses code-based agents that run iterative experiments over hours or days, launching hundreds of... — Tools: kubernetes,pytorch,tensorflow,guardrails,monitoring | Techniques: agent_based,multi_agent_systems,harness_engineering,memory,human_in_the_loop,model_optimization,latency_optimization

**Source:** https://www.youtube.com/watch?v=FJUrsZn1BSI

---

### 4. Open Source LLM Infrastructure for Production AI: Building Sovereign, Customizable Intelligence

**Company:** nvidia

**Industry:** Tech

**Relevance score:** 132

**nvidia / Tech** — This panel discussion features leaders from NVIDIA, Prime Intellect, and RCAI discussing the infrastructure and operational challenges of deploying open source large language models in production environments. The conversation addresses the problem of enterprises lacking control, transparency, and cost predictability when using closed API models... — Tools: open_source,vllm,pytorch,langchain | Techniques: fine_tuning,reinforcement_learning,rlhf,model_optimization,cost_optimization,latency_optimization,agent_based,multi_agent_systems,harness_engineering,evals

**Source:** https://www.youtube.com/watch?v=FWMJQDH3iK0

---

### 5. Training Specialized Legal AI Models with Synthetic Data and KV Cache Compaction

**Company:** harvey_/_baseten

**Industry:** Legal

**Relevance score:** 132

**harvey_/_baseten / Legal** — Harvey, a legal AI company, partnered with Baseten's training team to develop specialized models for legal tasks like due diligence data room analysis. The core challenge was that frontier models failed at exhaustive document review and struggled with context windows far smaller than typical legal... — Tools: open_source,documentation,guardrails,reliability,scalability,pytorch,langchain,llama_index,chromadb,pinecone,qdrant | Techniques: fine_tuning,prompt_engineering,agent_based,multi_agent_systems,reinforcement_learning,rlhf,model_optimization,semantic_search,vector_search,token_optimization,cost_optimization,latency_optimization,harness_engineering,memory,chunking,evals

**Source:** https://www.youtube.com/watch?v=TU8kwE7z1qY

---

## Industry News

### 1. Building Scalable AI Agents for Go-to-Market Automation at Production Scale

**Company:** unify

**Industry:** Tech

**Relevance score:** 152

**unify / Tech** — UniFi developed an AI agent platform that automates go-to-market research and outreach for sales teams, powering $900 million in pipeline. The company evolved from running millions of asynchronous web research agents to launching a chat-based interface where sales reps interact with agents that can write... — Tools: langchain,postgresql,docker,monitoring,security,cache | Techniques: prompt_engineering,agent_based,multi_agent_systems,memory,harness_engineering,cost_optimization,latency_optimization,few_shot,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=6898VdRtKDE

---

### 2. Multi-Agent AI Platform for Streaming Media Analytics and Content Production

**Company:** mbc_shahid

**Industry:** Media & Entertainment

**Relevance score:** 152

**mbc_shahid / Media & Entertainment** — MBC Shahid, the leading Arabic streaming platform in the MENA region with 35 million monthly active users, evolved from traditional BI dashboards to AI-powered data products through a three-season journey. The company built multiple production LLM applications using Databricks, including Enigma (a conversational analytics platform... — Tools: langchain,chromadb,pinecone,qdrant,fastapi,postgresql,redis,cache,monitoring,databases,api_gateway,orchestration,open_source,documentation,compliance,wandb | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,multi_agent_systems,agent_based,cost_optimization,human_in_the_loop,few_shot,evals

**Source:** https://www.youtube.com/watch?v=cA_HTWEhTtM

---

### 3. UK-Sovereign AI Platform with Self-Hosted LLMs and 50+ Specialized Agents

**Company:** oneadvanced

**Industry:** Tech

**Relevance score:** 147

**oneadvanced / Tech** — OneAdvanced, a UK-based enterprise software provider serving over 10,000 customers in regulated industries including healthcare, legal, and public sector, needed to deploy AI capabilities while ensuring strict UK data sovereignty requirements. The company built a production AI solution by self-hosting Llama 4 Maverick and Llama... — Tools: vllm,postgresql,docker,microservices,guardrails,documentation,security,compliance,databases,monitoring | Techniques: rag,embeddings,prompt_engineering,multi_agent_systems,agent_based,semantic_search,vector_search,chunking,system_prompts,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/how-oneadvanced-deployed-over-50-ai-agents-on-uk-sovereign-aws/

---

### 4. Enterprise-Scale Agentic Engineering: Building LLM Infrastructure and Tooling for 250+ Engineering Teams

**Company:** zalando

**Industry:** E-commerce

**Relevance score:** 142

**zalando / E-commerce** — Zalando, a major e-commerce company, shares their 2.5-year journey implementing agentic engineering and LLMOps practices across 250+ engineering teams. The company built a comprehensive LLM infrastructure starting with a LiteLLM-based API proxy deployed in January 2024, complemented by chat UIs, CLI tools, and coding agents... — Tools: kubernetes,docker,api_gateway,monitoring,cicd,orchestration,devops,open_source,documentation,security,guardrails,langchain,fastapi,scalability,reliability,cache,microservices | Techniques: prompt_engineering,agent_based,multi_agent_systems,cost_optimization,latency_optimization,evals,mcp,token_optimization

**Source:** https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html

---

### 5. Enterprise Sales Intelligence Agent: From Prototype to Production

**Company:** postman

**Industry:** Tech

**Relevance score:** 142

**postman / Tech** — Postman developed an enterprise sales intelligence agent to address context loss and information handoff challenges across their sales organization, which relied on multiple disconnected systems throughout the sales lifecycle. Starting with a hackathon that produced numerous prototypes, they identified a win-loss analysis agent as most... — Tools: guardrails,microservices | Techniques: prompt_engineering,multi_agent_systems,agent_based,human_in_the_loop,cost_optimization,evals

**Source:** https://www.youtube.com/watch?v=gjGAnb0if28

---

### 6. Building Autonomous Software Factories with AI Agents

**Company:** factory

**Industry:** Tech

**Relevance score:** 142

**factory / Tech** — Factory presents a vision for transforming software development through "software factories" - autonomous systems where signals like customer feedback, bugs, and business requirements flow directly to deployed code with minimal human intervention. The problem addressed is that while AI-powered coding tools have evolved from autocomplete... — Tools: docker,monitoring,devops,orchestration,cicd,continuous_deployment,continuous_integration,guardrails,reliability,scalability,security | Techniques: agent_based,multi_agent_systems,harness_engineering,human_in_the_loop,cost_optimization,latency_optimization,evals

**Source:** https://www.youtube.com/watch?v=Pa3MAnWeNB4

---

### 7. Verifiable and Auditable AI Agent Payment Processing with Hardware Attestation

**Company:** solv_labs

**Industry:** Tech

**Relevance score:** 142

**solv_labs / Tech** — Solv Labs built an AI agent payment workflow on Amazon Bedrock AgentCore payments to address the enterprise challenge of proving that autonomous agent payments are authorized, risk-priced, and auditable. The solution combines AgentCore payments for payment processing, ORACLE (Solv's policy engine) for pre-authorization, ICME PreFlight... — Tools: monitoring,security,compliance,guardrails,reliability,fastapi,databases | Techniques: agent_based,multi_agent_systems,cost_optimization,latency_optimization,error_handling

**Source:** https://aws.amazon.com/blogs/machine-learning/pay-with-confidence-how-solv-labs-built-verifiable-auditable-agent-payments-on-amazon-bedrock-agentcore-payments/

---

### 8. Multi-Tenant AI Agent Deployment with Secure Isolation Using Amazon Bedrock AgentCore

**Company:** axonious

**Industry:** Tech

**Relevance score:** 142

**axonious / Tech** — Axonius, a cybersecurity asset intelligence platform serving hundreds of isolated customer environments, needed to add AI agents to their SaaS offering while maintaining strict tenant isolation and security requirements. They deployed a silo-model architecture using Amazon Bedrock AgentCore runtime, where each customer receives a dedicated... — Tools: langchain,docker,monitoring,databases,api_gateway,microservices,cicd,devops,orchestration,continuous_deployment,security,compliance,guardrails,scalability | Techniques: rag,prompt_engineering,agent_based,multi_agent_systems,memory,cost_optimization,latency_optimization

**Source:** https://aws.amazon.com/blogs/machine-learning/how-axonius-built-secure-multi-tenant-ai-agents-on-bedrock-agentcore/

---

### 9. Practical Approaches to AI Agent Evaluation and Floor Raising in Production

**Company:** raindrop

**Industry:** Tech

**Relevance score:** 142

**raindrop / Tech** — Raindrop's CTO presents practical lessons from observing real-world AI agent deployments across finance, healthcare, and defense sectors. The talk challenges conventional evaluation approaches inherited from the chatbot era, arguing that static benchmark-style evaluations don't scale for modern agentic systems. Instead, the company advocates for "raising... — Tools: monitoring,open_source,documentation | Techniques: prompt_engineering,agent_based,evals,error_handling

**Source:** https://www.youtube.com/watch?v=jHMiYtjoJfA

---

### 10. Building Context-Aware Consumer AI at Scale with Agentic Recommendations

**Company:** doordash

**Industry:** E-commerce

**Relevance score:** 137

**doordash / E-commerce** — DoorDash transformed their recommendation systems from legacy one-shot predictions to a sophisticated agentic platform to support multi-state shopping experiences like grocery planning. The company developed language-native consumer memory blocks to replace traditional embeddings, implemented semantic IDs (RQ-VAE) for granular catalog representation, built grounded search systems... — Tools: langchain,pytorch,tensorflow,chromadb,pinecone,qdrant,monitoring,databases,api_gateway,microservices,open_source | Techniques: rag,embeddings,semantic_search,vector_search,few_shot,reranking,prompt_engineering,memory,multi_agent_systems,agent_based,harness_engineering,mcp,evals

**Source:** https://www.infoq.com/presentations/ai-agentic-recommendations-semantic-ids/

---

### 11. Runtime Security and Governance Framework for AI Agents

**Company:** thales_group

**Industry:** Tech

**Relevance score:** 137

**thales_group / Tech** — Thales Group developed a comprehensive security and governance framework to address the operational risks of autonomous AI agents in production environments. The problem centered on agents potentially exceeding their intended boundaries and performing unauthorized actions, particularly concerning given the complex interactions between users, agents, sub-agents... — Tools: monitoring,security,compliance,orchestration,guardrails | Techniques: multi_agent_systems,agent_based,human_in_the_loop,error_handling,latency_optimization,cost_optimization,fallback_strategies

**Source:** https://www.youtube.com/watch?v=czfKC-p79tA

---

### 12. Building Agent-First Data Infrastructure with Comprehensive Evaluation Frameworks

**Company:** bauplan

**Industry:** Tech

**Relevance score:** 137

**bauplan / Tech** — Bauplan, a data infrastructure company built for agents as first-class users, developed a comprehensive evaluation framework for LLM coding agents working on data engineering tasks. The company created 700 evaluation tasks derived from real-world customer usage patterns, significantly more than competing frameworks from Supabase (20+... — Tools: fastapi,postgresql,docker,kubernetes,cicd,api_gateway,open_source,documentation | Techniques: prompt_engineering,evals,agent_based,multi_agent_systems,human_in_the_loop,cost_optimization,latency_optimization,system_prompts

**Source:** https://www.youtube.com/watch?v=3JvR0Wb3XWg

---

### 13. Securing AI Agents with Network-Level Proxy Controls for Production Infrastructure

**Company:** deno

**Industry:** Tech

**Relevance score:** 137

**deno / Tech** — Deno faced the challenge of using AI agents powered by models like Claude Opus to automatically handle production incidents in their Deno Deploy hosting service, requiring agents to access critical systems like PostgreSQL, Kubernetes, ClickHouse, AWS, GitHub, and Slack with write permissions. While the agents... — Tools: kubernetes,postgresql,monitoring,databases,security,guardrails,fastapi,docker,microservices | Techniques: agent_based,prompt_engineering,human_in_the_loop,multi_agent_systems

**Source:** https://www.youtube.com/watch?v=MkRYPFIMCSA

---

### 14. AI-Powered Citizen Inquiry Automation with Ticketing System Integration

**Company:** city_of_munich

**Industry:** Government

**Relevance score:** 137

**city_of_munich / Government** — The City of Munich IT department developed an AI-powered system to automate citizen inquiries through their Zammad ticketing platform, initially targeting the driver's licensing authority which handles approximately 16,000 requests annually. The solution uses a RAG-based architecture combining LLM-driven ticket classification, automated response generation from... — Tools: kubernetes,docker,langchain,postgresql,fastapi,chromadb | Techniques: rag,prompt_engineering,embeddings,few_shot,semantic_search,vector_search,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=9Sfxy2nmUU0

---

### 15. Autonomous Integration Factory Using LLM Agents

**Company:** ramp

**Industry:** Finance

**Relevance score:** 132

**ramp / Finance** — Ramp faced the classic engineering scaling problem where customer demand for integrations with third-party tools far exceeded their team's capacity to build and maintain them manually. To solve this, they built two complementary LLM-powered systems: a customer-facing agentic system that autonomously builds custom integrations on-demand... — Tools: api_gateway,monitoring,security,guardrails,fastapi,documentation | Techniques: agent_based,multi_agent_systems,prompt_engineering,error_handling,harness_engineering,evals

**Source:** https://builders.ramp.com/post/integrations-that-write-themselves

---

### 16. Building an Evaluation-First Culture for Enterprise Agent Platform

**Company:** uber

**Industry:** Tech

**Relevance score:** 132

**uber / Tech** — Uber's agent platform team faced a common challenge where development teams would ship LLM-powered agents to production and defer evaluation development until later, creating a cycle of retrofitting and debugging. To solve this, they built platform capabilities that made evaluations the default from day one... — Tools: monitoring | Techniques: prompt_engineering,multi_agent_systems,agent_based,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=UTcKagbKp4A

---

## Cool Use Cases

### 1. Building Shared Memory for AI Agents with Notion-Backed Persistence

**Company:** notion

**Industry:** Tech

**Relevance score:** 142

**notion / Tech** — Notion developed Lore, an open-source system for shared, persistent memory for AI agents, to address the problem of tribal knowledge and experiential learning being lost across agent sessions. The solution uses Notion as a backing store with five interconnected databases (Projects, Topics, Memories, Entities, Facts)... — Tools: open_source,documentation | Techniques: memory,multi_agent_systems,agent_based,rag,semantic_search,evals

**Source:** https://www.notion.com/blog/building-shared-memory-for-ai-agents-in-notion

---

### 2. Building Production-Scale Voice and Multi-Modal Customer Experience Agents

**Company:** sierra

**Industry:** Tech

**Relevance score:** 132

**sierra / Tech** — Sierra has built an enterprise agent platform serving most of the Fortune 20 companies, focusing on customer experience across sales, service, and loyalty touchpoints. The platform addresses the challenge of building reliable, low-latency conversational agents that can handle complex customer interactions across voice and chat... — Tools: monitoring,api_gateway,microservices,cicd,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,postgresql,cache,langchain | Techniques: prompt_engineering,few_shot,semantic_search,vector_search,model_optimization,token_optimization,error_handling,multi_agent_systems,agent_based,harness_engineering,memory,latency_optimization,cost_optimization,fallback_strategies,system_prompts,mcp,a2a,evals,fine_tuning,reranking,rag,embeddings,reinforcement_learning

**Source:** https://www.youtube.com/watch?v=uCKhOmth2ms

---

## Tools & Infrastructure

### 1. Production AI and Trust in High-Stakes Government, Travel, and Healthcare Applications

**Company:** oracle_/_ca_dmv_/_tripadvisor

**Industry:** Government

**Relevance score:** 132

**oracle_/_ca_dmv_/_tripadvisor / Government** — This panel discussion brings together AI leaders from California DMV, Tripadvisor, and Oracle Health to explore the challenges of deploying LLM-based systems in production environments where failures have serious consequences. The panelists discuss how they ensure trust and reliability when deploying AI agents and GenAI... — Tools: monitoring,guardrails,langchain,crewai,postgresql,redis,chromadb,pinecone,wandb | Techniques: multi_agent_systems,agent_based,human_in_the_loop,memory,harness_engineering,prompt_engineering,embeddings

**Source:** https://www.youtube.com/watch?v=hXk-Ahocp04

---

### 2. Production LLM Systems: RAG Evaluation, Voice Agent Turn Detection, and Digital Persona Training

**Company:** various

**Industry:** Tech

**Relevance score:** 132

**various / Tech** — This case study presents three distinct production LLM implementations. Deep Verified built a self-hosted RAG platform for regulated fintech environments with comprehensive evaluation frameworks measuring answer accuracy, retrieval accuracy, latency, and observability over time. Alex AI developed a conversational voice agent for recruiting that solves... — Tools: langchain,postgresql,redis,chromadb,pinecone,qdrant,monitoring,databases,api_gateway,docker,kubernetes | Techniques: rag,embeddings,prompt_engineering,semantic_search,vector_search,agent_based,latency_optimization,evals,chunking

**Source:** https://www.youtube.com/watch?v=Wgud1JJNLfs

---
