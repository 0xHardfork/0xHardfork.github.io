---
name: web3-security
description: Daily Web3 Security learning skill that generates a 90-day intensive curriculum. Extensively covers blockchain basics, auditing tools, in-depth CTF target range setup & walkthroughs (Ethernaut, Damn Vulnerable DeFi), advanced attacks, secure implementation, and 29 hands-on vulnerability labs with runnable exploit code. Outputs content directly into the pages/web3/security/ directory.
---

# Web3 Security Daily Learning Skill

This skill helps you learn Web3, Smart Contracts, and Smart Contract Security one topic per day over a **90-day** intensive course. It begins with foundational concepts, progresses to code auditing, heavily emphasizes hands-on CTF exercises and advanced real-world attack vectors, and culminates with **29 vulnerability deep-dive labs** where you hand-write vulnerable contracts and exploits from scratch.

## When to Use This Skill

- User says **"start today's web3 security task"**
- User says **"start today's web3 task"** or **"start daily web3 security task"**
- User says **"begin daily web3 security practice"** or **"web3 security today"**
- User wants to continue their daily Web3 Security learning routine

## Workflow

### Step 1 — Read History

Before generating any content:

1. Read `history.yaml` from the skill directory (`.agent/skills/web3-security/history.yaml`)
2. Extract the list of all **previously covered topics** (the `topic_key` field of each entry)
3. Also note the most recent entry's date so you can inform the user of their streak

If `history.yaml` does not exist yet, treat the history as **empty** and create the file after the session.

### Step 2 — Select Today's Topic

Pick **one topic** from the curriculum below that:

- Has **NOT** appeared in `history.yaml`
- Is appropriate as the **next step** given what topics have already been covered (prefer sequential/progressive ordering).

**Topic Curriculum (The 60-Day Intensive Track):**

#### Phase 1: Web3 Fundamentals & Demos (0x01 - 0x0A)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day01_blockchain_basics` | 0x01: Blockchain Basics, Consensus, & P2P | Blocks, transactions, state machine basics, and consensus mechanisms. |
| `day02_ethereum_architecture` | 0x02: Ethereum Architecture & Accounts | EOA vs Smart Contracts, Nonce, Gas limitations, and network structure. |
| `day03_crypto_basics` | 0x03: Cryptography Basics | Hash functions (Keccak256), Elliptic Curve cryptography, and ECDSA basics. |
| `day04_evm_deepdive` | 0x04: EVM Storage, Memory, & Calldata | EVM memory layout, storage slots packing, and calldata structure. |
| `day05_solidity_basics1` | 0x05: Solidity Fundamentals I | Data types, state variables, visibility modifiers, and mappings. |
| `day06_solidity_basics2` | 0x06: Solidity Fundamentals II | Functions, custom modifiers, events, interfaces, and custom errors. |
| `day07_hardhat_setup` | 0x07: Development Environment: Hardhat | Setting up Hardhat, local node, writing basic compiling/deployment scripts. |
| `day08_foundry_setup` | 0x08: Development Environment: Foundry | Using forge, cast, and anvil for an ultra-fast local blockchain environment. |
| `day09_erc20_deepdive` | 0x09: Token Standards: ERC20 Sandbox | Minting, transferring, approvals, and the `transferFrom` pattern. |
| `day10_erc721_1155` | 0x0A: Token Standards: ERC721 & ERC1155 | NFTs, metadata, and multi-token standard architectures. |

