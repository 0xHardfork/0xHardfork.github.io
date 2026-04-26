---
name: web3-security
description: Daily Web3 Security learning skill that generates a 107-day intensive curriculum. Extensively covers blockchain basics, DeFi protocol internals (Uniswap, Aave, Curve), auditing tools (Slither, Aderyn, Foundry, Echidna, Halmos, Certora), in-depth CTF target range setup & walkthroughs (Ethernaut, Damn Vulnerable DeFi v4), advanced attacks (MEV, L2, ERC-4337, bridge hacks, combo attacks), mainnet forensics & hack replay, secure implementation, and 30 hands-on vulnerability labs with runnable exploit code. Outputs content directly into the pages/web3/security/ directory.
---

# Web3 Security Daily Learning Skill

This skill helps you learn Web3, Smart Contracts, and Smart Contract Security one topic per day over a **107-day** intensive course. It begins with foundational concepts and DeFi protocol internals, progresses to code auditing, heavily emphasizes hands-on CTF exercises and advanced real-world attack vectors, includes mainnet attack forensics & replay, and culminates with **30 vulnerability deep-dive labs** where you hand-write vulnerable contracts and exploits from scratch.

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

**Topic Curriculum (The 107-Day Intensive Track):**

#### Phase 1: Web3 Fundamentals & Demos (0x01 - 0x0A)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `day01_blockchain_basics` | 0x01: Blockchain Basics, Consensus, & P2P | Blocks, transactions, state machine basics, and consensus mechanisms. |
| `day02_ethereum_architecture` | 0x02: Ethereum Architecture & Accounts | EOA vs Smart Contracts, Nonce, Gas limitations, and network structure. |
| `day03_crypto_basics` | 0x03: Cryptography Basics | Hash functions (Keccak256), Elliptic Curve cryptography, and ECDSA basics. |
| `day04_evm_deepdive` | 0x04: EVM Storage, Memory, & Calldata | EVM memory layout, storage slots packing, and calldata structure. |
| `day05_solidity_basics1` | 0x05: Solidity Fundamentals I | Data types, state variables, visibility modifiers, and mappings. |
| `day06_solidity_basics2` | 0x06: Solidity Fundamentals II | Functions, custom modifiers, events, interfaces, and custom errors. |
| `day07_foundry_setup` | 0x07: Development Environment: Foundry | Using forge, cast, and anvil for an ultra-fast local blockchain environment. The primary tool for security auditing & CTFs. |
| `day08_hardhat_setup` | 0x08: Development Environment: Hardhat & Deployment Toolchain | Setting up Hardhat, local node, ethers.js, and deployment scripts. Useful for project deployment alongside Foundry. |
| `day09_erc20_deepdive` | 0x09: Token Standards: ERC20 Sandbox | Minting, transferring, approvals, and the `transferFrom` pattern. |
| `day10_erc721_1155` | 0x0A: Token Standards: ERC721 & ERC1155 | NFTs, metadata, and multi-token standard architectures. |

#### Phase 2: DeFi Protocol Internals (0x0B - 0x0D)

*You cannot audit what you don't understand. This phase builds "protocol thinking" — the ability to read and reason about real DeFi architecture before hunting for vulnerabilities. Exercises require reading real protocol source code (Uniswap, Aave).*

| topic_key | Title | Description |
|-----------|-------|-------------|
| `defi01_amm_dex` | 0x0B: DeFi Internals: AMM & DEX | Constant product formula (x*y=k), Uniswap V2 architecture, V3 concentrated liquidity, LP token mechanics, fee tiers, price impact. Includes reading real Uniswap V2 Router/Pair source code. |
| `defi02_lending` | 0x0C: DeFi Internals: Lending, Liquidation & Stablecoins | Aave/Compound architecture: supply, borrow, health factor, liquidation mechanics, interest rate models. MakerDAO CDPs, DAI peg. Includes reading real Aave V3 Pool source code. |
| `defi03_vaults_standards` | 0x0D: DeFi Internals: Vaults, Staking & Advanced Token Standards | ERC4626 vault mechanics, Yearn-style yield strategies, staking reward distribution (Synthetix model). ERC777 hooks, ERC1363 callbacks, Uniswap Permit2 architecture. |

