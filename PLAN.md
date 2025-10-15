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

- [X] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on document engineering.
- [X] Review the content in the `index.qmd` file in the root of the repository
that explains the idea of a "Prosegrammer" and the concept of document
engineering.
- [X] Following the guidelines for creating slides, translate the content in the
`index.qmd` in the root of the repository to slides that introduce the course in
the `slides/weekone/index.qmd` file.
- [X] Note that the existing content was from slides that Gregory M. Kapfhammer
previously created to introduce a course in the field of algorithm analysis. You
should revise all the technical content in these slides to fit into a course
about document engineering. However, you should also use this content in these
slides as good examples for what your generated slides should look like. Make
sure to use similar formatting, layout, and content as the provided slides.
- [X] The slides that introduce the course should contain Python source code
like that which you found in the `index.qmd` file in the root of the repository.
Make sure that students can run this source code and see the output.
- [X] After finishing the slides that introduce the course, create more slides
that introduce the following technologies and explain how to install them:
    - Terminal window
    - Git, GitHub, and GitHub CLI (i.e., `gh`)
    - Register for a free GitHub Student Developer Pack
    - Register for the free use of GitHub Copilot at the pro level
    - VS Code
    - `uv` (stress the use of `uv` for virtual environments, dependencies, and
    Python installation, especially focusing on the fact that a learner
    should not use alternative mechanisms for installing Python or any of
    the other aforementioned tasks like creating virtual environments)
    - Python 3.12 or 3.13 (which should come from using the `uv` tool)
    - Quarto
    - Quarto extension for VS Code
    - Customize VS Code by picking a theme and installing extensions
    - Npm and Node.js and all affiliated tools like `npx`
    - Google Gemini CLI (run through the use of `npx`)
    - OpenCode (run through the use of `npx`)
- [X] Ensure that the instructions in the slides from the previous step will
work correctly regardless of the operating system (Windows, MacOS, Linux).
- [X] Ensure that the instructions for installing each of the aforementioned
tools clearly explain what the tool does, why it is important, and how it can
help a prosegrammer to create, maintain, and analyze documents.
- [X] Ensure that the instructions for installing each of the aforementioned
tools stress the importance of testing the setup to make sure that they are
working. There should be links to online documentation that a learner can read
if they have trouble installing or testing any of the tools.
- [X] Add content about the responsible use of artificial intelligence (AI)
coding and writing tools that use large language models (LLMs) like Claude
Sonnet 4 or GPT-4. Make it clear that the prosegrammer who uses these tools is
ultimately responsible for wielding them correctly and ethically.

### Create Slides for Week Four in `slides/weekfour/index.qmd`

- [X] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on document engineering.
- [X] Review the content in the `index.qmd` file in the root of the repository
that explains the idea of a "Prosegrammer" and the concept of document
engineering.
- [X] Review the content in the `index.qmd` file in the `syllabus` directory of
the repository that explains rules and regulations for this course on document
engineering. Note that these are the rules that students follow and not
specifically the rules and regulations that you follow as a coding agent.
- [X] The new slides that I want you to create should be in the file
`slides/weekfour/index.qmd`. The purpose of these slides is to introduce the
basics of Markdown and Quarto. Here are some basic features of Markdown and
Quarto that you should include in these slides:
  - Structure of a Markdown document
  - Headings and subheadings
  - Paragraphs and line breaks
  - Bold and italic text
  - Lists (ordered and unordered)
  - Links and images
  - Code blocks and inline code
  - Tables
  - Blockquotes
  - Horizontal rules
  - Mathematical expressions
- You can look at the other slide decks that I have already prepared:
  - `slides/weekone/index.qmd`
  - `slides/weektwo/index.qmd`
  - `slides/weekthree/index.qmd` and see how I am currently using Markdown and
  Quarto in my slides! I want students to be able to understand all of these
  examples and know how to write them on their own for their own documentation.
- [X] When you create all of these examples, make sure that they connect to the
concepts of document engineering and prosegramming, as I have already defined in
the contents of this GitHub repository. For instance, you can connect the need
to write Markdown to the Markdown files that they write to document their own
document engineering projects, where they are building tools that input
and process and analyze text documents in JSON, YAML, Markdown, and plaintext.
You can add slides that make suggestions on how they could use the features of
Markdown inside of the `README.md` file for the tool. You can also add slides
that explain how they could create a website for their tool using Quarto.
- [X] You must show the actual source code of the basic feature (e.g., bold and
italic text) and then show how that actually renders. This means that the
student should be able to look at the slide and see both the source code and the
rendered output.
- [X] Make sure that all the content is accessible to beginners who do not have
extensive experience with programming or the documentation of a software tool.
- [X] Make sure that all the content has concrete examples that make points
clear to beginners.

