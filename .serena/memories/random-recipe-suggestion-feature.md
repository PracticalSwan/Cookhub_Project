# Random Recipe Suggestion Feature Memory

**Memory Type:** Feature Implementation Memory  
**Date Created:** February 11, 2026  
**Related Implementation Plan:** `plan/feature-random-recipe-suggestion-1.md` (v1.1, Feb 9, 2026)  
**Related Documentation:** `plan/feature-guest-mode-1.md` (v1.2, Feb 9, 2026) for cross-feature compatibility

## Feature Summary

Random Recipe Suggestion provides users with quality-filtered random recipe recommendations via a "Surprise Me" button on the Home page. Feature opens modal with recipe details and navigation options.

## Core Architecture

**Button Location:** Home page hero section (existing Search.jsx component)  
**Entry Point:** `src/pages/Recipe/Home.jsx` - "Surprise Me" button (existing page, new button)  
**Data Flow:** storage.getRandomSuggestion() → Modal.jsx (existing component) → RecipeDetail navigation  
**Quality Constraints:** 
- Primary filter: >= 5 likes AND >= 1 review  
- Fallback: Any published recipe (if no recipes meet primary constraints)  
- Excludes: Unpublished, pending, rejected recipes  

## Key Implementation Details

### Modal Integration
- **Component:** Existing `src/components/ui/Modal.jsx`
- **Content:** Recipe image (with aspect ratio and loading state), title, difficulty badge, like/review counts, navigation buttons
- **Buttons:** "View Recipe" (navigates to RecipeDetail), "Try Another" (loads new suggestion)
- **State Management:** useState for open/close, loading state during "Try Another", suggestion state reset on unmount

### Storage Layer Updates
- **Function:** `getRandomSuggestion()` in `src/lib/storage.js`
- **Logic:** Filter readable recipes, apply quality constraints, random selection, cache optimization (1 minute)
- **Dependencies:** Uses existing getUsers(), getRecipes(), getReviews(recipeId)
- **Analytics:** Normal users increment view counts via recipeDetail, guests do NOT (see Guest Mode compatibility)

### Styling & UX
- **Button:** Brand color #C8102E from Tailwind theme, positioned in Search.jsx hero section
- **Modal:** Consistent with existing Modal patterns, backdrop blur, smooth animations
- **Images:** Fixed aspect ratio, skeleton loading states, graceful fallback for broken URLs
- **Accessibility:** ARIA labels, keyboard navigation, focus management, screen reader announcements

### Testing Strategy
- **Manual Testing:** 30+ functional edge cases, visual quality, responsive design, accessibility
- **Automated Testing:** Playwright E2E tests (Phase 6, TASK-036-TASK-047)
- **Cross-Browser:** Chrome, Firefox, Edge, Safari verification
- **Performance:** Layout shift monitoring (CLS), loading state verification

## Guest Mode Integration

Implemented cross-feature compatibility with Guest Mode (v1.2, Feb 9, 2026):

- **Read-Only Access:** Guests can view suggestions and navigate to recipes
- **Analytics Isolation:** Guest usage does NOT increment view counts or appear in daily_stats
- **UI Integration:** Works seamlessly with Guest Mode AuthContext canInteract logic
- **Test Coverage:** TEST-RS-ROLE-005 verifies Guest user experience

## Acceptance Criteria

**Total:** 35 acceptance criteria (AC-RS-001 through AC-RS-035)  
**Key Categories:**
- Functional completeness (AC-RS-001 through AC-RS-008)
- Data integrity & filtering (AC-RS-009 through AC-RS-015)
- Visual & interaction quality (AC-RS-016 through AC-RS-025)
- Accessibility & compatibility (AC-RS-026 through AC-RS-032)
- Error handling & edge cases (AC-RS-033 through AC-RS-035)

## Implementation Tasks

**Total:** 47 tasks across 6 phases (TASK-TBD through TASK-047)  
**Phases:**
1. **Storage & Core Logic:** getRandomSuggestion implementation (TASK-001 through TASK-007)
2. **Modal & State:** Modal integration and state management (TASK-008 through TASK-013)
3. **Styling & Visual:** Button, modal styling, image handling (TASK-014 through TASK-020)
4. **Navigation & Flow:** Recipe integration, error handling, analytics hooks (TASK-021 through TASK-025)
5. **Testing & Refinement:** Functional tests, responsiveness, accessibility (TASK-026 through TASK-035)
6. **Playwright Automated:** E2E test setup and execution (TASK-036 through TASK-047)

## Risk Management

**Mitigated Risks:**
- Request collisions: Loading states disable concurrent requests
- Image loading: Fixed aspect ratios prevent layout shift
- Empty state: Explicit messaging when no recipes available
- Modal cleanup: useEffect prevents memory leaks

**Active Mitigations:**
- RISK-RS-005: Request ID/cancellation token for "Try Another"
- RISK-RS-004: Caching strategy every 1 minute for repeated calls
- RISK-RS-001: Documented that random repetition is expected behavior

## Cross-Feature Dependencies

### Guest Mode Dependency
- **DEP-RS-CROSS-001:** Depends on Guest Mode AuthContext isGuest flag for canInteract logic
- **DEP-RS-CROSS-002:** Depends on storage analytics bypass for guest users (recordView verification)
- **DEP-RS-CROSS-003:** Guest-UA notifications orchestration
- **Implementation Order:** Guest Mode should be implemented first to ensure analytics isolation works correctly

## Quality Assurance

**Test Stats:**
- Manual tests: 30+ edge cases covering all AC criteria
- Automated tests: 12 Playwright tests covering modal flow, navigation, error states
- Randomness testing: Statistical verification (50-100 trials, chi-square test)
- Performance: CLS monitoring, loading animations optimization

**Browser Support:**
- Modern browsers (Chrome 90+, Firefox 88+, Edge 90+, Safari 14+)
- Responsive design verified: Mobile (< 640px), Tablet (640-1024px), Desktop (>1024px)

## Future Extensibility

**Enhancement Opportunities:**
- Personalized suggestions: Machine learning based on user history
- Category filtering: Honoring existing category UI preferences
- Seasonal suggestions: Time-aware recipe recommendations
- Social features: "Surprise a friend" functionality

**Backend Migration Notes:**
- Client-side filtering logic will translate to backend query filters
- View count tracking to respect guest mode permissions
- Caching strategy to move to Redis or similar

## Files Modified

Based on current project structure:
- `src/lib/storage.js`: Add getRandomSuggestion()
- `src/pages/Recipe/Home.jsx`: Add "Surprise Me" button in Search component hero section
- `src/components/ui/Modal.jsx`: Ensure image handling support (aspect ratio, error states)
- Tests: `tests/random-recipe.spec.js` (creation) in Phase 6

## Related Documentation

- [Recipe Features Memory](../recipe-features.md) - Recipe interaction patterns
- [Storage Data Model](../storage-data-model.md) - localStorage structure
- [Auth Context Memory](../auth-context.md) - Authentication state management
- [Guest Mode Plan](../../plan/feature-guest-mode-1.md) - Cross-feature compatibility