#### Phase 3: Common Vulnerabilities & Exploits (0x0E - 0x17)

*Ordered by ascending conceptual difficulty. Front-running/MEV moved to Phase 6 (Advanced Attacks).*

| topic_key | Title | Description |
|-----------|-------|-------------|
| `day11_reentrancy_basics` | 0x0E: Reentrancy Attacks | Single-function & Cross-function reentrancy, Checks-Effects-Interactions pattern. |
| `day12_arithmetic` | 0x0F: Integer Overflow & Underflow | Pre-0.8.0 math vulnerabilities vs Solidity 0.8.0+ `unchecked` blocks. |
| `day13_access_control` | 0x10: Access Control & `tx.origin` | Why `tx.origin` is dangerous for authorization; `ecrecover` pitfalls. |
| `day14_unsafe_calls` | 0x11: Return Value Ignored & Unsafe External Calls | Forgetting to check return values of low-level `call`, `send`, or ERC20 transfers. |
| `day15_dos` | 0x12: Denial of Service (DoS) Vulnerabilities | Unexpected reverts, out-of-gas, and traversing unbounded arrays. |
| `day16_randomness` | 0x13: Timestamp Dependence & Bad Randomness | Manipulating `block.timestamp`/`blockhash`; introduction to Chainlink VRF. |
| `day17_delegatecall` | 0x14: Unsafe `delegatecall` | Context preservation, proxy vulnerability patterns, and library exploitation. |
| `day18_storage_collisions` | 0x15: Uninitialized Storage Pointers & Collisions | How uninitialized variables can overwrite critical contract storage slots. |
| `day19_reentrancy_advanced` | 0x16: Cross-Contract & Read-only Reentrancy | Complex state inconsistency across multiple contracts, read-only attacks. |
| `day20_accounting_precision` | 0x17: Accounting Logic Errors & Precision Loss | Rounding errors, division before multiplication, double-spending in DeFi protocols. |

#### Phase 4: Smart Contract Code Auditing Tools (0x18 - 0x20)

*9 days: static analysis, fuzzing, formal verification, manual methodology, and on-chain intelligence.*

| topic_key | Title | Description |
|-----------|-------|-------------|
| `day21_slither_aderyn` | 0x18: Static Analysis: Slither & Aderyn | Automating vulnerability hunting with Slither's detectors and the Rust-based Aderyn analyzer. |
| `day22_symbolic_exec` | 0x19: Symbolic Execution with Mythril & Manticore | Exploring edge cases mathematically through symbolic execution. |
| `day23_foundry_fuzzing` | 0x1A: Fuzz Testing with Foundry | Writing property-based and invariant tests using Foundry. |
| `day24_echidna_medusa` | 0x1B: Advanced Fuzzing: Echidna & Medusa | State machine testing, complex invariant fuzzing, and parallel fuzzing with Medusa. |
| `day25_halmos_certora` | 0x1C: Symbolic Testing: Halmos & Certora Basics | Foundry-native symbolic testing with Halmos; introduction to Certora Prover for formal verification. |
| `day26_manual_audit` | 0x1D: Manual Audit Methodology, Severity Rating & Threat Modeling | Attack surface mapping, business logic analysis, CVSS-like severity classification (Critical/High/Medium/Low/Informational/Gas), and professional report writing. |
| `day27_solodit_reports` | 0x1E: Reading Real Audit Reports & Using Solodit | Studying past findings on Solodit, understanding severity classification, and learning from professional audit report formats. |
| `day_onchain_intel` | 0x1F: On-chain Intelligence: Tenderly, Dune, Etherscan & BlockSec | Transaction tracing with Tenderly, data analysis with Dune Analytics, advanced Etherscan usage (internal txns, token flow), Phalcon/BlockSec for incident analysis. Bridges Web2 security investigation skills to on-chain forensics. |
| `day_finding_writing` | 0x20: Audit Finding Writing Workshop | Structured practice writing professional audit findings: severity, impact, PoC, mitigation. From Phase 5 onward, every exercise must output at least one finding in this format. |

