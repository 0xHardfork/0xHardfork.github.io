---
name: rust-learning
description: Daily Rust learning skill that generates a focused topic with concept explanation, code examples, and practice exercises. 25-day curriculum from basics to advanced, async, and project tools. Tracks learning history in history.yaml.
---

# Rust Daily Learning Skill

This skill helps you learn Rust one topic per day, following a 25-day intensive curriculum from basic syntax to advanced concepts like Concurrency, Unsafe Rust, Async/Tokio, Tooling, Ecosystem crates (Serde, Anyhow, Clap), and a Capstone project.

## When to Use This Skill

- User says **"开始今日rust任务"** (start today's rust task)
- User says **"start today's rust task"** or **"start daily rust task"**
- User says **"begin daily rust practice"** or **"rust today"**
- User wants to continue their daily Rust learning routine

## Workflow

### Step 1 — Read History

Before generating any content:

1. Read `history.yaml` from the skill directory (`.agent/skills/rust-learning/history.yaml`)
2. Extract the list of all **previously covered topics** (the `topic_key` field of each entry)
3. Also note the most recent entry's date so you can inform the user of their streak

If `history.yaml` does not exist yet, treat the history as **empty** and create the file after the session.

### Step 2 — Select Today's Topic

Pick **one topic** from the curriculum below that:

- Has **NOT** appeared in `history.yaml`
- Is appropriate as the **next step** given what topics have already been covered (prefer sequential/progressive ordering)
- If all topics in a category are covered, move to the next category

**Topic Curriculum (ordered by progression):**

#### The 25-Day Zero to Mastery Curriculum
| topic_key | Title | Description |
|-----------|-------|-------------|
| **Phase 1: Basic Syntax & Core (0x01 - 0x05)** | | |
| `day1_fundamentals` | 0x01: Rust Fundamentals | Variables, Mutability, Data Types, Functions, and Control Flow. |
| `day2_ownership_borrowing` | 0x02: Ownership & Borrowing | Core concept: Ownership rules, references, borrowing, and slices. |
| `day3_pattern_matching` | 0x03: Pattern Matching Deep Dive | `enum`, `match`, `if let`, `while let`, match guards, and destructuring. |
| `day4_structs_methods` | 0x04: Structs & Methods | Custom types, associated functions, methods (`&self`, `&mut self`). |
| `day5_modules_cargo` | 0x05: Project Management & Toolchain | Modules, Crates, Paths, Cargo (`cargo test`, `cargo clippy`, `rustfmt`). |
| **Phase 2: Standard Library & Idioms (0x06 - 0x0B)** | | |
| `day6_collections` | 0x06: Common Collections | Vector (`Vec<T>`), String vs `&str`, and `HashMap`. |
| `day7_error_handling_std` | 0x07: Error Handling Basics | Recoverable errors (`Result`), unrecoverable (`panic!`), the `?` operator. |
| `day8_error_handling_ecosystem`| 0x08: Error Ecosystem | Using `anyhow` for applications and `thiserror` for libraries. Error propagation. |
| `day9_generics_traits` | 0x09: Generics & Traits | Defining generic types, defining shared behavior with Traits, trait bounds. |
| `day10_lifetimes` | 0x0A: Lifetimes | Validating references with lifetimes, lifetime annotations in functions/structs. |
| `day11_closures_iterators` | 0x0B: Closures & Iterator Pipelines | Functional style: iterators, `map`, `filter`, `collect`, and closure capture rules. |
| **Phase 3: Advanced Memory & Concurrency (0x0C - 0x10)** | | |
| `day12_smart_pointers_1` | 0x0C: Smart Pointers (Part 1) | `Box<T>`, `Deref` trait, `Drop` trait, and heap allocation. |
| `day13_smart_pointers_2` | 0x0D: Smart Pointers (Part 2) | `Rc<T>`, `RefCell<T>`, Interior Mutability, and memory leaks. |
| `day14_concurrency_threads` | 0x0E: Concurrency (Threads & Channels) | Spawning threads, message passing via `mpsc`, `Sync` and `Send`. |
| `day15_concurrency_state` | 0x0F: Concurrency (Shared State) | `Mutex`, `RwLock`, `Arc`, Atomic operations, and thread safety. |
| `day16_testing_docs` | 0x10: Testing & Documentation | Unit tests, Integration tests, Doc tests, and benchmarking (`#[bench]`). |
| **Phase 4: Ecosystem & Async (0x11 - 0x16)** | | |
| `day17_serde_io` | 0x11: Serde & File I/O | Reading/Writing files (`std::fs`), Parsing JSON/YAML with `serde` and `serde_json`. |
| `day18_macros_ffi` | 0x12: Macros & Unsafe FFI | Declarative macros (`macro_rules!`), Unsafe Rust basics, calling C code. |
| `day19_async_futures` | 0x13: Async Rust (Futures & Pin) | How `async`/`await` works under the hood. The `Future` trait and `Pin`. |
| `day20_async_tokio_1` | 0x14: Async Rust (Tokio Basics) | Tokio runtime, spawning tasks, async I/O, `tokio::spawn`. |
| `day21_async_tokio_2` | 0x15: Async Rust (Tokio Advanced) | Tokio Mutex vs Std Mutex, `tokio::select!`, managing task cancellation. |
| `day22_cli_clap` | 0x16: Building CLIs with Clap | Using `clap` (derive API) for command-line argument parsing. |
| **Phase 5: Capstone Project (0x17 - 0x19)** | | |
| `day23_project_design` | 0x17: Capstone - Project Setup | Project structure (`src/bin`, `src/lib`, `error.rs`), CI/CD basic thoughts. |
| `day24_project_impl_1` | 0x18: Capstone - Core Logic | Implementing a concurrent file/network scanner (combining Clap, Serde, Tokio). |
| `day25_project_impl_2` | 0x19: Capstone - Polish | Adding logging (`tracing` / `env_logger`), finalizing error handling, compiling release. |

### Step 3 — Generate the Daily Learning Session

Generate a full, structured learning session directly inside the **`pages/development/rust/`** directory.

**Naming convention**: Use `YYYY-MM-DD_rust{NN}.md` where NN is a 2-digit sequence (usually 01 for the first topic of the day).
**File path**: `pages/development/rust/YYYY-MM-DD_rust01.md`  

---

#### Output Format

**IMPORTANT — Jekyll Front-matter**:
Every generated `.md` file MUST begin with Jekyll front-matter so the page renders correctly on the GitHub Pages site:

```markdown
---
layout: default
title: "{Title}"
---

# Rust

## 🧠 Concept Overview

[Clear, concise, and in-depth explanation of the concepts. Be precise about memory layout and ownership semantics.]

---

## 🔑 Key Points

- [Key point 1]
- [Key point 2]
- [Key point 3]

---

## 💻 Code Examples

### Example 1 — {Descriptive title}

\`\`\`rust
// File: main.rs
fn main() {
    // Clear, well-commented code
}
\`\`\`

**What this demonstrates**: [1–2 sentence explanation of the example]

### Example 2 — {Descriptive title}

\`\`\`rust
// File: main.rs
fn main() {
    // A slightly more complex or realistic example
}
\`\`\`

**What this demonstrates**: [1–2 sentence explanation]

---

## ⚠️ Common Mistakes

| Mistake | Why it's wrong | Correct approach |
|---------|---------------|-----------------|
| [mistake 1] | [reason] | [fix] |
| [mistake 2] | [reason] | [fix] |

---

## 🏋️ Practice Exercises

### Exercise 1 — {Title} (Easy)

**Goal**: [Clear description of what to implement]

**Requirements**:
- [Requirement 1]
- [Requirement 2]

**Starter code**:

\`\`\`rust
fn main() {
    // TODO: Complete the implementation
}
\`\`\`

**Hint**: [A subtle hint]

---

### Exercise 2 — {Title} (Medium)

**Goal**: [Clear description]

**Requirements**:
- [Requirement 1]
- [Requirement 2]

**Starter code**:

\`\`\`rust
fn main() {
    // TODO: Complete the implementation
}
\`\`\`

**Hint**: [A subtle hint]

---

### Exercise 3 — {Title} (Hard / Challenge)

**Goal**: [A more realistic, real-world scenario]

**Requirements**:
- [Requirement 1]
- [Requirement 2]

**Starter code**:

\`\`\`rust
fn main() {
    // TODO: Complete the implementation
}
\`\`\`

**Hint**: [A subtle hint pointing toward the right approach]

---

## 📖 Reference & Further Reading

- [The Rust Programming Language: {relevant chapter}]({url})
- [Rust by Example: {topic}](https://doc.rust-lang.org/rust-by-example/{topic}.html)

---

## 🗒️ Quick Cheat Sheet

\`\`\`rust
// One-liner reference for today's topic — the most important syntax
\`\`\`

---

[← back to rust](./) | [← back to development](..) | [← back to home](/)
```

### Step 4 — Update history.yaml

After generating the session file, **append** a new entry to `history.yaml`:

```yaml
# Example structure of history.yaml
- date: "2026-03-08"
  topic_key: "day1_fundamentals"
  title: "0x01: Rust Fundamentals"
  category: "Zero to Mastery"
  file: "pages/development/rust/2026-03-08_rust01.md"
```

**Rules**:
- Always append; never overwrite existing entries
- If `history.yaml` does not exist, create it with proper YAML formatting
- Use `"YYYY-MM-DD"` date string format (quoted for YAML safety)

### Step 5 — Confirm to the User

After generating the file and updating history, tell the user:

1. **Today's topic**: The title and category
2. **File created**: The path to the session file
3. **Progress**: How many topics have been covered so far (e.g., "1 / 25 topics completed")
4. **Streak reminder**: The date of their last session
5. **Quick start**: Suggest they open the file and start with the Concept Overview, then try the exercises

## Content Quality Guidelines

### Concept Explanations
- Be clear and precise about **Rust semantics**, ownership, borrowing, and lifetimes.
- Highlight common pain points (like fighting the borrow checker) and how to overcome them.
- Use professional terminology.

### Code Examples
- All code must be **complete and runnable** (`fn main()`, proper imports with `use`)
- Comment code heavily to explain *why* something compiles or why it doesn't.
- Show both the wrong way (that the compiler rejects) and the right way where applicable.

### Exercises
- Progressive difficulty from basic syntax application to slightly tricky ownership/borrowing scenarios.
- Require compiling and running simple tests or assertions if applicable.

### Progression
- Always check `history.yaml` first — **never repeat a topic**
- Follow the 25-day curriculum order.

## File Organization

```
# Skill files
.agent/skills/rust-learning/
├── SKILL.md              ← This file
└── history.yaml          ← Auto-managed learning history

# Generated articles go here (GitHub Pages site)
pages/development/rust/
├── index.md                            # Directory index (auto-lists articles)
├── YYYY-MM-DD_rust01.md               # Session file for that day
└── ...
```

## Error Handling

- If `history.yaml` is not parseable, warn the user and start with an empty history
- If all 25 topics are covered, congratulate the user and offer to generate custom real-world projects or advanced crate deep-dives (e.g., Actix/Axum, advanced Serde tricks).
- If the user requests a specific topic (even if already covered), generate it but note it was covered before.