### Create Slides for Week Six in `slides/weeksix/index.qmd`

- [X] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on document engineering.
- [X] Review the content in the `index.qmd` file in the root of the repository
that explains the idea of a "Prosegrammer" and the concept of document
engineering.
- [X] Review the content in the `index.qmd` file in the `syllabus` directory of
the repository that explains rules and regulations for this course on document
engineering. Note that these are the rules that students follow and not
specifically the rules and regulations that you follow as a coding agent.
- [X] The new slides that I want you to create should be in the file
`slides/weeksix/index.qmd`. The purpose of these slides is to introduce the
basics of software testing. I previously created these slides for a course
on Algorithm Analysis. However, I would like you to customize all of this
content for document engineering.
- You can look at the other slide decks that I have already prepared:
  - `slides/weekone/index.qmd`
  - `slides/weektwo/index.qmd`
  - `slides/weekthree/index.qmd`
  and see how I am currently using Markdown and Quarto in my slides!
- Please note that I am currently working on the slides in
`slides/weekfour/index.qmd` that introduce Markdown and Quarto. So, please
don't use those as an example because they are not yet complete.
- I want students to understand the basics of software testing so that when
they are building their document engineering tools they can also test them.
- Please customize all the examples in the slides so that they connect to
document engineering and are accessible to beginners. However, you should
keep the simple `DaysOfTheWeek` source code because that one is easy to
understand and accessible to beginners.
- If you check the `index.qmd` file in this GitHub repository, you can see a
simple example of word frequency analysis. You should illustrate how to write
test cases for a function like this one.
- [X] Make sure that all the content is accessible to beginners who do not have
extensive experience with programming or the documentation of a software tool.
- [X] Make sure that all the content has concrete examples that make points
clear to beginners.
- [X] I added some template content to start off the slides. You should keep
the first and last slides, but make sure to customize them for a course on
document engineering and the module that is about data containers.

### Create Slides for Week Eight in `slides/weekeight/index.qmd`

- [ ] Review the content in the `GEMINI.md` file (or the `AGENTS.md` file) that
explains the theme of the course on document engineering.
- [ ] Review the content in the `index.qmd` file in the root of the repository
that explains the idea of a "Prosegrammer" and the concept of document
engineering.
- [ ] Review the content in the `index.qmd` file in the `syllabus` directory of
the repository that explains rules and regulations for this course on document
engineering. Note that these are the rules that students follow and not
specifically the rules and regulations that you follow as a coding agent.
- [ ] The new slides that I want you to create should be in the file
`slides/weeksix/index.qmd`. The purpose of these slides is to introduce the
basics of software testing. I previously created these slides for a course on
Algorithm Analysis. However, I would like you to customize all of this content
for document engineering.
- You can look at the other slide decks that I have already prepared:
  - `slides/weekone/index.qmd`
  - `slides/weektwo/index.qmd`
  - `slides/weekthree/index.qmd`
  - `slides/weekfour/index.qmd`
  - `slides/weekfive/index.qmd`
  - `slides/weeksix/index.qmd`
  and see how I am currently using Markdown and Quarto in my slides!
- Please do not use Markdown or Quarto formats that I am not currently
using in my slides to make sure that the content has a consistent format.
- [ ] Please remember that I am currently working on the slides in
`slides/weekeight/index.qmd` that introduce how to use data containers in
Python. I want the slides to cover these topics:
  - Lists (single-dimensional and two-dimensional)
    - A single-dimensional list that stores five different documents
    - A two-dimensional list that stores a list of the same document
      but with different metadata or arising from different formats
  - Tuples and sets
    - A tuple that stores the title, author, and date of a document
    - A set that stores the unique keywords or tags associated with a document
  - Any other basic content about lists, sets, or tuples, including:
    - Creating and initializing lists, tuples, and sets
    - Accessing elements in lists, tuples, and sets
    - Adding and removing elements from lists, tuples, and sets
- [ ] If you check the `index.qmd` file in this GitHub repository, you can see a
simple example of word frequency analysis. Please use simple examples like this
one to illustrate how to use containers like lists, tuples, and sets in Python.
- [ ] Make sure that all the content is accessible to beginners who do not have
extensive experience with programming or the documentation of a software tool.
- [ ] Make sure that all the content has concrete examples that make points
clear to beginners. Provide simple summaries of the concrete code examples.

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

