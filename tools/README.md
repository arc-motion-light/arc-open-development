# Documentation validation

Run `python3 tools/validate_docs.py` from the repository. It checks required public files, nonempty text, relative Markdown/HTML image links, both official license hashes, documentation attribution and branding exclusions, logo hashes/dimensions/RGBA transparency, legal identity and `CVR: 34843341`, planned repository names and selected secret/private-path patterns.

It also checks that internal Phase 1/1B reports are absent from the current public tree and that `.review/publication/` remains untracked and Git-ignored. If earlier commits contain these reports, it reports the remaining publication-history issue; deleting a file does not make its earlier copies private.

To additionally verify the separately prepared profile and matching logo/avatar/license copies, use `python3 tools/validate_docs.py --profile-package ../arc-organization-profile-staging`. The profile package is optional so validation remains usable in a future public clone. Remotes are reported; the validator never configures, pushes or changes them.

Checks are offline and validate the candidate tree. They do not determine legal ownership, clear a proposed public history, inspect private firmware, certify hardware or prove that every secret is absent. Review results with the publication checklists. Executable `tools/*.py` remain outside CC BY-NC 4.0 pending a separate tooling license decision; this original explanatory README uses the approved documentation license.
