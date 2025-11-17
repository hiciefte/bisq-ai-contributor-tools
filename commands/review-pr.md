---
name: review-pr
description: Comprehensive PR review checker that extracts ALL review comments from CodeRabbitAI and other reviewers, categorizes them, and ensures nothing is missed
---

# Comprehensive PR Review Handler

You are tasked with comprehensively reviewing ALL comments on a GitHub PR and ensuring NOTHING is missed.

## ⚠️ CRITICAL: MANDATORY PHASES

You MUST complete each phase in order and SHOW PROOF of completion. Do NOT skip ahead. Do NOT summarize - show actual data.

---

## PHASE 0: GITHUB ACTIONS CHECK (MUST CHECK FIRST)

### 0.1 Check CI/CD Status

**Before reviewing any comments, check if the PR has passing builds:**

```bash
# Get PR details including CI status
gh pr view {pr_number} --repo {owner}/{repo} --json statusCheckRollup,url > /tmp/pr_{pr}_status.json

# List recent workflow runs for this PR's branch
gh run list --repo {owner}/{repo} --branch {branch} --limit 5 --json status,conclusion,name,createdAt,databaseId
```

### 0.2 PROOF OF CI STATUS REQUIRED

You MUST show:

```markdown
## GitHub Actions Status

**PR Branch**: {branch_name}
**Recent Workflow Runs**:
1. Run ID: {id} - Name: {name} - Status: {status} - Conclusion: {conclusion}
2. ...

**Failing Runs**: {count}
**Latest Failure**: {run_id} if any

**⚠️ CI FAILURES DETECTED**: YES/NO
```

### 0.3 If CI Failing, Get Failure Details

```bash
# If there are failing runs, get the logs
gh run view {failing_run_id} --repo {owner}/{repo} --log-failed > /tmp/pr_{pr}_ci_failure.log
```

**Show first 100 lines of failure:**
```
[PASTE FIRST 100 LINES OF FAILURE LOG]
```

**⚠️ DO NOT PROCEED TO PHASE 1 UNTIL CI STATUS IS DOCUMENTED**

---

## PHASE 0.5: GET LATEST COMMIT TIMESTAMP (EFFICIENCY OPTIMIZATION)

**Purpose**: Only process NEW comments posted after the latest commit to avoid re-verifying already-addressed feedback.

### 0.5.1 Get Latest Commit Timestamp

```bash
# Get the most recent commit timestamp on this PR
gh api repos/{owner}/{repo}/pulls/{pr_number}/commits \
  --jq '.[-1].commit.committer.date' > /tmp/pr_{pr}_last_commit_time.txt

LAST_COMMIT_TIME=$(cat /tmp/pr_{pr}_last_commit_time.txt)
echo "Latest commit time: $LAST_COMMIT_TIME"
```

### 0.5.2 Show Timestamp

You MUST show:
```markdown
## Latest Commit Timestamp
**Time**: {timestamp}
**Filter**: Only processing comments created AFTER this time
**Benefit**: Skip already-addressed comments, focus on NEW feedback only
```

---

## PHASE 1: EXTRACTION (FILTER FOR NEW COMMENTS ONLY)

### 1.1 Extract ONLY New Comments (After Latest Commit)

**CRITICAL OPTIMIZATION**: Filter comments by timestamp to only get NEW feedback.

Save each API response to a file WITH TIMESTAMP FILTERING:

