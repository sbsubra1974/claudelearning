# 4 entry points - Chat[only as tab on Windows Pro]/Code/Artifacts[for both tabs only on Windows Pro
# (i.e (Cloud-Based only))]/Research[Windows Pro only: Chat tab via "+", Code tab via built-in
# /anthropic-skills:deep-research command]
# Running Claude Code from Claude.ai Projects folder (Cloud-Based)[as tab on Windows Pro]: 
#   - No Direct Execution: Cannot run local terminal commands, execute build scripts, or modify files 
#     directly on your machine
#   - Limited Scope: Best for high-level brainstorming, writing documentation, drafting code snippets, 
#     or querying static design specs rather than multi-file refactoring
# Running Claude Code from a VS Code project folder[as an extension on VS Code]:
#   - Local Access: Runs directly inside your local repository, either via the Claude Code VS Code 
#   Extension or the terminal CLI.
#   - File Operations: Can read, create, edit, and delete files directly across your entire codebase.
#   - Execution & Commands: Can run shell commands, tests, build scripts, and local development servers.
#   - Project Structure: Utilizes local configuration files like CLAUDE.md, .mcp.json, and 
#     .claude/ directories to anchor custom rules, skills, and context. 

# 3 features extending Claude's default text-generation behavior - 
#   Skills for consistent procedures, 
#   Code Execution for verified computation, and 
#   Memory for continuity across sessions.
#   Q: How is memory.md of windows pro->code tab->Projects->Code sample project getting updated
#   with actions taken on https://github.com/sbsubra1974/claudelearning [CCode as an extension on VSCode]?
#   A: <>

# 4 layer capability layer - 
#   projects carry context,
#   skills define repeatable procedures,
#   code execution verifies computations,
#   memory persists continuity

#   The capability layer determines what Claude does:
#   standing instructions, knowledge base, Skill, or Code Execution
#   Capability layer handles tools, file-system access, bash execution, or 
#   specialized extensions like Skills. Capability layer includes local file scrapers, 
#   MCP servers, or code-execution sandboxes
# Q: "One-off drafting task; no capability layer needed"- what does it mean?
# Q: If capability layer is optional in Claude why so? And when?
# A: In Claude (such as Claude Code and agent architectures), the capability layer is optional because 
# the core language model can function purely as a text-based reasoning engine

#   The most common mix-up is standing instructions versus knowledge base. 
#   Standing instructions are behavioral directives, while knowledge base is reference material. 
#   Ask of each: is this telling Claude what to do, or what to know? Both live in the Project, 
#   but they serve different functions.

# If speed and volume are the primary requirements and the task is structured, then consider Haiku.
# If quality is falling short for a complex task, upgrade to Opus
# Sonnet handles the full range of professional tasks with strong quality across task types: drafting, 
# synthesis, analysis, research assistance, and document review. For most knowledge-worker work, 
# Sonnet is the right starting point
# Refer: ModelsSelectionCards.png

# speed-versus-capability trade-off also becomes a per-call cost trade-off:
# A higher-capability tier such as Opus consumes *more usage per call* than Haiku or Sonnet, so on those 
# plans *"efficiency" means cost as well as speed*. 
# On the standard claude.ai subscription surface, *treat efficiency (speed and usage headroom) as the 
# practical proxy for cost*.
# Ex: nuanced interpretation of ambiguous signals where the quality ceiling matters more than turnaround, 
# Opus buys depth of reasoning at the cost of speed, and for a one-off, high-stakes deliverable that 
# trade is worth making. Sonnet would be the right call if the same analysis were routine or time-critical 
# rather than high-stakes; Haiku would under-resource the interpretation the task demands.

# Model selection and capability configuration determine what Claude can do in a session. 
# Context management determines how long it can do it well.
# In practical terms: a long session where you gave Claude detailed instructions in the first 10 minutes 
# may produce responses 90 minutes later that don't follow those instructions, not because Claude is 
# ignoring them, but because detail can compress when earlier context is summarized.

# These selection decisions are applied together:
# Entry point, capability layer, model tier, and context strategy are four related choices made for the 
# *same task*.

# Project-scoped Memory keeps Memory contexts separate per Project. Separate client Projects with 
# Project-scoped Memory is the correct configuration.

# Module 2: Prompting & Task Execution
# Description: The competency of telling Claude precisely what you want. It is the habit of making each 
# prompt component explicit instead of assuming Claude will infer it. 
# Task: Primary verb stated unambiguously

# Prompt component stack: Role, Context, Task, Constraints, Output Format
# Not every prompt needs all five: The skill is noticing which components a given task requires
# Missing context produces generic output. An ambiguous task verb produces the wrong action. 
# Absent constraints produce output that is the wrong length or tone. 
# Analysis wants constraints; brainstorming wants latitude
# The most common slips are placing the code execution instruction under Task instead of Constraints.
# and dragging the "professional and polished" fragment such as "Make the summary sound professional and
# polished" into a real component. 

# Decomposition means splitting a multi-part problem into discrete, ordered steps, then running them in 
# sequence rather than asking for everything at once.

# One conversation or several: Keep sequential steps that build on each other in one conversation, so each 
# step sees the prior results. Move to a separate conversation when a step is genuinely independent, or 
# when the conversation has grown long enough that early context is degrading.
# Refer: OutputDeficienciesVsPromptDiagnostics.png

# The 4 task types:
# Analysis, research, drafting, and brainstorming
# Analysis wants constraints; brainstorming wants latitudes
# Refer: OutputDeficienciesVsPromptDiagnostics.png

