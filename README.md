<style>
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  @keyframes glowPulse {
    0%, 100% { text-shadow: 0 0 20px rgba(88,166,255,0.3); }
    50% { text-shadow: 0 0 40px rgba(88,166,255,0.6); }
  }
  @keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-30px); }
    to { opacity: 1; transform: translateX(0); }
  }
  @keyframes slideInRight {
    from { opacity: 0; transform: translateX(30px); }
    to { opacity: 1; transform: translateX(0); }
  }
  @keyframes scaleIn {
    from { opacity: 0; transform: scale(0.9); }
    to { opacity: 1; transform: scale(1); }
  }
  .profile-header { animation: fadeIn 1s ease-out; }
  .profile-name { animation: glowPulse 3s ease-in-out infinite, fadeInUp 1s ease-out 0.2s both; }
  .profile-subtitle { animation: fadeInUp 1s ease-out 0.4s both; }
  .stats-section { animation: fadeInUp 1s ease-out 0.6s both; }
  .about-section { animation: slideInLeft 0.8s ease-out 0.8s both; }
  .tech-section { animation: slideInRight 0.8s ease-out 1s both; }
  .projects-section { animation: scaleIn 0.8s ease-out 1.2s both; }
  .journey-section { animation: fadeInUp 0.8s ease-out 1.4s both; }
  .connect-section { animation: fadeInUp 0.8s ease-out 1.6s both; }
  .footer-section { animation: fadeIn 1s ease-out 1.8s both; }
  table { transition: all 0.3s ease; }
  td { transition: all 0.3s ease; }
  tr:hover td { background: rgba(88,166,255,0.05); }
  a { transition: all 0.3s ease; }
  a:hover { opacity: 0.8; }
  .project-card:hover { transform: translateY(-2px); box-shadow: 0 4px 20px rgba(88,166,255,0.15); }
</style>

<div class="profile-header" align="center">

<svg width="100%" height="120" viewBox="0 0 1200 120" preserveAspectRatio="none">
  <defs>
    <linearGradient id="wave-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0d1117;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#161b22;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0d1117;stop-opacity:1" />
    </linearGradient>
  </defs>
  <path fill="url(#wave-gradient)" opacity="0.6">
    <animate attributeName="d" dur="8s" repeatCount="indefinite" values="
      M0,60 C150,90 350,30 600,60 C850,90 1050,30 1200,60 L1200,0 L0,0 Z;
      M0,60 C150,30 350,90 600,60 C850,30 1050,90 1200,60 L1200,0 L0,0 Z;
      M0,60 C150,90 350,30 600,60 C850,90 1050,30 1200,60 L1200,0 L0,0 Z" />
  </path>
  <path fill="#0d1117" opacity="0.8">
    <animate attributeName="d" dur="6s" repeatCount="indefinite" values="
      M0,80 C200,100 400,60 600,80 C800,100 1000,60 1200,80 L1200,0 L0,0 Z;
      M0,80 C200,60 400,100 600,80 C800,60 1000,100 1200,80 L1200,0 L0,0 Z;
      M0,80 C200,100 400,60 600,80 C800,100 1000,60 1200,80 L1200,0 L0,0 Z" />
  </path>
  <path fill="#0d1117">
    <animate attributeName="d" dur="4s" repeatCount="indefinite" values="
      M0,100 C300,110 600,90 900,100 C1050,105 1150,95 1200,100 L1200,0 L0,0 Z;
      M0,100 C300,90 600,110 900,100 C1050,95 1150,105 1200,100 L1200,0 L0,0 Z;
      M0,100 C300,110 600,90 900,100 C1050,105 1150,95 1200,100 L1200,0 L0,0 Z" />
  </path>
</svg>

<h1 class="profile-name" style="margin-top:-60px; font-size:2.5em; font-weight:800; letter-spacing:-0.02em; color:#c9d1d9;">ANDRIANARIJERY Toaviniaina Maharavo</h1>

<p class="profile-subtitle" style="font-size:1.1em; color:#8b949e; letter-spacing:0.05em; margin-top:8px;">SOFTWARE DEVELOPER &middot; MADAGASCAR</p>

<br/>

