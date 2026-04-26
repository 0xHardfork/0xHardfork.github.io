---
name: k8s-security
description: Daily Kubernetes Security learning skill that generates a 57-day intensive curriculum. Starts from basic concepts and commands, scaling up to advanced cluster and container security patterns, and culminates with 27 hands-on vulnerability labs with runnable exploit scenarios. Outputs content directly into the pages/cloud-security/k8s-security/ directory.
---

# Kubernetes Security Daily Learning Skill

This skill helps you learn Kubernetes (k8s) and Kubernetes Security one topic per day over a **57-day** intensive course. It begins with foundational concepts and command-line usage, progresses towards advanced workload, network, and cluster security implementations, and culminates with **27 vulnerability deep-dive labs** where you hand-craft insecure configurations and attack scenarios from scratch.

## When to Use This Skill

- User says **"start today's k8s task"**
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

#### Phase 7: Vulnerability Lab — RBAC & Privilege Escalation (0x1F - 0x22)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_overpermissive_rbac_lab` | 0x1F: 🔬 Lab — Overly Permissive RBAC | Hand-craft ClusterRoleBindings with wildcard verbs/resources and demonstrate how a compromised pod escalates to cluster-admin. |
| `vuln_rbac_escalation_lab` | 0x20: 🔬 Lab — RBAC Privilege Escalation Chains | Hand-craft a multi-step escalation: ServiceAccount → create pods → mount hostPath → read node secrets. Demonstrate `kubectl auth can-i` misses. |
| `vuln_sa_token_abuse_lab` | 0x21: 🔬 Lab — ServiceAccount Token Abuse | Hand-craft pods with auto-mounted SA tokens, extract them, and use `curl` against the API server to list secrets across namespaces. |
| `vuln_impersonation_lab` | 0x22: 🔬 Lab — API Server Impersonation | Hand-craft an RBAC policy allowing `impersonate` verb, then demonstrate how an attacker impersonates a cluster-admin user. |

#### Phase 8: Vulnerability Lab — Container Escape & Host Access (0x23 - 0x26)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_privileged_container_lab` | 0x23: 🔬 Lab — Privileged Container Escape | Deploy a privileged pod, mount the host filesystem, and demonstrate full node compromise via `nsenter` or `chroot`. |
| `vuln_hostpath_abuse_lab` | 0x24: 🔬 Lab — HostPath Volume Abuse | Hand-craft a pod mounting `/etc/shadow` or `/var/run/docker.sock` via hostPath and demonstrate credential theft or container spawning on the host. |
| `vuln_cap_abuse_lab` | 0x25: 🔬 Lab — Dangerous Linux Capabilities | Hand-craft pods with `SYS_PTRACE`, `SYS_ADMIN`, or `NET_RAW` capabilities and demonstrate process injection, namespace escape, or ARP spoofing. |
| `vuln_procfs_escape_lab` | 0x26: 🔬 Lab — /proc & /sys Filesystem Escape | Hand-craft a pod without `readOnlyRootFilesystem`, access `/proc/1/root` or cgroup release_agent to escape the container namespace. |

#### Phase 9: Vulnerability Lab — Network & Lateral Movement (0x27 - 0x2A)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_no_netpol_lab` | 0x27: 🔬 Lab — Missing NetworkPolicy (Flat Network) | Deploy multiple services without any NetworkPolicy and demonstrate unrestricted pod-to-pod lateral movement using `nmap` and `curl`. |
| `vuln_dns_exfil_lab` | 0x28: 🔬 Lab — DNS-Based Data Exfiltration | Hand-craft a pod that exfiltrates secrets via DNS queries to an external server, bypassing egress rules that only block TCP. |
| `vuln_metadata_api_lab` | 0x29: 🔬 Lab — Cloud Metadata API SSRF | Deploy a pod that accesses the cloud provider's metadata endpoint (169.254.169.254) to steal IAM credentials and escalate to cloud resources. |
| `vuln_service_mesh_bypass_lab` | 0x2A: 🔬 Lab — Service Mesh mTLS Bypass | Hand-craft a pod with `sidecar.istio.io/inject: false` annotation or direct IP access to bypass Istio/Linkerd mutual TLS enforcement. |

#### Phase 10: Vulnerability Lab — Secrets & Data Exposure (0x2B - 0x2E)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_secrets_plaintext_lab` | 0x2B: 🔬 Lab — Secrets in Plain Sight | Hand-craft Secrets in environment variables and demonstrate extraction via `kubectl exec env`, `/proc/1/environ`, and etcd direct read. |
| `vuln_etcd_unencrypted_lab` | 0x2C: 🔬 Lab — Unencrypted etcd Access | Demonstrate reading raw secret data from etcd when encryption-at-rest is not configured, and when the etcd endpoint is exposed. |
| `vuln_configmap_secrets_lab` | 0x2D: 🔬 Lab — Sensitive Data in ConfigMaps | Hand-craft ConfigMaps containing database passwords and API keys, demonstrate exposure via `kubectl get configmap -o yaml`. |
| `vuln_image_secrets_lab` | 0x2E: 🔬 Lab — Secrets Baked into Container Images | Build a container image with hardcoded credentials in ENV or filesystem, extract them via `docker history` and layer inspection. |