#### Phase 5: Target Range Setup & CTF Practice (0x21 - 0x37)

*Covers all 32 Ethernaut levels and Damn Vulnerable DeFi v4 (including new challenges).*

| topic_key | Title | Description |
|-----------|-------|-------------|
| `day28_ctf_setup` | 0x21: CTF Local Range Setup | Forking mainnet, setting up foundry scripts for remote/local CTF solving. |
| `day29_ethernaut_1` | 0x22: Ethernaut Part 1 | Fallback, Fallout, CoinFlip, Telephone. Basic state & access exploitation. |
| `day30_ethernaut_2` | 0x23: Ethernaut Part 2 | Token, Delegation, Force, Vault. Overflows, forced ether, storage reading. |
| `day31_ethernaut_3` | 0x24: Ethernaut Part 3 | King, Re-entrancy, Elevator, Privacy. DoS, reentrancy limits, memory offsets. |
| `day32_ethernaut_4` | 0x25: Ethernaut Part 4 | Gatekeeper One & Two, Naught Coin. Gas mechanics, bitwise masks, EVM `extcodesize`. |
| `day33_ethernaut_5` | 0x26: Ethernaut Part 5 | Preservation, Recovery, MagicNumber. Delegatecall routing, raw EVM bytecode. |
| `day34_ethernaut_6` | 0x27: Ethernaut Part 6 | Alien Codex, Denial, Shop. Dynamic array underflows, assert limits, external calls. |
| `day35_ethernaut_7` | 0x28: Ethernaut Part 7 | Dex, Dex Two, Puzzle Wallet. AMM math bugs, proxy-logic collisions. |
| `day36_ethernaut_8` | 0x29: Ethernaut Part 8 | Motorbike, DoubleEntryPoint, Good Samaritan. UUPS initialization fixes, custom errors. |
| `day37_ethernaut_9` | 0x2A: Ethernaut Part 9 | Gatekeeper Three, Switch, Higher Order, Stake. Advanced bytecode, calldata tricks, staking edge cases. |
| `day38_cte` | 0x2B: Capture The Ether Highlights | Solving specific math and warmup challenges in CTE. |
| `day39_dvdf_unstoppable` | 0x2C: Damn Vulnerable DeFi - Unstoppable | Accounting mismatches, vault exploitation, flash loan DoS. |
| `day40_dvdf_naive_receiver` | 0x2D: Damn Vulnerable DeFi - Naive Receiver | Flash loan griefing attacks and unsafe interfaces. |
| `day41_dvdf_truster` | 0x2E: Damn Vulnerable DeFi - Truster | Malicious external calls via low-level execution within flash loans. |
| `day42_dvdf_side_entrance` | 0x2F: Damn Vulnerable DeFi - Side Entrance | Reentrancy into flash loan deposits, accounting bypass. |
| `day43_dvdf_rewarder` | 0x30: Damn Vulnerable DeFi - The Rewarder | Manipulating snapshot-based governance/rewards using flash loans. |
| `day44_dvdf_selfie_compromised` | 0x31: Damn Vulnerable DeFi - Selfie & Compromised | Governance takeover via flash loans; Oracle manipulation using leaked keys. |
| `day45_dvdf_puppet` | 0x32: Damn Vulnerable DeFi - Puppet & Puppet V2 | Spot price manipulation on Uniswap V1 & V2. |
| `day46_dvdf_free_rider` | 0x33: Damn Vulnerable DeFi - Free Rider | Flash swaps, NFT marketplace vulnerabilities, checking `msg.value`. |
| `day47_dvdf_backdoor` | 0x34: Damn Vulnerable DeFi - Backdoor | Gnosis Safe proxy wallet initialization exploits. |
| `day48_dvdf_climber` | 0x35: Damn Vulnerable DeFi - Climber | Timelock contract vulnerabilities and execution sequence manipulation. |
| `day49_dvdf_wallet_mining` | 0x36: Damn Vulnerable DeFi v4 - Wallet Mining & Shards | CREATE2 address mining, vanity address prediction, ERC-1155 marketplace vulnerabilities. |
| `day50_dvdf_advanced` | 0x37: Damn Vulnerable DeFi v4 - Curvy Puppet & Withdrawal | Complex Curve/oracle manipulation, L1/L2 bridge withdrawal exploits. |