<div class="stats-section">
<a href="https://github.com/toaandri">
  <img src="https://github-readme-stats.vercel.app/api?username=toaandri&show_icons=true&theme=radical&hide_border=true&count_private=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&icon_color=58a6ff" width="48%" />
</a>
<a href="https://github.com/toaandri">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=toaandri&layout=compact&theme=radical&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9" width="48%" />
</a>
<br/>
<img src="https://github-readme-streak-stats.herokuapp.com/?user=toaandri&theme=radical&hide_border=true&background=0d1117&stroke=58a6ff&ring=58a6ff&fire=58a6ff&currStreakLabel=c9d1d9&sideLabels=c9d1d9" width="70%" />
</div>

</div>

---

## About Me

<div class="about-section">

> **Full-stack developer** with a passion for building clean, scalable applications. I turn complex problems into elegant, user-friendly solutions.

- Based in **Antananarivo, Madagascar** (UTC+3)
- Focused on **React, Node.js, TypeScript** & modern web stacks
- Always exploring -- lately diving into **AI-assisted development** with opencode
- Open to collaborations on exciting projects

</div>

---

## Tech Stack

<div class="tech-section">

<table>
  <tr>
    <td><b>Languages</b></td>
    <td>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" />
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black" />
      <img src="https://img.shields.io/badge/Java-ED8B00?style=flat&logo=openjdk&logoColor=white" />
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/PHP-777BB4?style=flat&logo=php&logoColor=white" />
      <img src="https://img.shields.io/badge/SQL-4169E1?style=flat&logo=postgresql&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td><b>Frontend</b></td>
    <td>
      <img src="https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black" />
      <img src="https://img.shields.io/badge/React_Native-61DAFB?style=flat&logo=react&logoColor=black" />
      <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat&logo=tailwindcss&logoColor=white" />
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white" />
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white" />
      <img src="https://img.shields.io/badge/SASS-CC6699?style=flat&logo=sass&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td><b>Backend</b></td>
    <td>
      <img src="https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white" />
      <img src="https://img.shields.io/badge/NestJS-E0234E?style=flat&logo=nestjs&logoColor=white" />
      <img src="https://img.shields.io/badge/Express-000000?style=flat&logo=express&logoColor=white" />
      <img src="https://img.shields.io/badge/Socket.io-010101?style=flat&logo=socketdotio&logoColor=white" />
      <img src="https://img.shields.io/badge/GraphQL-E10098?style=flat&logo=graphql&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td><b>Database</b></td>
    <td>
      <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white" />
      <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white" />
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white" />
      <img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat&logo=firebase&logoColor=black" />
      <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=flat&logo=supabase&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td><b>DevOps</b></td>
    <td>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" />
      <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white" />
      <img src="https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white" />
      <img src="https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white" />
      <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white" />
      <img src="https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black" />
    </td>
  </tr>
  <tr>
    <td><b>Tools</b></td>
    <td>
      <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white" />
      <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" />
      <img src="https://img.shields.io/badge/VS_Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white" />
      <img src="https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white" />
      <img src="https://img.shields.io/badge/Jest-C21325?style=flat&logo=jest&logoColor=white" />
      <img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white" />
    </td>
  </tr>
</table>

</div>

---

## Featured Projects

<div class="projects-section">