### Support for Week One Slides Content

#### Document Engineering Definition and Scope

- Document engineering combines computational methods with technical writing
principles, as evidenced by academic programs at institutions like Carnegie
Mellon and MIT that integrate technical communication with computer science
- The field encompasses automated document generation, content analysis, and
workflow optimization, supported by research in computational linguistics and
information science

#### Python for Text Processing and Analysis

- Python's built-in `string` module and `re` library provide robust text
processing capabilities that are fundamental to document engineering tasks
- Word frequency analysis using dictionary-based counting is a standard
technique in natural language processing, as demonstrated in NLTK documentation
and computational linguistics textbooks
- Document statistics like word count, sentence count, and readability metrics
are established measures in content analysis research

#### Development Tools for Document Engineering

- VS Code with Quarto extension provides integrated development environment for
combining code and prose, as documented in Quarto's official documentation
- UV package manager represents modern Python dependency management, following
best practices from Python Enhancement Proposals (PEPs) and recommendations
from the Python Software Foundation
- Git and GitHub form the industry standard for version control and
collaboration, with widespread adoption in both software development and
academic publishing workflows

#### Cross-Platform Tool Installation

- Installation instructions for UV, Python, and Quarto are designed to work
across Windows, macOS, and Linux systems, following each tool's official
documentation and installation guides
- Command-line verification methods (`--version` flags) provide standard
approaches for confirming successful installations across operating systems
- Documentation links provided (UV docs, Quarto docs, VS Code docs) offer
official troubleshooting resources maintained by tool creators

#### AI Tool Responsibility

- Responsible use of AI coding assistants is emphasized in academic literature
on AI ethics and educational guidelines from institutions implementing AI tools
in curricula
- The principle that users remain responsible for AI-generated content aligns
with emerging best practices in AI-assisted writing and coding, as outlined by
organizations like the ACM and IEEE

### Support for Week Two Slides Content

#### Python as Beginner-Friendly Programming Language

- Python's syntax is designed to be readable and intuitive, following the Zen of
Python principle "Readability counts" (PEP 20)
- Python consistently ranks as one of the top programming languages for
beginners according to IEEE Spectrum's annual programming language rankings
- The language's emphasis on clear, English-like syntax reduces cognitive load
for new programmers, as documented in educational research on programming
language design

#### Python Collections for Document Engineering

- Python's built-in collection types (strings, lists, tuples, dictionaries,
sets) provide comprehensive data structures for organizing document information
- String objects in Python are immutable sequences, making them safe for
storing document content that shouldn't be accidentally modified
- Lists provide mutable sequences ideal for document sections and chapters that
may change during editing
- Dictionaries implement hash tables for efficient key-value storage, perfect
for document metadata and properties
- Sets ensure unique elements, valuable for maintaining collections of document
keywords and tags without duplicates

#### Sequence, Selection, and Iteration in Programming

- These three fundamental programming concepts (sequence, selection, iteration)
form the theoretical foundation of structured programming, as defined by
computer science pioneers like Edsger Dijkstra
- Sequential execution ensures predictable program behavior, essential for
document processing workflows
- Conditional statements (selection) enable adaptive document formatting and
content generation based on different criteria
- Loops (iteration) facilitate processing of document collections and repetitive
text operations

#### Document Engineering Applications of Python Concepts

- Text processing functions like `word_frequency` and `document_summary`
demonstrate practical applications of Python for document analysis
- Containment checking operations (`in` operator) are fundamental for search
functionality in document management systems
- Collection slicing enables extraction of document sections and content
segments for analysis and manipulation
- String methods like `lower()`, `upper()`, and `title()` provide essential
text formatting capabilities for document standardization

#### Python Type System for Document Engineering

- Python's type hints (introduced in PEP 484) improve code readability and help
  catch errors in document processing functions
- Strong typing helps ensure data integrity when working with document metadata
  and content
- Type annotations serve as inline documentation, making code more maintainable
  for collaborative document engineering projects

### Support for Week Three Slides Content

#### Object-Oriented Programming for Document Engineering

- Object-oriented programming (OOP) is a fundamental paradigm in software engineering
  that models real-world entities as objects with properties and behaviors
- OOP principles (abstraction, inheritance, encapsulation, polymorphism) provide
  structured approaches to software design, as established in design patterns
  literature like the Gang of Four book "Design Patterns"