```bash
# Get latest commit timestamp first
LAST_COMMIT_TIME=$(gh api repos/{owner}/{repo}/pulls/{pr_number}/commits --jq '.[-1].commit.committer.date')

# Method 1: Get NEW PR review comments (inline code comments) - Filter by created_at
gh api repos/{owner}/{repo}/pulls/{pr_number}/comments --paginate | \
  jq --arg time "$LAST_COMMIT_TIME" '[.[] | select(.created_at > $time)]' > /tmp/pr_{pr}_inline_comments.json

# Method 2: Get NEW PR review summaries - Filter by submitted_at
gh api repos/{owner}/{repo}/pulls/{pr_number}/reviews --paginate | \
  jq --arg time "$LAST_COMMIT_TIME" '[.[] | select(.submitted_at > $time)]' > /tmp/pr_{pr}_review_summaries.json

# Method 3: Get NEW issue comments - Filter by created_at
gh api repos/{owner}/{repo}/issues/{pr_number}/comments --paginate | \
  jq --arg time "$LAST_COMMIT_TIME" '[.[] | select(.created_at > $time)]' > /tmp/pr_{pr}_issue_comments.json

# Show filtering results
echo "Comments BEFORE filtering:"
gh api repos/{owner}/{repo}/pulls/{pr_number}/comments --paginate | jq 'length'
echo "Comments AFTER filtering (new only):"
jq 'length' /tmp/pr_{pr}_inline_comments.json
```

### 1.2 PROOF OF EXTRACTION REQUIRED

You MUST show:

```markdown
## Extraction Results (NEW Comments Only)

**Latest Commit**: {timestamp}

**Method 1 - Inline Comments:**
- File: /tmp/pr_{pr}_inline_comments.json
- Total comments (before filter): X
- NEW comments (after filter): Y
- Sample (first 2 NEW): [paste file path, line numbers, body excerpt, created_at timestamp]

**Method 2 - Review Summaries:**
- File: /tmp/pr_{pr}_review_summaries.json
- Total reviews (before filter): X
- NEW reviews (after filter): Y
- Sample (first 2 NEW): [paste reviewer, state, submitted_at timestamp, body excerpt]

**Method 3 - Issue Comments:**
- File: /tmp/pr_{pr}_issue_comments.json
- Total comments (before filter): X
- NEW comments (after filter): Y
- Sample (first 2 NEW): [paste author, created_at timestamp, body excerpt]

**Total NEW Comments to Process: Y (filtered from X total)**
**Time Saved**: Skipped {X - Y} already-addressed comments ✅
```

**⚠️ DO NOT PROCEED TO PHASE 2 UNTIL YOU SHOW THIS PROOF**

---

## PHASE 2: INVENTORY (MUST COMPLETE BEFORE CATEGORIZATION)

### 2.1 Parse Review Bodies for Embedded Comments

**CRITICAL**: CodeRabbit comments are embedded in review body markdown under sections:
- `🧹 Nitpick comments (N)`
- `♻️ Duplicate comments (N)`
- `🔇 Additional comments (N)`
- `⚠️ Potential issue` inline comments

You MUST:
1. **Parse each review body** using regex/text parsing to extract these sections
2. **Extract individual comments** from markdown blocks like:
   ```
   `{file}:{lines}`: **{title}**
   {body}
   ```

**Parsing Strategy**:
```bash
# Example: Extract CodeRabbit sections from review body
cat /tmp/pr_{pr}_review_summaries.json | jq -r '.[].body' > /tmp/pr_{pr}_review_bodies.txt
```

Then manually parse for patterns:
- `<summary>🧹 Nitpick comments (N)</summary>` → Contains N nitpicks
- `<summary>♻️ Duplicate comments (N)</summary>` → Contains N duplicates
- Look for code blocks with file paths and line numbers

### 2.2 Create Numbered Comment List

Create a complete numbered inventory of EVERY comment from ALL sources:
- Inline comments (Method 1)
- **Embedded review body comments (Method 2 - PARSE THIS)**
- Issue comments (Method 3)
- **CI failures (Phase 0)**

