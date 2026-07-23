# Weekly LLMOps Newsletter — 2026-07-23

A curated roundup of relevant LLMOps case studies, production patterns, tools, and use cases.

## This Week’s Angle

This edition highlights practical LLMOps patterns across production deployment, RAG, agents, automation, evaluation, and infrastructure.

## Research Highlights

### 1. Building Production-Grade Evaluation Systems for Customer Support AI Agents

**Company:** lyft

**Industry:** Tech

**Relevance score:** 137

**lyft / Tech** — Lyft's data science team developed a comprehensive evaluation framework for their customer support AI agent system over a two-year period, addressing the challenge of ensuring AI agents perform reliably before deployment to live users. The solution involves a multi-layered approach combining offline evaluations with synthetic... — Tools: langchain,crewai,monitoring,documentation | Techniques: multi_agent_systems,prompt_engineering,fine_tuning,few_shot,error_handling,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=3z2uT5aDx_Y

---

### 2. Autonomous Agent System for Scientific Machine Learning Model Optimization

**Company:** radicait

**Industry:** Healthcare

**Relevance score:** 127

**radicait / Healthcare** — Radicait developed an autonomous agent system to address the challenge of improving scientific machine learning models, specifically for generating synthetic PET scans from CT images for cancer detection. The core problem was that traditional coding agents would saturate after implementing initial optimizations, lacking the ability... — Tools: documentation | Techniques: prompt_engineering,multi_agent_systems,agent_based,model_optimization,harness_engineering

**Source:** https://www.youtube.com/watch?v=XLEYtv3cMlw

---

### 3. Data-Centric AI for Virtual Cell Modeling and Drug Discovery

**Company:** xaira

**Industry:** Healthcare

**Relevance score:** 127

**xaira / Healthcare** — Xaira Therapeutics developed X-Cell, a foundation model for predicting cellular responses to gene expression changes, to enable AI-driven drug discovery. The team encountered a fundamental scaling limitation where test loss flatlined at 1.5B parameters despite continued training loss improvements, indicating an information bottleneck in existing... — Tools: pytorch,open_source | Techniques: embeddings,model_optimization

**Source:** https://www.latent.space/p/xaira

---

### 4. Forward-Deployed AI Engineering in UK Government Justice System

**Company:** uk_ministry_of_justice

**Industry:** Government

**Relevance score:** 127

**uk_ministry_of_justice / Government** — The UK Ministry of Justice established the Justice AI Unit to address critical inefficiencies in the prison, probation, and court systems that were causing operational failures including erroneous prisoner releases. The unit adopted a forward-deployed engineering model where a lean team of approximately 40 engineers... — Tools: monitoring,databases,api_gateway,microservices,cicd,devops,documentation,security,compliance,guardrails,cache | Techniques: prompt_engineering,agent_based,human_in_the_loop,latency_optimization

**Source:** https://www.youtube.com/watch?v=qlHaO6laBlM

---

## Industry News

### 1. Building and Operating Claude Code with AI Agents at Scale

**Company:** anthropic

**Industry:** Tech

**Relevance score:** 142

**anthropic / Tech** — Anthropic's product and engineering teams describe their internal use of Claude Code and Claude Tag AI coding agents to build and ship production software at unprecedented speed. The teams leverage aggressive dogfooding, automated code review through AI classifiers, extensive evaluation suites, and security features like... — Tools: docker,monitoring,cicd,devops,documentation,security,guardrails,reliability,fastapi | Techniques: prompt_engineering,agent_based,multi_agent_systems,system_prompts,evals,human_in_the_loop,error_handling,token_optimization,memory

**Source:** https://www.youtube.com/watch?v=uU5Gv2h8-9g

---

### 2. AI-Powered Vulnerability Discovery and Patching at Scale

**Company:** anthropic

**Industry:** Tech

**Relevance score:** 137

