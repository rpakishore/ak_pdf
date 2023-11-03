<!--- Heading --->
<div align="center">
  <h1>AK_PDF</h1>
  <p>
    Library to Parse/Edit/Create/Read PDF documents
  </p>
<h4>
    <a href="https://github.com/rpakishore/ak_pdf/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_pdf">Documentation</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_pdf/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_pdf/issues/">Request Feature</a>
  </h4>
</div>
<br />

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rpakishore/ak_pdf)
![GitHub last commit](https://img.shields.io/github/last-commit/rpakishore/ak_pdf)
<!-- Table of Contents -->
<h2>Table of Contents</h2>

- [1. About the Project](#1-about-the-project)
  - [1.1. Screenshots](#11-screenshots)
  - [1.2. Features](#12-features)
- [2. Getting Started](#2-getting-started)
  - [2.1. Prerequisites](#21-prerequisites)
  - [2.2. Installation](#22-installation)
    - [2.2.1. Production](#221-production)
    - [2.2.2. Development](#222-development)
- [3. Usage](#3-usage)
- [4. Roadmap](#4-roadmap)
- [5. FAQ](#5-faq)
- [6. License](#6-license)
- [7. Contact](#7-contact)
- [8. Acknowledgements](#8-acknowledgements)

<!-- About the Project -->
## 1. About the Project
<!-- Screenshots -->
### 1.1. Screenshots

<div align="center"> 
  <img src="https://placehold.co/600x400?text=Your+Screenshot+here" alt="screenshot" />
</div>

<!-- Features -->
### 1.2. Features

- Read contents of existing PDFs
- Cache results for improved performance
- Feature 3

<!-- Getting Started -->
## 2. Getting Started

<!-- Prerequisites -->
### 2.1. Prerequisites

Python 3.11 or above

<!-- Installation -->
### 2.2. Installation

#### 2.2.1. Production

Install directly from pip

```bash
pip install ak_pdf
```

#### 2.2.2. Development

Download the git and install via flit

```bash
git clone https://github.com/rpakishore/ak_pdf.git
cd ak_pdf
pip install flit
flit install
```
<!-- Usage -->
## 3. Usage

Reader Functionality

```python
from ak_pdf import Reader

# Initialize
pdf = Reader(filepath=r"textbook.pdf", password=None)

## Document metadata
pdf.metadata

## Check if pdf is encrypted
pdf.encrypted

## get number of pages
pdf.num_pages

## get list of page objects
pdf.pages   #list[PageObjects]

## get page text
pdf.text(10)    #gets text from 11th page (page_idx=10); Results cached

## get images from page
pdf.images(page_idx=10) #List of PIL Image Objects from 11th page

## Extract and save images
pdf.save_images(page_idx=10, folderpath='C:\\')

## get pagelabel
pdf.page_number(page_idx=10) #or
pdf.page_number(page=pdf.pages[10])
```

Writer Functionality
```python
```

<!-- Roadmap -->
## 4. Roadmap

- [x] Reader/Parser
- [ ] Creator Template
- [ ] Modification of Existing PDFs

<!-- FAQ -->
## 5. FAQ

- Question 1
  - Answer 1


<!-- License -->
## 6. License

See LICENSE for more information.

<!-- Contact -->
## 7. Contact

Arun Kishore - [@rpakishore](mailto:pypi@rpakishore.co.in)

Project Link: [https://github.com/rpakishore/ak_pdf](https://github.com/rpakishore/ak_pdf)

<!-- Acknowledgments -->
## 8. Acknowledgements

Use this section to mention useful resources and libraries that you have used in your projects.

- [Shields.io](https://shields.io/)