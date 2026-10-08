# Official ARC branding assets

The founder-designated Logo directory contains two existing assets: `arc-logo.svg` and `arc-logo-email.png`. The SVG is the primary vector artwork; the PNG is a transparent 300×272 email/display export. Both show the same nested green and purple ARC mark. No separate square source icon or light/dark color variant was found.

| Prepared file | Purpose | Transformation |
|---|---|---|
| [branding/arc-logo.svg](branding/arc-logo.svg) | Original vector reference | Byte-for-byte copy of existing `arc-logo.svg`; no tracing or edits |
| [branding/arc-logo.png](branding/arc-logo.png) | Central README and staged profile | Byte-for-byte copy of `arc-logo-email.png`; destination filename only changed |
| [branding/arc-logo-icon.png](branding/arc-logo-icon.png) | Organization avatar | Original SVG uniformly rendered to 512×464, centered on a transparent 512×512 canvas with 24-pixel top/bottom padding |

Transparency and aspect ratio are preserved. The icon does not crop, stretch, recolor or reinterpret the artwork. Original source files remain unchanged. [The asset manifest](branding/manifest.json) records hashes and transformations without publishing private filesystem paths.

**Branding and trademark rights are all rights reserved.** Images in `assets/branding/` and staged profile copies are excluded from CC BY-NC 4.0 and PolyForm Noncommercial 1.0.0. The surrounding original explanatory documentation uses the approved documentation license. Do not infer commercial brand permission or ARC endorsement from repository access.

## Applying the avatar later

After explicit founder authorization, an organization owner can open the `arc-motion-light` organization settings, use the profile-picture upload control and select `arc-logo-icon.png`. Review the preview and save the change. A README logo does not set the avatar. No live settings change is performed in Phase 1B. [GitHub's profile documentation](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile) describes the separate controls.

A separate local organization-profile package contains matching images and `profile/README.md`; its publication remains unapproved. No third-party logos, photographs or unrelated financial/investor assets were imported.
