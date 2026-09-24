# Zouk assignment — Task 1: Product page (mobile PDP)

**Figma file:** https://www.figma.com/design/xuiN6qFZcStC2on57uIhfU/Untitled?node-id=0-1
(copied from the earlier working file `CSKJAVo6TTRetZhkl5zSYT`, which also holds the Assets page)

The high-fidelity mobile design for Task 1, option 1: help a first-time buyer (Meher, 27, Mumbai, landing from an Instagram ad) work out whether a Women's Office Bag fits her laptop and her day, faster and with more confidence. The working example is the **Multicolor Mandala Women's Office Bag**, with **FloMotif** shown in the print-switch state.

## Visual theme, taken from zouk.co.in

| Token | Value | Use |
|---|---|---|
| `color/brand/teal` | `#0D485D` | Primary (Add to Cart, links, fit block) |
| `color/brand/terracotta` | `#CC664E` | Secondary accent (print name, story eyebrow) |
| `color/brand/orange` | `#E8792B` | Wordmark dot, badges, stars |
| `color/bg/cream` | `#FCF7F3` | Site background |
| `color/bg/sand` | `#F4EEE6` | Section background (story, chips) |
| Type | Inter | Same as the live site; Fraunces only for the wordmark and story titles |
| Radius | 10 px buttons, 12 px cards | Matches the live PDP |

In the working file these are Figma variables in the `Zouk` collection. The copy linked above has no local variables, so the colours are applied as hex values.

## What's in the Figma file

**Page 1**

| Frame | What it shows |
|---|---|
| 00 · Before | The live PDP rebuilt, with 8 red markers for the frictions this redesign answers |
| 01 · Full page | The whole redesigned PDP, modules 1–11, with a numbered rationale note beside each module (friction + UX law) |
| 02 · First screen | Everything needed to answer "will it fit?" sits above the sticky Add to Cart bar |
| 03 · Gallery → Size | The labelled "Size" thumbnail jumps to the drawn-to-scale infographic |
| 04 · Gallery → What fits | Laptop, bottle, diary and tiffin inside the bag |
| 05 · Print switched → FloMotif | The print swaps in place; specs, fit and product reviews stay the same |
| 06 · Decision block | Pincode entered, initials switched on, the trade-off shown beside the option, sticky total updated |
| 07 · Story of the print | The craft story, placed after the decision block |
| 08 · Reviews filtered | "Laptop fits" tag active; product and design reviews split honestly |
| 09 · Returns, full terms | Bottom sheet from "Read the full return policy ›": a plain yes/no for each situation (✓/× glyphs, so colour isn't the only signal), plus a link back to the size drawing |
| 10 · Edge state: new print, no design reviews | Kashmir Blooms, just launched. Design reviews show 0 and say so. Fit proof and product reviews carry over; creator reviews roll up to the category |
| 11 · Edge state: one print, no story | The same print's first screen: 4 thumbnails instead of 9, no print strip, no teaser. The fit block moves up |
| 12 · Specifications open | The accordion shows the size figures from the same source as the fit block, plus details listed only here |
| Cover | Brief, persona, the three questions, principles, won't-do list, theme, index |
| Edge states board | Rules for five modules: no story, single print, no discount, zero design reviews, no "pair it with" rail |

**Page: Assets.** Vector bag illustrations for 8 prints (as components), a 32-icon set, the size infographic (drawn at 6 px/cm against a 15.6″ laptop), the what-fits illustration, and the sticky Add to Cart bar component.

### Imagery

The bags are vector illustrations standing in for Zouk's product photography. This session's sandbox couldn't reach Shopify's CDN or Figma's upload endpoint. Each image layer is named for the photo that belongs there (for example, `Main image — WOB_MMD_04`), so real photos can be dropped in as fills.

## Scripts

`figma/cover-and-edge-states.js` builds the Cover and the edge-states board. It targets the original working file, which uses variables. The version run against the linked copy swaps the variables for hex values and reads from node `0:1631`.
