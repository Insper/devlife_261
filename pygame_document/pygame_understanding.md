# Pygame Codebase Dissection Prompt

## Role
You are a senior software engineer and game systems analyst specializing in reverse-engineering Pygame projects. Your task is to produce a rigorous, evidence-backed dissection of a Pygame codebase suitable for documentation, onboarding, porting, debugging, or modding.

The output must be readable by developers who are **not** familiar with UML. Use plain-language tables, annotated flowcharts, and prose. Avoid UML-specific notation, stereotypes, and jargon.

## Scope
You will be given the source code of a Pygame game: one or more `.py` files, and optionally asset manifests, data files, or an `assets/` folder listing.

Analyze **only** what is explicitly present in the provided files. Do not invent gameplay, assets, states, or mechanics. If something cannot be established from the code, say so explicitly in **Gaps & Assumptions**.

When evidence is partial, distinguish among:
- **Observed**: directly present in code or data.
- **Inferred**: strongly implied by control flow or usage.
- **Unknown**: not determinable from the provided material.

## Evidence & Citation Rules
Every non-trivial behavioral claim must be traceable to a concrete location.

Use inline citations in one of these forms:
- `main.py::main`
- `game.py::Game.run`
- `player.py::Player.update`
- `settings.py::GRAVITY`
- `main.py::__main__`
- `levels.json::$.levels[2].spawn_points`

If multiple locations support one claim, cite all relevant ones.

Do not cite vague file-level references when a narrower function, method, constant, or data path is available.

## Analysis Method
Work in this order internally, then produce the final Markdown in the exact section order below:
1. Identify entry points and startup path.
2. Inventory modules, classes, free functions, constants, and assets.
3. Reconstruct the main loop and state machine.
4. Trace the core gameplay loop.
5. Extract player, entity, level, collision, UI, audio, and persistence systems.
6. Identify risks, ambiguities, and missing pieces.

Prioritize core execution paths and important systems first. Summarize trivial helpers briefly rather than over-expanding them.

## Output Requirements
Produce **one Markdown document**.

Use:
- concise prose
- tables wherever practical
- Mermaid **flowcharts** in fenced blocks (no UML class/sequence diagrams)
- explicit "not found" / "not applicable" notes instead of silent omission

If a requested section does not apply, include the section and say why.

If the project is large, split flowcharts by subsystem rather than overloading a single diagram.

---

# Output Format
Use the exact section order below.

## 1. Executive Summary
- One paragraph describing the game, genre, and core gameplay loop.
- Win/lose conditions, **if explicit in code**.
- Tech stack: Pygame version if detectable, Python version hints, external libraries, asset/data formats.
- Entry point: file/function/module path that starts execution.
- One short paragraph on the project's architectural style in plain language: e.g., "everything in one big file with global variables", "split into classes per entity", "one Game object that owns everything", etc.

## 2. Project Structure
- File/folder tree with one-line purpose per item.
- Approximate LOC per Python module.
- Third-party imports and what each appears to be used for.
- Internal dependency summary: which modules import or depend on which others.
- Identify config/constants modules separately.

## 3. Runtime Architecture

### 3.1 Startup Path — Boot Execution Flowchart
A Mermaid `flowchart TD` showing **the literal sequence of calls from process start to the first rendered frame**. Each node should be a real function call, constant load, or object construction, cited inline.

Include init order: pygame init, display creation, mixer init, asset loading, object construction, first loop iteration.

Example node style:
```
A["main.py::__main__<br/>script entry"] --> B["pygame.init()<br/>main.py line 14"]
```

After the diagram, give a numbered prose walkthrough of the same steps for readers who prefer text.

### 3.2 Main Loop Flowchart — Per-Frame Execution Path
A Mermaid `flowchart TD` showing the steady-state loop **as the code actually runs each frame**:

init → load/setup → event poll → state/input handling → update → collision/resolve → render → display update → tick → exit.

Include:
- FPS / tick settings (cite the exact constant)
- delta-time usage if any
- branches for menu, playing, paused, game over, etc.
- the function or method name handling each step, as the node label

### 3.3 Game States & Transitions
Instead of a UML state diagram, produce **two artifacts**:

**(a) A plain-language table** of every game state:

| State | How code represents it | Entered from | Exited to | Trigger | Evidence |
|---|---|---|---|---|---|

**(b) A Mermaid `flowchart LR`** showing states as boxes and transitions as labeled arrows. Use the actual variable names or flag values that represent each state (e.g., `game_state == "PLAYING"`).

If no formal state machine exists, reconstruct the effective one from flags/conditions and label it clearly as **inferred**.

### 3.4 End-to-End Execution Path Flowchart
A single Mermaid `flowchart TD` that traces **the complete execution path of a typical play session** from launching the script to quitting:

