# Zouk assignment — Task 1: Product page (mobile PDP)

**Figma file:** https://www.figma.com/design/CSKJAVo6TTRetZhkl5zSYT

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

All colors are Figma variables in the `Zouk` collection and are bound to the layers.

## What's in the Figma file

**Page: Task 1 · PDP Redesign**

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

**Page: Assets.** Vector bag illustrations for 8 prints (as components), a 32-icon set, the size infographic (drawn at 6 px/cm against a 15.6″ laptop), the what-fits illustration, and the sticky Add to Cart bar component.

### Imagery

The bags are vector illustrations standing in for Zouk's product photography. This session's sandbox couldn't reach Shopify's CDN or Figma's upload endpoint. Each image layer is named for the photo that belongs there (for example, `Main image — WOB_MMD_04`), so real photos can be dropped in as fills.

## Not built yet

`figma/cover-and-edge-states.js` holds the script for the last two frames:

- the **Cover**: brief, persona, principles, theme and index
- the **09 · Edge states** board: no story, a single print, no discount, zero design reviews, no "pair it with" rail

It stopped at the Figma MCP Starter-plan limit (20 tool calls per month). Run it with `use_figma` against the file once the quota resets, or on a Professional plan.

---

# Audit — "Make Your Own Set · Final" (combo builder)

**Figma file:** https://www.figma.com/design/mf5eFMoSk0N3PUW7u1Dtu3/Zouk?node-id=1588-3255

A senior UX + product (AOV) audit of the mobile "Make Your Own Set" builder: all 25 frames on the page (Box of 2 / 3 / 4, empty and added states, the milestones variant, exit dialogs and review screens), checked against the file's "Make Your Own Combo · Flow" and navigation/PLP pages and against live zouk.co.in offers.

Open `audit/make-your-own-set/index.html` in a browser. It covers:

- The product decisions it assumes: no discounts during the A/B test (gifts are the fallback lever), a matching same-print look as the reason to use the builder, savings shown as real MRP savings added up across the box, and the discount screens kept as a ready variant
- 24 findings (3 blockers) in four areas: pricing and savings, flow and interaction, UI consistency, accessibility and copy
- A price-reconciliation table: what the tray shows now vs. what it should show
- A ranked plan for the test build, an A/B test design, and open questions for the business
