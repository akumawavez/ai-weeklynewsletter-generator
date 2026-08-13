# Weekly LLMOps Newsletter — 2026-08-13

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

### 2. LLM-Powered Product Relevance Labeling for E-commerce Search

**Company:** flipkart

**Industry:** E-commerce

**Relevance score:** 137

**flipkart / E-commerce** — Flipkart replaced a manual, human-driven product relevance labeling process with an LLM-based system called Product Analyser (PA) to address bottlenecks in their search quality evaluation pipeline. The manual process was slow, expensive, and produced inconsistent judgments across annotators, limiting their ability to generate the high-quality... — Techniques: fine_tuning,prompt_engineering,reinforcement_learning,instruction_tuning,knowledge_distillation

**Source:** https://blog.flipkart.tech/llms-for-relevance-automating-high-quality-product-relevance-labeling-in-flipkart-search-ddd5ca50b584

---

### 3. Open Source LLM Infrastructure for Production AI: Building Sovereign, Customizable Intelligence

**Company:** nvidia

**Industry:** Tech

**Relevance score:** 132

**nvidia / Tech** — This panel discussion features leaders from NVIDIA, Prime Intellect, and RCAI discussing the infrastructure and operational challenges of deploying open source large language models in production environments. The conversation addresses the problem of enterprises lacking control, transparency, and cost predictability when using closed API models... — Tools: open_source,vllm,pytorch,langchain | Techniques: fine_tuning,reinforcement_learning,rlhf,model_optimization,cost_optimization,latency_optimization,agent_based,multi_agent_systems,harness_engineering,evals

**Source:** https://www.youtube.com/watch?v=FWMJQDH3iK0

---

### 4. Training Specialized Legal AI Models with Synthetic Data and KV Cache Compaction

**Company:** harvey_/_baseten

**Industry:** Legal

**Relevance score:** 132

**harvey_/_baseten / Legal** — Harvey, a legal AI company, partnered with Baseten's training team to develop specialized models for legal tasks like due diligence data room analysis. The core challenge was that frontier models failed at exhaustive document review and struggled with context windows far smaller than typical legal... — Tools: open_source,documentation,guardrails,reliability,scalability,pytorch,langchain,llama_index,chromadb,pinecone,qdrant | Techniques: fine_tuning,prompt_engineering,agent_based,multi_agent_systems,reinforcement_learning,rlhf,model_optimization,semantic_search,vector_search,token_optimization,cost_optimization,latency_optimization,harness_engineering,memory,chunking,evals

**Source:** https://www.youtube.com/watch?v=TU8kwE7z1qY

---

## Industry News

### 1. AI-Powered Citizen Inquiry Automation with Ticketing System Integration

**Company:** city_of_munich

**Industry:** Government

**Relevance score:** 157

**city_of_munich / Government** — The City of Munich IT department developed an AI-powered system to automate citizen inquiries through their Zammad ticketing platform, initially targeting the driver's licensing authority which handles approximately 16,000 requests annually. The solution uses a RAG-based architecture combining LLM-driven ticket classification, automated response generation from... — Tools: kubernetes,docker,langchain,postgresql,fastapi,chromadb | Techniques: rag,prompt_engineering,embeddings,few_shot,semantic_search,vector_search,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=9Sfxy2nmUU0

---

### 2. Scaling Generative AI in Large Industrial Enterprise Through Platform Architecture

**Company:** omv

**Industry:** Energy

**Relevance score:** 147

**omv / Energy** — OMV, Austria's largest industrial company operating across chemicals, fuels, and plastics sectors, faced the challenge of scaling generative AI across highly heterogeneous business divisions with 140+ use case demands from business units. The company implemented a federated platform approach centered on a central AI platform... — Tools: langchain,llama_index,chromadb,pinecone,qdrant,fastapi,microservices,api_gateway,documentation,orchestration,open_source | Techniques: rag,embeddings,reranking,prompt_engineering,agent_based,multi_agent_systems