#### Phase 2: Common Vulnerabilities & Exploits (0x0B - 0x14)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day11_reentrancy_basics` | 0x0B: Reentrancy Attacks | Single-function & Cross-function reentrancy, Checks-Effects-Interactions pattern. |
| `day12_reentrancy_advanced` | 0x0C: Cross-Contract & Read-only Reentrancy | Complex state inconsistency across multiple contracts, read-only attacks. |
| `day13_arithmetic` | 0x0D: Integer Overflow & Underflow | Pre-0.8.0 math vulnerabilities vs Solidity 0.8.0+ `unchecked` blocks. |
| `day14_access_control` | 0x0E: Access Control & `tx.origin` | Why `tx.origin` is dangerous for authorization; `ecrecover` pitfalls. |
| `day15_storage_collisions` | 0x0F: Uninitialized Storage Pointers & Collisions | How uninitialized variables can overwrite critical contract storage slots. |
| `day16_dos` | 0x10: Denial of Service (DoS) Vulnerabilities | Unexpected reverts, out-of-gas, and traversing unbounded arrays. |
| `day17_front_running` | 0x11: Front-Running & MEV | Transaction ordering dependence, priority gas auctions, and sandwiching. |
| `day18_randomness` | 0x12: Timestamp Dependence & Bad Randomness | Manipulating `block.timestamp`/`blockhash`; introduction to Chainlink VRF. |
| `day19_delegatecall` | 0x13: Unsafe `delegatecall` | Context preservation, proxy vulnerability patterns, and library exploitation. |
| `day20_unsafe_calls` | 0x14: Return Value Ignored & Unsafe External Calls | Forgetting to check return values of low-level `call`, `send`, or ERC20 transfers. |

#### Phase 3: Smart Contract Code Auditing Tools (0x15 - 0x19)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day21_slither` | 0x15: Static Analysis with Slither | Automating basic vulnerability hunting using Slither's detectors. |
| `day22_symbolic_exec` | 0x16: Symbolic Execution with Mythril & Manticore | Exploring edge cases mathematically through symbolic execution. |
| `day23_foundry_fuzzing` | 0x17: Fuzz Testing with Foundry | Writing property-based and invariant tests using Foundry. |
| `day24_echidna` | 0x18: Advanced Fuzzing with Echidna | Setting up state machine testing and complex invariant fuzzing. |
| `day25_manual_audit` | 0x19: Manual Audit Methodology & Threat Modeling | Mapping the attack surface, business logic analysis, and report writing. |

#### Phase 4: Target Range Setup & CTF Practice (0x1A - 0x2D)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day26_ctf_setup` | 0x1A: CTF Local Range Setup | Forking mainnet, setting up foundry scripts for remote/local CTF solving. |
| `day27_ethernaut_1` | 0x1B: Ethernaut Part 1 | Fallback, Fallout, CoinFlip, Telephone. Basic state & access exploitation. |
| `day28_ethernaut_2` | 0x1C: Ethernaut Part 2 | Token, Delegation, Force, Vault. Overflows, forced ether, storage reading. |
| `day29_ethernaut_3` | 0x1D: Ethernaut Part 3 | King, Re-entrancy, Elevator, Privacy. DoS, reentrancy limits, memory offsets. |
| `day30_ethernaut_4` | 0x1E: Ethernaut Part 4 | Gatekeeper One & Two, Naught Coin. Gas mechanics, bitwise masks, EVM `extcodesize`. |
| `day31_ethernaut_5` | 0x1F: Ethernaut Part 5 | Preservation, Recovery, MagicNumber. Delegatecall routing, raw EVM bytecode. |
| `day32_ethernaut_6` | 0x20: Ethernaut Part 6 | Alien Codex, Denial, Shop. Dynamic array underflows, assert limits, external calls. |
| `day33_ethernaut_7` | 0x21: Ethernaut Part 7 | Dex, Dex Two, Puzzle Wallet. AMM math bugs, proxy-logic collisions. |
| `day34_ethernaut_8` | 0x22: Ethernaut Part 8 | Motorbike, DoubleEntryPoint, Good Samaritan... UUPS initialization fixes, custom errors. |
| `day35_cte` | 0x23: Capture The Ether Highlights | Solving specific math and warmup challenges in CTE. |
| `day36_dvdf_unstoppable` | 0x24: Damn Vulnerable DeFi - Unstoppable | Accounting mismatches, vault exploitation, flash loan DoS. |
| `day37_dvdf_naive_receiver` | 0x25: Damn Vulnerable DeFi - Naive Receiver | Flash loan griefing attacks and unsafe interfaces. |
| `day38_dvdf_truster` | 0x26: Damn Vulnerable DeFi - Truster | Malicious external calls via low-level execution within flash loans. |
| `day39_dvdf_side_entrance` | 0x27: Damn Vulnerable DeFi - Side Entrance | Reentrancy into flash loan deposits, accounting bypass. |
| `day40_dvdf_rewarder` | 0x28: Damn Vulnerable DeFi - The Rewarder | Manipulating snapshot-based governance/rewards using flash loans. |
| `day41_dvdf_selfie_compromised` | 0x29: Damn Vulnerable DeFi - Selfie & Compromised | Governance takeover via flash loans; Oracle manipulation using leaked keys. |
| `day42_dvdf_puppet` | 0x2A: Damn Vulnerable DeFi - Puppet & Puppet V2 | Spot price manipulation on Uniswap V1 & V2. |
| `day43_dvdf_free_rider` | 0x2B: Damn Vulnerable DeFi - Free Rider | Flash swaps, NFT marketplace vulnerabilities, checking `msg.value`. |
| `day44_dvdf_backdoor` | 0x2C: Damn Vulnerable DeFi - Backdoor | Gnosis Safe proxy wallet initialization exploits. |
| `day45_dvdf_climber` | 0x2D: Damn Vulnerable DeFi - Climber | Timelock contract vulnerabilities and execution sequence manipulation. |

