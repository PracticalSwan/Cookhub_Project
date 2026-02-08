---
goal: Random Recipe Suggestion Feature - Smart recipe recommendations with quality constraints
version: 1.0
date_created: 2026-02-09
last_updated: 2026-02-09
owner: Project Team
status: 'Planned'
tags: ['feature', 'recipe-suggestion', 'random', 'ui-components', 'testing']
---

# Introduction

![Status: Planned](https://img.shields.io/badge/status-Planned-blue)

This implementation plan adds a random recipe suggestion feature to the Recipe Sharing System. When users click "Surprise Me", the system recommends a random recipe that meets quality criteria (at least 5 likes and 1 review). If no recipes match these constraints, the system falls back to suggesting any published recipe. The suggestion is presented in a modal with options to view the recipe or try again.

## 1. Requirements & Constraints

### Functional Requirements

- **FREQ-RS-001**: Users must be able to access random recipe suggestion from Home page
- **FREQ-RS-002**: Suggested recipes must meet quality constraints: >= 5 likes AND >= 1 review
- **FREQ-RS-003**: System must fall back to any published recipe if no recipes match constraints
- **FREQ-RS-004**: System must handle empty recipe list gracefully with appropriate message
- **FREQ-RS-005**: Suggestion modal must display recipe details (image, title, difficulty, likes, reviews)
- **FREQ-RS-006**: Suggestion modal must provide "View Recipe" button to navigate to RecipeDetail page
- **FREQ-RS-007**: Suggestion modal must provide "Try Another" button to get new suggestion
- **FREQ-RS-008**: "Try Another" button must show loading state while fetching new suggestion
- **FREQ-RS-009**: Must suggest only published recipes (status === 'published')
- **FREQ-RS-010**: Feature must be accessible to all user types (admin, user, pending, suspended)
- **FREQ-RS-011**: Random selection must be truly random using Math.random()
- **FREQ-RS-012**: Each "Try Another" click should fetch fresh random selection

### Technical Constraints

- **CON-RS-001**: Must work with existing localStorage-based storage layer
- **CON-RS-002**: Must use existing storage.js API surface (add new function only)
- **CON-RS-003**: Must not modify existing recipe data model
- **CON-RS-004**: Must follow existing React component patterns
- **CON-RS-005**: Must reuse existing Modal, Button, Badge components
- **CON-RS-006**: Must be compatible with existing routing (HashRouter)
- **CON-RS-007**: Must handle null/undefined likedBy arrays safely

### Data Requirements

- **DATA-RS-001**: Uses existing Recipe model (likedBy array, status, id)
- **DATA-RS-002**: Uses existing Reviews model (getReviews(recipeId) returns array)
- **DATA-RS-003**: No new localStorage keys required
- **DATA-RS-004**: No persistence required for suggestions

### UI/UX Requirements

- **UI-RS-001**: "Surprise Me" button must be visible on Home page
- **UI-RS-002**: Button placement should be intuitive (near search bar in hero section)
- **UI-RS-003**: Suggestion modal must use Modal component with proper backing
- **UI-RS-004**: Modal must be resizable and responsive (mobile-friendly)
- **UI-RS-005**: Recipe image in modal must be full-width and properly proportioned
- **UI-RS-006**: Must show badge for difficulty level
- **UI-RS-007**: Must display like count and review count to justify suggestion quality
- **UI-RS-008**: Must support closing modal via ESC key, backdrop click, or close button
- **UI-RS-009**: Loading state must have visual feedback (spinner or button disabled state)

### Accessibility Requirements

- **A11Y-RS-001**: "Surprise Me" button must have proper ARIA labels
- **A11Y-RS-002**: Modal must focus management (trap focus when open)
- **A11Y-RS-003**: Modal must be keyboard navigable (ESC to close, Tab to navigate)
- **A11Y-RS-004**: Loading states must be announced to screen readers

### Testing Requirements

- **TEST-RS-001**: Test with recipes matching constraints (>= 5 likes, >= 1 review)
- **TEST-RS-002**: Test fallback behavior when no recipes meet constraints
- **TEST-RS-003**: Test empty state when no recipes exist
- **TEST-RS-004**: Test random selection produces different suggestions
- **TEST-RS-005**: Test "Try Another" functionality multiple times
- **TEST-RS-006**: Test "View Recipe" button navigates correctly
- **TEST-RS-007**: Test modal close interactions (ESC, backdrop, X button)
- **TEST-RS-008**: Test responsive design on mobile and desktop
- **TEST-RS-009**: Test with pending/suspended users (feature should work for all)
- **TEST-RS-010**: Test loading states prevent duplicate requests

### Guidelines & Patterns

- **GUD-RS-001**: Follow existing storage.js function patterns (getRecipes, getReviews, etc.)
- **GUD-RS-002**: Use existing UI component library (Modal, Button, Badge, Card structures)
- **GUD-RS-003**: Use existing state management patterns from Home.jsx
- **GUD-RS-004**: Follow existing navigation patterns (useNavigate for "View Recipe")
- **GUD-RS-005**: Use existing Tailwind v4 color scheme (brand #C8102E, cool-gray scales)
- **GUD-RS-006**: Follow existing hero section styling from Home.jsx
- **PAT-RS-001**: Reuse existing Modal component wrapper pattern
- **PAT-RS-002**: Follow RecipeCard structure for suggestion display
- **PAT-RS-003**: Use existing useEffect pattern for data fetching
- **PAT-RS-004**: Use existing cn() utility for className merging

## 2. Implementation Steps

### Implementation Phase 1: Storage Layer Function (Estimated: 1-2 hours)

- GOAL-001: Add getRandomSuggestion function to storage.js with quality constraint filtering

| Task     | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-001 | Update `src/lib/storage.js` - Add `getRandomSuggestion()` function that filters published recipes by constraints (>= 5 likes, >= 1 review) |           |            |
| TASK-002 | Update `src/lib/storage.js` - Implement fallback logic to use all published recipes when none match constraints |           |            |
| TASK-003 | Update `src/lib/storage.js` - Return null when no published recipes exist for proper empty state handling |           |            |
| TASK-004 | Update `src/lib/storage.js` - Export the new `getRandomSuggestion()` function |           |            |

### Implementation Phase 2: Suggestion Modal Component (Estimated: 2-3 hours)

- GOAL-002: Create RecipeSuggestionModal component using existing Modal and Button patterns

| Task     | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-005 | Create `src/components/recipe/RecipeSuggestionModal.jsx` - Component structure with Modal wrapper, recipe data display, and action buttons |           |            |
| TASK-006 | Update `src/components/recipe/RecipeSuggestionModal.jsx` - Implement recipe display section with image, title, difficulty badge, likes count, reviews count |           |            |
| TASK-007 | Update `src/components/recipe/RecipeSuggestionModal.jsx` - Add "View Recipe" button with navigation to RecipeDetail page using recipe ID |           |            |
| TASK-008 | Update `src/components/recipe/RecipeSuggestionModal.jsx` - Add "Try Another" button with onTryAgain handler and loading state |           |            |
| TASK-009 | Update `src/components/recipe/RecipeSuggestionModal.jsx` - Implement empty state with user-friendly message when recipe is null |           |            |
| TASK-010 | Update `src/components/recipe/RecipeSuggestionModal.jsx` - Add close button (X) in modal header and backdrop click handler |           |            |
| TASK-011 | Update `src/components/recipe/RecipeSuggestionModal.jsx` - Style component using Tailwind v4 colors and existing patterns |           |            |

### Implementation Phase 3: Home Page Integration (Estimated: 2-3 hours)

- GOAL-003: Integrate "Surprise Me" functionality into Home.jsx hero section

| Task     | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-012 | Update `src/pages/Recipe/Home.jsx` - Add state variables: randomSuggestion, isSuggestionModalOpen, isLoadingSuggestion |           |            |
| TASK-013 | Update `src/pages/Recipe/Home.jsx` - Add `handleSurpriseMe` async function that calls getRandomSuggestion() and handles loading/empty state |           |            |
| TASK-014 | Update `src/pages/Recipe/Home.jsx` - Add "Surprise Me" button in hero section next to search bar with proper styling |           |            |
| TASK-015 | Update `src/pages/Recipe/Home.jsx` - Wire up "Surprise Me" button click to handleSurpriseMe function |           |            |
| TASK-016 | Update `src/pages/Recipe/Home.jsx` - Add RecipeSuggestionModal component to JSX with proper state bindings (isOpen, onClose, recipe, onTryAgain) |           |            |
| TASK-017 | Update `src/pages/Recipe/Home.jsx` - Add onTryAgain handler that calls handleSurpriseMe again to fetch new suggestion |           |            |
| TASK-018 | Update `src/pages/Recipe/Home.jsx` - Add onViewRecipe handler that navigates to /recipe/{id} and closes modal |           |            |
| TASK-019 | Update `src/pages/Recipe/Home.jsx` - Ensure modal state resets when component unmounts or user navigates away |           |            |

### Implementation Phase 4: Styling & Polish (Estimated: 1-2 hours)

- GOAL-004: Refine visual design and ensure responsive behavior

| Task     | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-020 | Verify RecipeSuggestionModal responsive design - test on mobile (375px), tablet (768px), desktop (1024px+) |           |            |
| TASK-021 | Verify "Surprise Me" button visibility and sizing across all screen sizes |           |            |
| TASK-022 | Verify recipe image aspect ratio in modal prevents layout shift |           |            |
| TASK-023 | Verify loading state visual feedback is clear (spinner or button text change) |           |            |
| TASK-024 | Verify color contrast and accessibility meet WCAG standards |           |            |
| TASK-025 | Verify modal transitions (fade-in, backdrop blur) are smooth |           |            |

### Implementation Phase 5: Testing & Validation (Estimated: 2-3 hours)

- GOAL-005: Comprehensive testing of all functionality and edge cases

| Task     | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-026 | Test with recipes that meet constraints (has recipe with >= 5 likes and >= 1 review) - verify suggestion shows correct recipe |           |            |
| TASK-027 | Test fallback behavior - modify test data to have no recipes matching constraints, verify any published recipe is suggested |           |            |
| TASK-028 | Test empty state - clear all recipes, verify modal shows empty message |           |            |
| TASK-029 | Test random selection - click "Try Another" multiple times, verify different recipes are suggested (statistical test with 10+ suggestions) |           |            |
| TASK-030 | Test "View Recipe" navigation - verify navigates to correct RecipeDetail page and recipe loads |           |            |
| TASK-031 | Test modal close methods - verify ESC key, backdrop click, and X button all close modal |           |            |
| TASK-032 | Test "Try Another" loading state - verify rapid clicks don't cause duplicate suggestions |           |            |
| TASK-033 | Test with pending/suspended users - login as pending user, verify feature works (read-only access only) |           |            |
| TASK-034 | Test responsive layout - resize browser window, verify modal and button remain usable |           |            |
| TASK-035 | Test accessibility - use keyboard navigation (Tab, Enter, ESC) to verify modal is keyboard accessible |           |            |

## 3. Alternatives

### Alternative Approaches Considered

- **ALT-RS-001**: Create dedicated /surprise route and page instead of modal
  - **Decision**: REJECTED
  - **Rationale**: Modal provides better UX, no page reload needed, faster interaction
  - **Trade-off**: Simpler routing vs. better user experience

- **ALT-RS-002**: Store last suggestion in localStorage
  - **Decision**: REJECTED
  - **Rationale**: No persistence needed; user can always click "Try Again"
  - **Trade-off**: Would add complexity without clear user benefit

- **ALT-RS-003**: Show recipe suggestions randomly in home grid interspersed
  - **Decision**: REJECTED
  - **Rationale**: Intentional action ("Surprise Me") is better than passive suggestions
  - **Trade-off**: Less discoverable but more user-controlled

- **ALT-RS-004**: Filter by user preferences (cookinglevel, favorite categories)
  - **Decision**: DEFERRED for future enhancement
  - **Rationale**: Out of scope for initial feature; personalization better as follow-up
  - **Trade-off**: Less personalized vs. simpler initial implementation

- **ALT-RS-005**: Create separate suggestion logic with algorithm (smart recommendations)
  - **Decision**: REJECTED
  - **Rationale**: Random selection meets requirements; smart recommendations require more infrastructure
  - **Trade-off**: Simpler vs. more sophisticated matching

- **ALT-RS-006**: Use server-side random generation (when backend is added)
  - **Decision**: REJECTED for client-side version
  - **Rationale**: Project is currently client-only; server-side optimization unnecessary
  - **Trade-off**: Less scalable vs. matches current architecture

**Chosen Approach**: Add getRandomSuggestion function to storage.js, create RecipeSuggestionModal component, integrate button into Home.jsx hero, use existing UI components and patterns. This provides feature richness with minimal architectural changes.

## 4. Dependencies

### External Dependencies

- **DEP-RS-001**: Math.random() - Built-in JavaScript function (no install needed)
- **DEP-RS-002**: React hooks (useState, useEffect, useNavigate) - Already in project

### Internal Dependencies

- **DEP-RS-003**: `src/lib/storage.js` - Must be updated with getRandomSuggestion (TASK-001 to TASK-004)
- **DEP-RS-004**: `src/components/ui/Modal.jsx` - Must exist and work correctly (used by TASK-005)
- **DEP-RS-005**: `src/components/ui/Button.jsx` - Must exist for "Surprise Me" and modal buttons (used in TASK-005, TASK-014)
- **DEP-RS-006**: `src/components/ui/Badge.jsx` - Must exist for difficulty badge display (used in TASK-006)
- **DEP-RS-007**: `src/pages/Recipe/Home.jsx` - Must be modified for integration (TASK-012 to TASK-019)
- **DEP-RS-008**: `src/pages/Recipe/RecipeDetail.jsx` - Must exist for view recipe navigation (used in TASK-018)

### Data Dependencies

- **DEP-RS-009**: `getRecipes()` function from storage.js - Returns all recipes including likedBy arrays
- **DEP-RS-010**: `getReviews(recipeId)` function from storage.js - Returns reviews array for constraint checking
- **DEP-RS-011**: Recipe data model - Must have `status`, `likedBy` (array), `id` fields

### Build Dependencies

- **DEP-RS-012**: Vite dev server must be running for testing
- **DEP-RS-013**: Existing Home page must be functional before adding feature
- **DEP-RS-014**: Recipe data must be seeded for testing (use existing seed data)

## 5. Files

### Files to Modify

- **FILE-RS-001**: `src/lib/storage.js`
  - Add getRandomSuggestion() function
  - Filter published recipes by constraints
  - Implement fallback to all published recipes
  - Handle empty recipe list (return null)
  - Export new function

- **FILE-RS-002**: `src/pages/Recipe/Home.jsx`
  - Add state: randomSuggestion, isSuggestionModalOpen, isLoadingSuggestion
  - Add handleSurpriseMe() async function
  - Add "Surprise Me" button in hero section
  - Add RecipeSuggestionModal component
  - Add onTryAgain and onViewRecipe handlers
  - Manage modal state lifecycle (reset on unmount)

### Files to Create

- **FILE-RS-003**: `src/components/recipe/RecipeSuggestionModal.jsx`
  - Component structure with Modal wrapper
  - Recipe display section (image, title, difficulty, likes, reviews)
  - "View Recipe" button with navigation
  - "Try Another" button with loading state
  - Empty state display (when recipe === null)
  - Close button (X) and backdrop handler
  - Tailwind v4 styling matching existing UI patterns

## 6. Acceptance Criteria

The Random Recipe Suggestion feature will be considered complete and ready for deployment when all of the following criteria are met:

### Functional Completeness

- **AC-RS-001**: "Surprise Me" button is visible and clickable on Home page
- **AC-RS-002**: Clicking "Surprise Me" opens modal with a recipe suggestion
- **AC-RS-003**: Suggested recipe has image, title, difficulty badge, like count, and review count displayed
- **AC-RS-004**: Suggestion meets quality constraints (>= 5 likes AND >= 1 review) if such recipes exist
- **AC-RS-005**: When no recipes meet constraints, fallback to any published recipe is suggested
- **AC-RS-006**: "View Recipe" button navigates to RecipeDetail page for suggested recipe
- **AC-RS-007**: "Try Another" button fetches a new random suggestion
- **AC-RS-008**: "Try Another" button shows loading state while fetching
- **AC-RS-009**: Multiple "Try Another" clicks produce different suggestions (randomness verified)
- **AC-RS-010**: Modal can be closed via ESC key, backdrop click, or X button
- **AC-RS-011**: Feature works for all user types (admin, user, pending, suspended)
- **AC-RS-012**: Only published recipes are suggested (status === 'published')

### Quality & Robustness

- **AC-RS-013**: System handles empty recipe list gracefully with user-friendly message
- **AC-RS-014**: Loading state prevents duplicate suggestion requests
- **AC-RS-015**: Modal state is properly managed (opens/closes correctly, no state leaks)
- **AC-RS-016**: No console errors or warnings when using the feature
- **AC-RS-017**: Feature works correctly across page navigations (random suggestion persists if modal stays open)
- **AC-RS-018**: Image loading errors are handled gracefully (fallback to placeholder)

### UI/UX Quality

- **AC-RS-019**: Modal design matches existing UI patterns and color scheme
- **AC-RS-020**: "Surprise Me" button placement is intuitive (near search bar in hero)
- **AC-RS-021**: Button has hover state and active feedback
- **AC-RS-022**: Modal is responsive and usable on mobile (screen width < 640px)
- **AC-RS-023**: Recipe image maintains proper aspect ratio without layout shift
- **AC-RS-024**: Loading state provides clear visual feedback (spinner or button state change)
- **AC-RS-025**: Modal has smooth fade-in animation and backdrop blur effect

### Accessibility & Standards

- **AC-RS-026**: "Surprise Me" button has proper ARIA label or text
- **AC-RS-027**: Modal has focus trapping (Tab cycles through modal content only)
- **AC-RS-028**: ESC key closes modal
- **AC-RS-029**: Color contrast meets WCAG AA standards (verified with color contrast tool)
- **AC-RS-030**: Feature is keyboard navigable (Tab, Enter, ESC keys work correctly)
- **AC-RS-031**: Loading states are announced to screen readers

#### Definition of Done

The Random Recipe Suggestion feature is **DONE** when:

1. All 31 acceptance criteria (AC-RS-001 through AC-RS-031) are met
2. All 35 implementation tasks (TASK-001 through TASK-035) are marked as completed
3. Manual testing of all 10 test scenarios (TASK-026 through TASK-035) is completed
4. No open bugs or issues related to random suggestion functionality
5. Code review confirms adherence to existing patterns and standards
6. Feature is documented in README or user guide (if applicable)

## 7. Testing

### Functional Testing

- **TEST-RS-FUNC-001**: Quality Constraint Filtering (TASK-026)
  - Test data: Create recipe with 5 likes and 1 review
  - Click "Surprise Me"
  - Verify suggested recipe has >= 5 likes and >= 1 review
  - Repeat 10 times: verify all suggestions meet constraints (if enough exist)

- **TEST-RS-FUNC-002**: Fallback Behavior (TASK-027)
  - Test data: No recipes with >= 5 likes or >= 1 review (modify or remove data)
  - Ensure published recipes exist
  - Click "Surprise Me"
  - Verify suggested recipe is published but may NOT meet constraints

- **TEST-RS-FUNC-003**: Empty State (TASK-028)
  - Test data: Clear all recipes (or set all to rejected status)
  - Click "Surprise Me"
  - Verify modal shows "No recipes available" message
  - Verify no recipe card renders

- **TEST-RS-FUNC-004**: Random Selection (TASK-029)
  - Ensure 10+ published recipes exist
  - Click "Try Another" 20 times
  - Record suggested recipe IDs
  - Calculate distribution: verify no single recipe appears > 30% of time (statistical randomness)

- **TEST-RS-FUNC-005**: View Recipe Navigation (TASK-030)
  - Click "Surprise Me"
  - Click "View Recipe" in modal
  - Verify URL changes to /recipe/{id}
  - Verify RecipeDetail page loads with correct recipe
  - Verify modal is closed

### Modal Interaction Testing

- **TEST-RS-MODAL-001**: ESC Key Close (TASK-031)
  - Click "Surprise Me"
  - Verify modal is open
  - Press ESC key
  - Verify modal closes

- **TEST-RS-MODAL-002**: Backdrop Click Close (TASK-031)
  - Click "Surprise Me"
  - Verify modal is open
  - Click modal backdrop (grayed-out area)
  - Verify modal closes

- **TEST-RS-MODAL-003**: X Button Close (TASK-031)
  - Click "Surprise Me"
  - Verify modal is open
  - Click X button in modal header
  - Verify modal closes

- **TEST-RS-MODAL-004**: Try Another Loading (TASK-032)
  - Click "Surprise Me"
  - Immediately click "Try Another" twice rapidly
  - Verify only one suggestion loads
  - Verify loading state prevents duplicate clicks
  - Verify final suggestion is different from first (statistical)

### User Role Testing

- **TEST-RS-ROLE-001**: Admin User (TASK-033)
  - Login as admin user
  - Click "Surprise Me"
  - Verify feature works (modal opens, suggestion displays)
  - Verify "View Recipe" and "Try Another" buttons work

- **TEST-RS-ROLE-002**: Regular User (TASK-033)
  - Login as regular user
  - Click "Surprise Me"
  - Verify feature works

- **TEST-RS-ROLE-003**: Pending User (TASK-033)
  - Login as pending user
  - Click "Surprise Me"
  - Verify feature works (read-only access only)
  - Verify modal displays correctly

- **TEST-RS-ROLE-004**: Suspended User (TASK-033)
  - Login as suspended user
  - Click "Surprise Me"
  - Verify feature works (read-only access only)
  - Verify modal displays correctly

### Responsive Design Testing

- **TEST-RS-RESP-001**: Mobile (< 640px) (TASK-034)
  - Open browser DevTools
  - Set viewport to iPhone SE (375px width)
  - Click "Surprise Me"
  - Verify button is fully visible and clickable
  - Verify modal fits screen width with proper scrolling
  - Verify recipe image displays correctly

- **TEST-RS-RESP-002**: Tablet (640px - 1024px) (TASK-034)
  - Set viewport to iPad (768px width)
  - Click "Surprise Me"
  - Verify layout looks appropriate
  - Verify modal centers correctly

- **TEST-RS-RESP-003**: Desktop (> 1024px) (TASK-034)
  - Set viewport to 1920px width
  - Click "Surprise Me"
  - Verify modal centers and has appropriate max-width
  - Verify visual balance

### Visual & Styling Testing

- **TEST-RS-VIS-001**: Color Scheme (TASK-024)
  - Verify "Surprise Me" button uses brand color #C8102E
  - Verify modal uses cool-gray colors from theme
  - Use color contrast checker: verify all text meets WCAG AA (4.5:1 ratio)

- **TEST-RS-VIS-002**: Image Aspect Ratio (TASK-022)
  - Open DevTools Performance tab
  - Click "Surprise Me"
  - Measure Layout Shift: verify no CLS > 0.1
  - Verify image maintains consistent proportions

- **TEST-RS-VIS-003**: Loading State (TASK-023)
  - Click "Surprise Me"
  - Monitor "Try Another" button
  - Verify: button shows spinner OR text changes to "Loading..."
  - Verify: button is disabled during load
  - Click rapidly: verify state persists until complete

- **TEST-RS-VIS-004**: Modal Transitions (TASK-025)
  - Click "Surprise Me"
  - Record modal fade-in animation: verify smooth (no jarring jumps)
  - Verify backdrop blur effect is visible
  - Close modal, verify fade-out animation is smooth

### Accessibility Testing

- **TEST-RS-A11Y-001**: Keyboard Navigation (TASK-035)
  - Use keyboard only (no mouse)
  - Tab to "Surprise Me" button
  - Press Enter
  - Verify modal opens
  - Tab through modal elements
  - Press ESC
  - Verify modal closes

- **TEST-RS-A11Y-002**: Focus Management (AC-RS-027)
  - Use screen reader or DevTools Accessibility panel
  - Click "Surprise Me"
  - Verify focus moves to first interactive elements inside modal
  - Tab through modal: verify focus stays inside modal
  - Close modal: verify focus returns to "Surprise Me" button

- **TEST-RS-A11Y-003**: ARIA Labels (AC-RS-026)
  - Inspect "Surprise Me" button: verify has aria-label or descriptive text
  - Inspect "View Recipe" button: verify has aria-label
  - Inspect "Try Another" button: verify has aria-label
  - Inspect Close (X) button: verify has aria-label="Close modal"

- **TEST-RS-A11Y-004**: Screen Reader Announcements (AC-RS-031, TASK-023)
  - Use screen reader (NVDA, JAWS, or VoiceOver)
  - Click "Surprise Me"
  - Verify modal open is announced
  - Click "Try Another"
  - Verify "Loading, please wait" or similar message is announced
  - Verify new recipe suggestion is announced

### Edge Case Testing

- **TEST-RS-EDGE-001**: Recipes with 0 likes (AC-RS-012)
  - Test data: Recipes with likedBy.length = 0
  - Click "Surprise Me"
  - Verify these recipes are not suggested (if recipes with >= 5 likes exist)

- **TEST-RS-EDGE-002**: Recipes with 0 reviews (AC-RS-012)
  - Test data: Recipes with empty reviews array
  - Click "Surprise Me"
  - Verify these recipes are not suggested (if recipes with >= 1 review exist)

- **TEST-RS-EDGE-003**: Unpublished Recipes (AC-RS-012)
  - Test data: Mix of published, pending, rejected recipes
  - Verify only published recipes can be suggested
  - Verify pending and rejected recipes never appear in suggestions

- **TEST-RS-EDGE-004**: Recipe with missing likedBy array (CON-RS-007)
  - Simulate recipe without likedBy property (null or undefined)
  - Click "Surprise Me"
  - Verify no errors occur (likes treated as 0)
  - Verify system continues to work

- **TEST-RS-EDGE-005**: Image Loading Failure (AC-RS-018)
  - Test data: Recipe with broken image URL
  - Click "Surprise Me"
  - Verify modal displays with fallback or placeholder image
  - Verify no console errors

### State Management Testing

- **TEST-RS-STATE-001**: Modal State Reset (TASK-019)
  - Click "Surprise Me"
  - Open recipe suggestion
  - Navigate to Profile or Admin page
  - Return to Home page
  - Click "Surprise Me" again
  - Verify modal shows new suggestion (state was reset)

- **TEST-RS-STATE-002**: Component Unmount (TASK-019)
  - Click "Surprise Me"
  - Open modal
  - Close browser tab (or navigate to different route)
  - Reopen app
  - Verify no stale suggestion state persists

### Test Execution Order

1. **Phase 1 to 2**: Implement Storage and Modal (TASK-001 to TASK-011)
   - Manual test: getRandomSuggestion function in browser console
   - Verify modal renders with test data

2. **Phase 3**: Home Page Integration (TASK-012 to TASK-019)
   - Integration test: Click "Surprise Me" from Home page
   - Verify modal opens with suggestion

3. **Phase 4 - 5**: Styling and Testing (TASK-020 to TASK-035)
   - Execute all test suites in order:
     - Functional testing first (TASK-026 to TASK-030)
     - Modal interaction testing (TASK-031, TASK-032)
     - User role testing (TASK-033)
     - Responsive design testing (TASK-034)
     - Visual & styling testing (TASK-020 to TASK-025)
     - Accessibility testing (TASK-035)
     - Edge case testing (TEST-RS-EDGE-001 to TEST-RS-EDGE-005)
     - State management testing (TEST-RS-STATE-001 to TEST-RS-STATE-002)

## 8. Risks & Assumptions

### Implementation Risks

- **RISK-RS-001**: getRandomSuggestion may return same recipe multiple times in a row (random nature)
  - **Mitigation**: Document this as expected behavior; users can click "Try Another"
  - **Impact**: Low - Users control randomness via interaction

- **RISK-RS-002**: Modal state management may cause memory leaks if not cleaned up properly
  - **Mitigation**: Use useEffect cleanup to reset state on unmount (TASK-019)
  - **Impact**: Medium - Could cause performance degradation or stale state issues

- **RISK-RS-003**: Recipe image loading may cause layout shift in modal
  - **Mitigation**: Set fixed aspect ratio or use skeleton loader (TASK-022)
  - **Impact**: Low - Visual quality issue, not functional

- **RISK-RS-004**: getReviews(recipeId) may be expensive if called for all recipes during filtering
  - **Mitigation**: For client-side localStorage, this is acceptable; would optimize for backend later
  - **Impact**: Low - Acceptable performance for current architecture

- **RISK-RS-005**: User may click "View Recipe" and "Try Another" rapidly causing race conditions
  - **Mitigation**: Implement loading state to disable buttons during operations (TASK-008, TASK-032)
  - **Impact**: Low - Loading state prevents duplicate requests

- **RISK-RS-006**: Empty recipe list may cause modal to display poorly without proper handling
  - **Mitigation**: Implement explicit empty state message and UI (TASK-009, TEST-RS-FUNC-003)
  - **Impact**: Medium - Poor UX if not handled, but explicit task covers this

- **RISK-RS-007**: Existing storage.js functions may break with new getRandomSuggestion function
  - **Mitigation**: Review existing function signatures and patterns before implementation (TASK-001)
  - **Impact**: Medium - Could cause regressions in existing features
  -Validation**: Run existing tests/manual checks after TASK-004

- **RISK-RS-008**: Modal component may not support the specific layout needed for suggestions
  - **Mitigation**: Review Modal component API and existing usage patterns (TASK-005)
  - **Impact**: Low - Reuse existing component; fallback to custom modal if needed

### Assumptions

- **ASSUMPTION-RS-001**: Existing Modal component supports closing via ESC, backdrop, and X button programmatically
  - **Validation**: Review Modal.jsx implementation before TASK-010
  - **Impact**: Low - Standard modal pattern; verify during implementation

- **ASSUMPTION-RS-002**: getReviews(recipeId) returns an array (possibly empty) and accepts recipe ID parameter
  - **Validation**: Review storage.js getReviews implementation before TASK-001
  - **Impact**: Medium - Core logic for constraint checking

- **ASSUMPTION-RS-003**: Recipe model always has likedBy array (may be empty but not null/undefined)
  - **Validation**: Review seed data and recipe creation code; implement safe navigation anyway (CON-RS-007)
  - **Impact**: Low - Handled with safe navigation (likedBy?.length || 0)

- **ASSUMPTION-RS-004**: Home.jsx has hero section with search bar that can accommodate additional buttons
  - **Validation**: Review Home.jsx structure before TASK-014
  - **Impact**: Low - Can add button if hero section doesn't exist

- **ASSUMPTION-RS-005**: Test data includes recipes with various like counts and review counts for testing
  - **Validation**: Check seed data in storage.js; create test data if needed
  - **Impact**: Low - Can create test data during testing phase

- **ASSUMPTION-RS-006**: useNavigate from react-router-dom is available in Home.jsx
  - **Validation**: Check existing imports in Home.jsx
  - **Impact**: Low - Standard routing; add import if missing

- **ASSUMPTION-RS-007**: Image URLs in recipes are valid and load reliably
  - **Validation**: Test with existing recipe images during TASK-022, TASK-025
  - **Impact**: Low - Implement error handling for broken images (AC-RS-018)

### Technical Debt Considerations

- **DEBT-RS-001**: Client-side filtering is O(n) for all recipes; scales poorly with large recipe counts (> 1000)
  - **Remediation**: When backend is added, move filtering logic to server-side with database indexing
  - **Effort**: Medium (backend optimization, not urgent for current scale)

- **DEBT-RS-002**: No algorithm-based personalization (only random selection)
  - **Remediation**: Future enhancement: ML-based recommendations, user preferences, collaborative filtering
  - **Effort**: Large (requires data analysis, ML infrastructure, user tracking)

- **DEBT-RS-003**: Randomness not truly cryptographically secure (Math.random() sufficient for this use case)
  - **Remediation**: If fairness becomes critical (contests, rewards), use crypto.getRandomValues()
  - **Effort**: Small (library change, not needed for current use case)

- **DEBT-RS-004**: getReviews called for each recipe during filtering (inefficient)
  - **Remediation**: Cache review counts in recipe model or optimize with batch fetching when backend added
  - **Effort**: Medium (schema change or optimization)

- **DEBT-RS-005**: No analytics tracking for suggestion feature (acceptance rate, repeat usage)
  - **Remediation**: Add event tracking for suggestion clicks, "View Recipe" clicks, "Try Another" clicks
  - **Effort**: Small (add storage calls to record suggestion analytics)

## 9. Related Specifications / Further Reading

### Project Documentation

- [Storage Data Model](../.serena/memories/storage-data-model.md) - localStorage structure and API
- [Recipe Features](../.serena/memories/recipe-features.md) - Recipe interaction features and data model
- [UI Components and Styling](../.serena/memories/ui-components-and-styling.md) - Component library and design system
- [Project Overview](../.serena/memories/project-overview.md) - Overall project architecture

### Related Implementation Plans

- [Guest Mode Feature](./feature-guest-mode-1.md) - Guest authentication and read-only access patterns
- [Routing and Layouts](../.serena/memories/routing-layouts.md) - Navigation patterns and routing architecture

### React Documentation

- [React Hooks](https://react.dev/reference/react) - useState, useEffect, useMemo usage
- [React Routing](https://reactrouter.com/en/main) - useNavigate API and routing patterns

### UI/UX Resources

- [Modal Design Patterns](https://www.nngroup.com/articles/modal-nonmodal-dialog/) - Modal UX best practices
- [Random Number Generation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random) - Math.random() documentation
- [WCAG Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Color contrast and accessibility standards

### Future Enhancement Notes

When implementing backend or advanced features, consider:

1. **Server-side randomization**: Use database's RANDOM() or equivalent function for better performance
2. **Personalized recommendations**: Implement collaborative filtering, content-based filtering, or ML models
3. **A/B testing**: Test different suggestion algorithms (random vs. personalized vs. trending)
4. **Suggestion analytics**: Track suggestion acceptance rate, time-to-view, repeat usage metrics
5. **Exclusion filters**: Allow users to exclude recipes they've already viewed or don't like
6. **Category-specific suggestions**: Add "Surprise Me with Breakfast", "Surprise Me Desserts", etc.
7. **Seasonal recommendations**: Feature seasonal recipes during holidays or special events
8. **Trending suggestions**: Combine random selection with trending/popular recipes boost
