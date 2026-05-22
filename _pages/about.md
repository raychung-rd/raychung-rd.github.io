---
permalink: /
title: "About Me"
seo_title: 'Ray-Yuan "Ray" Chung'
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a PhD student studying human-centered AI at the University of Washington, advised by [Ari Pollack](https://bime.uw.edu/faculty/ari-pollack/), [Wanda Pratt](https://ischool.uw.edu/people/faculty/profile/wpratt), and [Xuhai “Orson” Xu](https://orsonxu.com/). My research sits at the intersection of artificial intelligence (AI), human–computer interaction (HCI), and health informatics. Before my doctoral studies, I completed my master's degree at the University of Michigan and then worked as a dietitian and research scientist across health organizations and tech startups such as Impossible Foods, Unita Health, and Dexcom.

<style>
.page__content > p:first-of-type a {
  color: inherit !important;
  text-decoration: underline;
}

body:has(.seeking-notice) .page__content {
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
}
</style>

My work combines human-centered design, mixed-methods user research, and AI/ML to study how intelligent systems can support human collaboration and decision-making in multi-stakeholder environments. I am especially motivated by work that measurably improves people’s lived experiences, or produces frameworks that help researchers and practitioners build more responsible, trustworthy AI. My research has appeared in high-impact venues such as *ACM CHI* conference, *AMIA* conference, and *Nutrients* journal.

I’m inspired by the late, great Kobe Bryant’s Mamba Mentality — his relentless commitment to inspiring those around him. If my work resonates with you, I’d love to connect and chat. Outside of research, I enjoy traveling and playing sports, mainly basketball and golf.

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
  border-left: 3px solid #2563EB;
  background: #EFF6FF;
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
  background: #2563EB;
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
  color: #1D4ED8;
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
  background: #EFF6FF;
  color: #2563EB;
  font-size: 0.74em;
  font-weight: 500;
  padding: 3px 10px;
  border-radius: 999px;
  border: 1px solid #BFDBFE;
}
</style>

## 🔭 Current Work

{% assign tag_order = "Generative AI,Human-AI Collaboration,Responsible AI,Agentic Systems,Health Informatics,User Experience Research" | split: "," %}
{% assign projects = site.projects | sort: "date" | reverse %}
{% for project in projects %}{% if project.hidden %}{% continue %}{% endif %}
  {% assign asset_name = project.nickname | default: project.name | remove: '.md' %}
<div class="selected-publication-item">
  <div class="sel-pub-thumb-wrap">
    <a href="/assets/projects/{{ asset_name }}.png" class="pub-img-popup" data-title="{{ project.title }}">
      <img src="/assets/projects/{{ asset_name }}.png"
           alt="{{ project.title }}"
           class="sel-pub-thumb"
           onerror="this.src='/assets/publications/placeholder.png'">
    </a>
  </div>
  <div class="sel-pub-body">
    <div class="publication-title-row">
      <strong>{{ project.title }}</strong>
    </div>
    {% if project.tags %}
    <div class="publication-tags">
      {% for ordered_tag in tag_order %}
        {% if project.tags contains ordered_tag %}
          <span class="publication-tag">{{ ordered_tag }}</span>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}
    <div class="project-description">{{ project.description }}</div>
  </div>
</div>
{% endfor %}

<style>
.project-status-badge {
  display: inline-block;
  font-size: 0.68em;
  font-weight: 600;
  color: #059669;
  background: #ECFDF5;
  border: 1px solid #A7F3D0;
  border-radius: 999px;
  padding: 1px 8px;
  margin-left: 8px;
  vertical-align: middle;
  letter-spacing: 0.03em;
}
.project-description {
  color: #555;
  font-size: 0.88em;
  line-height: 1.6;
  margin-top: 6px;
}
</style>

## 📚 Selected Publications

