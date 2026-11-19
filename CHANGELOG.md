# Changelog

## 1.1.0 - 2026-11-19

Synced the five skills from bisq2 `main`, which now holds their reviewed versions (bisq-network/bisq2#4837).

- Security examples: the vote-weight calculation uses `Math.multiplyExact` instead of an overflow check that missed overflows, and bond locking uses `Math.addExact`/`Math.subtractExact` with an explicit invariant check instead of `assert`, which Java disables by default.
- Portable commands: Claude-only `Grep ... --output_mode` lines are now plain `grep -R -l -E`, and the `gh api` commit query, which read a field the commits endpoint does not return, now counts files through the pull request files endpoint.

One local difference from bisq2: the upstream `gh api` line combines `--slurp` with `--jq`, which gh rejects. This repo uses `gh api --paginate .../files --jq '.[].filename' | wc -l` instead until the fix lands upstream.
- Compatibility guidance uses the last released version as the baseline for `.proto` and protocol changes.