#### Phase 6: Advanced Attacks & Real-world Cases (0x38 - 0x44)

*MEV moved here from old Phase 2. Added cross-chain fundamentals, L2/Rollup security, ERC-4337, and multi-step combo attack training.*

| topic_key | Title | Description |
|-----------|-------|-------------|
| `day51_flash_loans_adv` | 0x38: Advanced Flash Loan Arbitrage | In-depth mechanics of Aave/Balancer flash loans empowering complex attacks. |
| `day52_oracle_manipulation_spot` | 0x39: Oracle Manipulation: Spot Prices | How relying on Uniswap V2 reserves fails catastrophically (e.g. bZx hack). |
| `day53_oracle_manipulation_twap` | 0x3A: Oracle Manipulation: TWAP & Multiblock | Defeating Time-Weighted Average Prices and complex AMM manipulation. |
| `day54_mev_frontrunning` | 0x3B: Front-Running, MEV & Sandwich Attacks | Transaction ordering, priority gas auctions, sandwiching, Flashbots Protect, PBS. Includes Foundry-based MEV simulation exercises. |
| `day55_signature_replay` | 0x3C: Signature Replay & Malleability Hacks | EIP-712 ecrecover risks, ECDSA malleability (e.g. OpenSea NFT thefts). |
| `day56_crosschain_fundamentals` | 0x3D: Cross-chain Fundamentals & Bridge Architecture | Messaging protocols, relayer infrastructure, lock-and-mint vs burn-and-mint, trust assumptions. |
| `day57_bridge_hacks` | 0x3E: Cross-chain Bridge Hacks: Verifier & Execution Logic | Forged proofs, validator key compromises (Ronin, Poly Network), logic errors (Nomad, Wormhole). |
| `day58_governance_attacks` | 0x3F: Governance & DAO Attacks | Proposal payload manipulation, malicious upgrades, flash-loan voting (Beanstalk). |
| `day59_composability` | 0x40: DeFi Composability Risks: ERC-777 & Yield Aggregators | Reentrancy via ERC-777 hooks (imBTC, Cream); vault inflation, Yearn-style strategy manipulation. |
| `day60_l2_rollup_security` | 0x41: L2/Rollup Security: Sequencers, Escape Hatches & Fraud Proofs | Sequencer centralization, L2 escape hatch design, optimistic rollup fraud proofs, ZK-rollup proof verification. |
| `day61_erc4337_security` | 0x42: ERC-4337 Account Abstraction Security | Smart account attack surfaces: validateUserOp bypass, Paymaster draining, bundler manipulation, initialization hijacking. |
| `day_combo_attack_1` | 0x43: Multi-step Attack Chains I | Combining flash loan + oracle manipulation + governance in a single exploit chain. Reproduce real-world multi-vector attacks (e.g. Beanstalk, Euler Finance). Write full Foundry PoC. |
| `day_combo_attack_2` | 0x44: Multi-step Attack Chains II | Combining reentrancy + accounting bugs + cross-contract calls. Design and execute novel 3+ step exploit chains against a provided multi-contract DeFi protocol. |

#### Phase 7: Mainnet Forensics & Attack Replay (0x45 - 0x46)

*Real auditors analyze messy mainnet state, not clean CTF setups. This phase bridges the gap from "CTF solver" to "incident responder".*

| topic_key | Title | Description |
|-----------|-------|-------------|
| `day_forensics_replay` | 0x45: Mainnet Forensics: Transaction Replay & Trace Analysis | Using Foundry fork mode and Tenderly to replay historical attack transactions. `debug_traceTransaction` analysis, call tree reconstruction, storage diff inspection. Reproduce a real hack tx step-by-step. |
| `day_forensics_postmortem` | 0x46: Historical Hack Reproduction & Post-mortem Deep Dive | Select 2-3 major hacks (e.g. Euler $197M, Curve $70M, Ronin $625M), fork mainnet at pre-attack block, reproduce the exact exploit in Foundry, write a professional post-mortem report with finding-format output. |