{% include base_path %}
{% assign all_pubs = site.publications | sort: "date" | reverse %}
{% assign filtered_pubs = "" | split: "" %}
{% for pub in all_pubs %}
  {% unless pub.hidden %}
    {% if pub.tags contains "Human-AI Collaboration" or pub.tags contains "Responsible AI" or pub.tags contains "Generative AI" %}
      {% assign filtered_pubs = filtered_pubs | push: pub %}
    {% endif %}
  {% endunless %}
{% endfor %}
{% assign tag_order = "Generative AI,Human-AI Collaboration,Responsible AI,Health Informatics,User Experience Research" | split: "," %}
{% for paper in filtered_pubs limit:5 %}
  {% assign pub_slug = paper.permalink | remove: '/publication/' | default: paper.name | remove: '.md' %}
  {% assign asset_name = paper.nickname | default: pub_slug %}
<div class="selected-publication-item">
  <div class="sel-pub-thumb-wrap">
    <a href="/assets/publications/{{ asset_name }}.png" class="pub-img-popup" data-title="{{ paper.title }}">
      <img src="/assets/publications/{{ asset_name }}.png"
           alt="{{ paper.title }}"
           class="sel-pub-thumb"
           onerror="this.src='/assets/publications/placeholder.png'">
    </a>
  </div>
  <div class="sel-pub-body">
    <div class="publication-title-row">
      <strong>{{ forloop.index }}.</strong>
      {% if paper.paperurl %}<a href="{{ paper.paperurl }}">{{ paper.title }}</a>{% else %}{{ paper.title }}{% endif %}
    </div>
    {% if paper.tags %}
    <div class="publication-tags">
      {% for ordered_tag in tag_order %}
        {% if paper.tags contains ordered_tag %}
          <span class="publication-tag">{{ ordered_tag }}</span>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}
    <div class="publication-meta">
      {{ paper.authors | replace: 'Ray-yuan Chung', '<b>Ray-yuan Chung</b>' | replace: 'Ray-Yuan Chung', '<b>Ray-Yuan Chung</b>' | replace: 'R Chung', '<b>R Chung</b>' | replace: 'Ray Chung', '<b>Ray Chung</b>' }}. <em>{{ paper.venue }}</em> ({{ paper.date | date: "%Y" }}).
    </div>
    <div class="pub-links">
      {% if paper.pdf %}
        <a href="/assets/publications/{{ asset_name }}.pdf" class="pub-link-chip" target="_blank" rel="noopener noreferrer">[paper]</a>
      {% endif %}
      {% if paper.paperurl %}
        {% if paper.paperurl contains 'arxiv.org' %}
          <a href="{{ paper.paperurl }}" class="pub-link-chip" target="_blank" rel="noopener noreferrer">[arxiv]</a>
        {% else %}
          <a href="{{ paper.paperurl }}" class="pub-link-chip" target="_blank" rel="noopener noreferrer">[doi]</a>
        {% endif %}
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}

<div id="pub-img-modal">
  <div class="modal-inner">
    <button class="modal-close" aria-label="Close">&#x2715;</button>
    <img src="" alt="">
  </div>
</div>

<style>
.selected-publication-item {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid #e0e0e0;
}

.selected-publication-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.sel-pub-thumb-wrap {
  flex-shrink: 0;
  width: 100px;
}

.sel-pub-thumb {
  width: 100px;
  height: 65px;
  object-fit: contain;
  border-radius: 5px;
  border: 1px solid #e2e8f0;
  background: #ffffff;
  display: block;
  cursor: zoom-in;
  transition: opacity 0.15s ease;
}

.sel-pub-thumb:hover {
  opacity: 0.85;
}

.sel-pub-body {
  flex: 1;
  min-width: 0;
}

.publication-title-row {
  margin-bottom: 6px;
  line-height: 1.4;
}

.publication-title-row a {
  color: #1E293B;
  text-decoration: none;
  font-weight: 700;
}