- Document engineering benefits from OOP by modeling documents, sections, and
  processing operations as objects with well-defined interfaces

#### Document Classes and Inheritance

- Class-based inheritance allows creation of specialized document types while
  maintaining shared functionality, following the Liskov Substitution Principle
- The `Document` base class encapsulates common document properties (title, author,
  content, metadata) following encapsulation principles
- Technical documents often require specialized attributes like complexity scoring
  and code examples, justifying inheritance hierarchies in document systems

#### Polymorphism in Document Processing

- Polymorphic interfaces enable uniform processing of different document types,
  supporting the Open/Closed Principle of software design
- Abstract base classes define contracts for document processors, ensuring
  consistent interfaces across different implementations
- Duck typing in Python allows flexible object interactions based on behavior
  rather than inheritance, supporting agile document processing architectures

#### Composition for Document Generation

- Composition over inheritance promotes flexible object assembly, as recommended
  in software design best practices
- Document generators composed of sections provide greater flexibility than
  rigid inheritance hierarchies
- The Strategy pattern (using composition) enables runtime selection of document
  generation strategies, supporting diverse output formats

#### OOP Principles Applied to Document Engineering

- Abstraction hides complexity of document operations, allowing users to work
  with high-level document objects rather than low-level file operations
- Encapsulation protects document state and ensures data integrity through
  controlled access methods
- Inheritance creates type hierarchies for different document categories while
  maintaining shared behavior
- Polymorphism enables extensible document processing systems that can handle
  new document types without modifying existing code

#### Interactive Code Examples

- Pyodide enables browser-based Python execution, providing immediate feedback
  for educational content
- Interactive examples reinforce learning through hands-on experimentation
- Real-time code execution helps students understand OOP concepts through
  practical application in document engineering scenarios

### Support for Week Two Skill-Check Slides Content

#### Document Engineering Skill-Check Assessment

- Skill-checks provide formative assessment opportunities that measure student
  progress in programming skills, following educational best practices for
  frequent, low-stakes testing
- Friday skill-checks create regular learning checkpoints that help students
  maintain consistent engagement with course material
- GitHub Classroom provides industry-standard workflow experience, mirroring
  professional software development practices that students will encounter
  in their careers

#### Automated Assessment with GatorGrade

- Automated testing and code quality checking reflects industry practices
  where continuous integration and automated testing are standard procedures
- The `gatorgrade` tool provides objective, consistent assessment criteria
  that ensure fairness across all student submissions
- Real-time feedback enables students to iteratively improve their solutions,
  supporting mastery-based learning approaches
- Pytest integration follows Python testing best practices and prepares
  students for professional development workflows

#### Git Version Control Workflow

- Regular commits and pushes reinforce version control best practices that
  are essential for collaborative software development
- Git workflow mirrors professional development environments where frequent
  commits and proper version control are critical skills
- GitHub Actions integration provides experience with automated testing
  pipelines common in modern software development

#### Programming Task Structure

- TODO markers and function stubs provide scaffolding that supports learning
  progression from novice to expert, following educational research on
  cognitive load theory
- Docstring-driven development encourages clear documentation practices
  essential for maintainable code
- Type annotations requirement reinforces modern Python best practices and
  helps prevent runtime errors

#### Honor Code and Academic Integrity

- Explicit honor code requirements establish ethical frameworks for academic
  work, particularly important when AI tools are available
- Citation requirements for AI assistance teach responsible use of emerging
  technologies in educational settings
- Individual assessment format ensures authentic demonstration of student
  learning and skill development

### Support for Week Four Slides Content

#### Markdown as Lightweight Markup Language

- Markdown was created by John Gruber in 2004 as a lightweight markup language
  designed to be easy to read and write in plain text form
- The CommonMark specification (2019) standardizes Markdown syntax to ensure
  consistency across different implementations and platforms
- GitHub Flavored Markdown (GFM) extends standard Markdown with features like
  tables, task lists, and syntax highlighting, making it the de facto standard
  for technical documentation

#### Markdown for Technical Documentation

- Stack Overflow Developer Survey consistently shows Markdown as one of the most
  loved markup languages among developers for its simplicity and readability
- Major platforms like GitHub, GitLab, Reddit, and Discord use Markdown for
  content creation, demonstrating its widespread adoption in technical communities
- README files in Markdown format are industry standard for project documentation,
  with GitHub automatically rendering README.md files as project homepages