#### Phase 11: Vulnerability Lab — Supply Chain & Image Security (0x2F - 0x32)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_unsigned_image_lab` | 0x2F: 🔬 Lab — Unsigned/Unverified Container Images | Deploy pods pulling from untrusted registries without signature verification, demonstrate image tampering and supply chain injection. |
| `vuln_latest_tag_lab` | 0x30: 🔬 Lab — Mutable Image Tags (:latest) | Demonstrate how `:latest` tag allows silent image replacement, and how `imagePullPolicy: Always` still doesn't protect against tag mutation. |
| `vuln_vuln_base_image_lab` | 0x31: 🔬 Lab — Vulnerable Base Images | Deploy a pod using an outdated base image with known CVEs, run Trivy/Grype scanning, and demonstrate exploitation of an unpatched vulnerability. |
| `vuln_admission_bypass_lab` | 0x32: 🔬 Lab — Admission Controller Bypass | Hand-craft scenarios that bypass OPA/Kyverno policies: ephemeral containers, CronJobs, or label-matching exceptions. |

#### Phase 12: Vulnerability Lab — Denial of Service & Resource Abuse (0x33 - 0x35)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_resource_exhaustion_lab` | 0x33: 🔬 Lab — Resource Exhaustion (No Limits) | Deploy pods without CPU/memory limits, run a fork bomb or memory leak, and demonstrate node-level OOM kills affecting neighboring workloads. |
| `vuln_api_dos_lab` | 0x34: 🔬 Lab — API Server Denial of Service | Hand-craft a script that floods the API server with list/watch requests, demonstrate rate limiting gaps and EventRateLimit admission controller. |
| `vuln_pod_disruption_lab` | 0x35: 🔬 Lab — Pod Disruption & Eviction Abuse | Demonstrate how missing PodDisruptionBudgets allow mass eviction, and how `kubectl drain` without safeguards causes service outages. |

#### Phase 13: Vulnerability Lab — Cluster Infrastructure & Persistence (0x36 - 0x39)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_kubelet_unauth_lab` | 0x36: 🔬 Lab — Unauthenticated Kubelet API | Demonstrate accessing the Kubelet's read-only port (10255) or unauthenticated port (10250) to list pods, exec into containers, and read logs. |
| `vuln_dashboard_exposed_lab` | 0x37: 🔬 Lab — Exposed Kubernetes Dashboard | Deploy the K8s Dashboard without authentication and demonstrate full cluster control via the web UI from an external network. |
| `vuln_cronjob_persistence_lab` | 0x38: 🔬 Lab — CronJob/DaemonSet Persistence | After gaining initial access, create a CronJob or DaemonSet backdoor that maintains persistent access and survives pod restarts. |
| `vuln_webhook_hijack_lab` | 0x39: 🔬 Lab — Mutating Webhook Hijack | Hand-craft a malicious MutatingAdmissionWebhook that injects sidecar containers or modifies pod specs to exfiltrate data on every deployment. |

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

**[CRITICAL: Do NOT output any "Welcome to" or AI intros. Immediately start the first sentence with a deep technical exploration of the topic.]**

[EXTREMELY exhaustive, double-length, step-by-step explanation of the concepts. Start from the absolute basics, then dive deep. Explain WHY this concept exists and WHAT security problem it mitigates in precise, meticulous detail.]

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

Generate exactly 8 exercises, pacing from basic investigation to hard scenario exploitation.

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

### Exercise 2 — {Title} (Basic Exploration)

**Goal**: [Observe how the security control behaves when violated]

**Instructions**:
1. Try to bypass the control using a specific `kubectl exec` or deployment strategy.
2. Note the API server error response or runtime blockage.

**Hint**: [A subtle hint]

### Exercise 3 — {Title} (Medium Analysis)

**Goal**: [Analyze existing configurations for security weaknesses]

**Instructions**:
1. Given a provided YAML manifest, identify potential misconfigurations.
2. Explain the security implications of these findings.

**Hint**: [A subtle hint]

### Exercise 4 — {Title} (Medium Implementation)

**Goal**: [Implement a specific security control or feature]

**Requirements**:
- [Requirement 1]
- [Requirement 2]

**Starter YAML/Command**:

\`\`\`yaml
# TODO: Complete the implementation
\`\`\`

**Hint**: [A subtle hint]

### Exercise 5 — {Title} (Medium Hardening)

**Goal**: [Modify an existing resource to improve its security posture]

**Instructions**:
1. Take a given insecure manifest and apply best practices to harden it.
2. Verify the changes have the intended security effect.

**Hint**: [A subtle hint]

### Exercise 6 — {Title} (Hard Escalation)

**Goal**: [Simulate an attack to gain elevated privileges or access]

**Instructions**:
1. Given a compromised resource, find a path to escalate privileges within the cluster.
2. Document the steps taken and the resulting access.

**Hint**: [A subtle hint]

### Exercise 7 — {Title} (Hard Mitigation)

**Goal**: [Design and implement a complex security mitigation strategy]

**Requirements**:
- [Requirement 1]
- [Requirement 2]

**Starter YAML/Command**:

\`\`\`yaml
# TODO: Complete the implementation
\`\`\`

**Hint**: [A subtle hint]

### Exercise 8 — {Title} (Challenge Simulation!)

**Goal**: [Solve a multi-step security challenge involving multiple concepts]

**Instructions**:
1. Identify vulnerabilities in a provided scenario.
2. Exploit them to achieve a specific objective.
3. Propose and implement comprehensive fixes.

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

#### Vulnerability Lab Output Format (Phase 7–13 ONLY)

For topics in **Phase 7 through Phase 13** (topic_keys starting with `vuln_`), use this **specialized template** instead of the standard template above. The emphasis is on **hand-crafting insecure configurations and attack scenarios from scratch**.

```markdown
---
layout: default
title: "{Title}"
---

# 🔬 Vulnerability Lab: {Vulnerability Name}

**Date**: YYYY-MM-DD
**Topic**: {Title}
**Phase**: {Phase Name}
**Lab Type**: Hand-crafted Vulnerability & Attack Scenario

---

## 📝 Vulnerability Overview

**[CRITICAL: Do NOT output any "Welcome to" or AI intros. Immediately start the first sentence with a deep technical exploration of the vulnerability.]**

[Exhaustive explanation of WHAT this vulnerability is, WHY it exists in Kubernetes architecture, HOW it is exploited in real clusters, and what real-world impact it has caused. Include API server internals, kubelet behavior, and Linux kernel details where relevant.]

---

## 🔑 Key Takeaways

- [Key point 1: Root cause]
- [Key point 2: Attack preconditions]
- [Key point 3: Detection signals]
- [Key point 4: Mitigation pattern]
- [Key point 5: Related vulnerability classes]

---

## 🔴 Vulnerable Configuration Example 1: {Scenario Title}