.publication-title-row a:hover {
  color: #2563EB;
  text-decoration: underline;
}

#pub-img-modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.75);
  z-index: 9999;
  align-items: center;
  justify-content: center;
}

#pub-img-modal.active {
  display: flex;
}

#pub-img-modal .modal-inner {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
}

#pub-img-modal img {
  display: block;
  max-width: 90vw;
  max-height: 85vh;
  border-radius: 6px;
  background: #fff;
}

#pub-img-modal .modal-close {
  position: absolute;
  top: -14px;
  right: -14px;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #fff;
  border: 1px solid #e2e8f0;
  color: #334155;
  font-size: 1em;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 1px 4px rgba(0,0,0,0.15);
}

#pub-img-modal .modal-close:hover {
  background: #f1f5f9;
}

.publication-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin: 6px 0 8px 0;
}

.publication-tag {
  display: inline-block;
  background: transparent;
  color: #64748B;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.72em;
  font-weight: 500;
  border: 1px solid #CBD5E1;
}

.publication-meta {
  color: #555;
  font-size: 0.88em;
  line-height: 1.6;
  margin-bottom: 6px;
}

.pub-links {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.pub-link-chip {
  display: inline-flex;
  align-items: center;
  padding: 3px 10px;
  border-radius: 4px;
  font-size: 0.76em;
  font-weight: 500;
  color: #2563EB;
  background: #EFF6FF;
  border: 1px solid #BFDBFE;
  text-decoration: none !important;
  transition: all 0.15s;
  font-family: inherit;
  line-height: 1.5;
}

.pub-link-chip:hover {
  background: #2563EB;
  color: #fff !important;
  border-color: #2563EB;
}
</style>

<script>
(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('pub-img-modal');
    if (!modal) return;
    var modalImg = modal.querySelector('img');
    var closeBtn = modal.querySelector('.modal-close');

    // Open advisor links in new tab
    document.querySelectorAll('.page__content > p:first-of-type a').forEach(function(a) {
      a.setAttribute('target', '_blank');
      a.setAttribute('rel', 'noopener noreferrer');
    });

    document.querySelectorAll('.pub-img-popup').forEach(function(link) {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        modalImg.src = this.getAttribute('href');
        modalImg.alt = this.getAttribute('data-title') || '';
        modal.classList.add('active');
      });
    });

    function closeModal() {
      modal.classList.remove('active');
      modalImg.src = '';
    }

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
      if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeModal();
    });
  });
})();
</script>

For a complete list of publications, please visit my [Publications page](/publications/) or [Google Scholar profile](https://scholar.google.com/citations?user=8Z-pAeQAAAAJ&hl=en).

## 📸 Photo Gallery

<div class="marquee-container">
  <div class="marquee-track">
    <img src="/assets/images/photo1.jpg" alt="Research photo 1" class="marquee-item">
    <img src="/assets/images/photo2.jpg" alt="Research photo 2" class="marquee-item">
    <img src="/assets/images/photo3.jpg" alt="Research photo 3" class="marquee-item">
    <img src="/assets/images/photo4.jpg" alt="Research photo 4" class="marquee-item">
    <img src="/assets/images/photo5.jpg" alt="Research photo 5" class="marquee-item">
    <img src="/assets/images/photo6.jpg" alt="Research photo 6" class="marquee-item">
    <img src="/assets/images/photo1.jpg" alt="Research photo 1" class="marquee-item">
    <img src="/assets/images/photo2.jpg" alt="Research photo 2" class="marquee-item">
    <img src="/assets/images/photo3.jpg" alt="Research photo 3" class="marquee-item">
    <img src="/assets/images/photo4.jpg" alt="Research photo 4" class="marquee-item">
    <img src="/assets/images/photo5.jpg" alt="Research photo 5" class="marquee-item">
    <img src="/assets/images/photo6.jpg" alt="Research photo 6" class="marquee-item">
  </div>
</div>

