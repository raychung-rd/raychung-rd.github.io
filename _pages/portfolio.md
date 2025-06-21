---
permalink: /portfolio/
title: "Portfolio"
layout: portfolio
---
  
  <div class="portfolio-list">
    {% assign ongoing_projects = site.projects | where: "status", "Ongoing" | sort: 'date' | reverse %}
    {% assign complete_p1 = site.projects | where: "status", "Complete" %}
    {% assign complete_p2 = site.projects | where: "status", "Completed" %}
    {% assign complete_projects = complete_p1 | concat: complete_p2 | sort: 'date' | reverse %}
    
    {% assign projects = ongoing_projects | concat: complete_projects %}
    
    {% if projects.size > 0 %}
      {% for project in projects %}
        <div class="portfolio-item">
          <h3>{{ project.title }}</h3>
          
          <div class="project-meta">
            {% if project.status %}
              <span class="project-status">
                {% if project.status == 'Ongoing' %}
                  <span style="color: #28a745; font-weight: bold;">● Ongoing</span>
                {% elsif project.status == 'Completed' %}
                  <span style="color: #6c757d; font-weight: bold;">● {{ project.status }}</span>
                {% else %}
                  <span style="color: #6c757d;">{{ project.status }}</span>
                {% endif %}
              </span>
            {% endif %}
          </div>

          {% if project.hashtags %}
            <div class="project-hashtags">
              {% assign tags = project.hashtags | split: ", " %}
              {% for tag in tags %}
                <span>{{ tag }}</span>
              {% endfor %}
            </div>
          {% endif %}

          <button class="portfolio-modal-trigger" onclick="openPortfolioModal('{{ project.slug }}')">Show Details</button>
        </div>
      {% endfor %}
    {% else %}
        <p>No projects to display yet. Add more to the <code>_projects</code> folder.</p>
    {% endif %}
  </div>

  {% include portfolio_modals.html %}

<style>
.portfolio {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}
.portfolio-list {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
}
.portfolio-item {
  flex: 1 1 350px;
  min-width: 300px;
  max-width: 420px;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: transform 0.2s, box-shadow 0.2s;
}
.portfolio-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.12);
}
.portfolio-item h3 {
  margin: 0 0 10px 0;
  color: #3a5795;
  font-size: 1.15em;
}
.project-meta {
  margin-bottom: 10px;
}
.project-status {
  font-size: 0.9em;
}
.project-hashtags {
  margin-bottom: 15px;
}
.project-hashtags span {
  display: inline-block;
  background-color: #e9ecef;
  color: #495057;
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 0.8em;
  margin: 2px;
}
.portfolio-modal-trigger {
  margin-top: auto;
  background: #3a5795;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 8px 18px;
  cursor: pointer;
  font-size: 1em;
  transition: background-color 0.2s;
}
.portfolio-modal-trigger:hover {
  background: #2c4373;
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
  text-align: left;
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
.modal-collaborators {
  margin-bottom: 1em;
  font-size: 0.9em;
  color: #555;
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