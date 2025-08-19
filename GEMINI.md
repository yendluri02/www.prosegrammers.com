# Gemini-Related Project Instructions

This document provides instructions for the Gemini AI assistant to follow when
working on this Quarto-based website project.

## General Principles

- Adhere to standard Markdown and Quarto conventions in all `.qmd` files.
- Maintain the existing style and structure of the website.
- Ensure that all new content is appropriately linked from existing pages if necessary.

## Editing and Creating Content

### Editing Existing Content

1.  Locate the relevant `.qmd` file for the page that requires editing (e.g.,
    `syllabus/index.qmd` for the syllabus).
2.  Make the necessary changes to the text, code, or other content within the
    file.
3.  After making changes, preview the site to ensure the changes are rendered
    correctly.

### Adding New Content (e.g., Assignment Descriptions)

1.  Create a new `.qmd` file in the appropriate directory (e.g., a new
    subdirectory in `schedule/`).
2.  Add the content to the new file using Markdown.
3.  If the new page should appear in the site navigation, add a link to it in
    the `navbar` section of the `_quarto.yml` file.
4.  Preview the site to verify that the new page is accessible and renders
    correctly.

## Creating Slides

Slides for this project are created using Quarto and reveal.js.

1.  Create a new `.qmd` file for the slide deck (e.g., in the `slides/` directory).
2.  Add the following YAML header to the top of the file to specify the `revealjs` format:
    ```yaml
    ---
    title: "Your Slide Title"
    format: revealjs
    ---
    ```
3.  Use Markdown headings to create slides. A level 2 heading (`##`) creates a new slide.
4.  Add content (text, images, code blocks) to each slide.
5.  Preview the site to see the rendered slides.

## Verification

Before committing any changes, it is crucial to verify that the site builds
correctly and that there are no issues with the content.

### Checking for Problems

Run the following command to check the project for common issues:

```bash
quarto check
```

This command will check for broken links, missing resources, and other potential problems.

### Previewing the Site

To preview the entire website locally, run the following command:

```bash
quarto preview
```

This will start a local web server and open the site in a browser. The site will
automatically reload when you make changes to the source files.

## Deployment

The site is automatically deployed to Netlify when changes are pushed to the `main` branch, as configured in the `.github/workflows/publish.yml` file.

To manually deploy the site, you can run the following command. Note that this requires having the `NETLIFY_AUTH_TOKEN` environment variable configured correctly.

```bash
quarto publish netlify
```
