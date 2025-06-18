---
permalink: /portfolio/
title: "Portfolio"
layout: single
---

<div class="portfolio">
  <h1 style="color: #4682b4;">Portfolio</h1>
  <div class="portfolio-list">
    {% assign projects = site.projects | sort: 'date' | reverse %}
    {% if projects.size == 0 %}
      {% assign projects = "Project 1,Project 2,Project 3" | split: "," %}
      {% for project in projects %}
        <div class="portfolio-item">
          <h3>{{ project }}</h3>
          <button class="portfolio-modal-trigger" onclick="openPortfolioModal('placeholder-{{ forloop.index }}')">Show Details</button>
          <div id="modal-placeholder-{{ forloop.index }}" class="portfolio-modal">
            <div class="modal-content">
              <button class="close" aria-label="Close">&times;</button>
              <img class="modal-image" src="/assets/images/portfolio/placeholder.png" alt="Project Image">
              <div class="modal-title">{{ project }}</div>
              <div class="modal-description">Project description goes here.</div>
            </div>
          </div>
        </div>
      {% endfor %}
    {% else %}
      {% for project in projects %}
        <div class="portfolio-item">
          <h3>{{ project.title }}</h3>
          <button class="portfolio-modal-trigger" onclick="openPortfolioModal('{{ project.slug }}')">Show Details</button>
          <div id="modal-{{ project.slug }}" class="portfolio-modal">
            <div class="modal-content">
              <button class="close" aria-label="Close">&times;</button>
              <img class="modal-image" src="/assets/images/portfolio/{{ project.slug }}.png" alt="Project Image" onerror="this.src='/assets/images/portfolio/placeholder.png'">
              <div class="modal-title">{{ project.title }}</div>
              <div class="modal-description">{{ project.description | default: 'No description available.' }}</div>
            </div>
          </div>
        </div>
      {% endfor %}
    {% endif %}
  </div>
</div>

<style>
.portfolio {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
.portfolio-list {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
}
.portfolio-item {
  flex: 1 1 250px;
  min-width: 250px;
  max-width: 350px;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  padding: 18px 16px 16px 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.portfolio-item h3 {
  margin: 0 0 10px 0;
  color: #4682b4;
}
.portfolio-modal-trigger {
  margin-bottom: 10px;
  background: #4682b4;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 6px 16px;
  cursor: pointer;
  font-size: 1em;
}
.portfolio-modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  overflow: auto;
  background: rgba(0,0,0,0.5);
  transition: opacity 0.2s;
}
.portfolio-modal .modal-content {
  background: #fff;
  margin: 5vh auto;
  padding: 2em 2em 1.5em 2em;
  border-radius: 12px;
  max-width: 600px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.18);
  position: relative;
  animation: fadeIn 0.3s;
}
.portfolio-modal .close {
  position: absolute;
  top: 1em;
  right: 1em;
  font-size: 1.5em;
  color: #888;
  cursor: pointer;
  background: none;
  border: none;
}
.portfolio-modal .modal-image {
  width: 100%;
  max-height: 250px;
  object-fit: contain;
  margin-bottom: 1em;
  background: #f0f0f0;
  border-radius: 8px;
}
.portfolio-modal .modal-title {
  font-size: 1.2em;
  font-weight: bold;
  margin-bottom: 0.5em;
}
.portfolio-modal .modal-description {
  font-size: 1em;
  color: #222;
  margin-bottom: 1em;
}
</style>
<script>
function openPortfolioModal(id) {
  document.getElementById('modal-' + id).style.display = 'block';
  document.body.style.overflow = 'hidden';
}
</script> 