#### Phase 8: Secure Implementation & Best Practices (0x47 - 0x4D)

*Expanded to cover gas/Yul security trade-offs and audit competition preparation.*

| topic_key | Title | Description |
|-----------|-------|-------------|
| `day62_openzeppelin` | 0x47: Secure Implementation: Standard Libraries | Properly leveraging OpenZeppelin's AccessControl, ReentrancyGuard, ERC20Permit. |
| `day63_proxy_patterns` | 0x48: Upgradeable Contracts: Proxies & UUPS | Transparent vs UUPS proxies, avoiding storage collisions, proxy admins. |
| `day64_initialization_safety` | 0x49: Upgradeable Contracts: Initialization Risks | Protecting `initialize()`, constructor disabling, uninitialized implementations. |
| `day65_gas_yul_security` | 0x4A: Gas Optimization, Yul/Assembly & Transient Storage Security | When gas optimization introduces security bugs; `unchecked` misuse; Yul safety; TSTORE/TLOAD implications. |
| `day66_multisigs_timelocks` | 0x4B: Governance Control: Multisigs & Timelocks | Decentralizing admin rights using Safe (Gnosis), setting up governance delays. |
| `day67_incident_response` | 0x4C: Incident Response & Defensive Operations | Emergency pause triggers, monitoring tools (Forta, OpenZeppelin Defender), war rooms, Bug Bounties (Immunefi). |
| `day68_audit_competition_prep` | 0x4D: Audit Competition Preparation: Code4rena, Sherlock & Immunefi | How to participate in competitive audits, write professional findings, and build a public security portfolio. |

#### Phase 9: Vulnerability Lab — Fund Safety & External Calls (0x4E - 0x52)

*In Phase 3 you learned concepts; labs require writing COMPLETE multi-contract DeFi exploit scenarios from scratch with Foundry tests.*

| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_reentrancy_lab` | 0x4E: Lab — Reentrancy Attack | Hand-write a multi-contract DeFi protocol with cross-function reentrancy, and a full exploit chain. Goes beyond Phase 3's single-contract examples. |
| `vuln_unchecked_call_lab` | 0x4F: Lab — Unchecked Call Return Value | Hand-write contracts that silently ignore low-level `call`/`send` failures, and exploit contracts that leverage this. |
| `vuln_selfdestruct_force_lab` | 0x50: Lab — Forced ETH via Selfdestruct | Hand-write contracts whose balance-dependent logic breaks when ETH is force-sent via `selfdestruct`. |
| `vuln_flash_loan_lab` | 0x51: Lab — Flash Loan Attack | Hand-write a simplified lending pool and an attacker contract using flash loans to manipulate state. |
| `vuln_oracle_manipulation_lab` | 0x52: Lab — Price Oracle Manipulation | Hand-write a lending protocol with vulnerable spot-price oracle and an exploit that manipulates DEX reserves. |

#### Phase 10: Vulnerability Lab — Permissions & Access Control (0x53 - 0x57)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_tx_origin_lab` | 0x53: Lab — tx.origin Authentication Bypass | Hand-write a wallet using `tx.origin` for auth and a phishing contract that drains the wallet. |
| `vuln_missing_access_control_lab` | 0x54: Lab — Missing Access Control | Hand-write contracts with unprotected sensitive functions and exploit contracts that call them directly. |
| `vuln_unprotected_initializer_lab` | 0x55: Lab — Unprotected Initializer | Hand-write a proxy where `initialize()` has no guard, and an exploit that front-runs initialization. |
| `vuln_delegatecall_hijack_lab` | 0x56: Lab — Delegatecall Hijack | Hand-write a proxy that delegatecalls to an untrusted target, overwriting storage slots to take ownership. |
| `vuln_uups_takeover_lab` | 0x57: Lab — UUPS Proxy Takeover | Hand-write an uninitialized UUPS implementation and demonstrate how an attacker calls `initialize()` directly then `upgradeToAndCall()` to brick all proxies. Wormhole-class pattern. |