```markdown
## Comment Inventory (Total: X)

### CI Failures (if any)
#### Comment 1/X [CI FAILURE]
- **Source**: GitHub Actions
- **Run ID**: {id}
- **Job**: {job_name}
- **Error**:
  ```
  [PASTE ERROR MESSAGE]
  ```

### Inline Code Comments
#### Comment 2/X [INLINE]
- **Source**: inline
- **File**: {file_path}
- **Lines**: {start}-{end}
- **Reviewer**: {name}
- **Full Comment Text**:
  ```
  [PASTE ENTIRE COMMENT BODY HERE - NO SUMMARIZING]
  ```

### Review Body Embedded Comments
#### Comment 3/X [NITPICK]
- **Source**: review body (nitpick section)
- **File**: {file_path}
- **Lines**: {start}-{end}
- **Reviewer**: CodeRabbit
- **Section**: 🧹 Nitpick comments
- **Full Comment Text**:
  ```
  [PASTE ENTIRE COMMENT FROM MARKDOWN PARSING]
  ```

#### Comment 4/X [DUPLICATE]
- **Source**: review body (duplicate section)
- **File**: {file_path}
- **Lines**: {start}-{end}
- **Reviewer**: CodeRabbit
- **Section**: ♻️ Duplicate comments
- **Full Comment Text**:
  ```
  [PASTE ENTIRE COMMENT FROM MARKDOWN PARSING]
  ```

[CONTINUE FOR ALL X COMMENTS INCLUDING CI FAILURES]
```

### 2.3 INVENTORY VERIFICATION REQUIRED

You MUST show:
```markdown
## Inventory Complete ✅
- CI failures: X comments
- Method 1 (inline) contributed: X comments
- Method 2 (review summaries) contributed: Y comments
  - Inline comments: Z
  - Nitpicks (parsed from body): N
  - Duplicates (parsed from body): M
  - Additional comments (parsed from body): P
- Method 3 (issue comments) contributed: Q comments
- **Total inventory count: X comments**
- **All comments numbered: 1/X through X/X**
```

**⚠️ DO NOT PROCEED TO PHASE 3 UNTIL INVENTORY IS COMPLETE INCLUDING PARSED REVIEW BODIES**

---

## PHASE 3: VERIFICATION (MUST VERIFY EACH COMMENT)

### 3.1 Process Each Comment With Evidence (MANDATORY FILE VERIFICATION)

For EACH comment in your inventory, you MUST perform ALL these steps:

**⚠️ CRITICAL RULE: NEVER TRUST COMMIT MESSAGES**
- Commit messages describe INTENT, not REALITY
- Code is the only source of truth
- You MUST use Read tool to verify actual current state
- "Fixed in commit X" is NOT verification - it's a claim that needs proof

For EACH comment:

1. **Show the comment** (reference by number: "Processing Comment 5/47")

2. **MANDATORY: Use Read tool (NO EXCEPTIONS, NO "IF")**
   - You MUST read the file at the exact lines mentioned
   - Do this EVEN IF you think the issue is fixed
   - Do this EVEN IF commits claim to have fixed it
   - Include 5-10 lines of context (before and after)
   ```bash
   # Example - you MUST do this for EVERY file-specific comment:
   Read {file_path} (offset: line - 5, limit: 15)
   ```

3. **Extract and show exact code**
   - Quote the EXACT lines from the comment
   - Show what's ACTUALLY in the file right now
   - Use line numbers for precise reference

4. **Compare with comment claim**
   - State what the comment says should be wrong
   - Show what the code actually contains
   - Explicitly state if they match or differ

5. **Determine status with PROOF**
   - ✅ FIXED: Show the code proves the fix exists
   - ❌ NOT FIXED: Show the code still has the issue
   - ⚠️ PARTIALLY FIXED: Show what's fixed and what remains
   - ❓ UNCLEAR: Explain why verification is ambiguous

6. **Document with evidence**

```markdown
## Comment-by-Comment Verification

### Processing Comment 1/X [CI FAILURE]
- **Comment**: requirements.txt out of date
- **CI Log**: Shows "requirements.txt is not up to date" error
- **Current Status**: ✅ VERIFIED - CI is failing
- **Status**: NEEDS FIX
- **Action**: Run pip-compile and commit updated requirements.txt

### Processing Comment 2/X [INLINE]
- **Comment**: [brief reference to inventory]
- **File Check**:
  ```bash
  # Reading {file}:{lines}
  ```
- **Current Code**:
  ```
  [PASTE ACTUAL CONTENT FROM READ TOOL]
  ```
- **Issue Claimed**: "Uses O(n) call instead of O(1)"
- **Issue Verified**: ✅ YES - line 117 shows get_feedback_stats_enhanced()
- **Status**: NEEDS FIX
- **Action**: Replace with get_total_feedback_count()

### Processing Comment 3/X [NITPICK]
- **Comment**: [from parsed review body]
- **File Check**: [use Read tool]
- **Current Code**: [show evidence]
- **Issue Verified**: ✅ YES/NO
- **Status**: OPTIONAL (nitpick) / NEEDS FIX / ALREADY FIXED

[CONTINUE FOR ALL COMMENTS INCLUDING CI AND PARSED REVIEW BODY COMMENTS]
```

