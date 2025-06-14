---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<div class="cv-container">
[Download CV as PDF](/files/Ray_Chung_CV.pdf){: .btn .btn--primary}

# Ray-Yuan (Ray) Chung – Curriculum Vitae

## 📧 Contact
- **Email:** raychung@uw.edu  
- **Location:** Seattle, WA, USA  
- **Languages:** English, Mandarin Chinese  

---

## 🎓 Education

### Ph.D. in Biomedical and Health Informatics  
**University of Washington, Seattle, WA** — *2023–2027 (anticipated)*  
- Concentration: HCI and Data Science

### M.P.H. in Nutritional Sciences  
**University of Michigan, Ann Arbor, MI** — *2018–2020*

### B.S., Pre-Med  
**National Chung-Hsing University, Taichung, Taiwan** — *2013–2017*

---

## 🔬 Research Experience

### Human-AI Interaction Researcher  
**Unita Health, Remote** — *2024–Present*  
- Designed LLM-powered AI agent using RAG pipelines for gastrointestinal health  
- Improved interpretability and satisfaction via few-shot prompting and heuristic evaluations

### Graduate Researcher  
**University of Washington, Seattle, WA** — *2023–Present*  
- Developed LLM chatbot for older adults using OpenAI API  
- Classified health misinformation on YouTube using Llama  
- Evaluated usability of home spirometer for CF patients  
- Built BERT + ViT content filter for pro-eating disorder material

### User Experience Research Intern  
**Dexcom, San Diego, CA** — *2024*  
- Designed mixed-methods survey using TTM  
- Worked with PMs, engineers, and designers for product insights

### Research Scientist  
**Impossible Foods, Redwood City, CA** — *2022–2023*  
- Conducted data mining on ingredients and nutrients to optimize products

### AI Researcher  
**Heali AI, Remote** — *2021*  
- Curated datasets for personalized nutrition AI model training

### Graduate Researcher  
**University of Michigan, Ann Arbor, MI** — *2019–2020*  
- Managed RCT logistics on HIIT and weight change using REDCap

### UX Analyst - Team Lead  
**TaskUs/Valve Corporation, Taipei, Taiwan** — *2018*  
- Led analysis of Steam UX trends, improving satisfaction by 180%

---

## 🏆 Honors and Awards

- **2023:** Top Scholars Award, UW  
- **2018–2020:** Global Scholars Award, NSF International  
- **2019:** Maxine Moore Scholarship, University of Michigan SPH  

---

## 🛠 Skills

### Tools  
Python, SQL, R, PyTorch, TensorFlow, Tableau, RedCap

### AI / ML  
LLMs, Prompt Engineering, NLP, ML, Multimodal Analysis, Causal Inference

### UX / HCI  
Mixed-methods, Usability Testing, A/B Testing, Inclusive Design

### Behavioral Science  
Content Analysis, Intervention Design, Psychology

---

## 📜 Certifications and Affiliations

- Registered Dietitian (ID: 86289001)  
- Certified Sports Nutrition Specialist – Taiwan Society for Sports Nutrition  
- Member of The DUB Group at UW, AND, NSCA

</div>

<style>
.cv-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.cv-container h1 {
  margin-top: 30px;
  margin-bottom: 20px;
}

.cv-container h2 {
  margin-top: 25px;
  margin-bottom: 15px;
}

.cv-container h3 {
  margin-top: 20px;
  margin-bottom: 10px;
}

.cv-container ul {
  margin-bottom: 15px;
}

.cv-container hr {
  margin: 25px 0;
}
</style>

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