#### Phase 11: Vulnerability Lab — Storage & EVM Mechanics (0x58 - 0x5A)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_storage_visibility_lab` | 0x58: Lab — Storage Visibility (Private != Secret) | Hand-write contracts storing "secrets" in private variables, then use `forge`/`cast` to read raw storage slots. |
| `vuln_storage_collision_lab` | 0x59: Lab — Storage Collision in Proxies | Hand-write a proxy + logic pair with mismatched layouts, demonstrating how upgrades corrupt state. |
| `vuln_uninitialized_storage_ptr_lab` | 0x5A: Lab — Uninitialized Storage Pointer | Hand-write contracts (Solidity <0.5.0) where uninitialized local structs point to storage slot 0. |

#### Phase 12: Vulnerability Lab — Business & Logic Errors (0x5B - 0x5D)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_incorrect_logic_lab` | 0x5B: Lab — Incorrect Logic Flow | Hand-write contracts with flawed `require` ordering, missing `else` branches, or inverted conditions. |
| `vuln_missing_validation_lab` | 0x5C: Lab — Missing Parameter Validation | Hand-write contracts failing to validate zero addresses, zero amounts, or array lengths. |
| `vuln_erc777_reentrancy_lab` | 0x5D: Lab — ERC-777 Hook Reentrancy | Hand-write ERC-777 token with `tokensReceived` hook and exploit via re-entry during transfers. imBTC/Cream pattern. |

#### Phase 13: Vulnerability Lab — Randomness (0x5E)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_weak_randomness_lab` | 0x5E: Lab — Weak Randomness | Hand-write a lottery using `blockhash`/`block.number` as randomness, and an attacker that predicts outcomes. |

#### Phase 14: Vulnerability Lab — Denial of Service (0x5F - 0x60)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_gas_limit_dos_lab` | 0x5F: Lab — Gas Limit DoS | Hand-write a contract with unbounded loops that becomes permanently stuck when gas exceeds block limit. |
| `vuln_revert_dos_lab` | 0x60: Lab — Revert DoS (Griefing) | Hand-write a payout contract and a malicious receiver that always reverts, blocking all payouts. |

#### Phase 15: Vulnerability Lab — Token & Standard Compatibility (0x61 - 0x64)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_signature_replay_lab` | 0x61: Lab — Signature Replay/Forgery | Hand-write a meta-transaction contract missing nonce/chainID checks, demonstrate replay double-spend. |
| `vuln_fee_on_transfer_lab` | 0x62: Lab — Fee-on-Transfer Token Incompatibility | Hand-write a vault assuming exact `transferFrom` delivery, and a deflationary token creating accounting gaps. |
| `vuln_erc4626_first_deposit_lab` | 0x63: Lab — ERC4626 First Deposit Inflation Attack | Hand-write a minimal ERC4626 vault and demonstrate share price inflation via tiny deposit + large donation. |
| `vuln_missing_slippage_lab` | 0x64: Lab — Missing Slippage Protection | Hand-write a DEX swap without `minAmountOut`, and a sandwich attacker that front/back-runs the victim. |

#### Phase 16: Vulnerability Lab — Advanced Low-Level Pitfalls (0x65 - 0x67)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_encodepacked_collision_lab` | 0x65: Lab — abi.encodePacked Hash Collision | Hand-write a contract using `abi.encodePacked` for signature verification, demonstrate hash collisions. |
| `vuln_extcodesize_bypass_lab` | 0x66: Lab — Bypassing extcodesize Check | Hand-write a contract blocking contract callers, and an attacker calling from its `constructor`. |
| `vuln_return_bomb_lab` | 0x67: Lab — Return Value Bomb | Hand-write a contract making a low-level call, and a malicious callee returning massive data to exhaust gas. |