#### Quarto as Publishing Platform

- Quarto is developed by Posit (formerly RStudio) and represents the evolution
  of scientific publishing tools, combining the best features of R Markdown,
  Jupyter notebooks, and modern web technologies
- The ability to execute code blocks in multiple languages (Python, R, Julia)
  makes Quarto suitable for reproducible research and technical documentation
- Quarto's support for multiple output formats (HTML, PDF, Word, presentations)
  follows the principle of single-source publishing used in professional
  technical writing

#### Document Engineering Workflow Applications

- Version control of documentation with Git follows software engineering best
  practices, enabling collaborative editing and change tracking for technical
  documents
- Automated documentation generation from code comments and Markdown source
  files is standard practice in software development, using tools like Sphinx,
  mkdocs, and Quarto
- The concept of "docs-as-code" treats documentation with the same rigor as
  source code, applying version control, review processes, and automated testing

#### Accessibility and SEO Benefits

- Alt text for images is required by Web Content Accessibility Guidelines (WCAG)
  2.1 Level AA, making content accessible to users with visual impairments
- Semantic HTML structure generated from Markdown headings improves search
  engine optimization (SEO) and document navigation
- Proper heading hierarchy (H1, H2, H3, H4) creates logical document structure
  essential for screen readers and automated content analysis

#### Mathematical Expression Support

- MathJax and KaTeX provide browser-based rendering of LaTeX mathematical
  notation, enabling complex mathematical expressions in web documents
- Mathematical markup in documentation is essential for technical fields like
  data science, engineering, and computer science algorithm documentation
- The example document quality formula demonstrates how mathematical concepts
  can be applied to evaluate documentation effectiveness

#### Interactive Code Execution

- Pyodide enables client-side Python execution in web browsers, providing
  immediate feedback for educational content without requiring server resources
- Interactive code examples improve learning outcomes by allowing students to
  experiment with code modifications and see immediate results
- Live code execution in documentation serves as both tutorial and testing
  mechanism, ensuring code examples remain functional and up-to-date

### Support for Week Six Slides Content

#### Quarto and Markdown for Document Engineering and Prosegramming
- Quarto is developed by Posit and is widely used for technical publishing, supporting reproducible research and professional documentation (see Quarto documentation).
- Markdown is the de facto standard for readable, plain-text documentation in software projects, with widespread adoption on platforms like GitHub, Stack Overflow, and Discord.
- Combining Quarto and Markdown enables prosegrammers to automate, analyze, and publish documentation that is clear, interactive, and professional (see Quarto and Markdown official docs).
- The "docs-as-code" approach treats documentation with the same rigor as source code, applying version control, review, and automated testing (see Sphinx, mkdocs, Quarto docs-as-code philosophy).
- Document engineering blends code and prose to create resources for both humans and machines, as supported by academic research in technical communication and computational linguistics.
- Mastery of Quarto and Markdown transforms coders into document engineers—prosegrammers who craft content that informs, inspires, and endures (see ACM/IEEE guidelines on technical documentation).

#### Software Testing for Document Engineering Tools

- Software testing principles apply directly to document processing systems,
  ensuring reliability and correctness in text analysis, parsing, and generation
- The IEEE Standard for Software Unit Testing (IEEE 829) provides established
  methodologies that adapt well to document processing validation
- Test-driven development practices help create robust document analysis
  functions by defining expected behavior before implementation

#### Document Analysis Testing Best Practices

- Testing document processing functions requires validation of text parsing,
  content extraction, and format conversion accuracy
- Edge cases in document processing include empty documents, malformed markup,
  encoding issues, and extremely large text files
- Automated testing frameworks like pytest enable systematic validation of
  document engineering tools across diverse input scenarios

#### Python Testing Ecosystem for Document Tools

- `pytest` provides parameterized testing capabilities ideal for testing
  document processing functions with varied input formats and content types
- `coverage.py` helps ensure comprehensive testing of document analysis code
  paths, critical for tools that process diverse document structures
- Property-based testing with `hypothesis` generates diverse text inputs to
  discover edge cases in document processing algorithms

#### Testing Integration with Document Workflows

- Continuous integration testing ensures document processing tools remain
  reliable as codebases evolve and new document formats are supported
- Mutation testing with tools like `mutmut` validates test suite quality by
  introducing controlled defects to verify test detection capabilities
- Performance testing of document processing tools helps identify bottlenecks
  in text analysis and generation pipelines