<table>
  <tr>
    <td width="50%" valign="top" class="project-card" style="border:1px solid #30363d; border-radius:8px; padding:16px; transition:all 0.3s ease;">
      <h3><a href="https://github.com/toaandri/MITANEKO" style="color:#58a6ff; text-decoration:none;">MITANEKO</a></h3>
      <p style="color:#8b949e; font-size:0.9em;">Participatory urban governance platform -- citizens report city issues, the community votes to prioritize them, and local authorities track resolution actions.</p>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" />
    </td>
    <td width="50%" valign="top" class="project-card" style="border:1px solid #30363d; border-radius:8px; padding:16px; transition:all 0.3s ease;">
      <h3><a href="https://github.com/toaandri/M-E-kaly" style="color:#58a6ff; text-decoration:none;">M-E-kaly</a></h3>
      <p style="color:#8b949e; font-size:0.9em;">Full-stack food delivery platform -- customer & driver apps, vendor back-office, admin dashboard, OTP auth, Mobile Money payments.</p>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top" class="project-card" style="border:1px solid #30363d; border-radius:8px; padding:16px; transition:all 0.3s ease;">
      <h3><a href="https://github.com/toaandri/Tantsaha-Connect" style="color:#58a6ff; text-decoration:none;">Tantsaha-Connect</a></h3>
      <p style="color:#8b949e; font-size:0.9em;"><em>"Tantsaha" = farmer</em> in Malagasy -- a platform connecting farmers with markets and resources.</p>
      <img src="https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black" />
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black" />
    </td>
    <td width="50%" valign="top" class="project-card" style="border:1px solid #30363d; border-radius:8px; padding:16px; transition:all 0.3s ease;">
      <h3><a href="https://github.com/toaandri/Portfolio" style="color:#58a6ff; text-decoration:none;">Portfolio</a></h3>
      <p style="color:#8b949e; font-size:0.9em;">My personal portfolio website -- a showcase of my work and skills.</p>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top" class="project-card" style="border:1px solid #30363d; border-radius:8px; padding:16px; transition:all 0.3s ease;">
      <h3><a href="https://github.com/toaandri/Projet-transversal-Anamboatra-L2" style="color:#58a6ff; text-decoration:none;">Anamboatra</a></h3>
      <p style="color:#8b949e; font-size:0.9em;">Full-stack platform -- citizen web app, staff dashboard & mobile field app with real-time updates.</p>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" />
    </td>
    <td width="50%" valign="top" class="project-card" style="border:1px solid #30363d; border-radius:8px; padding:16px; transition:all 0.3s ease;">
      <h3><a href="https://github.com/toaandri/BTP-site-" style="color:#58a6ff; text-decoration:none;">BTP-site</a></h3>
      <p style="color:#8b949e; font-size:0.9em;">A website for the building & public works (BTP) sector.</p>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top" class="project-card" style="border:1px solid #30363d; border-radius:8px; padding:16px; transition:all 0.3s ease;">
      <h3><a href="https://github.com/toaandri/Opencode-Skills" style="color:#58a6ff; text-decoration:none;">Opencode-Skills</a></h3>
      <p style="color:#8b949e; font-size:0.9em;">My personal collection of opencode AI skills.</p>
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black" />
    </td>
    <td width="50%" valign="top" class="project-card" style="border:1px solid #30363d; border-radius:8px; padding:16px; transition:all 0.3s ease;">
      <h3><a href="https://github.com/toaandri/Complexite-algorithmique-examen-L2" style="color:#58a6ff; text-decoration:none;">Algorithmic Complexity</a></h3>
      <p style="color:#8b949e; font-size:0.9em;">Algorithmic complexity project -- Big O analysis and optimization.</p>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
    </td>
  </tr>
</table>

</div>

---

## My Journey

<div class="journey-section">

| When | What |
|------|------|
| **Nov 2024** | Joined GitHub |
| **May 2025** | First repository: `Projet_tranversal_G7` (group project in PHP) |
| **Apr 2026** | Started `Projet-transversal-Anamboatra-L2` |
| **May 2026** | Built **MITANEKO**, a participatory urban governance platform |
| **Jul 2026** | Shipped **M-E-kaly** (food delivery), a BTP site, and opencode skills |
| **Sep 2026** | Exploring AI-assisted development with opencode |

</div>

---

## Let's Connect

<div class="connect-section" align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://toaandri.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/maharavo)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://web.facebook.com/ravo.mah)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:toavinamaharavo@gmail.com)

</div>

---

<div class="footer-section" align="center">

*Misaotra anao misidina eto! (Thanks for stopping by!)*

<svg width="200" height="40" viewBox="0 0 200 40">
  <defs>
    <linearGradient id="line-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0d1117;stop-opacity:0" />
      <stop offset="50%" style="stop-color:#58a6ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0d1117;stop-opacity:0" />
    </linearGradient>
  </defs>
  <line x1="0" y1="20" x2="200" y2="20" stroke="url(#line-gradient)" stroke-width="2">
    <animate attributeName="stroke-dasharray" from="0,200" to="200,0" dur="2s" fill="freeze" />
  </line>
</svg>

</div>