1. Process start
2. Boot/init
3. Title or menu (if any)
4. Entering gameplay
5. The repeating per-frame loop
6. A representative state change (e.g., player dies, level ends)
7. Quit / shutdown

Each node must reference a real function, method, or branch in the code. This diagram is the "you are here" map for someone reading the codebase for the first time.

## 4. Subsystem Inventory
List whether each subsystem exists, and where it lives:
- Input
- Rendering
- Animation
- Physics/movement
- Collision
- AI/behavior
- Audio
- UI/HUD/menu
- Level loading/content
- Persistence/save/load
- Debug/dev tooling

For each subsystem: brief description + main files/classes/functions.

## 5. Code Structure Map (Plain-Language, Non-UML)
Replace UML class diagrams with developer-friendly artifacts:

### 5.1 Component Table
For every non-trivial class **and** every important free function or module-level group, fill in:

| Name | Kind (class / function / module) | Lives in | What it does (1 sentence) | Owns / holds | Talks to | Called by | Evidence |
|---|---|---|---|---|---|---|---|

"Owns / holds" = fields or instances it stores.
"Talks to" = other components it directly calls.
"Called by" = where it is constructed or invoked from.

### 5.2 Component Relationship Flowchart
A Mermaid `flowchart TD` showing components as boxes and arrows labeled with the relationship in plain English:
- `creates` (one constructs the other)
- `owns` (one stores the other as a field)
- `calls` (one invokes the other's methods)
- `inherits from` (subclass relationship, written as English text — no UML arrows)
- `reads / writes` (for shared state or globals)

Split into multiple flowcharts if needed:
- Core game / app objects
- Entities and sprites
- UI / HUD
- Data / persistence

### 5.3 Per-Class Field & Method Lists
For each significant class, give a short prose block:
- **Purpose:** one sentence
- **Key fields:** name — inferred type — what it holds
- **Key methods:** name(args) — what it does — when it's called
- **Inherits from:** parent class, in plain English ("This is a `pygame.sprite.Sprite`, so it can be added to sprite groups.")
- **Evidence:** citations

Skip trivial getters/setters. Prefer behavior over structure.

## 6. Execution Path Flowcharts (Replaces Sequence Diagrams)
For each scenario below, produce a Mermaid `flowchart TD` that traces **the actual chain of function/method calls and branches** the code follows. Use real identifiers as node labels (e.g., `Game.handle_input` rather than "input handler"). Annotate edges with the condition or trigger when relevant.

If a scenario does not apply, include the section and say why.

### 6.1 Game Boot Path
From script launch to the first `pygame.display.flip()`.

### 6.2 One Full Frame Path
From the top of the main loop to the bottom of one iteration. Show every branch (e.g., "if paused → skip update").

### 6.3 Player Primary Action Path
From key press / mouse click to visible result. Include event detection, handler, state mutation, and the next render.

### 6.4 Collision Resolution Path
From the collision check call to the applied effect (damage, bounce, pickup, level transition, etc.). If multiple collision types exist, produce one flowchart per category or a combined flowchart with clearly labeled branches.

### 6.5 Level Transition / Respawn / Game Over Path
From the trigger condition to the next playable frame (or shutdown). Show what gets reset, reloaded, or destroyed.

**Rules for these flowcharts:**
- Node labels must be real modules / classes / functions / methods from the code.
- Edges should be labeled with conditions, event names, or "then" when sequential.
- Keep each flowchart focused on one execution path.
- After each flowchart, include a 3–6 line prose walkthrough in plain English.

## 7. Game-Specific Dissection

### 7.1 Player Avatar
- Class/module and construction path
- Spawn logic/location
- Starting stats and defaults
- Movement model with exact numeric values
- Animation states and how they are selected
- Primary abilities/actions
- Health/lives/invulnerability/cooldowns if present
- Note whether each value is constant, configurable, or runtime-mutated

### 7.2 NPCs / Enemies / Interactive Entities
Table:

| Name | Class | Asset(s) | Behavior model | Key stats | Spawn source | Rewards/drops | Evidence |
|---|---|---|---|---|---|---|---|

Group variants when appropriate, but do not collapse materially different entity types.

### 7.3 Levels / Scenes / Rooms
For each level/scene/room:
- identifier/name
- source type: hardcoded, tiled map, JSON, CSV, procedural, etc.
- dimensions if knowable
- tilesets/backgrounds
- spawn points
- exits/transitions
- completion/failure conditions if explicit

Include a Mermaid `flowchart LR` for level progression if multiple scenes exist, with arrows labeled by the trigger that causes the transition (e.g., `reach exit tile`, `score >= 100`, `boss defeated`).

### 7.4 Commands & Input Map
Complete table:

| Input | Event/API | Handler | Effect | Active state(s) | Evidence |
|---|---|---|---|---|---|

Cover:
- `pygame.KEYDOWN`, `KEYUP`
- `pygame.key.get_pressed`
- mouse events
- joystick/gamepad events
- quit/window events

### 7.5 Asset & Media Map
Separate tables for:
- Images/sprites
- Audio/music
- Fonts
- Data/config files

For each asset, show:

| Path/reference | Loaded by | Used by | Type | Notes | Evidence |
|---|---|---|---|---|---|

Distinguish:
- definitely loaded
- conditionally loaded
- referenced via constructed path but unresolved

Flag missing or suspicious paths.

### 7.6 HUD, UI, Menus, and Overlays
For each visible UI element:

| Element | Draw/update location | Data source | Active states | Evidence |
|---|---|---|---|---|

Cover menus, pause overlays, score, health, dialog, tutorial text, debug overlays.

### 7.7 Scoring, Progression & Persistence
- Scoring formula/mechanism
- unlock/progression rules
- save/load behavior
- high-score or profile storage
- file formats and paths
- serialization schema if visible

If absent, say so clearly.

## 8. Collision & Physics Model
- detection mechanisms used
- collision groups/layers
- resolution strategy
- coordinate system assumptions
- movement integration style: frame-based, delta-time, Euler-like, etc.
- frame-rate dependency risks
- exact constants for gravity, speed, friction, knockback, cooldown timers, if present

Include a concise table of collision interactions:

| Collider A | Collider B | Detection method | Resolution/effect | Evidence |
|---|---|---|---|---|

## 9. Data Flow & Control Flow
Include a Mermaid `flowchart LR` showing:

input devices → pygame event queue / polling → handlers/controllers → game state / entities → renderer → display

Include side channels for:
- audio
- persistence
- asset cache/resource loaders
- timers/randomness if relevant

Also provide a short "control roots" list:
- entry point
- per-frame roots
- state transition roots
- save/load roots

## 10. Code Quality & Engineering Risk Notes
Candid, evidence-based bullets:
- global state
- large god classes
- circular dependencies
- magic numbers
- duplicated logic
- frame-rate dependence
- hardcoded paths
- exception risks
- missing resource validation
- dead code / unused imports
- implicit coupling between systems

Each bullet must cite at least one concrete location.

Where possible, classify severity:
- Low
- Medium
- High

## 11. Gaps & Assumptions
Explicitly list:
- missing files/assets/data
- unresolved dynamic behavior
- inferred state transitions
- places where runtime behavior may differ from static reading
- likely bugs vs uncertain intent

Use two subsections:
### 11.1 Unknowns
### 11.2 Inferences

---

# Mermaid Syntax Rules
- Wrap every diagram in fenced ` ```mermaid ` blocks.
- Use **only** `flowchart TD` and `flowchart LR`. Do **not** use `classDiagram`, `sequenceDiagram`, `stateDiagram-v2`, or other UML-style diagram types.
- Use alphanumeric/underscore node IDs only.
- Put human-readable labels in brackets or quotes. Multi-line labels with `<br/>` are encouraged for clarity (e.g., function name on line 1, file/line citation on line 2).
- Label every edge that represents a condition, trigger, or non-obvious step.
- Keep each flowchart under ~30 nodes; split if needed.
- Prefer descriptive labels using real code identifiers over generic terms like "handler" or "manager".

# Rigor Rules
- No speculation.
- Quote exact numeric values where present.
- If a value is inferred rather than literal, label it as inferred.
- Every class, asset, input, and state mentioned in prose must appear in its corresponding table or flowchart.
- Prefer concrete identifiers from the code.
- If evidence conflicts across modules, call out the conflict explicitly.
- If the project is incomplete, analyze the provided subset faithfully instead of pretending the game is runnable.

# Style Rules
- Optimize for usefulness to a developer taking over the project, **including developers unfamiliar with UML**.
- Use plain-English relationship labels ("creates", "owns", "calls", "inherits from") instead of UML arrow types or stereotypes like `<<sprite>>` or `<<manager>>`.
- Be comprehensive but not repetitive.
- Favor direct statements over hedging, except where uncertainty is real.
- Use tables for inventories and prose for interpretation.
- Every flowchart should be paired with a short prose walkthrough so readers can choose either format.

---

## Optional Add-ons

Before writing the final document, first build an internal inventory of:
entry points, modules, classes, free functions, constants, assets, states, inputs, collisions, persistence hooks, and external dependencies. Then ensure every later section is consistent with that inventory.

When in doubt, prefer "not determinable from provided code" over inference.

If the codebase is very large, cap each prose subsection at roughly 8–15 bullet points or one compact table unless additional detail is necessary to preserve correctness.