#### Phase 5: Advanced Attacks & Real-world Cases (0x2E - 0x37)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day46_flash_loans_adv` | 0x2E: Advanced Flash Loan Arbitrage | In-depth mechanics of Aave/Balancer flash loans empowering complex attacks. |
| `day47_oracle_manipulation_spot` | 0x2F: Oracle Manipulation: Spot Prices | How relying on Uniswap V2 reserves fails catastrophically (e.g. bZx hack). |
| `day48_oracle_manipulation_twap` | 0x30: Oracle Manipulation: TWAP & Multiblock | Defeating Time-Weighted Average Prices and complex AMM manipulation. |
| `day49_signature_replay` | 0x31: Signature Replay & Malleability Hacks | EIP-712 ecrecover risks, ECDSA malleability (e.g. OpenSea NFT thefts). |
| `day50_bridge_verifier` | 0x32: Cross-chain Bridge Hacks: Verifier Logic | Forged proofs, validator key compromises (e.g. Ronin, Poly Network). |
| `day51_bridge_logic` | 0x33: Cross-chain Bridge Hacks: Execution Logic | Exploiting bridging smart contracts logic errors (e.g. Nomad, Wormhole). |
| `day52_governance_attacks` | 0x34: Governance & DAO Attacks | Proposal payload manipulation, malicious upgrades, flash-loan voting (Beanstalk). |
| `day53_comp_reentrancy` | 0x35: DeFi Composability Risks: ERC777 | Reentrancy exploiting ERC777 hooks (e.g. imBTC, Cream Finance). |
| `day54_comp_yield` | 0x36: DeFi Composability Risks: Yield Aggregators | Vault inflation attacks, Yearn-style strategy manipulation. |
| `day55_accounting_precision` | 0x37: Accounting Logic Errors & Precision Loss | Rounding errors, division before multiplication, double-spending in DeFi. |

#### Phase 6: Secure Implementation & Best Practices (0x38 - 0x3C)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day56_openzeppelin` | 0x38: Secure Implementation: Standard Libraries | Properly leveraging OpenZeppelin's AccessControl, ReentrancyGuard, ERC20Permit. |
| `day57_proxy_patterns` | 0x39: Upgradeable Contracts: Proxies & UUPS | Transparent vs UUPS proxies, avoiding storage collisions, proxy admins. |
| `day58_initialization_safety` | 0x3A: Upgradeable Contracts: Initialization Risks | Protecting `initialize()`, constructor disabling, uninitialized implementations. |
| `day59_multisigs_timelocks` | 0x3B: Governance Control: Multisigs & Timelocks | Decentralizing admin rights using Safe (Gnosis), setting up governance delays. |
| `day60_incident_response` | 0x3C: Incident Response & Defensive Operations | Emergency pause triggers, monitoring tools, war rooms, and Bug Bounties (Immunefi). |

