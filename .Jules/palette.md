## 2025-05-14 - [Icon-only Button Accessibility]
**Learning:** Icon-only buttons (like those for liking, saving, or deleting) are common in this app but frequently lack `aria-label` or proper keyboard focus visibility. This makes them inaccessible to screen reader users and difficult for keyboard-only users to discover.
**Action:** Always ensure icon-only buttons have an `aria-label` that describes their action, and ensure they are visible when they receive focus, even if they are normally hidden on hover. (Recently updated: Added focus-visible rings to avatar selection and ingredient checklists).

## 2025-05-15 - [Interactive List and Selection Accessibility]
**Learning:** Interactive elements that are not standard HTML form controls (like clickable list items for checklists or custom selection buttons) often lack necessary ARIA roles and keyboard support. This prevents users who rely on assistive technologies or keyboard navigation from interacting with these features.
**Action:** Implement `role="checkbox"`, `tabIndex="0"`, and `aria-checked` for custom checklist items. Add `onKeyDown` handlers to support 'Enter' and 'Space' keys. For custom selection buttons, use `aria-pressed` to indicate state and ensure clear `focus-visible` styles are applied.

## 2025-05-22 - [Keyboard Navigation and Layout Accessibility]
**Learning:** Standard layouts often lack a "Skip to Content" link, making keyboard navigation tedious. Additionally, custom interactive elements like rating stars or clear-search buttons often lack clear focus indicators, making them hard to use with a keyboard.
**Action:** Always include a "Skip to Content" link in main layouts pointing to the main content area. Use Tailwind's `focus-visible` to add distinct rings or transforms to interactive elements that lack default indicators, ensuring a consistent and accessible experience without affecting mouse users' visual design.

## 2025-05-23 - [Accessible Star Ratings and Pluralization]
**Learning:** Star rating displays are often implemented with raw characters (★) which screen readers announce individually, creating noise. Furthermore, shorthand review counts like "(5)" lack context for assistive technology.
**Action:** Wrap star groups in a container with `role="img"` and a descriptive, pluralized `aria-label` (e.g., "Rating: 4 out of 5 stars"). Hide individual stars with `aria-hidden="true"`. For counts, use explicit labels like `${count} ${count === 1 ? 'review' : 'reviews'}`.