\`\`\`yaml
# COMPLETE, DEPLOYABLE, RUNNABLE insecure Kubernetes manifest
# Heavily commented — explain exactly where the flaw is
# This must be a REAL manifest that can be applied via kubectl
apiVersion: ...
kind: ...
metadata:
  name: ...
spec:
  # ... insecure configuration ...
\`\`\`

\`\`\`bash
# Command to deploy
kubectl apply -f vulnerable-example-1.yaml
\`\`\`

**🔍 Vulnerability Analysis**:
- [Where exactly is the flaw?]
- [What preconditions enable exploitation?]
- [What is the attacker's goal?]

---

## 🔴 Vulnerable Configuration Example 2: {Different Scenario Title}

\`\`\`yaml
# A DIFFERENT scenario demonstrating the SAME vulnerability class
# Must be a distinct manifest with different attack surface
apiVersion: ...
kind: ...
metadata:
  name: ...
spec:
  # ... different insecure configuration ...
\`\`\`

**🔍 Vulnerability Analysis**:
- [Where exactly is the flaw?]
- [How does this differ from Example 1?]

---

## ⚔️ Attack Scenario 1: Exploiting Vulnerable Config 1

\`\`\`bash
# COMPLETE attack script / kubectl commands
# Must be runnable against Vulnerable Configuration Example 1
# Step-by-step exploitation from attacker's perspective
\`\`\`

\`\`\`yaml
# If an attacker pod manifest is needed:
apiVersion: v1
kind: Pod
metadata:
  name: attacker-pod
spec:
  # ... attack payload ...
\`\`\`

**📋 Attack Walkthrough**:
1. [Step-by-step description of the attack flow]
2. [What happens at each stage]
3. [Final state after exploitation — what did the attacker gain?]

**Expected Output**:
\`\`\`
# What the attacker sees after successful exploitation
\`\`\`

---

## ⚔️ Attack Scenario 2: Exploiting Vulnerable Config 2

\`\`\`bash
# COMPLETE attack script using a DIFFERENT approach or target
\`\`\`

**📋 Attack Walkthrough**:
1. [Step-by-step]

**Expected Output**:
\`\`\`
# What the attacker sees
\`\`\`

---

## 🟢 Secure Implementation

### Fix for Vulnerable Config 1

\`\`\`yaml
# Patched version of Vulnerable Configuration 1
# Highlight the specific lines that changed with comments
apiVersion: ...
kind: ...
metadata:
  name: ...
spec:
  # ... secured configuration ...
\`\`\`

### Fix for Vulnerable Config 2

\`\`\`yaml
# Patched version of Vulnerable Configuration 2
\`\`\`

**✅ Why these fixes work**:
- [Explain the mitigation mechanism for each fix]
- [Reference industry best practices: CIS Benchmarks, NSA/CISA guidelines, etc.]

---

## ⚠️ Real-World Impact

| Real-World Incident | Impact | Root Cause |
|---------------------|--------|------------|
| [Company/Project] | [Data breach / Cryptomining / etc.] | [Brief description] |
| [Company/Project] | [Impact] | [Brief description] |

---

## 🏋️ Practice Exercise: {Challenge Title}

**Scenario**: [Describe a new insecure cluster configuration the user must analyze and exploit]

\`\`\`yaml
# TARGET CONFIGURATION — Find and exploit the vulnerability!
# The user should craft their own attack and remediation
apiVersion: ...
kind: ...
metadata:
  name: practice-target
spec:
  # ... vulnerable configuration ...
\`\`\`

**🎯 Goal**: [What the user needs to achieve — e.g., read secrets from another namespace, escape to host, etc.]

**💡 Hint**: [A subtle hint without giving away the answer]

<details>
<summary>📖 Click to reveal solution</summary>

\`\`\`bash
# Solution: Attack commands
\`\`\`

\`\`\`yaml
# Solution: Remediated manifest
apiVersion: ...
kind: ...
spec:
  # ... fixed configuration ...
\`\`\`

</details>

---

## 📖 Reference & Further Reading

- [CIS Kubernetes Benchmark: {relevant section}]({url})
- [NSA/CISA Kubernetes Hardening Guide]({url})
- [Kubernetes Threat Matrix (Microsoft)]({url})

---

## 🗒️ Quick CLI Cheat Sheet

\`\`\`bash
# Essential kubectl / attack tool commands for this lab
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
3. **Progress**: How many topics have been covered so far (e.g., "1 / 57 topics completed - Phase 1")
4. **Streak reminder**: The date of their last session
5. **Quick start**: Suggest they open the file and dive into the security mechanisms.

## Content Quality Guidelines

### Tone & Style
- **Tone**: Use a warm, human-like, and conversational tone. Write like a friendly senior DevOps engineer chatting with a colleague. Use simple, colloquial language and fiercely avoid sounding like a rigid, automated AI bot. Avoid clichéd AI intros ("In this article...").
- **Exhaustive Content Length**: You MUST generate extremely long, exhaustive content to ensure absolutely NO knowledge points are missed. Dive deeply into every security mechanism, API flag, and edge case. Do NOT summarize or abbreviate. Your output must be a definitive, deeply comprehensive security guide.
- **Natural Delivery**: While maintaining structure, make the transitions and paragraph text feel relaxed and human-written.

### Concept Explanations
- **Balance Beginner & Advanced**: The user is an experienced developer but a **Complete Beginner** to Kubernetes and K8s Security. You MUST balance the content by initially thoroughly explaining the foundational Kubernetes resources (e.g., Pods/Services) so a beginner can understand. Once the foundation is laid, scale up to satisfy an experienced engineer by discussing advanced security architectures, deep attack surface analysis, and intricate mitigation techniques.
- Provide step-by-step guidance. Relate K8s concepts to traditional Linux/server environments to bridge the gap.
- Maintain a **security-first** mindset, explaining the attack surface in accessible terms before diving deep.

### Code Examples
- **Volume & Variety**: Provide MULTIPLE YAML and CLI examples. Show basic configurations, advanced secured configurations, and common misconfigurations. Do not provide just one short snippet.
- YAML examples should be syntactically correct (apiVersion, kind, metadata, spec).
- Include `kubectl apply -f` or similar context commands rather than just raw YAML.

### Exercises
- **Volume (Phase 1–6)**: You MUST generate exactly **8 practice exercises** per daily session, scaling from simple resource inspection to complex runtime attack scenarios.
- **Volume (Phase 7–13 Vulnerability Labs)**: Generate exactly **2 vulnerable configuration examples**, **2 attack scenario examples** (with full kubectl/bash commands), and **1 practice exercise** (with hidden solution). All manifests must be **complete, deployable, and runnable** — no pseudocode or stubs.

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
- If all 57 intensive topics are covered, congratulate the user!
- If the user requests a specific topic (even if already covered), generate it but note it was covered before.