#### Phase 7: Vulnerability Lab — Fund Safety & External Calls (0x3D - 0x41)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_reentrancy_lab` | 0x3D: 🔬 Lab — Reentrancy Attack | Hand-write single-function & cross-function reentrancy vulnerable contracts and exploit contracts. Demonstrate how an attacker re-enters a function before state updates to drain funds. |
| `vuln_unchecked_call_lab` | 0x3E: 🔬 Lab — Unchecked Call Return Value | Hand-write contracts that silently ignore low-level `call`/`send` failures, and exploit contracts that leverage this to steal funds or corrupt state. |
| `vuln_selfdestruct_force_lab` | 0x3F: 🔬 Lab — Forced ETH via Selfdestruct | Hand-write contracts whose balance-dependent logic breaks when ETH is force-sent via `selfdestruct`, and exploit contracts that demonstrate the attack. |
| `vuln_flash_loan_lab` | 0x40: 🔬 Lab — Flash Loan Attack | Hand-write a simplified lending pool and an attacker contract that uses flash loans to manipulate protocol state or prices within a single transaction. |
| `vuln_oracle_manipulation_lab` | 0x41: 🔬 Lab — Price Oracle Manipulation | Hand-write a lending protocol using a vulnerable spot-price oracle and an exploit contract that manipulates the DEX reserve ratio to steal collateral. |

#### Phase 8: Vulnerability Lab — Permissions & Access Control (0x42 - 0x45)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_tx_origin_lab` | 0x42: 🔬 Lab — tx.origin Authentication Bypass | Hand-write a wallet contract using `tx.origin` for auth and a phishing contract that tricks the owner into calling it, draining the wallet. |
| `vuln_missing_access_control_lab` | 0x43: 🔬 Lab — Missing Access Control | Hand-write contracts with unprotected sensitive functions (withdraw, setOwner) and exploit contracts that call them directly. |
| `vuln_unprotected_initializer_lab` | 0x44: 🔬 Lab — Unprotected Initializer | Hand-write a proxy pattern where `initialize()` has no guard, and an exploit that front-runs initialization to hijack admin. |
| `vuln_delegatecall_hijack_lab` | 0x45: 🔬 Lab — Delegatecall Hijack | Hand-write a proxy that delegatecalls to an untrusted target, and an attacker contract that overwrites the proxy's storage slots to take ownership. |

#### Phase 9: Vulnerability Lab — Storage & EVM Mechanics (0x46 - 0x49)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_storage_visibility_lab` | 0x46: 🔬 Lab — Storage Visibility (Private ≠ Secret) | Hand-write contracts storing "secrets" in private variables, then use `forge`/`cast` to read raw storage slots and reveal them. |
| `vuln_storage_collision_lab` | 0x47: 🔬 Lab — Storage Collision in Proxies | Hand-write a proxy + logic contract pair with mismatched variable layouts, demonstrating how upgrades corrupt critical state data. |
| `vuln_uninitialized_storage_ptr_lab` | 0x48: 🔬 Lab — Uninitialized Storage Pointer | Hand-write contracts (targeting Solidity <0.5.0) where uninitialized local struct variables point to storage slot 0, allowing state corruption. |
| `vuln_dirty_storage_lab` | 0x49: 🔬 Lab — Dirty Storage (Residual Data) | Hand-write contracts that delete mappings or structs incompletely, leaving residual data that causes incorrect logic in subsequent operations. |

#### Phase 10: Vulnerability Lab — Business & Logic Errors (0x4A - 0x4C)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_integer_overflow_lab` | 0x4A: 🔬 Lab — Integer Overflow/Underflow | Hand-write pre-0.8.0 style contracts (using `unchecked` blocks) demonstrating how arithmetic wrapping zeroes out balances or inflates token supply. |
| `vuln_incorrect_logic_lab` | 0x4B: 🔬 Lab — Incorrect Logic Flow | Hand-write contracts with flawed `require` ordering, missing `else` branches, or inverted conditions that allow unintended state transitions. |
| `vuln_missing_validation_lab` | 0x4C: 🔬 Lab — Missing Parameter Validation | Hand-write contracts that fail to validate zero addresses, zero amounts, or array lengths, and exploit contracts that abuse these gaps. |

#### Phase 11: Vulnerability Lab — Randomness & Time Dependence (0x4D - 0x4E)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_weak_randomness_lab` | 0x4D: 🔬 Lab — Weak Randomness | Hand-write a lottery/gambling contract using `blockhash`/`block.number` as randomness, and an attacker contract that predicts the outcome. |
| `vuln_time_manipulation_lab` | 0x4E: 🔬 Lab — Timestamp Manipulation | Hand-write a time-locked vault relying on `block.timestamp`, and demonstrate how miners can adjust timestamps within allowed ranges to unlock early. |

