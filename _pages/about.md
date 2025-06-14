---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Born and raised in Taiwan, I moved to the US seven years ago to become a registered dietitian in this country. After completing my degree from the University of Michigan, I then worked in collegiate athletic teams; mental health clinics, research institutions, and biotech companies - including multiple startups.

I returned to the University of Washington to begin my PhD in Biomedical and Health Informatics. My current research interest lies in the intersection of artificial intelligence (AI), human-AI interaction, and consumer health informatics. I am working on leveraging human-centered design techniques and AI/ML methods to build holistic digital health applications.

I am inspired by the late great Kobe Bryant's Mamba Mentality - to become a better version of myself every day and to inspire people around me. Thus, I enjoyed mentorship or just casual coffee chats. It's been a fun and distinct journey, and I'd love to chat with anyone who's interested.

Outside of work, I enjoy traveling and playing team sports - mainly basketball and golf (working on my swing) now. If you see me at IMA or on the green, come say hi!

Go Blue! Go Dawgs!

## Selected Publications

{% assign selected_papers = site.publications | where: "author_position", "first" | sort: "date" | reverse %}
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

