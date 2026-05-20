---
permalink: /
title: "About Me"
seo_title: "Ray Chung - Research Portfolio | Ray-Yuan Chung"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a PhD student studying human-centered AI at the University of Washington, advised by [Ari Pollack](https://bime.uw.edu/faculty/ari-pollack/), [Wanda Pratt](https://ischool.uw.edu/people/faculty/profile/wpratt), and [Orson “Xuhai” Xu](https://orsonxu.com/). My research sits at the intersection of artificial intelligence (AI), human–computer interaction (HCI), and health informatics. Before my doctoral studies, I worked as a dietitian and research scientist across health organizations and tech startups like Impossible Foods, Unita Health, and Dexcom.

My work combines human-centered design, mixed-methods user research, and AI/ML to study how intelligent systems can support human collaboration and decision-making in multi-stakeholder environments. I am especially motivated by work that measurably improves people’s lived experiences, or produces frameworks that help researchers and practitioners build more responsible, trustworthy AI. My research has appeared in high-impact venues such as ACM CHI conference, AMIA conference, and Nutrients journal.

I’m inspired by the late, great Kobe Bryant’s Mamba Mentality — his relentless commitment to inspiring those around him. If my work resonates with you, don’t hesitate to reach out. Outside of research, I enjoy traveling and playing sports, mainly basketball and golf.

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