#### Phase 12: Vulnerability Lab — Denial of Service (0x4F - 0x50)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_gas_limit_dos_lab` | 0x4F: 🔬 Lab — Gas Limit DoS | Hand-write a contract with unbounded loops processing an ever-growing array, and demonstrate how it becomes permanently stuck when gas exceeds block limit. |
| `vuln_revert_dos_lab` | 0x50: 🔬 Lab — Revert DoS (Griefing) | Hand-write a payout contract that iterates over recipients, and a malicious receiver contract that always reverts, blocking all payouts. |

#### Phase 13: Vulnerability Lab — Token & Standard Compatibility (0x51 - 0x54)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_signature_replay_lab` | 0x51: 🔬 Lab — Signature Replay/Forgery | Hand-write a meta-transaction contract missing nonce/chainID checks, and demonstrate replaying the same signature to double-spend. |
| `vuln_fee_on_transfer_lab` | 0x52: 🔬 Lab — Fee-on-Transfer Token Incompatibility | Hand-write a vault that assumes `transferFrom` delivers the exact amount, and a deflationary token that silently deducts fees, creating accounting gaps. |
| `vuln_erc4626_first_deposit_lab` | 0x53: 🔬 Lab — ERC4626 First Deposit Inflation Attack | Hand-write a minimal ERC4626 vault and demonstrate how an attacker inflates share price via tiny deposit + large donation to steal from subsequent depositors. |
| `vuln_missing_slippage_lab` | 0x54: 🔬 Lab — Missing Slippage Protection | Hand-write a DEX swap function without `minAmountOut`, and a sandwich attacker contract that front-runs and back-runs the victim's trade. |

#### Phase 14: Vulnerability Lab — Advanced Low-Level Pitfalls (0x55 - 0x57)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_encodepacked_collision_lab` | 0x55: 🔬 Lab — abi.encodePacked Hash Collision | Hand-write a contract using `abi.encodePacked` on variable-length args for signature verification, and demonstrate how different inputs produce identical hashes. |
| `vuln_extcodesize_bypass_lab` | 0x56: 🔬 Lab — Bypassing extcodesize Check | Hand-write a contract that blocks contract callers via `extcodesize == 0`, and an attacker that calls from its `constructor` where code size is 0. |
| `vuln_return_bomb_lab` | 0x57: 🔬 Lab — Return Value Bomb | Hand-write a contract that makes a low-level call to an external address, and a malicious callee that returns massive data to exhaust the caller's gas via memory expansion. |

#### Phase 15: Vulnerability Lab — System & Cross-Chain Architecture (0x58 - 0x59)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_crosschain_replay_lab` | 0x58: 🔬 Lab — Cross-chain Message Replay | Hand-write a simplified bridge contract without uniqueness validation, and demonstrate replaying a burn proof to claim tokens multiple times. |
| `vuln_rug_pull_risk_lab` | 0x59: 🔬 Lab — Centralization & Rug Pull Risk | Hand-write contracts with dangerous admin privileges (unlimited minting, fee modification, pause+drain), and analyze how to detect and mitigate these patterns. |

### Step 3 — Generate the Daily Learning Session

Generate a full, structured learning session directly inside the **`pages/web3/security/`** directory.

**Naming convention**: Use `YYYY-MM-DD_web3sec{NN}.md` where NN is a 2-digit sequence (usually 01 for the first topic of the day).
**File path**: `pages/web3/security/YYYY-MM-DD_web3sec01.md`  
(e.g., `pages/web3/security/2026-03-12_web3sec01.md`)

---

#### Output Format

**IMPORTANT — Jekyll Front-matter**:
Every generated `.md` file MUST begin with Jekyll front-matter so the page renders correctly on the GitHub Pages site:

