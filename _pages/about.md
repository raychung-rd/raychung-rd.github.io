---
permalink: /
title: "About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

Born and raised in Taiwan, I moved to the U.S. in 2018 with the goal of becoming a registered dietitian. After earning my degree from the University of Michigan, I then worked in collegiate athletic teams, mental health clinics, research institutions, and health technology companies as a dietitian and a research scientist.

Through my clinical work, I witnessed firsthand how profoundly technology can influence human health—for better or worse. Much like the Chinese proverb "水能載舟，亦能覆舟" ("Water can carry a boat, but it can also overturn it"), I've come to believe that technology, when thoughtfully designed, can support and uplift people's health; when misapplied, it can just as easily create harm or inequity.

Thus, I returned to the University of Washington to pursue a PhD in Biomedical and Health Informatics. My research sits at the intersection of artificial intelligence (AI), human-computer interaction (HCI), and consumer health informatics. I am working on leveraging human-centered design techniques and AI/ML methods to build context-aware health applications.

I'm inspired by the late Kobe Bryant and his Mamba Mentality—to become a better version of myself every day and to inspire people around me. I'm always open to mentorship, collaboration, or simply a good coffee chat. If my work resonates with you, don't hesitate to reach out!

Outside of work, I enjoy traveling and playing sports - mainly basketball and golf (working on my swing) now. If you see me at IMA or on the green, come say hi!

<span style="color: #00274c;">Go Blue!</span> <span style="color: #32006e;">Go Dawgs!</span>

<div style="background-color: #f0f8ff; padding: 15px; margin-bottom: 20px;">
  <h2 style="margin-top: 0; color: #4682b4;">Currently seeking internship opportunities for Fall/Winter 2025!</h2>
  <p>Interested in Human-AI Interaction, Health AI, Explainable AI, Agentic AI.</p>
</div>

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