**anthropic / Tech** — Anthropic developed an agentic harness system to help security teams discover, verify, and patch code vulnerabilities at scale using Claude. The system addresses the challenge that while frontier AI models have dramatically increased the number of vulnerabilities that can be found (Mozilla Firefox saw findings... — Tools: docker,postgresql,redis | Techniques: agent_based,prompt_engineering,harness_engineering,multi_agent_systems,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=imFedndyXYQ

---

### 3. Multi-Agent Orchestration for Enterprise Sales with Amazon Bedrock AgentCore

**Company:** aws

**Industry:** Tech

**Relevance score:** 132

**aws / Tech** — AWS Sales faced an agent proliferation challenge with over 20 domain-specific AI agents deployed globally, forcing sales representatives to manually navigate between systems and manage context across fragmented conversations. To address this, AWS built Field Advisor on Amazon Bedrock AgentCore, creating a unified conversational interface... — Tools: microservices,orchestration,monitoring,guardrails,langchain,fastapi,cache | Techniques: multi_agent_systems,agent_based,prompt_engineering,memory,human_in_the_loop,rag,semantic_search,embeddings,token_optimization,error_handling,latency_optimization

**Source:** https://aws.amazon.com/blogs/machine-learning/powering-agentic-ai-sales-strategy-with-amazon-bedrock-agentcore/

---

### 4. Multi-Model AI Architecture for Database Developer Assistant

**Company:** couchbase

**Industry:** Tech

**Relevance score:** 127

**couchbase / Tech** — Couchbase built Capella iQ, an AI-powered developer assistant that generates database queries, recommends indexes, and supports multi-turn conversational workflows. As enterprise adoption grew, they needed a scalable, multi-model inference architecture that could handle traffic bursts and maintain high availability across regions without pre-provisioned capacity. They... — Tools: kubernetes,api_gateway,microservices,scaling,serverless,monitoring,databases,documentation,reliability,scalability,security | Techniques: prompt_engineering,multi_agent_systems,model_optimization,few_shot,latency_optimization,cost_optimization,fallback_strategies,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/how-couchbase-built-a-multi-model-ai-architecture-for-capella-iq-with-amazon-bedrock/

---

### 5. Healthcare Agentic AI Transformation: From Pilot to Production Scale

**Company:** davita_/_elevance_health_/_hca_healthcare_/_independence_blue_cross

**Industry:** Healthcare

**Relevance score:** 127

**davita_/_elevance_health_/_hca_healthcare_/_independence_blue_cross / Healthcare** — This panel discussion at Google Cloud Next features leaders from HCA Healthcare, Independence Blue Cross, Davita, and Elevance Health discussing their journeys from pilot projects to production-scale deployment of AI agents across healthcare operations. The organizations address common challenges including pilot purgatory, fragmented use cases... — Tools: monitoring,databases,orchestration,documentation,security,compliance,guardrails,reliability,scalability | Techniques: multi_agent_systems,agent_based,rag,prompt_engineering,semantic_search,human_in_the_loop,cost_optimization,latency_optimization

**Source:** https://youtu.be/lm5mHq95Hbg

---

### 6. Multi-Agent Skills Matching Platform for Construction Workforce

**Company:** burns_&_mcdonnel

**Industry:** Consulting

**Relevance score:** 127

**burns_&_mcdonnel / Consulting** — Burns & McDonnell, a global architectural engineering and construction company, deployed a multi-agent system called "Experience IQ" to solve the challenge of matching employees with complex skill requirements across diverse projects and locations. Built using Google Cloud's Agent Development Kit (ADK) and deployed through Gemini... — Tools: kubernetes,docker,monitoring,databases,orchestration,open_source,documentation,security,compliance,guardrails,langchain,postgresql | Techniques: multi_agent_systems,agent_based,prompt_engineering,embeddings,semantic_search,memory,evals,few_shot,error_handling,fallback_strategies,human_in_the_loop

**Source:** https://youtu.be/Req2PndZ7HM

---

### 7. Production-Grade AI Agents for Financial Compliance Review Automation

**Company:** stripe

**Industry:** Finance

**Relevance score:** 127

**stripe / Finance** — Stripe, processing $1.4 trillion annually across 50 countries, faced a critical compliance scaling challenge where skilled analysts spent up to 80% of their time navigating fragmented systems rather than performing risk assessments. To address this, Stripe built a production-grade AI agent system on AWS using... — Tools: microservices,orchestration,monitoring,api_gateway,databases,cache | Techniques: agent_based,prompt_engineering,rag,token_optimization,human_in_the_loop,harness_engineering,few_shot

**Source:** https://aws.amazon.com/blogs/machine-learning/production-grade-ai-agents-for-financial-compliance-lessons-from-stripe/

---

### 8. Rethinking Insurance with AI: Operational Deployment Strategies for Brokers, Carriers, and Advisors

**Company:** deloitte

**Industry:** Insurance

**Relevance score:** 127

**deloitte / Insurance** — This panel discussion features insurance technology leaders from Baldwin Group, Ameriprise Financial (RiverSource), and Hudson Insurance discussing how they are deploying AI and LLM-based solutions into production workflows. The discussion covers the challenges of moving from AI experimentation to production adoption, including the need to... — Tools: api_gateway,guardrails,documentation,security,compliance | Techniques: prompt_engineering,embeddings,agent_based,human_in_the_loop,semantic_search

**Source:** https://www.youtube.com/watch?v=8THW-2PpwnY

---

### 9. AI-Powered Conversational Business Intelligence Assistant for Enterprise Leadership

**Company:** aws

**Industry:** Tech

**Relevance score:** 127

**aws / Tech** — AWS SMGS faced significant business intelligence challenges including time-intensive manual data preparation, fragmented data across multiple systems, and limited dashboard accessibility that delayed critical leadership decisions. To address these issues, they built NarrateAI, an AI-powered conversational assistant using Amazon Bedrock AgentCore that delivers on-demand business... — Tools: serverless,guardrails,monitoring,orchestration,databases,langchain | Techniques: rag,prompt_engineering,multi_agent_systems,agent_based,memory,evals

**Source:** https://aws.amazon.com/blogs/machine-learning/how-aws-smgs-uses-an-ai-powered-conversational-assistant-to-transform-business-management-with-amazon-bedrock-agentcore/

---

### 10. Purpose-Built AI Agent Hierarchies for GPU Infrastructure Reliability

**Company:** nvidia

**Industry:** Tech

**Relevance score:** 127

**nvidia / Tech** — NVIDIA's Applied AI Lab for DGX Cloud developed LLo11yPop, a hierarchical agent system for managing large-scale GPU infrastructure. The problem involved monitoring and optimizing hundreds of GPU clusters with complex failure modes, resource allocation constraints, and the need for proactive incident detection. The solution employed... — Tools: kubernetes,monitoring,guardrails,langchain,databases,elasticsearch,postgresql,open_source,documentation,reliability,scalability | Techniques: multi_agent_systems,agent_based,prompt_engineering,rag,evals,mcp,few_shot,error_handling,human_in_the_loop,latency_optimization,cost_optimization,system_prompts

**Source:** https://www.infoq.com/presentations/reliable-ai-platforms

---

### 11. Infrastructure Challenges in Production AI: Multi-Company Panel on Scaling, Cost, and Governance

**Company:** forge_/_cockroach_labs_/_doubleword_/_mesa

**Industry:** Tech

**Relevance score:** 127

**forge_/_cockroach_labs_/_doubleword_/_mesa / Tech** — This panel discussion from InfoQ Live brings together infrastructure experts from Forge, Cockroach Labs, Doubleword, and MESA to address the operational challenges of running AI systems at scale. The problem identified is that while building AI models has become relatively straightforward, maintaining production databases and... — Tools: kubernetes,databases,monitoring,scaling,devops,orchestration,postgresql,mysql,sqlite,redis,cache,elasticsearch,open_source,security,guardrails,reliability,scalability,documentation | Techniques: agent_based,multi_agent_systems,embeddings,vector_search,prompt_engineering,cost_optimization,latency_optimization,error_handling,fallback_strategies,evals

**Source:** https://www.infoq.com/presentations/ai-infrastructure-scaling-architecture/

---

### 12. Building a Production Data Agent for 90,000 Tables at Scale

**Company:** openai

**Industry:** Tech

**Relevance score:** 127

**openai / Tech** — OpenAI's data platform team built an internal data agent to help ~4,000 users navigate 1.5 exabytes of data across 90,000 datasets. The core challenge was not writing SQL queries but finding the right tables and understanding how to use them semantically, with analysts spending hours... — Tools: langchain,postgresql,redis,cache,pinecone,chromadb,qdrant,fastapi,spacy,monitoring,orchestration,databases,open_source,documentation | Techniques: embeddings,rag,semantic_search,vector_search,prompt_engineering,agent_based,memory,harness_engineering,chunking

**Source:** https://blog.bytebytego.com/p/how-openai-built-its-data-agent

---

### 13. Building Production AI Customer Support Agents with Multi-Agent Architecture and Human-in-the-Loop Design

**Company:** lorikeet

**Industry:** Tech

**Relevance score:** 127

**lorikeet / Tech** — Lorikeet is an AI customer support startup that evolved from building basic automation tools to creating sophisticated multi-agent systems for handling customer support at scale. The company developed two primary agents: a customer-facing concierge agent that handles support tickets across email, live chat, and voice... — Tools: langchain,monitoring,databases,api_gateway,guardrails,open_source | Techniques: multi_agent_systems,prompt_engineering,human_in_the_loop,agent_based,evals,system_prompts,error_handling,harness_engineering

**Source:** https://www.youtube.com/watch?v=eZj1xSiyd9U

---

### 14. Building an AI-Powered Slack Agent with MCP Standardization

**Company:** duolingo

**Industry:** Education

**Relevance score:** 127

**duolingo / Education** — Duolingo developed an AI-powered Slack bot to democratize access to their Model Context Protocol (MCP) infrastructure after discovering that manual MCP server setup was too complex for widespread adoption. The journey began with individual engineers connecting MCP servers to local editors in late 2024, evolved... — Tools: fastapi,docker,monitoring,security,guardrails,open_source,documentation,cicd,orchestration,postgresql | Techniques: mcp,prompt_engineering,human_in_the_loop,multi_agent_systems,agent_based,evals,system_prompts

**Source:** https://www.youtube.com/watch?v=5sb9iA2v78g

---

### 15. Cost-Efficient LLM Routing with Online Learning and Thompson Sampling

**Company:** ramp

**Industry:** Finance

**Relevance score:** 122

**ramp / Finance** — Ramp built an internal LLM gateway processing trillions of tokens daily to centralize AI usage across internal development and external products. To optimize costs while maintaining reliability, they developed a dynamic, failure-aware routing system using Thompson Sampling and exponentially-weighted moving averages (EWMA) to learn real-time... — Tools: redis | Techniques: cost_optimization,latency_optimization,error_handling,fallback_strategies

**Source:** https://builders.ramp.com/post/thompson-sampling-model-routing

---

## Cool Use Cases

### 1. Scaling AI-Powered Developer Support Through Agentic Systems

**Company:** coinbase

**Industry:** Finance

**Relevance score:** 147

**coinbase / Finance** — Coinbase's developer support engineering team transformed their support model from manual Discord responses to a comprehensive agentic AI system to scale support for their growing developer platform. The small team built multiple customer-facing and internal AI agents including Discord AI Chat, Slack Triage, and Support... — Tools: langchain,fastapi,databases,redis,chromadb,pinecone,qdrant,docker,kubernetes,monitoring,api_gateway,microservices,cicd,devops,orchestration,open_source,documentation,security,guardrails,scalability | Techniques: rag,prompt_engineering,agent_based,multi_agent_systems,human_in_the_loop,few_shot,evals,mcp,semantic_search,vector_search,error_handling,fallback_strategies

**Source:** https://www.youtube.com/watch?v=py9d6zTl4Dc

---

### 2. End-to-End Automation of Oncology Prior Authorization Workflows

**Company:** risa_labs

**Industry:** Healthcare

**Relevance score:** 142

**risa_labs / Healthcare** — Trisca, a healthcare automation company, developed a multi-agent LLM system to automate oncology prior authorization workflows for cancer drugs, eliminating human review for a significant portion of orders. The system uses four specialized agents (EV, Auth, Necessity, and Submission) to handle patient eligibility verification, authorization... — Tools: orchestration,databases | Techniques: multi_agent_systems,prompt_engineering,semantic_search,embeddings,human_in_the_loop,error_handling,agent_based

**Source:** https://www.youtube.com/watch?v=_cVfz88_j7A

---

### 3. Building Production-Scale Voice and Multi-Modal Customer Experience Agents

**Company:** sierra

**Industry:** Tech

**Relevance score:** 142

**sierra / Tech** — Sierra has built an enterprise agent platform serving most of the Fortune 20 companies, focusing on customer experience across sales, service, and loyalty touchpoints. The platform addresses the challenge of building reliable, low-latency conversational agents that can handle complex customer interactions across voice and chat... — Tools: monitoring,api_gateway,microservices,cicd,orchestration,continuous_deployment,continuous_integration,open_source,documentation,security,compliance,guardrails,reliability,scalability,fastapi,postgresql,cache,langchain | Techniques: prompt_engineering,few_shot,semantic_search,vector_search,model_optimization,token_optimization,error_handling,multi_agent_systems,agent_based,harness_engineering,memory,latency_optimization,cost_optimization,fallback_strategies,system_prompts,mcp,a2a,evals,fine_tuning,reranking,rag,embeddings,reinforcement_learning

**Source:** https://www.youtube.com/watch?v=uCKhOmth2ms

---

### 4. AI-Powered Customer Feedback Analysis System for Container Shipping

**Company:** hapag-lloyd

**Industry:** Other

**Relevance score:** 127

**hapag-lloyd / Other** — Hapag-Lloyd, a global container shipping company, transformed their manual and time-consuming customer feedback analysis process into an automated AI-powered system using Amazon Bedrock. Previously, product managers spent hours or days manually categorizing sentiment and themes from hundreds of feedback comments exported as CSV files. The... — Tools: langchain,elasticsearch,monitoring,serverless,orchestration,open_source,guardrails | Techniques: embeddings,rag,prompt_engineering,multi_agent_systems,agent_based,semantic_search

**Source:** https://aws.amazon.com/blogs/machine-learning/how-hapag-lloyd-uses-amazon-bedrock-to-transform-customer-feedback-into-actionable-insights/

---

## Tools & Infrastructure

### 1. Agentic Diagnostics Tool for Apache Spark Failure Troubleshooting

**Company:** pinterest

**Industry:** Tech

**Relevance score:** 147

**pinterest / Tech** — Pinterest built Medic for Apache Spark, an agentic diagnostics tool that automatically troubleshoots Spark job failures to address the unsustainable burden of manual support and complex distributed system debugging. The system evolved from a simple prototype using Model Context Protocol and a single ReAct agent... — Tools: langchain,llama_index,fastapi,monitoring,open_source,documentation,databases,orchestration | Techniques: prompt_engineering,multi_agent_systems,agent_based,rag,semantic_search,vector_search,token_optimization,error_handling,human_in_the_loop,evals

**Source:** https://www.youtube.com/watch?v=0RNNfxpdbQk

---

### 2. Production-Ready AI Agents for Automated User Story Generation in Financial Services

**Company:** ford

**Industry:** Automotive

**Relevance score:** 127

**ford / Automotive** — Ford Credit, the financial services arm of Ford Motor Company, deployed production-ready AI agents to automate the conversion of product requirements in Confluence into technical user stories. The problem addressed was the "blank page problem" where product managers had to manually translate high-level requirements into... — Tools: kubernetes,docker,monitoring,cicd,scaling,serverless,devops,orchestration,guardrails,security,compliance,reliability,scalability,fastapi,databases,api_gateway,microservices | Techniques: agent_based,multi_agent_systems,prompt_engineering,human_in_the_loop,memory,rag,embeddings,semantic_search,vector_search,cost_optimization,latency_optimization,error_handling,mcp,a2a,evals

**Source:** https://www.youtube.com/watch?v=Mq4ZY3eE5dI&list=PLFZU5nT4APFA&index=15

---