```markdown
---
layout: default
title: "{Title}"
---

# Web3 Security Daily Learning

**Date**: YYYY-MM-DD  
**Topic**: {Title}  
**Phase**: {Phase Name}  

---

## 🧠 Concept Overview

**[CRITICAL: Do NOT output any "Welcome to" or AI intros. Immediately start the first sentence with a deep technical exploration of the topic.]**

[EXTREMELY exhaustive, step-by-step explanation of the concepts. Start from the absolute basics, then dive deep. Explain WHAT the vulnerability/concept is, WHY it exists at the EVM/Solidity architecture level, and HOW it operates or is exploited.]

---

## 🔑 Key Points

- [Key point 1]
- [Key point 2]
- [Key point 3]
- [Key point 4]
- [Key point 5]

---

## 💻 Code Deep Dive / Mechanics

### 🔴 Vulnerable Mechanism (or Core Concept)

\`\`\`solidity
// Vulnerable Smart Contract Code or Concept Code
// Provide heavily commented Solidity code showing the flaw or protocol design
\`\`\`

**Attack Vector / Analysis**: [Explain exactly how an attacker would exploit this code, or analyze the design flaw]

### 🟢 Secure Implementation (or Solution)

\`\`\`solidity
// Secure Smart Contract Code / Mitigation
// Demonstrate how to fix the vulnerability or implement safely
\`\`\`

**Why this is secure**: [Explain the mitigation mechanism]

---

## 🔬 Tooling, Auditing & PoC (Proof of Concept)

[Show how tools like Slither, Foundry `forge test`, or Mythril interact with this concept. Provide a PoC script if relevant.]

\`\`\`solidity
// Example Foundry Test Script
function testExploit() public {
    // Attack code here
}
\`\`\`

\`\`\`bash
# Expected output or command to run
forge test -vvvv --match-test testExploit
\`\`\`

---

## ⚠️ Real-World Impact (For Vulnerability Days)

| Real-World Hack | Loss | Root Cause / Post Mortem Link |
|-----------------|------|-------------------------------|
| [Project Name] | [$X Million] | [Brief description of what went wrong] |

---

## 🏋️ Practice Exercises & CTF Integration

Generate exactly 6 exercises. **For Phase 4 (CTF Range)**, focus heavily on breaking down the specific CTF challenge of the day.

### Exercise 1 — {Title} (Analysis)

**Goal**: [Analyze code/state to pinpoint the specific flaw]

**Hint**: [A subtle hint]

### Exercise 2 — {Title} (Environment Setup)

**Goal**: [Set up the Foundry/Hardhat environment to test this challenge]

**Instructions**:
1. [Setup instruction]
2. [Setup instruction]

### Exercise 3 — {Title} (Exploit Drafting)

**Goal**: [Draft the raw EVM/Solidity logic to compromise the target]

**Starter Code**:
\`\`\`solidity
contract Attacker {
    // TODO: Implement the exploit logic
}
\`\`\`

**Hint**: [A subtle hint]

### Exercise 4 — {Title} (Foundry Proof of Concept Execution)

**Goal**: [Write a complete Foundry test to confirm the exploit works locally]

**Hint**: [A subtle hint]

### Exercise 5 — {Title} (Secure the Code)

**Goal**: [Refactor the vulnerable contract to patch the flaw, maintaining intended business logic]

**Hint**: [A subtle hint]

### Exercise 6 — {Title} (Extended CTF Challenge / Alternative Vector)

**Goal**: [Refer to a harder variation or another public CTF challenge related to today's topic]

**Hint**: [A subtle hint]

---

## 📖 Reference & Further Reading

- [Solidity / EVM Documentation: {relevant page}]({url})
- [SWC Registry / Smart Contract Weakness Classification]({url})
- [DeFiHackLabs repository / Specific Hack Post-mortem]({url})

---

## 🗒️ Quick CLI / Foundry Cheat Sheet

\`\`\`bash
# Essential short commands for today's topic
\`\`\`

---

[← back to web3 security](./) | [← back to web3](..) | [← back to home](/)
```

---

#### Vulnerability Lab Output Format (Phase 7–15 ONLY)

For topics in **Phase 7 through Phase 15** (topic_keys starting with `vuln_`), use this **specialized template** instead of the standard template above. The emphasis is on **hand-writing vulnerable code and exploit code from scratch**.

