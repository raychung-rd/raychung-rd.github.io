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

I am inspired by the late great Kobe Bryant's Mamba Mentality - to become a better version of myself every day and to inspire people around me. Thus, I'm open to mentorship oppurtunities or just casual coffee chats. 

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
{{ forloop.index }}. **{{ paper.authors }}** ({{ paper.date | date: "%Y" }}). [{{ paper.title }}]({{ paper.paperurl }}). *{{ paper.venue }}*. {% if paper.citation %}{{ paper.citation }}{% endif %}
{% endfor %}

For a complete list of publications, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=8Z-pAeQAAAAJ&hl=en).

## 📸 Photo Gallery


<div class="row">
  <div class="column">
    <img src="/images/photo1.jpg" alt="Description of photo 1" style="width:100%">
  </div>
  <div class="column">
    <img src="/images/photo2.jpg" alt="Description of photo 2" style="width:100%">
  </div>
  <div class="column">
    <img src="/images/photo3.jpg" alt="Description of photo 3" style="width:100%">
  </div>
</div>

<style>
.row {
  display: flex;
  flex-wrap: wrap;
  padding: 0 4px;
}

.column {
  flex: 33.33%;
  padding: 0 4px;
}

.column img {
  margin-top: 8px;
  vertical-align: middle;
  border-radius: 8px;
}

@media screen and (max-width: 800px) {
  .column {
    flex: 50%;
  }
}

@media screen and (max-width: 600px) {
  .column {
    flex: 100%;
  }
}
</style>