**Source:** https://www.youtube.com/watch?v=c8KP7I7x6f8

---

### 3. Deploying AI Agents in High-Risk Finance and Legal Operations

**Company:** circle_/_wells_fargo_/_mayfield

**Industry:** Finance

**Relevance score:** 147

**circle_/_wells_fargo_/_mayfield / Finance** — Circle and Wells Fargo discuss their approaches to deploying AI agents in high-stakes finance and legal environments where the cost of failure is substantial. The organizations emphasize the critical importance of verifiability, auditability, and rigorous evaluation frameworks when implementing agents for tasks like SOX compliance... — Tools: langchain,crewai,documentation,security,compliance,guardrails | Techniques: agent_based,multi_agent_systems,evals,human_in_the_loop,harness_engineering,a2a,reinforcement_learning

**Source:** https://www.youtube.com/watch?v=elptCI-FSCA

---

### 4. Risk Management and Production Deployment Practices for Generative AI Agents in Banking and Retail

**Company:** carrefour_/_lloyds_banking

**Industry:** Finance

**Relevance score:** 142

**carrefour_/_lloyds_banking / Finance** — This panel discussion brings together practitioners from Lloyds Banking, Yaya Finance, and Carrefour to discuss practical approaches to managing risk when deploying generative AI agents in production. The panelists share their experiences building customer-facing conversational AI systems, from low-risk internal documentation assistants to high-stakes financial... — Tools: langchain,monitoring,guardrails,documentation | Techniques: rag,prompt_engineering,agent_based,multi_agent_systems,error_handling,fallback_strategies,human_in_the_loop,evals,few_shot,system_prompts

**Source:** https://www.youtube.com/watch?v=SmC6-LS7EtY

---

### 5. Rapid Deployment of Agentic AI for Customer Experience Through Structured Onboarding

**Company:** accelerate

**Industry:** Consulting

**Relevance score:** 142

**accelerate / Consulting** — Accelerate, a Zoom CX and AI specialist deployment partner, and Zoom present their approach to deploying agentic AI systems in production environments within 30 days. They argue that AI initiatives often stall not due to model capability limitations but because of inadequate operational management, messy... — Tools: guardrails,monitoring,orchestration,documentation,security,compliance | Techniques: agent_based,prompt_engineering,human_in_the_loop,error_handling,fallback_strategies,system_prompts,evals

**Source:** https://www.youtube.com/watch?v=O-gQIsQI2Ac

---

### 6. Autonomous AI Agent for Development Workflow Automation

**Company:** nordic_corporate_bank

**Industry:** Finance

**Relevance score:** 142

**nordic_corporate_bank / Finance** — Nordic Corporate Bank, a small bank with only 26 employees, implemented an autonomous AI development agent named Nils Korg to handle their entire software development workflow. The agent, built using GitHub Copilot SDK and deployed on Azure, was integrated directly into Azure DevOps where product... — Tools: docker,kubernetes,postgresql,cicd,monitoring,fastapi,devops,orchestration,continuous_integration,continuous_deployment,microservices,serverless | Techniques: prompt_engineering,agent_based,multi_agent_systems,memory,harness_engineering,error_handling,fallback_strategies,system_prompts

**Source:** https://www.youtube.com/watch?v=p8M8--12h1Y

---

### 7. Agentic Engineering: Building Production Systems with Coding Agents

**Company:** oschlo

**Industry:** Tech

**Relevance score:** 142

**oschlo / Tech** — This case study explores the evolution of software development using AI coding agents over an 18-month period, from late 2024 through 2025 and into 2026. The speaker, a developer at Oschlo, transitioned from traditional software engineering to building production systems primarily using coding agents like... — Tools: docker,cicd,devops,open_source,security,guardrails,langchain | Techniques: prompt_engineering,multi_agent_systems,agent_based,harness_engineering,human_in_the_loop,latency_optimization,cost_optimization,evals,mcp

**Source:** https://www.youtube.com/watch?v=Tj6Df_K-IRc