```markdown
---
layout: default
title: "{Title}"
---

# 🔬 Vulnerability Lab: {Vulnerability Name}

**Date**: YYYY-MM-DD
**Topic**: {Title}
**Phase**: {Phase Name}
**Lab Type**: Hand-written Vulnerability & Exploit

---

## 📝 Vulnerability Overview

**[CRITICAL: Do NOT output any "Welcome to" or AI intros. Immediately start the first sentence with a deep technical exploration of the vulnerability.]**

[Exhaustive explanation of WHAT this vulnerability is, WHY it exists at the EVM/Solidity architecture level, HOW it is exploited in production, and what real-world impact it has caused. Include EVM opcode-level details where relevant.]

---

## 🔑 Key Takeaways

- [Key point 1: Root cause]
- [Key point 2: Attack preconditions]
- [Key point 3: Detection signals]
- [Key point 4: Mitigation pattern]
- [Key point 5: Related vulnerability classes]

---

## 🔴 Vulnerable Contract Example 1: {Scenario Title}

\`\`\`solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.x;

// COMPLETE, COMPILABLE, RUNNABLE vulnerable contract
// Heavily commented — explain exactly where the flaw is
// This must be a REAL, deployable contract (not pseudocode)
\`\`\`

**🔍 Vulnerability Analysis**:
- [Where exactly is the flaw?]
- [What preconditions enable exploitation?]
- [What is the attacker's goal?]

---

## 🔴 Vulnerable Contract Example 2: {Different Scenario Title}

\`\`\`solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.x;

// A DIFFERENT scenario demonstrating the SAME vulnerability class
// Must be a distinct contract with different business logic
\`\`\`

**🔍 Vulnerability Analysis**:
- [Where exactly is the flaw?]
- [How does this differ from Example 1?]

---

## ⚔️ Exploit Example 1: Attacking Vulnerable Contract 1

\`\`\`solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.x;

// COMPLETE attacker contract
// Must be runnable against Vulnerable Contract Example 1
contract Attacker1 {
    // Full exploit logic here
}
\`\`\`

### Foundry Test for Exploit 1

\`\`\`solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.x;

import "forge-std/Test.sol";

contract Exploit1Test is Test {
    function testExploit1() public {
        // 1. Deploy vulnerable contract
        // 2. Setup initial state
        // 3. Execute attack
        // 4. Assert attacker gained funds / state is corrupted
    }
}
\`\`\`

\`\`\`bash
forge test --match-test testExploit1 -vvvv
\`\`\`

**📋 Attack Walkthrough**:
1. [Step-by-step description of the attack flow]
2. [What happens at each EVM call frame]
3. [Final state after exploitation]

---

## ⚔️ Exploit Example 2: Attacking Vulnerable Contract 2

\`\`\`solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.x;

// COMPLETE attacker contract for a DIFFERENT approach or target
contract Attacker2 {
    // Full exploit logic here
}
\`\`\`

### Foundry Test for Exploit 2

\`\`\`solidity
contract Exploit2Test is Test {
    function testExploit2() public {
        // Full test setup and attack execution
    }
}
\`\`\`

\`\`\`bash
forge test --match-test testExploit2 -vvvv
\`\`\`

**📋 Attack Walkthrough**:
1. [Step-by-step]

---

## 🟢 Secure Implementation

### Fix for Vulnerable Contract 1

\`\`\`solidity
// Patched version of Vulnerable Contract 1
// Highlight the specific lines that changed with comments
\`\`\`

### Fix for Vulnerable Contract 2

\`\`\`solidity
// Patched version of Vulnerable Contract 2
\`\`\`

**✅ Why these fixes work**:
- [Explain the mitigation mechanism for each fix]
- [Reference industry best practices: OpenZeppelin, Checks-Effects-Interactions, etc.]

---

## ⚠️ Real-World Impact

| Real-World Hack | Loss | Root Cause |
|-----------------|------|------------|
| [Project Name] | [$X Million] | [Brief description] |
| [Project Name] | [$X Million] | [Brief description] |

---

## 🏋️ Practice Exercise: {Challenge Title}

**Scenario**: [Describe a new vulnerable contract the user must analyze and exploit]

\`\`\`solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.x;

// TARGET CONTRACT — Find and exploit the vulnerability!
// The user should write their own attacker contract and Foundry test
contract PracticeTarget {
    // ... vulnerable code ...
}
\`\`\`

**🎯 Goal**: [What the user needs to achieve — e.g., drain all ETH, become owner, etc.]

**💡 Hint**: [A subtle hint without giving away the answer]

<details>
<summary>📖 Click to reveal solution</summary>

\`\`\`solidity
// Solution: Attacker contract
contract PracticeSolution {
    // ...
}
\`\`\`

\`\`\`solidity
// Solution: Foundry test
contract PracticeTest is Test {
    function testPracticeExploit() public {
        // ...
    }
}
\`\`\`

</details>

---

## 📖 Reference & Further Reading

- [SWC Registry: {relevant entry}]({url})
- [OpenZeppelin Security Advisories]({url})
- [DeFiHackLabs: {relevant hack reproduction}]({url})

---

## 🗒️ Quick CLI Cheat Sheet

\`\`\`bash
# Essential Foundry commands for this lab
\`\`\`

---

[← back to web3 security](./) | [← back to web3](..) | [← back to home](/)
```

