<div align="center">
  <h3><code>s0pex@github ~ $ ./contributions.sh</code></h3>
  <img src="./img/contrib-heatmap.svg" width="860" alt="GitHub contribution heatmap for the last year" />
  <br><br>
  <h3><code>s0pex@github ~ $ whoami</code></h3>
  <img src="./img/whoami.svg" width="860" alt="whoami: Artur Komaristych, Senior Software Developer at Infolytics AG. M.Sc. Computer Science, University of Cologne, 2026, with honors, thesis at DLR. B.Sc. Computer Science, RWTH Aachen, 2022, thesis at Fraunhofer IPT. Focus: distributed systems, backend, DevOps. Away from the keyboard: scuba diving, climbing, badminton." />
  <br>
  <sub>"Code is like humor. When you have to explain it, it's bad." - Cory House</sub>
</div>

<br>

<p align="center">Backend and infrastructure developer. I work on distributed systems, cloud infrastructure and CI/CD.</p>

<p align="center">
<a href="https://de.linkedin.com/in/artur-komaristych-89b623171"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://github.com/S0PEX"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
</p>

<br>

<div align="center">

<h3><code>s0pex@github ~ $ cat experience.md</code></h3>
<img src="./img/experience.svg" width="860" alt="Experience at Infolytics AG: Senior Software Developer 2026 to present, Software Developer 2022 to 2026, Working Student 2018 to 2022." />

<br><br>

<h3><code>s0pex@github ~ $ cat stack.md</code></h3>
<img src="./img/stack.svg" width="860" alt="Stack: Java, C#, TypeScript, C++, Python. Spring Boot, ASP.NET Core, NestJS, Angular, React, Next.js. Kubernetes, OpenShift, Docker, Helm, Argo CD, Proxmox VE, Ansible, GitLab CI, GitHub Actions. Google Compute Engine, Oracle Cloud Infrastructure. PostgreSQL, MySQL, MariaDB, JPA, Hibernate, Entity Framework, Drizzle." />

<br><br>

<h3><code>s0pex@github ~ $ cat education.md</code></h3>
<img src="./img/education.svg" width="860" alt="Education: M.Sc. Computer Science with honors, University of Cologne (2023 to 2026), master thesis at DLR. B.Sc. Computer Science, RWTH Aachen University (2018 to 2022), bachelor thesis at Fraunhofer IPT. IT Assistant with A-levels (Abitur), Georg-Simon-Ohm-Berufskolleg (2015 to 2018)." />

</div>

<div align="center">

<h3><code>s0pex@github ~ $ ./away-from-keyboard.sh</code></h3>
<img src="./img/offline.svg" width="860" alt="Away from the keyboard: scuba diving, bouldering and climbing, badminton." />

</div>

<!-- plain-text:start -->
<details>
<summary>Plain text version</summary>

#### Experience

**Senior Software Developer**, Infolytics AG (2026 to present)

- Technical owner of three business domains of a live public-sector platform (Spring Boot, Angular, OpenShift) where applications are submitted and processed by caseworkers
- End-to-end responsibility for these domains: architecture, delivery, operations and direct customer contact
- Still active on SDF, the Infolytics signal data platform: feature development and consulting
- Mentor junior developers and working students

**Software Developer**, Infolytics AG (2022 to 2026)

- Continued developing SDF alongside new responsibilities
- Led the migration of the SDF frontend applications from jQuery to Angular, and of the backend from MaxDB to PostgreSQL including all existing data, with no downtime
- Tracked down hard production issues (memory leaks, network protocol bugs) and shipped the fixes
- Replaced manual deploys with GitOps on Kubernetes and Argo CD

**Working Student**, Infolytics AG (2018 to 2022)

- Developed the Java client library for the native TCP protocol of SDF, the signal data platform behind WiValdi<b>*</b>, a DLR wind research project with 2,000+ sensors. Also worked on the C++ backend
- Other Java projects: optimization and maintenance
- Hired full-time right after the B.Sc.

<b>*</b> WiValdi (also called DFWind) is a DLR research project. I worked on SDF, the Infolytics signal data platform it runs on, not on WiValdi itself.

#### Stack

- **Languages:** Java, C#, TypeScript, C++, Python
- **Frameworks:** Spring Boot, ASP.NET Core, NestJS, Angular, React, Next.js
- **Infrastructure:** Kubernetes, OpenShift, Docker, Helm, Argo CD, Proxmox VE, Ansible, GitLab CI, GitHub Actions
- **Cloud:** Google Compute Engine, Oracle Cloud Infrastructure
- **Data:** PostgreSQL, MySQL, MariaDB, JPA, Hibernate, Entity Framework, Drizzle

#### Education

**M.Sc. Computer Science, with honors**, University of Cologne (2023 to 2026)

- Focus areas: Software-Intensive Systems and High-Performance Computing
- Master thesis at the German Aerospace Center (DLR), Distributed Software Systems group: "A Unifying Framework for Provisioning and Executing Computational Tools across Heterogeneous Computing Environments"
  - Designed a coordinator-worker architecture and implemented a prototype that unifies tool execution across heterogeneous computing environments (Kubernetes, Slurm, native Linux, Windows) behind a single REST API<b>*</b>
  - In production use at DLR, open source release planned
- Member of the faculty selection committee

**B.Sc. Computer Science**, RWTH Aachen University (2018 to 2022)

- Minor in Business Administration
- Bachelor thesis at Fraunhofer IPT: "Development and Deployment of a Cloud-Based System Architecture for Domain-Specific AutoML Systems"
  - Migrated an AutoML pipeline to Kubernetes (Oracle OKE) and built a cloud-native architecture with a NestJS backend and ReactJS frontend

**IT Assistant with A-levels**, Georg-Simon-Ohm-Berufskolleg (2015 to 2018)

- School-based vocational training in Germany (schulische Ausbildung) in programming, networking and more, completed together with the Abitur (German A-levels)

<b>*</b> Tools are described in a declarative YAML specification (name, version, typed inputs and outputs, runtime). Workers parse it and register their tools with the central coordinator. Its REST API lists the registered tools and accepts jobs with binary or primitive inputs. Each job is scheduled onto a suitable worker, which stages the artifacts, executes the task and uploads the results. Failed jobs are retried, and users follow job progress through real-time events instead of polling.

</details>
<!-- plain-text:end -->