### 3.2 VERIFICATION PROOF REQUIRED

You MUST show:
```markdown
## Verification Complete ✅
- Comments processed: X/X
- CI failures verified: X
- Files read with Read tool: X files (LIST EVERY FILE)
- Lines specifically checked: [file:line, file:line, ...]
- Issues verified as existing: X
- Issues verified as resolved: Y
- Issues cannot verify (outdated): Z
- **Zero files skipped**: ✅ (if any file was skipped, verification FAILS)
```

**⚠️ DO NOT PROCEED TO PHASE 3.3 UNTIL ALL X/X COMMENTS VERIFIED WITH READ TOOL**

---

### 3.3 TEST VERIFICATION (For Code Changes)

**CRITICAL**: If you make ANY code changes during verification, you MUST run tests BEFORE marking as fixed.

**When Required**:
- Test file changes
- Component changes that affect tests
- Selector changes (button, form, navigation)
- API changes
- Any code modification

**Process**:
1. **Identify Affected Tests**: Which test files cover the changed code?
2. **Run Those Tests**: Execute specific test suite
3. **Verify Results**: Tests must pass 100%
4. **Document**: Show test output in verification
5. **Only Then**: Mark issue as "FIXED"

**Example**:
```bash
# Changed button selectors in faq-management.spec.ts
# MUST run these tests before marking as fixed:
npx playwright test tests/e2e/faq-management.spec.ts --reporter=line --workers=1
```

**Test Results Documentation**:
```markdown
### Test Verification Results
- **Tests Run**: tests/e2e/faq-management.spec.ts
- **Status**: ✅ All 12 tests passed
- **Output**:
  ```
  [paste test output showing pass/fail status]
  ```
- **Conclusion**: Safe to mark as FIXED
```

**If Tests Fail**:
- Status is "IN PROGRESS", NOT "FIXED"
- Document failure
- Investigate and fix
- Re-run tests
- Only mark "FIXED" after tests pass

**Rule**: Code changes without test verification = INCOMPLETE

**⚠️ DO NOT PROCEED TO PHASE 4 UNTIL TEST VERIFICATION COMPLETE**

---

## PHASE 4: CATEGORIZATION (AFTER VERIFICATION)

### 4.1 Apply Categories Based on Verification

NOW that you've verified each comment, categorize them based on ACTUAL current state:

**🚨 CI FAILURES** - Must fix to merge:
- GitHub Actions failures (verified from logs)
- Build errors (verified)
- Test failures (verified)
- Dependency issues (verified)

**🔴 CRITICAL** - Must fix before merge:
- Security vulnerabilities (verified to exist)
- Breaking changes (verified to exist)
- Incomplete functionality (verified to exist)
- Data loss risks (verified to exist)

**🟡 HIGH PRIORITY** - Should fix:
- Code quality issues (verified to exist)
- Performance problems (verified to exist)
- Missing error handling (verified to exist)
- Inconsistent patterns (verified to exist)

**🟢 MEDIUM PRIORITY** - Nice to have:
- Style improvements (verified to exist)
- Documentation suggestions (verified to exist)
- Refactoring opportunities (verified to exist)

**⚪ NITPICKS** - Optional (from CodeRabbit nitpick section):
- Formatting preferences (verified to exist but low impact)
- Minor style choices (verified to exist but low impact)
- Comment improvements (verified to exist but low impact)

**🔄 DUPLICATES** - Already addressed elsewhere (from CodeRabbit duplicate section):
- Same issue mentioned in multiple places
- Reference original comment location

