---
theme: default
background: https://cover.sli.dev
title: VS Code 101 - Your Modern Development Companion
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# VS Code 101

Your Modern Development Companion

<div class="abs-br m-6 text-xl">
  <a href="https://github.com/AI-in-Practice-UOS/course-material" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

---
layout: image-right
image: https://thecodinglove.com/content/043/vi_visual_studio_code.jpg
backgroundSize: contain
---

# Why VS Code?
There are lot of options when it comes to code editors, but we chose VS Code for the following reasons:

- Free
- Customizable
- Extensions
- GitHub Copilot
- Not as opinionated as an IDE

---
transition: fade-out
---

# What are we going to do?

Learn how to quickly setup and use VS Code to maximize your coding efficiency

- **Environment setup** - Install VS Code + useful tools and extensions
- **Navigation** - How to quickly navigate the workspace
- **Refactoring** - How to restructure or change your code more robustly
- **Debugging** - How to run and debug your code from VS Code
- **Github Copilot** - Automatic code generation integrated in VS Code
<br>
<br>

So let's start with the installation!

---
layout: intro
---

# Installation

- Prerequisites: [git](https://git-scm.com/downloads)
- Download: [VS Code Download page](https://code.visualstudio.com/Download)

---

# Extensions

VS Code has an enormous extension system for LSP setup, formatting, linting and much more.<br> In this course we will need the following, but feel free to install whatever additional extensions you need:

- LSP Extension: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Formatting + Linting: [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- AI Code Generation: [Github Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

---
layout: center
---


Use an extensions.json file to inform codebase users what extensions might be useful: 


```json
// .vscode/extensions.json
{
  "recommendations": ["ms-python.python", "charliermarsh.ruff"]
}
```
---
layout: center
---

Use a settings.json file to configure the editor:

```json {all|4,5|6-9}
// .vscode/settings.json
{
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        }
    }
}
```

---
layout: intro
---

# Keyboard shortcuts

[Full reference](https://code.visualstudio.com/docs/reference/default-keybindings)


---

# Navigation

Use keyboard shortcuts to quickly navigate the workspace
| Shortcut         | Description         |
|------------------|---------------------|
| `Ctrl/Cmd + P`   | Quick Open          |
| `Ctrl/Cmd + Shift + P` | Command Palette |
| `Ctrl/Cmd + W`   | Close Current File  |
| `Ctrl/Cmd + B`   | Toggle Sidebar      |
| `Ctrl/Cmd + J`   | Toggle Terminal     |

---
layout: image-right
image: https://programmerhumor.io/wp-content/uploads/2022/04/programmerhumor-io-debugging-memes-programming-memes-f9cbf4082867882.jpg
backgroundSize: contain
---

# Debugging

There are many different ways on how to debug your code, but we will focus on the debugging capabilities of VS code

- How to use breakpoints
- Inspect variable values

---

# Code Debugging

Use these keyboard shortcuts to run and debug your code

| Shortcut | Description |
|----------|-------------|
| `F5` | Start Debugging |
| `⇧ + F5` | Stop Debugging |
| `⌥ + F5` | Run Without Debugging |
| `F9` | Toggle Breakpoint |
| `F10` | Step Over |
| `F11` | Step Into |
| `⇧ + F11` | Step Out |