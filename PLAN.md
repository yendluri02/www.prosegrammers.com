# Plan for Prosegrammers

## Plan for Content

### Revise the Index for the Entire Site

- [X] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on document engineering.
- [X] Rewrite each of the introductory paragraphs so that they focus on the
concept of a "Prosegrammer". 
- [X] Rewrite the course overview so that it connects to the concept
of a "Prosegrammer" and a course on document engineering
- [X] Create a new Python source code example that connects to the
topic of document engineering and does not require any dependencies.
- [X] Delete any content related to performance engineering, as this is not
the focus of a course on document engineering.
- [X] Give the correct link to the discord server, which is specified in
the `_quarto.yml` file.

### Create Slides for Week One in `slides/weekone/index.qmd`

- [ ] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on document engineering.
- [ ] Review the content in the `index.qmd` file in the root of the repository
that explains the idea of a "Prosegrammer" and the concept of document
engineering.
- [ ] Following the guidelines for creating slides, translate the content in the
`index.qmd` in the root of the repository to slides that introduce the course in
the `slides/weekone/index.qmd` file.
- [ ] Note that the existing content was from slides that Gregory M. Kapfhammer
previously created to introduce a course in the field of algorithm analysis. You
should revise all the technical content in these slides to fit into a course
about document engineering. However, you should also use this content in these
slides as good examples for what your generated slides should look like. Make
sure to use similar formatting, layout, and content as the provided slides.
- [ ] After finishing the slides that introduce the course, create more slides
that introduce the following technologies and explain how to install them:
    - Terminal window
    - Git, GitHub, and GitHub CLI (i.e., `gh`)
    - Register for a free GitHub Student Developer Pack
    - Register for the free use of GitHub Copilot at the pro level
    - VS Code
    - `uv` (stress the use of `uv` for venvs, dependencies, and Python
    installation)
    - Python 3.12 or 3.13 (which should come from using the `uv` tool)
    - Quarto
    - Quarto extension for VS Code
    - Customize VS Code by picking a theme and installing extensions
    - Npm and Node.js and all affiliated tools like `npx`
    - Google Gemini CLI (run through the use of `npx`)
    - OpenCode (run through the use of `npx`)
- [ ] Ensure that the instructions in the slides from the previous step will
work correctly regardless of the operating system (Windows, MacOS, Linux).
- [ ] Ensure that the instructions for installing each of the aforementioned
tools clearly explain what the tool does, why it is important, and how it can
help a prosegrammer to create, maintain, and analyze documents.
- [ ] Ensure that the instructions for installing each of the aforementioned
tools stress the importance of testing the setup to make sure that they are
working. There should be links to online documentation that a learner can read
if they have trouble installing or testing any of the tools.
- [ ] Add content about the responsible use of artificial intelligence (AI)
coding and writing tools that use large language models (LLMs) like Claude
Sonnet 4 or GPT-4. Make it clear that the prosegrammer who uses these tools is
ultimately responsible for wielding them correctly and ethically.

## Support for Content

### Support for Index.qmd Revision Content

#### Definition and Etymology of "Prosegrammer"

- The term "prosegrammer" effectively combines "prose" (written text) and
"programmer" (software developer)
- This portmanteau reflects the interdisciplinary nature of document engineering
- Similar compound terms exist in technical fields (e.g., "bioinformatics"
combines biology and informatics)

#### Document Engineering as Academic Field

- Document engineering is recognized as a legitimate academic discipline
combining computer science and technical communication
- Research in this field includes automated document generation, content
management systems, and text analytics
- Universities offer courses in technical writing, computational linguistics,
and information design that align with document engineering principles

#### Python for Document Processing

- Python's string manipulation capabilities, regex support, and libraries like
NLTK make it ideal for document analysis
- The `string` module provides built-in methods for text cleaning and processing
- Dictionary-based word frequency analysis is a standard technique in natural
language processing and computational linguistics

#### Document Analysis Metrics

- Word count, sentence count, and readability metrics are standard measures in
content analysis
- The Flesch-Kincaid readability score and similar metrics rely on
words-per-sentence calculations
- Document summary statistics help technical writers assess and improve content
quality
