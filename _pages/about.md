---
permalink: /
title: "About Me"
seo_title: "Ray Chung - Research Portfolio | Ray-Yuan Chung"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a human-centered AI PhD student at the University of Washington, advised by <a href="https://bime.uw.edu/faculty/ari-pollack/" target="_blank">Ari Pollack</a>, <a href="https://ischool.uw.edu/people/faculty/profile/wpratt" target="_blank">Wanda Pratt</a> and <a href="https://orsonxu.com/" target="_blank">Orson "Xuhai" Xu</a>. My research sits at the intersection of artificial intelligence (AI), human–computer interaction (HCI), and health informatics. Prior to pursuing my terminal degree, I worked as a dietitian and research scientist in multiple health organizations and tech startups.

My work combines human-centered design, mixed-methods user research, and AI/ML techniques to investigate how intelligent systems can enhance human collaboration and decision-making in high-stakes, multi-stakeholder environments. I am especially motivated by research that produces measurable improvements in people’s lived experiences or generates frameworks and design implications that researchers and practitioners can adopt to build more responsible and trustworthy AI systems for social good. My research has been published in and submitted to high-impact venues such as <i>ACM CHI</i> conference, <i>AMIA</i> conference, and <i>Nutrients</i> journal.

<!--
Before beginning my doctoral studies, I earned my master’s degree from the University of Michigan and worked as a registered dietitian and research scientist across collegiate athletic teams, mental health clinics, research institutions, and health technology companies including <i>Impossible Foods</i> and <i>Dexcom</i>. Through my clinical work, I witnessed firsthand how profoundly technology can influence human health—for better or worse. Much like the Chinese proverb “Water can carry a boat, but it can also overturn it” (「水能載舟，亦能覆舟」), I’ve come to believe that technology, when thoughtfully designed, can support and uplift people’s health; when misapplied, it can just as easily create harm or inequity. This belief drives my commitment to advancing more human-centered AI technologies.
-->

I'm inspired by the late Kobe Bryant and his Mamba Mentality—to inspire people around me. If my work resonates with you, don't hesitate to reach out! I'm always happy to connect. Outside of work, I enjoy traveling and playing sports—mainly basketball and golf.

<span style="color: #00274c;">Go Blue!</span> <span style="color: #32006e;">Go Dawgs!</span>

<div class="announcement-box">
  <div class="announcement-content">
    <div class="announcement-icon">💼</div>
    <div class="announcement-text">
      <h2 class="announcement-title">Currently seeking internship opportunities for Summer/Fall 2026 and beyond!</h2>
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

{% include base_path %}
{% assign first_author_papers = site.publications | where: "author_position", "first" %}
{% assign second_author_papers = site.publications | where: "author_position", "second" %}
{% assign selected_papers = first_author_papers | concat: second_author_papers | sort: "date" | reverse %}
{% for paper in selected_papers limit:3 %}
  {% if paper.paperurl %}
    {% assign paper_link = paper.paperurl %}
  {% else %}
    {% assign paper_link = 'https://scholar.google.com/scholar?q=' | append: paper.title | uri_escape %}
  {% endif %}
<div class="selected-publication-item">
  <div class="publication-title-row">
    <strong>{{ forloop.index }}.</strong> <a href="{{ paper_link }}">{{ paper.title }}</a>
  </div>
  {% if paper.tags %}
  <div class="publication-tags">
    {% for tag in paper.tags %}
      <span class="publication-tag">{{ tag }}</span>
    {% endfor %}
  </div>
  {% endif %}
  <div class="publication-meta">
    {{ paper.authors | replace: 'Ray-yuan Chung', '<b>Ray-yuan Chung</b>' | replace: 'Ray-Yuan Chung', '<b>Ray-Yuan Chung</b>' | replace: 'R Chung', '<b>R Chung</b>' | replace: 'Ray Chung', '<b>Ray Chung</b>' }} ({{ paper.date | date: "%Y" }}). <em>{{ paper.venue }}</em>. {% if paper.citation %}{{ paper.citation }}{% endif %}
  </div>
</div>
{% endfor %}

<style>
.selected-publication-item {
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid #e0e0e0;
}

.selected-publication-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.publication-title-row {
  margin-bottom: 8px;
  line-height: 1.4;
}

.publication-title-row {
  margin-bottom: 8px;
  line-height: 1.4;
}

.publication-title-row a {
  color: #4682b4;
  text-decoration: none;
  font-weight: 500;
}

.publication-title-row a:hover {
  text-decoration: underline;
}

.publication-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin: 8px 0 10px 0;
}

.publication-tag {
  display: inline-block;
  background: linear-gradient(135deg, #4682b4 0%, #5a9bd4 100%);
  color: #fff;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.75em;
  font-weight: 500;
  letter-spacing: 0.02em;
  box-shadow: 0 2px 4px rgba(70, 130, 180, 0.2);
}

.publication-meta {
  color: #555;
  font-size: 0.95em;
  line-height: 1.6;
}
</style>

For a complete list of publications, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=8Z-pAeQAAAAJ&hl=en).

## 👥 Main Collaborators

{% include collaborators.html %}

## 📸 Photo Gallery

<div class="marquee-container">
  <div class="marquee-track">
    <img src="/assets/images/photo1.jpg" alt="Research photo 1" class="marquee-item">
    <img src="/assets/images/photo2.jpg" alt="Research photo 2" class="marquee-item">
    <img src="/assets/images/photo3.jpg" alt="Research photo 3" class="marquee-item">
    <img src="/assets/images/photo4.jpg" alt="Research photo 4" class="marquee-item">
    <img src="/assets/images/photo5.jpg" alt="Research photo 5" class="marquee-item">
    <img src="/assets/images/photo1.jpg" alt="Research photo 1" class="marquee-item">
    <img src="/assets/images/photo2.jpg" alt="Research photo 2" class="marquee-item">
    <img src="/assets/images/photo3.jpg" alt="Research photo 3" class="marquee-item">
    <img src="/assets/images/photo4.jpg" alt="Research photo 4" class="marquee-item">
    <img src="/assets/images/photo5.jpg" alt="Research photo 5" class="marquee-item">
  </div>
</div>