---

### Step 4 — Update history.yaml

After generating the session file, **append** a new entry to `history.yaml`:

```yaml
# Example structure of history.yaml
- date: "2026-03-12"
  topic_key: "day01_blockchain_basics"
  title: "0x01: Blockchain Basics, Consensus, & P2P"
  category: "Phase 1: Web3 Fundamentals & Demos"
  file: "pages/web3/security/2026-03-12_web3sec01.md"
```

**Rules**:
- Always append; never overwrite existing entries
- If `history.yaml` does not exist, create it with proper YAML formatting
- Use `"YYYY-MM-DD"` date string format (quoted for YAML safety)

### Step 5 — Confirm to the User

After generating the file and updating history, tell the user:

1. **Today's topic**: The title and phase
2. **File created**: The path to the session file
3. **Progress**: How many topics have been covered so far (e.g., "1 / 60 topics completed")
4. **Streak reminder**: The date of their last session
5. **Quick start**: Suggest they open the file and dive into the specific Web3 security module.

## Content Quality Guidelines

### Tone & Style
- **Tone**: Use a warm, human-like, and conversational tone. Write like a friendly senior Smart Contract Auditor, Whitehat Hacker, or CTF veteran mentoring a colleague.
- **Exhaustive Content Length**: You MUST generate extremely long, exhaustive content to ensure absolutely NO knowledge points are missed. Dive deeply into opcode-level interactions, EVM memory/storage details, and edge cases.
- **Natural Delivery**: Avoid clichéd AI intros. Get straight to the technical deep dive while remaining engaging.

### Concept Explanations
- **Deep Technical Accuracy**: Ensure that Solidity code uses recent versions (typically `^0.8.0` unless explicitly demonstrating `<0.8.0` vulnerabilities like arithmetic overflow).
- **EVM-Level Insight**: For Phase 4 and Phase 5 especially, explain the EVM context—why does a `delegatecall` behave the way it does? How is context `msg.value` preserved? How do storage slots clash exactly?

### Code Examples
- **Volume & Variety**: Provide multiple Solidity examples, contrasting vulnerable code with secure implementations.
- Include Foundry `forge` / `cast` CLI commands and test script structures extensively. Local testing with Foundry is the industry standard for CTFs.

### Exercises
- **Volume (Phase 1–6)**: Generate exactly **6 practice exercises/CTF challenges** per daily session, scaling from simple code inspection to full PoC (Proof of Concept) implementation. Ensure the steps guide the user toward getting a local fork working.
- **Volume (Phase 7–15 Vulnerability Labs)**: Generate exactly **2 vulnerable contract examples**, **2 exploit examples** (with full Foundry tests), and **1 practice exercise** (with hidden solution). All code must be **complete, compilable, and runnable** — no pseudocode or stubs.

### File Organization

```
# Skill files (auto-generated)
.agent/skills/web3-security/
├── SKILL.md              ← This file
└── history.yaml          ← Auto-managed learning history

# Generated articles go here (GitHub Pages site)
pages/web3/security/
├── index.md              # Directory index (if you wish to configure it)
├── YYYY-MM-DD_web3sec01.md   # Session file for that day
└── ...
```

## Error Handling

- If `history.yaml` is not parseable, warn the user and start with an empty history
- If all 89 intensive topics are covered, congratulate the user!
- If the user requests a specific topic (even if already covered), generate it but note it was covered before.
