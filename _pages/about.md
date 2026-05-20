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

My work combines human-centered design, mixed-methods user research, and AI/ML to study how intelligent systems can support human collaboration and decision-making in multi-stakeholder environments. I am especially motivated by work that measurably improves people’s lived experiences, or produces frameworks that help researchers and practitioners build more responsible, trustworthy AI. My research has appeared in high-impact venues such as *ACM CHI* conference, *AMIA* conference, and *Nutrients* journal.

I’m inspired by the late, great Kobe Bryant’s Mamba Mentality — his relentless commitment to inspiring those around him. If my work resonates with you, don’t hesitate to reach out. Outside of research, I enjoy traveling and playing sports, mainly basketball and golf.

<span style="color: #00274c;">Go Blue!</span> <span style="color: #32006e;">Go Dawgs!</span>

<div class="seeking-notice">
  <div class="seeking-notice-top">
    <span class="seeking-dot"></span>
    <span class="seeking-open-label">Open to Opportunities</span>
  </div>
  <p class="seeking-notice-text">Currently seeking internship opportunities in the following areas for Summer/Fall 2026 and beyond!</p>
  <div class="seeking-tags">
    <span class="seeking-tag">Generative AI</span>
    <span class="seeking-tag">Human-AI Collaboration</span>
    <span class="seeking-tag">Responsible AI</span>
    <span class="seeking-tag">Agentic Systems</span>
    <span class="seeking-tag">Health &amp; Social Technologies</span>
  </div>
</div>

<style>
.seeking-notice {
  border-left: 3px solid #7C3AED;
  background: #f5f3ff;
  padding: 12px 16px;
  margin: 20px 0 28px 0;
  border-radius: 0 6px 6px 0;
}

.seeking-notice-top {
  display: flex;
  align-items: center;
  gap: 7px;
  margin-bottom: 5px;
}

.seeking-dot {
  width: 7px;
  height: 7px;
  background: #7C3AED;
  border-radius: 50%;
  display: inline-block;
  flex-shrink: 0;
  animation: pulse-dot 2s ease-in-out infinite;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(0.75); }
}

.seeking-open-label {
  font-size: 0.7em;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: #6D28D9;
}

.seeking-notice-text {
  margin: 0 0 10px 0 !important;
  font-size: 0.92em;
  font-weight: 600;
  color: #1a202c;
  line-height: 1.4;
}

.seeking-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.seeking-tag {
  background: #ede9fe;
  color: #6D28D9;
  font-size: 0.74em;
  font-weight: 500;
  padding: 3px 10px;
  border-radius: 999px;
  border: 1px solid #c4b5fd;
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
  color: #2563EB;
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
  background: #EFF6FF;
  color: #1D4ED8;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.75em;
  font-weight: 500;
  border: 1px solid #BFDBFE;
}

.publication-meta {
  color: #555;
  font-size: 0.95em;
  line-height: 1.6;
}
</style>

For a complete list of publications, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=8Z-pAeQAAAAJ&hl=en).

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