---

### 8. Building Production AI Chatbot for Compliance Intelligence in Life Sciences

**Company:** qualio

**Industry:** Healthcare

**Relevance score:** 142

**qualio / Healthcare** — Qualio, a compliance-as-code platform for life sciences companies, developed an AI-powered chatbot to help customers remediate compliance gaps in their quality management documentation. The team evolved their architecture from an over-engineered multi-agent system with 20+ specialized tools to a simplified single-agent approach using API abstraction... — Tools: fastapi,postgresql,open_source,documentation | Techniques: prompt_engineering,agent_based,system_prompts,human_in_the_loop,harness_engineering,evals

**Source:** https://www.youtube.com/watch?v=MTyO3W7MYTs

---

### 9. AI-Powered Analytics Platform with Contextual Governance and Agent-Driven Workflows

**Company:** hex

**Industry:** Tech

**Relevance score:** 137

**hex / Tech** — Hex addresses the challenge of data teams struggling to meet infinite demand for insights while managing fragmented tooling across BI tools, notebooks, SQL editors, and spreadsheets. Their solution provides a unified analytics platform that combines deep technical workflows (SQL, Python notebooks) with AI agent capabilities... — Tools: postgresql,mysql,sqlite,databases,monitoring,guardrails,documentation,compliance | Techniques: agent_based,prompt_engineering,semantic_search,evals

**Source:** https://www.youtube.com/watch?v=zlwqx05qNSk

---

### 10. Converged Database Architecture for RAG and AI Agent Workloads

**Company:** oracle

**Industry:** Tech

**Relevance score:** 137

**oracle / Tech** — Oracle presents a converged database architecture designed to address the challenges of deploying RAG (Retrieval-Augmented Generation) systems and AI agents in production environments. The problem centers on the limitations of multi-store architectures where vector indexes, operational databases, and search systems exist as separate services connected... — Tools: docker,databases,postgresql,open_source,documentation,cicd,continuous_integration,onnx,pinecone,redis,cache,elasticsearch | Techniques: rag,embeddings,vector_search,semantic_search,agent_based

**Source:** https://blogs.oracle.com/developers/what-is-a-converged-database-definition-five-tests-and-ai-use-cases?utm_source=substack&utm_medium=email

---

### 11. Building a Production AI Agent for Project Management Software

**Company:** linear

**Industry:** Tech

**Relevance score:** 132

**linear / Tech** — Linear, a project management software company, built Linear Agent, an AI assistant designed to help users manage their workflows through natural language interactions. The challenge was to create an agent flexible enough to handle unanticipated user requests while maintaining predictability and safety in a production... — Tools: fastapi,cache | Techniques: prompt_engineering,agent_based,multi_agent_systems,human_in_the_loop,system_prompts,token_optimization

**Source:** https://linear.app/now/how-we-built-linear-agent

---

### 12. Building and Scaling an AI-Powered Virtual Banking Assistant

**Company:** virgin_money

**Industry:** Finance

**Relevance score:** 132

**virgin_money / Finance** — Virgin Money developed Ready, an AI-powered virtual assistant for conversational banking, starting with a credit card service problem in 2023. The team began with basic FAQ bot functionality and gradually evolved through 2024 and 2025, adding API connectivity, proactive messaging, and contextual capabilities. Despite two... — Tools: fastapi,monitoring | Techniques: prompt_engineering,few_shot,error_handling,human_in_the_loop,latency_optimization

**Source:** https://www.youtube.com/watch?v=WuhytMprzcc

---

### 13. Deep Research News Analysis Platform with Synthetic Data and Vector Search

**Company:** asknews

**Industry:** Media & Entertainment

**Relevance score:** 132

