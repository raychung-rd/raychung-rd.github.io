---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Born and raised in Taiwan, I moved to the US in 2018 with the goal of becoming a registered dietitian in this country. After completing my degree from the University of Michigan, I then worked in collegiate athletic teams, mental health clinics, research institutions, and health technology companies as a dietitian and research scientist.

With a passion of creating better techonology to improve people's health and well-being, I returned to the University of Washington to begin my PhD in Biomedical and Health Informatics in 2023. My current research interest lies in the intersection of artificial intelligence (AI), human-computer interaction, and consumer health informatics. I am working on leveraging human-centered design techniques and AI/ML methods to build health applications.

I am inspired by the late great Kobe Bryant's Mamba Mentality - to become a better version of myself every day and to inspire people around me. Thus, I welcome mentorship oppurtunities or just casual coffee chats. If you are interest in my work, please feel free to reach out!

Outside of work, I enjoy traveling and playing sports - mainly basketball and golf (working on my swing) now. If you see me at IMA or on the green, come say hi!

<span style="color: #00274c;">Go Blue!</span> <span style="color: #32006e;">Go Dawgs!</span>

<div style="background-color: #f0f8ff; padding: 15px; margin-bottom: 20px;">
  <h2 style="margin-top: 0; color: #4682b4;">Currently seeking internship opportunities for Fall/Winter 2025!</h2>
  <p>Interested in Human-AI Interaction, Health AI, Explainable AI, Agentic AI.</p>
</div>

## Selected Publications

{% assign first_author_papers = site.publications | where: "author_position", "first" %}
{% assign second_author_papers = site.publications | where: "author_position", "second" %}
{% assign selected_papers = first_author_papers | concat: second_author_papers | sort: "date" | reverse %}
{% for paper in selected_papers limit:3 %}
{{ forloop.index }}. {{ paper.authors | replace: 'Ray-yuan Chung', '<b>Ray-yuan Chung</b>' | replace: 'Ray-Yuan Chung', '<b>Ray-Yuan Chung</b>' | replace: 'R Chung', '<b>R Chung</b>' | replace: 'Ray Chung', '<b>Ray Chung</b>' }} ({{ paper.date | date: "%Y" }}). [{{ paper.title }}]({{ paper.paperurl }}). *{{ paper.venue }}*. {% if paper.citation %}{{ paper.citation }}{% endif %}
{% endfor %}

For a complete list of publications, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=8Z-pAeQAAAAJ&hl=en).

## 📸 Photo Gallery

<div class="photo-gallery">
  <img src="/images/photo1.jpg" alt="Description of photo 1">
  <img src="/images/photo2.jpg" alt="Description of photo 2">
  <img src="/images/photo3.jpg" alt="Description of photo 3">
</div>

<style>
.photo-gallery {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  margin: 20px 0;
}
.photo-gallery img {
  width: 280px;
  height: 200px;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  background: #f8f8f8;
}
@media (max-width: 600px) {
  .photo-gallery img {
    width: 90vw;
    height: 160px;
  }
}
</style>

