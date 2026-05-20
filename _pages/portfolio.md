---
permalink: /portfolio/
title: "Portfolio"
layout: portfolio
---
  
  <div class="portfolio-grid">
    {% assign ongoing_projects = site.projects | where: "status", "Ongoing" | sort: 'date' | reverse %}
    {% assign complete_p1 = site.projects | where: "status", "Complete" %}
    {% assign complete_p2 = site.projects | where: "status", "Completed" %}
    {% assign complete_projects = complete_p1 | concat: complete_p2 | sort: 'date' | reverse %}
    
    {% assign projects = ongoing_projects | concat: complete_projects %}
    
    {% if projects.size > 0 %}
      {% for project in projects %}
        <article class="portfolio-card">
          <img src="/assets/images/portfolio/{{ project.slug }}.png" alt="{{ project.title }}" class="portfolio-image" onerror="this.src='/assets/images/portfolio/placeholder.png'">
          <div class="card-content" style="padding: 1.5rem;">
            <h3>{{ project.title }}</h3>
            
            {% if project.hashtags %}
              <div class="tags">
                {% assign tags = project.hashtags | split: ", " %}
                {% for tag in tags %}
                  <span class="publication-tag">{{ tag }}</span>
                {% endfor %}
              </div>
            {% endif %}
            
            <a href="#" class="btn" onclick="openPortfolioModal('{{ project.slug }}'); return false;">View Summary &rarr;</a>
          </div>
        </article>
      {% endfor %}
    {% else %}
        <p>No projects to display yet. Add more to the <code>_projects</code> folder.</p>
    {% endif %}
  </div>

  {% include portfolio_modals.html %}

<style>
/* Additional styles for portfolio page */
.card-content h3 {
  margin: 0 0 1rem 0;
  color: #3a5795;
  font-size: 1.2em;
}

.tags {
  margin-bottom: 1rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.publication-tag {
  display: inline-block;
  background-color: #e9ecef;
  color: #495057;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.85em;
}

.card-content .btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #0d1812;
  color: #4ade80 !important;
  text-decoration: none !important;
  border-radius: 999px;
  border: 1px solid rgba(74, 222, 128, 0.22) !important;
  padding: 8px 18px;
  font-size: 0.88em;
  font-weight: 600;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
  transition: all 0.18s ease;
}

.card-content .btn:hover {
  background: #132b1f;
  box-shadow: 0 0 0 1.5px rgba(74, 222, 128, 0.38), 0 4px 14px rgba(0,0,0,0.38);
  transform: translateY(-1px);
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

// Close modal when clicking the close button
document.addEventListener('DOMContentLoaded', function() {
  const closeButtons = document.querySelectorAll('.portfolio-modal .close');
  closeButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      const modal = this.closest('.portfolio-modal');
      modal.style.display = 'none';
      document.body.style.overflow = '';
    });
  });
  
  // Close modal when clicking outside
  const modals = document.querySelectorAll('.portfolio-modal');
  modals.forEach(function(modal) {
    modal.addEventListener('click', function(e) {
      if (e.target === this) {
        this.style.display = 'none';
        document.body.style.overflow = '';
      }
    });
  });
});
</script> 