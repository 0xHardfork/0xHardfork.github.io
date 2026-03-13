---
name: golang-learning
description: Daily Golang learning skill that generates a focused topic with concept explanation, code examples, and practice exercises. Use when user says "开始今日任务", "start today's task", "start daily task", or any equivalent. Tracks learning history in history.yaml to avoid repeating topics.
---

# Golang Daily Learning Skill

This skill helps you learn Go (Golang) one topic per day. Each session covers a single concept with a clear explanation, runnable code examples, and hands-on exercises.

## When to Use This Skill

- User says **"开始今日golang任务"** (start today's golang task)
- User says **"start today's golang task"** or **"start daily golang task"**
- User says **"begin daily golang practice"** or **"golang today"**
- User wants to continue their daily Go learning routine

## Workflow

### Step 1 — Read History

Before generating any content:

1. Read `history.yaml` from the skill directory (`.agent/skills/golang-learning/history.yaml`)
2. Extract the list of all **previously covered topics** (the `topic_key` field of each entry)
3. Also note the most recent entry's date so you can inform the user of their streak

If `history.yaml` does not exist yet, treat the history as **empty** and create the file after the session.

### Step 2 — Select Today's Topic

Pick **one topic** from the curriculum below that:

- Has **NOT** appeared in `history.yaml`
- Is appropriate as the **next step** given what topics have already been covered (prefer sequential/progressive ordering)
- If all topics in a category are covered, move to the next category

**Topic Curriculum (ordered by progression):**

#### The 7-Day Intensive Curriculum (For Experienced Developers)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day1_fundamentals_types` | 0x01: Go Fundamentals & Type System | Structs, Interfaces, Memory Layout, Pointers vs Values, Type Assertions vs Type Switches. No basic syntax. |
| `day2_concurrency_errors` | 0x02: Concurrency & Error Philosophy | Goroutines, Channels (Buffered/Unbuffered), Select, Defer/Panic/Recover, Error Handling (Wrapping, Is/As). |
| `day3_stdlib_io` | 0x03: Standard Library, I/O & Context | `io.Reader`/`io.Writer`, `bufio`, `context` (Cancellation/Timeouts), JSON encoding, HTTP Client/Server basics. |
| `day4_intermediate_patterns` | 0x04: Patterns, Testing & Generics | Dependency Injection, Functional Options, Table-driven Tests, `testing.T`/`testing.B`, Go Generics (Type constraints). |
| `day5_advanced_concurrency` | 0x05: Advanced Concurrency & Memory Model | `sync` (`Mutex`, `WaitGroup`, `Once`, `Cond`), `sync/atomic`, Data Races, Race Detector, Go Memory Model. |
| `day6_system_integration` | 0x06: System & External Integration | Reflection (`reflect`), `unsafe` package, CGo (Calling C), Build Tags, Profiling (`pprof`). |
| `day7_realworld_architecture` | 0x07: Real-world Architecture | Building gRPC Services, `database/sql` connection pooling, Clean Architecture in Go, k8s containerd in Go. |

### Step 3 — Generate the Daily Learning Session

Generate a full, structured learning session directly inside the **`pages/development/golang/`** directory (the GitHub Pages site directory).

**Naming convention**: Use `YYYY-MM-DD_golang{NN}.md` where NN is a 2-digit sequence (usually 01 for the first topic of the day).
**File path**: `pages/development/golang/YYYY-MM-DD_golang01.md`  
(e.g., `pages/development/golang/2026-03-08_golang01.md`)

---

#### Output Format

**IMPORTANT — Jekyll Front-matter**:
Every generated `.md` file MUST begin with Jekyll front-matter so the page renders correctly on the GitHub Pages site:

```markdown
---
layout: default
title: "{Title}"
---

# Golang

## 🧠 Concept Overview

---

## 🧠 Concept Overview

[Clear, concise, and in-depth explanation of the concepts.
**CRITICAL**: Since the user is an experienced developer from other languages, SKIP basic syntax explanations (like how to define a variable). Instead, focus tightly on **Go's specific design philosophy**, memory layout, performance implications, and how Go differs from other languages like Java/Python/C++. Explain the internal mechanics.]

---

## 🔑 Key Points

- [Key point 1]
- [Key point 2]
- [Key point 3]
- [Key point 4]
- [Key point 5]

---

## 💻 Code Examples

### Example 1 — {Descriptive title}

\`\`\`go
// File: example1.go
package main

import "fmt"

func main() {
    // Clear, well-commented code
    // Each step explained inline
}
\`\`\`

**What this demonstrates**: [1–2 sentence explanation of the example]

### Example 2 — {Descriptive title}

\`\`\`go
// File: example2.go
package main

import "fmt"

func main() {
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
| [mistake 3] | [reason] | [fix] |

---

## 🏋️ Practice Exercises

### Exercise 1 — {Title} (Easy)

**Goal**: [Clear description of what to implement]

**Requirements**:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

**Starter code**:

\`\`\`go
package main

// TODO: Complete the implementation
\`\`\`

**Hint**: [A subtle hint without giving away the answer]

---

### Exercise 2 — {Title} (Medium)

**Goal**: [Clear description]

**Requirements**:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

**Starter code**:

\`\`\`go
package main

// TODO: Complete the implementation
\`\`\`

**Hint**: [A subtle hint]

---

### Exercise 3 — {Title} (Hard / Challenge)

**Goal**: [A more realistic, real-world scenario]

**Requirements**:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
- [Requirement 4]

**Starter code**:

\`\`\`go
package main

// TODO: Complete the implementation
\`\`\`

**Hint**: [A subtle hint pointing toward the right approach]

---

## 📖 Reference & Further Reading

- [Official Go Documentation: {relevant page}]({url})
- [Go by Example: {topic}](https://gobyexample.com/{topic})
- [Effective Go — {section}](https://go.dev/doc/effective_go#{section})

---

## 🗒️ Quick Cheat Sheet

\`\`\`go
// One-liner reference for today's topic — the most important syntax
\`\`\`

---

[← back to golang](./) | [← back to development](..) | [← back to home](/)

---

### Step 4 — Update history.yaml

After generating the session file, **append** a new entry to `history.yaml`:

```yaml
# Example structure of history.yaml
- date: "2026-03-08"
  topic_key: "day1_fundamentals_types"
  title: "0x01: Go Fundamentals & Type System"
  category: "Intensive Track"
  file: "pages/development/golang/2026-03-08_golang01.md"

- date: "2026-03-09"
  topic_key: "day2_concurrency_errors"
  title: "0x02: Concurrency & Error Philosophy"
  category: "Intensive Track"
  file: "pages/development/golang/2026-03-09_golang01.md"
```

**Rules**:
- Always append; never overwrite existing entries
- If `history.yaml` does not exist, create it with proper YAML formatting
- Use `"YYYY-MM-DD"` date string format (quoted for YAML safety)

### Step 5 — Confirm to the User

After generating the file and updating history, tell the user:

1. **Today's topic**: The title and category
2. **File created**: The path to the session file
3. **Progress**: How many topics have been covered so far (e.g., "3 / 50 topics completed")
4. **Streak reminder**: The date of their last session
5. **Quick start**: Suggest they open the file and start with the Concept Overview, then try the exercises

## Content Quality Guidelines

### Concept Explanations
- Assume the user is an **experienced engineer**. Never explain what a variable, loop, or HTTP request is.
- Focus strictly on **Go idioms**, internal behavior (e.g., slice headers, goroutine scheduling), and performance.
- Compare memory allocation behaviors (e.g. heap vs stack escapes).
- Use professional terminology.

### Code Examples
- All code must be **complete and runnable** (`package main`, `func main()`, proper imports)
- Prefer complex, high-performance, and idiomatic use cases over toy examples.
- Demonstrate advanced edge cases (e.g., channel deadlocks, memory leaks via slices).

### Exercises
- Exercise 1: Advanced language nuance or refactoring non-idiomatic code.
- Exercise 2: Implementing a common high-performance pattern (e.g., worker pool, pipeline).
- Exercise 3 (Challenge): A system-design level mini-implementation (e.g., thread-safe cache, concurrent web scraper).
- Ensure exercises force the user to think about concurrency, pointers, or system resources.

### Progression
- Always check `history.yaml` first — **never repeat a topic**
- Follow the 7-day curriculum order.

## File Organization

```
# Skill files (unchanged)
.agent/skills/golang-learning/
├── SKILL.md              ← This file
└── history.yaml          ← Auto-managed learning history

# Generated articles go here (GitHub Pages site)
pages/development/golang/
├── index.md                            # Directory index (auto-lists articles)
├── YYYY-MM-DD_golang01.md             # Session file for that day
└── ...
```

## Error Handling

- If `history.yaml` is not parseable, warn the user and start with an empty history
- If all 7 intensive topics are covered, congratulate the user and offer to generate custom system-design scenarios or dive into specific framework codebases.
- If the user requests a specific topic (even if already covered), generate it but note it was covered before.
