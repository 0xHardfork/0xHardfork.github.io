---
name: k8s-security
description: Daily Kubernetes Security learning skill that generates a 30-day intensive curriculum. Starts from basic concepts and commands, scaling up to advanced cluster and container security patterns. Outputs content directly into the pages/cloud-security/k8s-security/ directory.
---

# Kubernetes Security Daily Learning Skill

This skill helps you learn Kubernetes (k8s) and Kubernetes Security one topic per day over a 30-day intensive course. It begins with foundational concepts and command-line usage, progressing towards advanced workload, network, and cluster security implementations.

## When to Use This Skill

- User says **"开始今日k8s任务"** (start today's k8s task)
- User says **"start today's k8s security task"** or **"start daily k8s task"**
- User says **"begin daily k8s practice"** or **"kubernetes today"**
- User wants to continue their daily Kubernetes learning routine

## Workflow

### Step 1 — Read History

Before generating any content:

1. Read `history.yaml` from the skill directory (`.agent/skills/k8s-security/history.yaml`)
2. Extract the list of all **previously covered topics** (the `topic_key` field of each entry)
3. Also note the most recent entry's date so you can inform the user of their streak

If `history.yaml` does not exist yet, treat the history as **empty** and create the file after the session.

### Step 2 — Select Today's Topic

Pick **one topic** from the curriculum below that:

- Has **NOT** appeared in `history.yaml`
- Is appropriate as the **next step** given what topics have already been covered (prefer sequential/progressive ordering).

**Topic Curriculum (The 30-Day Intensive Track):**

#### Phase 1: Kuberenetes Fundamentals (0x01 - 0x05)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day01_k8s_architecture` | 0x01: Cluster Architecture & Control Plane | Master vs Worker nodes, API Server, etcd, Scheduler, Kubelet, and Kube-proxy. |
| `day02_kubectl_basics` | 0x02: The `kubectl` CLI | Contexts, kubeconfig, basic imperatives commands to view and manage resources. |
| `day03_workloads_pods` | 0x03: Pods, Deployments & ReplicaSets | Ephemeral containers, workload scheduling, yaml manifests. |
| `day04_services_networking` | 0x04: Services & Basic Networking | ClusterIP, NodePort, LoadBalancer, and basic internal routing. |
| `day05_configmaps_secrets` | 0x05: ConfigMaps & Basic Secrets | Decoupling configuration from containers and base64-encoded secrets. |

#### Phase 2: Authentication & Authorization (0x06 - 0x10)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day06_authn_mechanisms` | 0x06: Authentication Mechanisms | X.509 certificates, OIDC, ServiceAccounts, and API Server flags. |
| `day07_service_accounts` | 0x07: ServiceAccounts Deep Dive | Automounting tokens (and why to disable it), Projected Volume Tokens. |
| `day08_rbac_basics` | 0x08: Role-Based Access Control (RBAC) 101 | Roles, RoleBindings, and Namespaced permissions. |
| `day09_rbac_advanced` | 0x09: Advanced RBAC & Escalation | ClusterRoles, ClusterRoleBindings, viewing effective permissions (`auth can-i`). |
| `day10_rbac_auditing` | 0x0A: Troubleshooting & Auditing RBAC | Finding overly permissive roles, default `view`, `edit`, `admin` roles. |

#### Phase 3: Workload & Container Security (0x11 - 0x16)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day11_security_context` | 0x0B: Security Context Basics | `RunAsUser`, `RunAsNonRoot`, `readOnlyRootFilesystem`, `privileged` containers. |
| `day12_linux_capabilities` | 0x0C: Managing Linux Capabilities | Dropping ALL capabilities, adding only necessary ones (e.g., `NET_BIND_SERVICE`). |
| `day13_pod_security_standards_1` | 0x0D: Pod Security Standards (PSS) | Introduction to Privileged, Baseline, and Restricted namespaces. |
| `day14_pod_security_standards_2` | 0x0E: Pod Security Admission (PSA) | Enforcing, warning, and auditing PSS at the namespace and cluster levels. |
| `day15_seccomp_profiles` | 0x0F: Restricting Syscalls with Seccomp | Applying default container runtime profiles (RuntimeDefault) vs Unconfined. |
| `day16_apparmor_selinux` | 0x10: Mandatory Access Control (MAC) | Integrating AppArmor profiles and SELinux contexts with Pods. |

#### Phase 4: Network Security (0x17 - 0x21)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day17_netpol_basics` | 0x11: NetworkPolicies 101 | Default-Deny posture, isolating namespaces, basic Ingress rules. |
| `day18_netpol_advanced` | 0x12: Advanced NetworkPolicies | Egress rules, exact IPBlocks, cross-namespace communication. |
| `day19_cni_security` | 0x13: Secure CNI Configuration | Intro to advanced CNIs like Cilium and Calico for node-level eBPF security. |
| `day20_ingress_tls` | 0x14: Securing Ingress objects | Termination vs Passthrough, TLS certificates configured via Secret. |
| `day21_service_mesh` | 0x15: Service Mesh & Mutual TLS | Introduction to Istio/Linkerd, enforcing mTLS between microservices. |

#### Phase 5: Secrets Management & Encryption (0x22 - 0x24)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day22_etcd_encryption` | 0x16: Encryption at Rest | Encrypting Secret data inside etcd. |
| `day23_kms_plugins` | 0x17: KMS Plugins | Kubernetes KMS providers with external cloud KMS (AWS KMS, Azure KeyVault). |
| `day24_external_secrets` | 0x18: External Secret Operators | Syncing credentials from HashiCorp Vault or AWS Secrets Manager. |

#### Phase 6: Cluster Security, Auditing & Supply Chain (0x25 - 0x30)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day25_kube_audit_logs` | 0x19: API Server Auditing | Configuring audit policies, examining audit events. |
| `day26_admission_controllers` | 0x1A: Custom Admission Webhooks | Mutating vs Validating webhooks architecture. |
| `day27_policy_engines` | 0x1B: Policy Engines (OPA / Kyverno) | Creating custom cluster policies (e.g., enforcing internal registries). |
| `day28_cis_benchmarks` | 0x1C: CIS Benchmarks & Kube-bench | Assessing node and control plane compliance. |
| `day29_image_scanning` | 0x1D: Container Image Security | Image vulnerability scanning (Trivy), distroless images, minimal base images. |
| `day30_runtime_security` | 0x1E: Runtime Security Detection | Using tools like Falco or Tetragon to catch reverse shells and unauthorized access. |

### Step 3 — Generate the Daily Learning Session

Generate a full, structured learning session directly inside the **`pages/cloud-security/k8s-security/`** directory (the GitHub Pages site directory).

**Naming convention**: Use `YYYY-MM-DD_k8s{NN}.md` where NN is a 2-digit sequence (usually 01 for the first topic of the day).
**File path**: `pages/cloud-security/k8s-security/YYYY-MM-DD_k8s01.md`  
(e.g., `pages/cloud-security/k8s-security/2026-03-12_k8s01.md`)

---

#### Output Format

**IMPORTANT — Jekyll Front-matter**:
Every generated `.md` file MUST begin with Jekyll front-matter so the page renders correctly on the GitHub Pages site:

```markdown
---
layout: default
title: "{Title}"
---

# Kubernetes Security Daily Learning

**Date**: YYYY-MM-DD  
**Topic**: {Title}  
**Phase**: {Phase Name}  

---

## 🧠 Concept Overview

[Clear, concise, and professional explanation of the concepts.
Explain WHY this concept exists in Kubernetes and WHAT security or operational problem it solves. Provide context about potential threats if this feature is ignored. Focus on architectural impact.]

---

## 🔑 Key Points

- [Key point 1]
- [Key point 2]
- [Key point 3]
- [Key point 4]
- [Key point 5]

---

## 💻 Code & Configuration Examples

### Example 1 — {Descriptive title}

\`\`\`yaml
# Clear, well-commented YAML manifest or bash script
# Each key step explained inline
\`\`\`

**What this demonstrates**: [1–2 sentence explanation of the deployment manifest or shell command sequence]

### Example 2 — {Descriptive title}

\`\`\`yaml
# A slightly more complex or realistic security configuration
\`\`\`

**What this demonstrates**: [1–2 sentence explanation]

---

## ⚠️ Common Misconfigurations & Risks

| Misconfiguration | Risk Assessment | Secure Approach |
|------------------|----------------|----------------|
| [Mistake/Default config] | [Why this exposes the cluster] | [How to fix it] |
| [Mistake/Default config] | [Why this exposes the cluster] | [How to fix it] |
| [Mistake/Default config] | [Why this exposes the cluster] | [How to fix it] |

---

## 🏋️ Practice Exercises

### Exercise 1 — {Title} (Practical application)

**Goal**: [Clear description of what to implement or deploy]

**Requirements**:
- [Requirement 1]
- [Requirement 2]

**Starter YAML/Command**:

\`\`\`yaml
# TODO: Complete the implementation
\`\`\`

**Hint**: [A subtle hint pointing toward the right `kubectl` command or YAML field]

---

### Exercise 2 — Exploring the impact (Security context)

**Goal**: [Observe how the security control behaves when violated]

**Instructions**:
1. Try to bypass the control using a specific `kubectl exec` or deployment strategy.
2. Note the API server error response or runtime blockage.

**Hint**: [A subtle hint]

---

## 📖 Reference & Further Reading

- [Official K8s Documentation: {relevant page}]({url})
- [Kubernetes Security Best Practices (CISA/NSA)]({url})

---

## 🗒️ Quick CLI Cheat Sheet

\`\`\`bash
# Essential short commands for today's topic
\`\`\`

---

[← back to k8s security](./) | [← back to cloud security](..) | [← back to home](/)
```

---

### Step 4 — Update history.yaml

After generating the session file, **append** a new entry to `history.yaml`:

```yaml
# Example structure of history.yaml
- date: "2026-03-12"
  topic_key: "day01_k8s_architecture"
  title: "0x01: Cluster Architecture & Control Plane"
  category: "Phase 1: Kuberenetes Fundamentals"
  file: "pages/cloud-security/k8s-security/2026-03-12_k8s01.md"

- date: "2026-03-13"
  topic_key: "day02_kubectl_basics"
  title: "0x02: The kubectl CLI"
  category: "Phase 1: Kuberenetes Fundamentals"
  file: "pages/cloud-security/k8s-security/2026-03-13_k8s01.md"
```

**Rules**:
- Always append; never overwrite existing entries
- If `history.yaml` does not exist, create it with proper YAML formatting
- Use `"YYYY-MM-DD"` date string format (quoted for YAML safety)

### Step 5 — Confirm to the User

After generating the file and updating history, tell the user:

1. **Today's topic**: The title and phase
2. **File created**: The path to the session file
3. **Progress**: How many topics have been covered so far (e.g., "1 / 30 topics completed - Phase 1")
4. **Streak reminder**: The date of their last session
5. **Quick start**: Suggest they open the file and dive into the security mechanisms.

## Content Quality Guidelines

### Concept Explanations
- Maintain a **security-first** mindset. Always explain concepts by defining the attack surface they mitigate.
- Write in clear, professional English.

### Code Examples
- YAML examples should be syntactically correct (apiVersion, kind, metadata, spec).
- Include `kubectl apply -f` or similar context commands rather than just raw YAML.

### File Organization

```
# Skill files (auto-generated)
.agent/skills/k8s-security/
├── SKILL.md              ← This file
└── history.yaml          ← Auto-managed learning history

# Generated articles go here (GitHub Pages site)
pages/cloud-security/k8s-security/
├── index.md              # Directory index (if you wish to configure it)
├── YYYY-MM-DD_k8s01.md   # Session file for that day
└── ...
```

## Error Handling

- If `history.yaml` is not parseable, warn the user and start with an empty history
- If all 30 intensive topics are covered, congratulate the user!
- If the user requests a specific topic (even if already covered), generate it but note it was covered before.