#### Phase 17: Vulnerability Lab — System, Cross-Chain & Governance (0x68 - 0x6B)
| topic_key | Title | Description |
|-----------|-------|-------------|
| `vuln_crosschain_replay_lab` | 0x68: Lab — Cross-chain Message Replay | Hand-write a simplified bridge without uniqueness validation, demonstrate replaying burn proofs. |
| `vuln_rug_pull_risk_lab` | 0x69: Lab — Centralization & Rug Pull Risk | Hand-write contracts with dangerous admin privileges (unlimited minting, pause+drain), analyze detection. |
| `vuln_governance_flashloan_lab` | 0x6A: Lab — Governance Flash-Loan Takeover | Hand-write governance token + DAO proposal system, flash-loan tokens to pass malicious proposal. Beanstalk ($182M) pattern. |
| `vuln_permit_phishing_lab` | 0x6B: Lab — Permit (EIP-2612) Phishing | Hand-write ERC20Permit token and phishing contract that tricks users into signing off-chain `permit` approvals. |


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

For topics in **Phase 9 through Phase 17** (topic_keys starting with `vuln_`), use this **specialized template** instead of the standard template above. The emphasis is on **hand-writing vulnerable code and exploit code from scratch**. These labs start at hex 0x4E.

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
3. **Progress**: How many topics have been covered so far (e.g., "1 / 107 topics completed")
4. **Streak reminder**: The date of their last session
5. **Quick start**: Suggest they open the file and dive into the specific Web3 security module.

## Content Quality Guidelines

### Tone & Style
- **Tone**: Use a warm, human-like, and conversational tone. Write like a friendly senior Smart Contract Auditor, Whitehat Hacker, or CTF veteran mentoring a colleague.
- **Exhaustive Content Length**: You MUST generate extremely long, exhaustive content to ensure absolutely NO knowledge points are missed. Dive deeply into opcode-level interactions, EVM memory/storage details, and edge cases.
- **Natural Delivery**: Avoid clichéd AI intros. Get straight to the technical deep dive while remaining engaging.

### Concept Explanations
- **Deep Technical Accuracy**: Ensure that Solidity code uses recent versions (typically `^0.8.0` unless explicitly demonstrating `<0.8.0` vulnerabilities like arithmetic overflow).
- **EVM-Level Insight**: For Phase 5 and Phase 6 especially, explain the EVM context—why does a `delegatecall` behave the way it does? How is context `msg.value` preserved? How do storage slots clash exactly?
- **Protocol Context**: For DeFi-related topics, always explain the protocol mechanics (AMM math, lending health factors) before the vulnerability. Students must understand what they're breaking.

### Code Examples
- **Volume & Variety**: Provide multiple Solidity examples, contrasting vulnerable code with secure implementations.
- Include Foundry `forge` / `cast` CLI commands and test script structures extensively. Local testing with Foundry is the industry standard for CTFs.
- **Real Code Reading**: Where relevant (especially Phase 2, Phase 5 CTFs), reference real protocol source code (OpenZeppelin, Uniswap, Aave) and guide students to read specific contracts.

### Exercises
- **Volume (Phase 1–8)**: Generate exactly **6 practice exercises/CTF challenges** per daily session, scaling from simple code inspection to full PoC (Proof of Concept) implementation. Ensure the steps guide the user toward getting a local fork working.
- **Runnable PoC from Phase 3**: From Phase 3 (Vulnerabilities) onward, at least 2 of the 6 exercises MUST require writing a runnable Foundry test that demonstrates the exploit. Students should not just read about attacks — they must write working exploit code from the start.
- **Finding-Format Output from Phase 5**: From Phase 5 (CTF) onward, at least 1 exercise per session MUST require the student to write a professional audit finding with: Severity, Title, Impact, Root Cause, PoC (Foundry test), and Mitigation.
- **Volume (Phase 9–17 Vulnerability Labs)**: Generate exactly **2 vulnerable contract examples**, **2 exploit examples** (with full Foundry tests), and **1 practice exercise** (with hidden solution). All code must be **complete, compilable, and runnable** — no pseudocode or stubs.

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
- If all 107 intensive topics are covered, congratulate the user!
- If the user requests a specific topic (even if already covered), generate it but note it was covered before.
