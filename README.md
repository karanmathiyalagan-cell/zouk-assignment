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

## Alternate directions: competitor-inspired versions

These sit below the main screens (y ≈ 4150), each as a full page plus a first-screen view with its own sticky bar. All three use the Zouk palette, type and content. Only the page structure and component patterns change.

| Version | Borrowed from the competitor | Deliberately left out |
|---|---|---|
| A · Miraggio-style | Sharp-cornered editorial look, uppercase title, photo-tile swatches, "Key Features" with laptop fit first, dimensions by axis (plus handle drop, still to measure), "Details worth loving" image story, 2-column rail tagged by use and laptop size | Buy-2-get-1 countdown |
| B · Lino Perros-style | Breadcrumb, thumbnail strip, oversized title, savings badge, EMI card, Add to cart + Buy it now, dark trust band, icon accordions, 2-column spec table, "what it holds" infographic, review mention tags, FAQs | "59 people viewing", sale timer, three stacked coupons (cut to one offer) |
| C · Mokobara-style | Inset header, Prints / Personalise / Compare tabs, a delivery date before any pincode, pay in full vs pay in 3, "Pair it with" above the description, feature carousel, bold promise block (Zouk's "100% vegan" in place of the 30-day trial), side-by-side Compare, delivery date in the sticky bar | Discount marquee, cart timer. Statement Office Bag figures in Compare are marked as placeholders until they're reconciled |

# Task 2 · Collection page banners

**Figma page:** `Task 2 · Collection banners` (same file)

Collection: **Women's Office Bags**, with the Multicolor Mandala print as the hero. Two 390 × 160 mobile banners in the Indian-heritage direction. In both, an arch (a nod to jharokha and temple arches) frames the print and the bag.

| Frame | What it shows |
|---|---|
| Banner 1 · Sale-led | Teal ground. "FLAT ₹400 OFF", a split code box (ON OFFICE BAGS / USE CODE WORK400), a plain end date with no countdown, and an underlined "Shop the collection" link. The arch is filled with the Mandala print, with the bag in front and a caption naming the print |
| Banner 2 · Concept-led | Cream ground. "Your whole *workday*, one bag." in Inter Light with Fraunces Italic. The subline says what fits, then "Discover the collection". A teal arch shows the laptop, bottle and lunch inside the bag, above a band of the print, with a "Fits 15.6″ laptops" chip |
| 2× previews | For review. Export at 3× (1170 × 480) |
| In context ×2 | Each banner on a Women's Office Bags collection page (390 × 844) |
| Brief & rationale | The brief, why aesthetics is the lever (Aesthetic-Usability Effect), the heritage direction, and what was and wasn't taken from the reference banners |
| Specs & accessibility | Export sizes, safe areas and minimum type size. WCAG AA contrast for every text pair: the eyebrow was darkened from #CC664E (3.27:1) to #A94F3B (4.71:1). Also lists the offer assumptions |

The offer amount and the code are placeholders for Zouk to set.

# Task 3 · Mobile navigation wireframe

**Figma page:** `Task 3 · Mobile navigation` (same file)

A greyscale mid-fidelity wireframe of the mobile drawer, with Zouk teal only for active states and orange numbered pins for annotations. Level one has four zones: **Shop → Browse by → Offers → Account**. Every product type is one tap from opening the drawer.

| Frame | What it shows |
|---|---|
| 01 · Drawer, level one | The full drawer, with a dashed line marking the fold at 844. Shop (7 product types, including Travel, Zouk For Men, Gift Boxes and Accessories). Browse by, second and led by Print. Offers as a separate chip block. Account quiet at the bottom |
| 02 · Shop → Bags | "All bags", then six equal tiles: Sling, Handbags, Tote, Satchels, Office, Lunch |
| 03 · Bags → Sling Bags | Plain shape first, model names second (Flap, U-shaped, Baguette, Shoulder, Crossbody, Phone sling). All five baguettes together; Crossbody collection moved here from Travel |
| 04 · Browse by → Print | Named prints with their home region, plus print families |
| 05 · Browse by → Occasion | One reconciled list of eight, shared with the collection filter |
| Pins + notes | 16 numbered notes, each tied to the friction or persona need it answers |
| Problem & persona | Brief, discover vs. reach, Riya (26, Pune), frictions F1, F8 and F9, assumptions |
| Information architecture | All four zones with every product line placed, plus the footwear question for Zouk |
| What I changed, and why | 12-row table: change → why → which friction it answers |
| One structure, two layouts / Metrics | Mobile and desktop read from one navigation source with one canonical URL per label; four success metrics |

Print home regions and the treatment of sold-out lines (Zoe, Regular) are marked for Zouk to confirm.

## Scripts

`figma/cover-and-edge-states.js` builds the Cover and the edge-states board. It targets the original working file, which uses variables. The version run against the linked copy swaps the variables for hex values and reads from node `0:1631`.
