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

# Zouk Vault · India is Maximal (v2)

**Figma file:** https://www.figma.com/design/mf5eFMoSk0N3PUW7u1Dtu3/Zouk?node-id=2831-4632 (page **Zouk Vault**, section **Zouk Vault · India is Maximal (v2)**)

Copies of **Final Design - Vault** and **Vault PDP · SKU 5**, rebuilt in the style of the "India is Maximal" moodboard: editorial poster pages, each on a saturated colour field, with cut-out photography over huge type. Handmade leather comes through the imagery. The first Desi Maximal attempt was deleted at the user's request. The original frames and components are untouched.

| Node | What it is |
|---|---|
| `2831:4633` Final Design - Vault · Maximal | Vault landing page |
| `2831:4696` Vault PDP · SKU 5 · Maximal | Product page |
| `2831:6153` Components · Vault Maximal (interactive) | Themed copies of the 19 interactive component sets |
| `2833:1839` Assets · Maximal | Figma AI imagery: 9 transparent cut-outs, a block-print texture tile, a haveli backdrop |

## System
- **Colour fields:** sindoor `#8C2A2C`, gulabi `#C9578E`, neela `#5E93C4`, kattha `#6A2418`, each overlaid with an AI-generated tone-on-tone block-print tile (soft-light).
- **Type and base:** haldi `#F4B53F` and white for type; kora `#FFF6E8` for the calm functional zones (cart, delivery, accordions, FAQ). All colours are variables in the `Vault Maximal` collection.
- **Fonts:** Plus Jakarta Sans (ExtraBold for headlines and bold keywords in body copy) and Instrument Serif for the giant hero word ("Too Good").
- **Imagery:** generated with Figma AI. A woman in a green silk saree holding a hand-tooled leather bag, lotus, karigar hands saddle-stitching leather, a Pulikali tiger mask, a peacock, a jewelled hand with a tooled-leather potli, hand-dyed hides, leather-craft tools, a marigold garland and a haveli backdrop. Real Zouk product photos stay on all product cards and in the gallery.
- **Cut-outs:** the image model bakes a fake checkerboard into its "transparent" PNGs. The backgrounds were keyed out inside Figma by a small script (PNG decode, edge flood-fill, defringe, PNG encode), so every cut-out has real alpha.

## Pages
- **Vault:** Chapter 01 hero ("Some designs are *Too Good* not to be seen."), haldi marquee, "Zouk Vault" PLP on kattha, Chapter 02 "our craft is a riot." (tiger and karigar hands), neela story carousel, product grids on kattha, sindoor and neela, Chapter 03 "A different side of Zouk." (print swatches and potli hand), and a closing "So yes, the Vault is maximal." (haveli and peacock).
- **PDP:** gallery and price as one sindoor poster with lotus, a neela "Good things take time." with craft tools, pill CTAs, colour-block delivery tiles, gulabi and kattha About posters with garland, lotus and dyed hides, colour trust pills, and More from the Vault on neela.

## Interaction & motion
- Every prototype interaction is kept on the themed component copies: marquee, story carousel, filter chips, wishlist, add to bag, accordions, FAQs, menu link. One exception: the PDP title heart is a remote library component.
- Each frame has an 8 s timeline. Vault: the hero rises in with a slow push-in, the lotuses bloom in and sway, "Too Good" types on letter by letter, headlines stagger in word by word, the CTA pulses, the cards stagger in, the tiger roars, the karigar hands keep stitching, the potli swings, the haveli does a slow zoom, and the peacock walks in. PDP: gallery entrance, title stagger and price pop, the tools drop in, the made-to-order timeline builds step by step, a sheen sweeps Add to cart, Buy it now pulses, and tiles and pills stagger in.
