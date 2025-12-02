---
permalink: /
title: "About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a Ph.D. candidate at the University of Washington, where my research sits at the intersection of artificial intelligence (AI), human–computer interaction (HCI), and consumer health informatics. With a background in behavioral science and dietetics, I bring a multidisciplinary perspective that bridges technology and human well-being. 

Broadly, I study how people collaborate with AI systems in high-stakes, multi-stakeholder environments. My work combines human-centered design, mixed-methods user research, and AI/ML techniques to investigate how intelligent systems can enhance human communication and decision-making. I'm currently working on building trustworthy AI systems to support collaborative decision-making in high-stakes, multi-stakeholder environments. My research has been published in and submitted to high-impact venues such as <i>Nutrients</i> journal and the <i>ACM CHI</i> conference.

<!--
Before beginning my doctoral studies, I earned my master’s degree from the University of Michigan and worked as a registered dietitian and research scientist across collegiate athletic teams, mental health clinics, research institutions, and health technology companies including <i>Impossible Foods</i> and <i>Dexcom</i>. Through my clinical work, I witnessed firsthand how profoundly technology can influence human health—for better or worse. Much like the Chinese proverb “Water can carry a boat, but it can also overturn it” (「水能載舟，亦能覆舟」), I’ve come to believe that technology, when thoughtfully designed, can support and uplift people’s health; when misapplied, it can just as easily create harm or inequity. This belief drives my commitment to advancing more human-centered AI technologies.
-->

I'm inspired by the late Kobe Bryant and his Mamba Mentality—to become a better version of myself every day and to inspire people around me. If my work resonates with you, don't hesitate to reach out! I'm always happy to connect. Outside of work, I enjoy traveling and playing sports - mainly basketball and golf.

<span style="color: #00274c;">Go Blue!</span> <span style="color: #32006e;">Go Dawgs!</span>

<div class="announcement-box">
  <div class="announcement-content">
    <div class="announcement-icon">💼</div>
    <div class="announcement-text">
      <h2 class="announcement-title">Currently seeking internship opportunities for Spring/Summer 2026!</h2>
      <p class="announcement-description">Interested in <strong>Generative AI</strong>, <strong>Human-AI Collaboration</strong>, <strong>Responsible AI</strong>, <strong>Agentic Systems</strong>, <strong>Health and Social Technologies</strong>.</p>
    </div>
  </div>
</div>

<style>
.announcement-box {
  background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
  border-left: 4px solid #4682b4;
  border-radius: 8px;
  padding: 24px;
  margin: 30px 0;
  box-shadow: 0 4px 12px rgba(70, 130, 180, 0.15);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.announcement-box:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(70, 130, 180, 0.2);
}

.announcement-content {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.announcement-icon {
  font-size: 2em;
  line-height: 1;
  flex-shrink: 0;
  margin-top: 4px;
}

.announcement-text {
  flex: 1;
}

.announcement-title {
  margin: 0 0 12px 0 !important;
  color: #2c5f8d !important;
  font-size: 1.4em !important;
  font-weight: 600 !important;
  line-height: 1.3;
}

.announcement-description {
  margin: 0;
  color: #4a5568;
  font-size: 1em;
  line-height: 1.6;
}

.announcement-description strong {
  color: #4682b4;
  font-weight: 600;
}

@media (max-width: 600px) {
  .announcement-box {
    padding: 18px;
  }
  
  .announcement-content {
    flex-direction: column;
    gap: 12px;
  }
  
  .announcement-icon {
    font-size: 1.5em;
    margin-top: 0;
  }
  
  .announcement-title {
    font-size: 1.2em !important;
  }
}
</style>

## 📚 Selected Publications

{% assign first_author_papers = site.publications | where: "author_position", "first" %}
{% assign second_author_papers = site.publications | where: "author_position", "second" %}
{% assign selected_papers = first_author_papers | concat: second_author_papers | sort: "date" | reverse %}
{% for paper in selected_papers limit:3 %}
{{ forloop.index }}. {{ paper.authors | replace: 'Ray-yuan Chung', '<b>Ray-yuan Chung</b>' | replace: 'Ray-Yuan Chung', '<b>Ray-Yuan Chung</b>' | replace: 'R Chung', '<b>R Chung</b>' | replace: 'Ray Chung', '<b>Ray Chung</b>' }} ({{ paper.date | date: "%Y" }}). [{{ paper.title }}]({{ paper.paperurl }}). *{{ paper.venue }}*. {% if paper.citation %}{{ paper.citation }}{% endif %}
{% endfor %}

For a complete list of publications, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=8Z-pAeQAAAAJ&hl=en).

## 👥 Main Collaborators

{% include collaborators.html %}

## 📸 Photo Gallery

<div class="photo-gallery">
  <img src="/images/photo1.jpg" alt="Description of photo 1">
  <img src="/images/photo2.jpg" alt="Description of photo 2">
  <img src="/images/photo3.jpg" alt="Description of photo 3">
  <img src="/images/photo4.jpg" alt="Description of photo 4">
</div>

<style>
.photo-gallery {
  display: flex;
  gap: 16px;
  justify-content: flex-start;
  align-items: center;
  margin: 20px 0;
  overflow-x: auto;
  padding: 10px 0;
}
.photo-gallery img {
  width: 240px;
  height: 360px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  background: #f8f8f8;
  flex-shrink: 0;
}
@media (max-width: 768px) {
  .photo-gallery {
    gap: 12px;
  }
  .photo-gallery img {
    width: 200px;
    height: 150px;
  }
}
@media (max-width: 600px) {
  .photo-gallery {
    gap: 8px;
  }
  .photo-gallery img {
    width: 160px;
    height: 120px;
  }
}
</style>