**❌ INVALID/OUTDATED** - Can ignore:
- Already fixed in later commits (verified fixed)
- Based on old code version (verified no longer applies)
- Misunderstanding of code (verified incorrect)

### 4.2 Create Action Checklist With Traceability

```markdown
## PR Review Action Items for #{pr_number}

### 🚨 CI Failures (X items - MUST FIX TO MERGE)

#### CI Failure 1/X
- **From Inventory**: Comment 1/X
- **Verification Reference**: Phase 3, Comment 1 verification
- **Run ID**: {id}
- **Error**: requirements.txt out of date
- **Required Fix**: Run pip-compile and update requirements.txt
- **Status**: [ ] Not started | In progress | Fixed
- **Fix Commit**: {hash when fixed}

### 🔴 Critical Issues (X items - MUST FIX)

#### Critical Issue 1/X
- **From Inventory**: Comment 15/47
- **Verification Reference**: Phase 3, Comment 15 verification
- **File**: {file}:{lines}
- **Current State**: Verified exists
- **Required Fix**: {specific action}
- **Status**: [ ] Not started | In progress | Fixed
- **Fix Commit**: {hash when fixed}

### 🟡 High Priority Issues (X items)
[Same format]

### 🟢 Medium Priority (X items)
[Same format]

### ⚪ Nitpicks (X items - Optional, from CodeRabbit)
[Same format with note that these are from nitpick section]

### 🔄 Duplicates (X items - Reference Original)
[List with reference to original comment that should be addressed]

### ❌ Invalid/Outdated (X items)
[Same format with verification proof]

## Verification Summary
- CI failures: X
- Total comments from API: Y
- Comments in inventory: Y ✅ MATCHES
- Comments verified: Y ✅ ALL VERIFIED
- Critical: X (including CI)
- High priority: X
- Medium: X
- Nitpicks: X (optional)
- Duplicates: X (see originals)
- Invalid: X (verified outdated)
```

---

## PHASE 5: FINAL VERIFICATION (BEFORE CLAIMING DONE)

### 5.1 Mandatory Verification Steps

```markdown
## Final Verification Checklist

### CI Status ✅
- [ ] GitHub Actions checked: YES/NO
- [ ] Failing runs documented: X runs
- [ ] CI failures added to action items: X items

### Count Verification ✅
- [ ] CI failures: X
- [ ] API Method 1 (inline): Y
- [ ] API Method 2 (review summaries): Z
  - [ ] Direct inline: A
  - [ ] Nitpicks (parsed): B
  - [ ] Duplicates (parsed): C
  - [ ] Additional (parsed): D
- [ ] API Method 3 (issue): E
- [ ] Total unique comments: N
- [ ] Inventory count: N ✅ MATCHES
- [ ] Verification count: N ✅ ALL PROCESSED

### Review Body Parsing ✅
- [ ] Review bodies read: X
- [ ] Nitpick sections parsed: X sections
- [ ] Duplicate sections parsed: X sections
- [ ] Additional comment sections parsed: X sections
- [ ] All embedded comments extracted: ✅

### File Coverage Verification ✅
- [ ] Files mentioned in comments: [list all]
- [ ] Files actually read with Read tool: [list all]
- [ ] ✅ MATCHES: All mentioned files were read
- [ ] **Zero files skipped**: All file-specific comments verified with Read tool

### Test Verification ✅
- [ ] Code changes identified: YES/NO
- [ ] If YES, affected tests identified: [list test files]
- [ ] Tests executed BEFORE marking as fixed: YES/NO
- [ ] Test results documented: [pass/fail status]
- [ ] All tests passed: YES/NO
- [ ] **No fixes marked without test verification**: ✅

### Evidence Trail ✅
- [ ] Phase 0: CI status checked ✅
- [ ] Phase 1: Extraction proof shown ✅
- [ ] Phase 2: Complete inventory created (including parsed review bodies) ✅
- [ ] Phase 3.1: Every comment verified with Read tool ✅
- [ ] Phase 3.2: Verification proof shown (files listed) ✅
- [ ] Phase 3.3: Tests run for all code changes ✅
- [ ] Phase 4: Categories linked to verification ✅
- [ ] Phase 5: Final counts match ✅
```

