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

# Zouk Vault · Desi Maximal × Handmade Leather

**Figma file:** https://www.figma.com/design/mf5eFMoSk0N3PUW7u1Dtu3/Zouk?node-id=2813-1560 (page **Zouk Vault**, section **Desi Maximal · Handmade Leather**)

Copies of **Final Design - Vault** and **Vault PDP · SKU 5**, restyled in a Desi maximal look built on leather craft. The originals and their components are untouched.

| Node | What it is |
|---|---|
| `2813:1561` Final Design - Vault · Desi Maximal | Vault landing page copy |
| `2813:1624` Vault PDP · SKU 5 · Desi Maximal | Product page copy |
| `2813:3081` Components · Desi Leather (interactive) | Themed copies of the 19 interactive component sets (marquee, story carousel, quick-filter chips, wishlist, add to bag, 7 accordions, 7 FAQs) |
| `2814:1849` Desi · Motifs & craft details | Buti tile, paisley, mandala, toran pennant, brass rivet, "हाथ से बना" seal, block-print border |
| `2814:1955` Brief | Direction note and palette |

## Visual language
- **Leather surfaces:** espresso, oxblood and cognac gradients with a noise grain, saddle-stitch dashed outlines, brass rivets, an embossed seal, a hanging leather price tag.
- **Desi maximal layer:** toran bunting, block-print buti borders, a lehariya band, paisley, mandalas, jharokha arch frames on every product image, Devanagari accents (तिजोरी, हाथ से बना, हर टाँका, हाथ से।).
- **Type:** Rozha One for display, Kalam for the handwritten accent, Yatra One for labels and CTAs, Poppins for body.
- **Colour:** a `Desi Leather` variable collection (19 colours). The theme pass binds the frames' solid fills to it.
- **Copy:** Zouk is a vegan brand, so the copy says "handcrafted" and "vegan leather". Leather is the look, not the material.

## Interactions & motion
- All prototype interactions still work on the themed component copies: Smart-Animate marquee, story-carousel arrows, filter chips, wishlist, add to bag, accordions, FAQs, menu navigation. One exception: the PDP title heart is a remote library component, so it keeps its original look.
- Each frame has an 8 s timeline. Vault: toran drops in and sways; mandalas spin; a thread sews the jharokha arch and becomes the dashed stitch; the headline staggers in word by word; the "not to be seen." script springs in; the seal stamps down; the CTA rises with a leather sheen; product cards stagger in; तिजोरी pops. PDP: toran sways; the gallery opens with a slow Ken-Burns zoom and the mandala turns; the title staggers in; the price tag swings like a pendulum; the made-to-order timeline builds dot by dot with rivets popping; the Add to cart sheen and Buy it now pulse loop; delivery tiles and trust pills stagger; the footer toran and mandala keep moving.
- The copies drop 25 layers that were hidden in the originals (old variants).