**asknews / Media & Entertainment** — AskNews built a production deep research system for news analysis that addresses the limitations of raw web scraping approaches used by competitors. The company processes 500,000 documents per day, converting raw news articles into grounded synthetic data that preserves context while removing journalistic narrative voice... — Tools: qdrant,kubernetes,docker,scaling,databases,open_source,documentation,monitoring,microservices,orchestration,elasticsearch,spacy | Techniques: rag,embeddings,semantic_search,vector_search,prompt_engineering,agent_based,multi_agent_systems,few_shot,reranking,token_optimization,error_handling,cost_optimization

**Source:** https://www.youtube.com/watch?v=mhsXLO5ZN8I

---

### 14. Scaling Vector Search Infrastructure with Kubernetes Operators

**Company:** hubspot

**Industry:** Tech

**Relevance score:** 132

**hubspot / Tech** — HubSpot built a centralized vector storage and search platform called VAST (Vector as a Service) on top of Qdrant to serve 38+ teams across the organization, managing 20 billion+ vectors across 150 clusters. The platform initially used Helm for deployments but faced significant operational challenges... — Tools: kubernetes,qdrant,monitoring,orchestration,scaling,devops,open_source,reliability,scalability | Techniques: embeddings,vector_search,semantic_search,model_optimization,cost_optimization

**Source:** https://www.youtube.com/watch?v=46aQff4pxRE

---

### 15. Scaling Synopsis Quality Evaluation with LLM-as-a-Judge

**Company:** netflix

**Industry:** Media & Entertainment

**Relevance score:** 132

**netflix / Media & Entertainment** — Netflix faced the challenge of evaluating hundreds of thousands of show synopses at scale to ensure members consistently receive high-quality content descriptions that help them choose what to watch. Manual evaluation by creative experts wasn't scalable given the volume and multiple variants per show. The... — Techniques: prompt_engineering,few_shot,agent_based,multi_agent_systems,human_in_the_loop

**Source:** https://netflixtechblog.com/evaluating-netflix-show-synopses-with-llm-as-a-judge-6269251e6f28

---

### 16. Containment Architectures for AI Agents Across Product Lines

**Company:** anthropic

**Industry:** Tech

**Relevance score:** 132

**anthropic / Tech** — Anthropic describes their engineering approach to containing AI agents across three products (claude.ai, Claude Code, and Claude Cowork) as agent capabilities and access expand. The problem centers on managing the blast radius of increasingly capable autonomous agents that can now access sensitive systems and data... — Tools: docker,kubernetes,security,guardrails,monitoring,open_source | Techniques: agent_based,multi_agent_systems,prompt_engineering,system_prompts,human_in_the_loop,mcp,error_handling,evals

**Source:** https://www.anthropic.com/engineering/how-we-contain-claude

---

## Cool Use Cases

### 1. Evolution of AI-Powered Digital Assistant for Telecommunications Customer Service

**Company:** bt

**Industry:** Telecommunications

**Relevance score:** 137

**bt / Telecommunications** — BT Group's consumer division developed Amy, an AI-powered digital assistant designed to handle customer service across broadband, mobile, and TV products. Starting from a basic routing chatbot in 2021, the team evolved the system through multiple generations, partnering with Sprinklr in 2024 after ChatGPT's launch... — Tools: guardrails | Techniques: rag,prompt_engineering,semantic_search,multi_agent_systems,agent_based,error_handling,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=4orLY_8QLAg

---

### 2. Building an Agentic Financial Guidance Chatbot from Deterministic Foundations

**Company:** lloyds_banking

**Industry:** Finance

**Relevance score:** 132

**lloyds_banking / Finance** — Lloyds Banking Group's Conversational Banking Lab developed a fully agentic financial guidance chatbot to help beginner investors understand investment concepts, representing a major shift from their mature deterministic Watson Assistant chatbot that had been in production since 2015. The team encountered significant challenges transitioning from... — Tools: guardrails,monitoring | Techniques: prompt_engineering,rag,agent_based,few_shot,error_handling,human_in_the_loop

**Source:** https://www.youtube.com/watch?v=mO-4TDElwwg

---

### 3. Building Production-Scale Voice and Multi-Modal Customer Experience Agents

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