---

## WHY THESE CHANGES EXIST

**Previous Issues Fixed**:

1. **Missing Nitpicks**: CodeRabbit embeds nitpicks in review body markdown, NOT as separate comments
   - ✅ **Fix**: Parse review body for `🧹 Nitpick comments (N)` section

2. **Missing Duplicates**: CodeRabbit marks duplicate comments in a special section
   - ✅ **Fix**: Parse review body for `♻️ Duplicate comments (N)` section

3. **Missing CI Failures**: GitHub Actions failures weren't checked
   - ✅ **Fix**: Phase 0 checks CI status and extracts failure logs

4. **Incomplete Review Body Processing**: Only looked at summary, not embedded comments
   - ✅ **Fix**: Systematic parsing of markdown structure in review bodies

5. **False "FIXED" Claims** (2025-01-06): Marked issues as fixed without actually verifying code
   - ❌ **Problem**: Phase 3 said "If file-specific, use Read tool" - too permissive
   - ❌ **Problem**: Trusted commit messages instead of reading actual code
   - ✅ **Fix**: Phase 3.1 now MANDATES Read tool usage for ALL file-specific comments
   - ✅ **Fix**: Added explicit rule "NEVER TRUST COMMIT MESSAGES"

6. **Code Changes Without Test Verification** (2025-01-06): Made changes and committed without running tests
   - ❌ **Problem**: No requirement to run tests before marking issues as fixed
   - ❌ **Problem**: Broke E2E tests with wrong button selectors (guessed `.lucide-pencil` without verification)
   - ✅ **Fix**: Phase 3.3 now REQUIRES test execution for all code changes
   - ✅ **Fix**: Phase 5 checklist includes test verification requirements

7. **Incomplete Verification Tracking** (2025-01-06): Didn't list all files read, allowing skips
   - ❌ **Problem**: Phase 3.2 said "Files read: X files" without listing them
   - ✅ **Fix**: Phase 3.2 now requires listing every file read
   - ✅ **Fix**: Added "Zero files skipped" verification requirement

8. **Inefficient Full-History Processing** (2025-11-06): Processed ALL comments on every run, including already-addressed ones
   - ❌ **Problem**: Command reviewed all 49 comments even after fixes were pushed
   - ❌ **Problem**: Wasted tokens and time re-verifying already-addressed feedback
   - ❌ **Problem**: No filtering by timestamp - treated every run as fresh review
   - ✅ **Fix**: Phase 0.5 gets latest commit timestamp for filtering
   - ✅ **Fix**: Phase 1 filters comments by `created_at > last_commit_time`
   - ✅ **Fix**: Only processes NEW comments posted after latest commit
   - ✅ **Benefit**: Dramatically reduces token usage and review time on subsequent runs

---

## Example Usage

```bash
# From within a repo with a PR
/review-pr 123

# Or specify repo
/review-pr bisq-network/bisq2#4013
```

## Success Criteria

You've completed the review when:
- ✅ CI status checked and failures documented
- ✅ All phases shown with proof (0 → 0.5 → 1 → 2 → 3.1 → 3.2 → 3.3 → 4 → 5)
- ✅ **Latest commit timestamp obtained** and used to filter comments
- ✅ **Only NEW comments processed** (created after latest commit)
- ✅ **Before/after filtering counts shown** (demonstrate efficiency gain)
- ✅ Review bodies parsed for embedded comments
- ✅ Every NEW comment (including nitpicks, duplicates, CI failures) has verification entry
- ✅ **All file-specific NEW comments verified with Read tool** (no exceptions)
- ✅ **All code changes tested before marking as fixed** (tests must pass)
- ✅ **All files read are listed explicitly** (zero files skipped)
- ✅ All counts match (CI + NEW API comments + Parsed = Inventory = Verification)
- ✅ No vague claims - all evidence-based
- ✅ **No reliance on commit messages** - code is the only source of truth
- ✅ **Efficiency achieved**: Skipped already-addressed comments, focused on NEW feedback
