---
goal: Dedicated Guest Mode Feature Implementation - Read-only browsing without metrics tracking
version: 1.0
date_created: 2025-02-07
last_updated: 2025-02-07
owner: Project Team
status: 'Planned'
tags: ['feature', 'guest-mode', 'authentication', 'testing', 'playwright']
---

# Introduction

![Status: Planned](https://img.shields.io/badge/status-Planned-blue)

This implementation plan adds a dedicated Guest mode to the Recipe Sharing System, allowing users to browse recipes without creating an account. Guest mode provides read-only access equivalent to users with Pending/Suspended status but critically **does not** contribute to any analytics metrics (view counts, daily statistics, or user management dashboards).

## 1. Requirements & Constraints

### Functional Requirements

- **FREQ-G-001**: Users must be able to enter Guest mode from Login and Signup pages
- **FREQ-G-002**: Guest mode must provide read-only access to published recipes
- **FREQ-G-003**: Guests must be able to search and filter recipes
- **FREQ-G-004**: Guests must be able to view recipe details
- **FREQ-G-005**: Guest mode MUST NOT increment recipe view counts in statistics
- **FREQ-G-006**: Guest mode MUST NOT contribute to daily active user counts
- **FREQ-G-007**: Guest mode MUST NOT allow liking recipes
- **FREQ-G-008**: Guest mode MUST NOT allow favoriting recipes
- **FREQ-G-009**: Guest mode MUST NOT allow adding reviews
- **FREQ-G-010**: Guest mode MUST NOT allow creating recipes
- **FREQ-G-011**: Guest mode MUST redirect to login when accessing profile pages
- **FREQ-G-012**: Guest mode MUST NOT appear in user management dashboard
- **FREQ-G-013**: Guests must be able to switch to login/signup mode without page reload
- **FREQ-G-014**: Guest ID must persist in localStorage for session duration only
- **FREQ-G-015**: Guest mode must not record any activity in activity logs

### Technical Constraints

- **GUEST-CON-001**: Guest mode uses localStorage only (no database records)
- **GUEST-CON-002**: Guest actions must be blocked at UI level with clear messaging
- **GUEST-CON-003**: Guest search history stored in localStorage (client-side only)
- **GUEST-CON-004**: Guest mode state must be tracked in AuthContext
- **GUEST-CON-005**: No changes required to localStorage schema (reuse existing GUEST_ID key)

### Data Requirements

- **DATA-G-001**: Guests must have a unique guest ID (format: `guest-{randomId}`)
- **DATA-G-002**: Guest IDs must NOT be recorded in `daily_stats.views`
- **DATA-G-003**: Guest IDs must NOT be recorded in `daily_stats.activeUsers`

### Security Requirements

- **SEC-G-001**: Guest mode must have same access control as Pending/Suspended users
- **SEC-G-002**: Guest mode must not expose any user management features
- **SEC-G-003**: Guest mode must not expose admin endpoints or routes
- **SEC-G-004**: Guest session must be cleared on browser close (localStorage only)
- **SEC-G-005**: Guest mode must prevent privilege escalation to admin roles

### Testing Requirements

- **TEST-G-001**: All guest-mode interactions must be tested with Playwright
- **TEST-G-002**: Analytics verification must confirm no guest metrics recorded
- **TEST-G-003**: Cross-browser testing required (Chrome, Firefox, Edge, Safari)
- **TEST-G-004**: Chrome DevTools testing required for localStorage inspection
- **TEST-G-005**: Mode transition testing (guest ↔ login ↔ signup)

### Guidelines & Patterns

- **GUD-G-001**: Follow existing React component structure and patterns
- **GUD-G-002**: Use existing storage.js API surface where possible
- **GUD-G-003**: Add new storage methods only when necessary for guest-specific logic
- **GUD-G-004**: Use consistent UI messaging: "Login to {action}"
- **GUD-G-005**: Guest mode should feel seamless, no jarring transitions
- **PAT-G-001**: Follow existing AuthContext provider pattern
- **PAT-G-002**: Use existing guard patterns for protected routes
- **PAT-G-003**: Reuse existing disabled button patterns for blocked features
- **PAT-G-004**: Follow Playwright test organization patterns

## 2. Implementation Steps

### Implementation Phase 1: Core Guest Mode State Management

- GOAL-001: Implement guest mode state tracking and session logic in AuthContext and storage layer

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-001 | Update `src/context/AuthContext.jsx` - Add `isGuest` state variable with useState hook |           |            |
| TASK-002 | Update `src/context/AuthContext.jsx` - Add `enterGuestMode()` function to set guest state and generate guest ID |           |            |
| TASK-003 | Update `src/context/AuthContext.jsx` - Modify `canInteract` to return false for guests (same as pending/suspended users) |           |            |
| TASK-004 | Update `src/lib/storage.js` - Modify `recordView()` to skip daily_stats.views recording for guests with viewer Key pattern `guest:{id}` |           |            |
| TASK-005 | Update `src/lib/storage.js` - Modify `recordActiveUser()` and `recordNewUser()` to skip processing for guest IDs |           |            |

### Implementation Phase 2: Guest Mode Entry UI

- GOAL-002: Add "Continue as Guest" option to authentication pages

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-006 | Update `src/pages/Auth/Login.jsx` - Add "Continue as Guest" button with styling consistent with existing UI |           |            |
| TASK-007 | Update `src/pages/Auth/Signup.jsx` - Add "Continue as Guest" button with consistent styling and messaging |           |            |

### Implementation Phase 3: Navigation Updates for Guest Mode

- GOAL-003: Update navigation components to reflect guest state and provide login/signup options

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-008 | Update `src/components/layout/Navbar.jsx` - Show "Guest" badge and Login/Signup buttons when in guest mode |           |            |
| TASK-009 | Update `src/components/layout/Sidebar.jsx` - Update menu items to hide Profile link and show Login/Signup for guests |           |            |

### Implementation Phase 4: Feature Blocking for Guest Interactions

- GOAL-004: Block all interactive features for guests with appropriate UI messaging

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-010 | Update `src/pages/Recipe/RecipeDetail.jsx` - Disable like/favorite/review buttons and show "Login to {action}" tooltips/messages |           |            |
| TASK-011 | Update `src/pages/Recipe/CreateRecipe.jsx` - Check for guest mode and redirect or show "Login to create recipes" message |           |            |
| TASK-012 | Update `src/pages/Recipe/Profile.jsx` - Add useEffect to redirect guests to login page if isGuest is true |           |            |
| TASK-013 | Verify `src/pages/Admin/*.jsx` - Confirm admin pages already block access for non-admin users (includes guests) |           |            |

### Implementation Phase 5: Playwright Testing Setup

- GOAL-005: Initialize Playwright test framework and configuration

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-014 | Install Playwright and required dependencies in project root via npm/pnpm |           |            |
| TASK-015 | Create `playwright.config.js` - Configure Playwright for Vite/React testing environment |           |            |
| TASK-016 | Create `tests/guest-mode.spec.js` - Set up test file structure with fixture definitions |           |            |

### Implementation Phase 6: Guest Mode Functionality Testing

- GOAL-006: Write comprehensive Playwright tests for guest mode features and blocks

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-017 | Write Playwright test: Guest mode entry from Login page - verify URL change and Guest badge visibility |           |            |
| TASK-018 | Write Playwright test: Guest mode entry from Signup page - verify consistent behavior across both entry points |           |            |
| TASK-019 | Write Playwright test: Guest browsing - verify can view Home page and recipe cards |           |            |
| TASK-020 | Write Playwright test: Guest search - verify can search and filter recipes |           |            |
| TASK-021 | Write Playwright test: Guest recipe detail view - verify can view recipe details |           |            |

### Implementation Phase 7: Guest Mode Blocking Verification

- GOAL-007: Write tests to verify all interactive features are blocked for guests

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-022 | Write Playwright test: LikeBlocking - verify like buttons are disabled and show login prompt |           |            |
| TASK-023 | Write Playwright test: FavoriteBlocking - verify favorite buttons are disabled and show login prompt |           |            |
| TASK-024 | Write Playwright test: ReviewBlocking - verify review form submission is blocked |           |            |
| TASK-025 | Write Playwright test: RecipeCreationBlocking - verify CreateRecipe page shows login prompt for guests |           |            |
| TASK-026 | Write Playwright test: ProfileRedirect - verify guests are redirected to login when accessing profile |           |            |

### Implementation Phase 8: Analytics Verification Testing

- GOAL-008: Create tests to confirm guests do not contribute to analytics metrics

| Task    | Description                                                   | Completed | Date       |
|--------|-------------------------------------------------------------|-----------|-------------|
| TASK-027 | Create `tests/guest-analytics.spec.js` - Set up analytics verification test file structure |           |            |
| TASK-028 | Write Playwright test: ViewCountNotTracked - verify guest views do not increment daily_stats.views |           |            |
| TASK-029 | Write Playwright test: ActiveUserNotCounted - verify guests are not in daily_stats.activeUsers array |           |            |
| TASK-030 | Write Playwright test: SearchHistoryLocalStorageOnly - verify guest search history exists in localStorage but not in server stats |           |            |

### Implementation Phase 9: Mode Transition Testing

- GOAL-009: Test transitions between guest, logged-in, and logged-out states

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-031 | Create `tests/guest-transitions.spec.js` - Set up mode transition test file |           |            |
| TASK-032 | Write Playwright test: GuestToLogin - verify guest can switch to login and become logged-in user |           |            |
| TASK-033 | Write Playwright test: GuestToSignup - verify guest can switch to signup and create account |           |            |
| TASK-034 | Write Playwright test: LogoutToGuest - verify logged-in user can logout and re-enter guest mode |           |            |
| TASK-035 | Write Playwright test: GuestSessionPersistence - verify guest state persists across page navigation |           |            |

### Implementation Phase 10: Chrome DevTools Testing

- GOAL-010: Create comprehensive testing procedures using Chrome DevTools

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-036 | Create `docs/testing/guest-mode-devtools-checklist.md` - Document all DevTools verification steps |           |            |
| TASK-037 | Document localStorage inspection procedure - verify GUEST_ID key structure and absence in daily_stats |           |            |
| TASK-038 | Document React DevTools inspection - verify AuthContext.isGuest state changes correctly |           |            |
| TASK-039 | Document Network tab inspection - verify no API calls with guest IDs (when backend is added) |           |            |
| TASK-040 | Document Console error checking - verify no errors when transitioning between modes |           |            |

### Implementation Phase 11: Cross-Browser Testing

- GOAL-011: Test guest mode functionality across different browsers

| Task    | Description                                                   | Completed | Date       |
| -------- | ------------------------------------------------------------- | --------- | ---------- |
| TASK-041 | Create `docs/testing/guest-mode-browser-compatibility.md` - Document browser testing matrix |           |            |
| TASK-042 | Test in Google Chrome - run all guest mode tests and verify UI rendering |           |            |
| TASK-043 | Test in Mozilla Firefox - verify guest mode works correctly and no console errors |           |            |
| TASK-044 | Test in Microsoft Edge - verify compatibility with Chromium-based browser |           |            |
| TASK-045 | Test in Apple Safari - verify guest mode works (MacOS/iOS testing required) |           |            |

## 3. Alternatives

### Alternative Approaches Considered

- **ALT-001**: Create dedicated Guest user accounts in database
  - **Decision**: REJECTED
  - **Rationale**: Adds unnecessary DB complexity, contradicts no-metrics requirement
  - **Trade-off**: Would persist guest data across sessions (not desired)

- **ALT-002**: Use same guest tracking as current system but ignore in stats
  - **Decision**: REJECTED
  - **Rationale**: Current system records guest metrics; need to prevent recording entirely
  - **Trade-off**: Would still add to daily_stats views array, requiring filtering

- **ALT-003**: Implement Guest mode as separate route/guard system
  - **Decision**: REJECTED
  - **Rationale**: Guest mode is application state, not a separate route or page
  - **Trade-off**: Would create duplicate routing logic, harder to maintain

- **ALT-004**: Store guest data in cookies instead of localStorage
  - **Decision**: REJECTED
  - **Rationale**: No benefit over localStorage, cookies are sent with requests (unnecessary overhead)
  - **Trade-off**: Cookies have size limits and expiration complexities

- **ALT-005**: Use Redux/Zustand for guest mode state management
  - **Decision**: REJECTED
  - **Rationale**: AuthContext already manages auth state; adding another store creates complexity
  - **Trade-off**: Would require syncing between Context and external store

**Chosen Approach**: Extend existing AuthContext with isGuest state, modify storage.js to skip guest metrics, update UI components to respect guest mode state. This leverages existing infrastructure and maintains consistency.

## 4. Dependencies

### External Dependencies

- **DEP-001**: Playwright testing framework (v1.40.0+) - Required for automated testing
- **DEP-002**: @playwright/test - Test runner for Playwright tests
- **DEP-003**: Chromium browser (for Playwright execution)

### Internal Dependencies

- **DEP-004**: `src/context/AuthContext.jsx` - Must exist and be updated first (TASK-001 to TASK-003)
- **DEP-005**: `src/lib/storage.js` - Must be updated before UI components (TASK-004 to TASK-005)
- **DEP-006**: Existing React components must be working before guest mode integration
- **DEP-007**: Existing storage.js API must remain backward compatible
- **DEP-008**: localStorage key `cookhub_guest_id` must already be defined

### Build Dependencies

- **DEP-009**: Vite dev server must be running for Playwright tests
- **DEP-010**: Existing authentication flow must be functional
- **DEP-011**: Recipe browsing/search flow must be functional

## 5. Files

### Files to Modify

- **FILE-001**: `src/context/AuthContext.jsx`
  - Add `isGuest` state
  - Add `enterGuestMode()` function
  - Update `canInteract` logic
  - Export new guest mode functions

- **FILE-002**: `src/lib/storage.js`
  - Modify `recordView()` to skip stats for guests
  - Modify `recordActiveUser()` to skip guests
  - Modify `recordNewUser()` to skip guests
  - Keep existing `getOrCreateGuestId()` method

- **FILE-003**: `src/pages/Auth/Login.jsx`
  - Add "Continue as Guest" button
  - Wire up to `enterGuestMode()` from AuthContext

- **FILE-004**: `src/pages/Auth/Signup.jsx`
  - Add "Continue as Guest" button
  - Wire up to `enterGuestMode()` from AuthContext

- **FILE-005**: `src/components/layout/Navbar.jsx`
  - Show "Guest" badge when in guest mode
  - Show Login/Signup buttons instead of Logout when guest

- **FILE-006**: `src/components/layout/Sidebar.jsx`
  - Hide Profile link for guests
  - Show Login/Signup options

- **FILE-007**: `src/pages/Recipe/RecipeDetail.jsx`
  - Disable like/favorite/review buttons for guests
  - Show "Login to {action}" messages

- **FILE-008**: `src/pages/Recipe/CreateRecipe.jsx`
  - Check for guest mode
  - Show login prompt or redirect

- **FILE-009**: `src/pages/Recipe/Profile.jsx`
  - Add guest mode check
  - Redirect guests to login

### Files to Create

- **FILE-010**: `playwright.config.js` - Playwright configuration
- **FILE-011**: `tests/guest-mode.spec.js` - Guest mode functionality tests
- **FILE-012**: `tests/guest-analytics.spec.js` - Analytics verification tests
- **FILE-013**: `tests/guest-transitions.spec.js` - Mode transition tests
- **FILE-014**: `docs/testing/guest-mode-devtools-checklist.md` - DevTools testing procedures
- **FILE-015**: `docs/testing/guest-mode-browser-compatibility.md` - Browser testing matrix

## 6. Testing

### Automated Testing (Playwright)

- **TEST-001**: Guest Mode Entry (TASK-017 to TASK-018)
  - Verify "Continue as Guest" button works from Login page
  - Verify "Continue as Guest" button works from Signup page
  - Verify redirect to Home page after entering guest mode
  - Verify "Guest" badge appears in Navbar

- **TEST-002**: Guest Browsing (TASK-019 to TASK-021)
  - Verify Guest can see Home page with recipe cards
  - Verify Guest can search recipes
  - Verify Guest can filter by category/difficulty
  - Verify Guest can click and view recipe details

- **TEST-003**: Feature Blocking (TASK-022 to TASK-026)
  - Verify Like button is disabled and shows "Login to like" message
  - Verify Favorite button is disabled and shows "Login to favorite" message
  - Verify Review form submission is blocked with "Login to review" message
  - Verify CreateRecipe page shows "Login to create recipes" message
  - Verify Profile access redirects to login page

- **TEST-004**: Analytics Verification (TASK-028 to TASK-030)
  - Verify guest views do NOT appear in daily_stats.views array
  - Verify guest IDs do NOT appear in daily_stats.activeUsers array
  - Verify guest search history exists in localStorage only
  - Verify no guest records appear in activity logs

- **TEST-005**: Mode Transitions (TASK-032 to TASK-035)
  - Verify Guest → Login transition works smoothly
  - Verify Guest → Signup → Login flow works
  - Verify Logged-in → Logout → Guest flow works
  - Verify guest ID persists across page navigation
  - Verify guest session cleared on logout

### Manual Testing (Chrome DevTools)

- **TEST-006**: LocalStorage Inspection (TASK-037)
  - Check `cookhub_guest_id` key exists and has format `guest-{randomId}`
  - Check `cookhub_daily_stats` does NOT contain any entries with guest IDs
  - Check guest search history in `cookhub_search_history` with guest IDs
  - Verify localStorage cleared on explicit logout or browser close

- **TEST-007**: React DevTools Inspection (TASK-038)
  - Verify AuthContext state shows `isGuest: true` in guest mode
  - Verify `canInteract: false` when in guest mode
  - Verify state updates correctly on mode transitions
  - Check for any console errors or warnings

- **TEST-008**: Network Tab Inspection (TASK-039)
  - Verify no API calls with guest IDs made (for future backend)
  - Verify only client-side localStorage operations occur
  - Check for any unexpected network requests

- **TEST-009**: Console Error Checking (TASK-040)
  - Monitor Console tab for errors during mode transitions
  - Verify no React hydration errors
  - Check for any type errors or warnings
  - Verify all event handlers execute without errors

### Cross-Browser Testing

- **TEST-010**: Google Chrome (TASK-042)
  - Run full test suite in Chrome
  - Verify Guest mode button styling matches UI
  - Check for Chromium-specific rendering issues
  - Test Chrome DevTools inspection procedures

- **TEST-011**: Mozilla Firefox (TASK-043)
  - Run full test suite in Firefox
  - Verify localStorage behavior (Firefox specific)
  - Check for Gecko engine rendering differences
  - Test Firefox Developer Tools compatibility

- **TEST-012**: Microsoft Edge (TASK-044)
  - Run full test suite in Edge
  - Verify Chromium-based browser compatibility
  - Check for Edge-specific CSS rendering
  - Test Edge DevTools

- **TEST-013**: Apple Safari (TASK-045)
  - Run full test suite in Safari
  - Verify WebKit engine rendering
  - Test Safari localStorage persistence behavior
  - Check for Safari-specific CSS quirks
  - Test Safari Web Inspector

### Test Execution Order

1. **Phase 1**: Implement Core Guest Mode (TASK-001 to TASK-005)
   - Run smoke tests: Guest mode entry works
   - Verify no errors in console

2. **Phase 2 to 4**: Update UI Components (TASK-006 to TASK-013)
   - Test guest mode navigation
   - Verify feature blocking UI
   - Check Profile redirect

3. **Phase 5 to 6**: Setup Playwright and Write Tests (TASK-014 to TASK-021)
   - Initialize test suite
   - Run basic functionality tests

4. **Phase 7**: Blocking Verification Tests (TASK-022 to TASK-026)
   - Verify all interactive features blocked
   - Confirm UI messaging displays correctly

5. **Phase 8**: Analytics Verification (TASK-027 to TASK-030)
   - Manually check localStorage
   - Run automated analytics tests
   - Confirm no guest metrics recorded

6. **Phase 9**: Mode Transitions (TASK-031 to TASK-035)
   - Test all transition paths
   - Verify state persistence

7. **Phase 10 to 11**: DevTools & Cross-Browser (TASK-036 to TASK-045)
   - Execute DevTools checklist
   - Run cross-browser test matrix
   - Document any browser-specific issues

## 7. Risks & Assumptions

### Implementation Risks

- **RISK-001**: AuthContext state management complexity may increase with isGuest flag
  - **Mitigation**: Keep guest logic simple and well-documented
  - **Impact**: Medium - Manageable with clear state transitions

- **RISK-002**: Incomplete feature blocking may allow guests to interact
  - **Mitigation**: Comprehensive Playwright test coverage for all interactive elements
  - **Impact**: High - Security and data integrity concern

- **RISK-003**: Existing components may have hardcoded assumptions about user.state
  - **Mitigation**: Code review and incremental testing after each component update
  - **Impact**: Medium - May require unexpected refactoring

- **RISK-004**: localStorage key conflicts or race conditions in concurrent tabs
  - **Mitigation**: Test with multiple tabs open, use unique guest IDs
  - **Impact**: Low - Guest mode is stateless by design

- **RISK-005**: Playwright tests may be flaky due to timing issues
  - **Mitigation**: Use explicit waits and assertions, retry failed tests
  - **Impact**: Low - Common testing challenge, manageable

### Assumptions

- **ASSUMPTION-001**: Existing AuthContext structure can be extended without breaking changes
  - **Validation**: Review AuthContext.jsx before implementation
  - **Impact**: Medium - Core change, requires careful analysis

- **ASSUMPTION-002**: storage.js current `recordView()` logic can be modified without breaking existing functionality
  - **Validation**: Check current implementation and test logged-in user views after changes
  - **Impact**: Low - Should be backward compatible

- **ASSUMPTION-003**: Users have modern browsers supporting ES6+ JavaScript
  - **Validation**: Browser compatibility testing in Phase 11
  - **Impact**: Low - Project already targets modern browsers

- **ASSUMPTION-004**: No additional localStorage schema changes required
  - **Validation**: Confirm existing GUEST_ID key works for session management
  - **Impact**: Low - Reusing existing infrastructure

- **ASSUMPTION-005**: Playwright test environment can be configured for Vite dev server
  - **Validation**: Setup test environment early in Phase 5
  - **Impact**: Medium - Testing infrastructure dependency

- **ASSUMPTION-006**: Future backend migration will respect guest mode constraints
  - **Validation**: Document guest mode requirements for future database migration
  - **Impact**: Medium - Technical debt for future work

- **ASSUMPTION-007**: No existing guest analytics data needs to be preserved
  - **Validation**: Current system tracks guests, but requirement is to remove those metrics
  - **Impact**: Low - Breaking change, matches project requirements

### Technical Debt Considerations

- **DEBT-001**: Guest mode state in AuthContext may conflict with future backend integration
  - **Remediation**: Document guest mode architecture for backend API design
  - **Effort**: Small (1-2 hours documentation)

- **DEBT-002**: localStorage-based guest tracking will need to be replaced with backend session management
  - **Remediation**: Plan guest session handling in future API endpoints
  - **Effort**: Medium (backend API design task)

- **DEBT-003**: No guest account recovery or persistent guest history (by design)
  - **Remediation**: Future feature: optional guest account upgrade to registered user
  - **Effort**: Large (backend + database + UI changes)

## 8. Related Specifications / Further Reading

### Project Documentation

- [Storage Data Model](../.serena/memories/storage-data-model.md) - Current localStorage structure and API
- [Auth Context](../.serena/memories/auth-context.md) - Authentication context implementation
- [Recipe Features](../.serena/memories/recipe-features.md) - Recipe interaction features
- [Project Overview](../.serena/memories/project-overview.md) - Overall project architecture

### React & Testing Documentation

- [React Context API](https://react.dev/reference/react/useContext) - React Context best practices
- [Playwright Documentation](https://playwright.dev/docs/intro) - Playwright testing framework
- [Vite Testing Guide](https://vitejs.dev/guide/testing.html) - Testing with Vite
- [React Testing Patterns](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library) - Testing best practices

### Chrome DevTools Resources

- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) - DevTools automation
- [React DevTools](https://react.dev/learn/react-developer-tools) - React DevTools usage
- [Local Storage Inspector](https://developer.chrome.com/docs/devtools/storage/localstorage) - localStorage inspection

### External References

- [Best Practices for Guest Mode](https://uxdesign.cc/ux-patterns-for-guest-users-7c5a5b6f4b7b) - UX patterns for guest users
- [Authentication State Management](https://auth0.com/blog/complete-guide-to-react-user-authentication) - Auth state patterns
- [Testing Authentication with Playwright](https://playwright.dev/docs/auth#multi-factor-authentication) - Authentication testing

### Future Implementation Notes

When implementing backend API integration (future work), the following guest mode constraints must be respected:

1. **No guest records in database** - Guests remain client-side only
2. **No guest contributions to metrics** - Backend must filter out guest IDs from analytics
3. **Guest search history** - Keep client-side in localStorage, do not persist to database
4. **Guest authentication** - Use session tokens but mark as guest type for permissions check
5. **Guest role permissions** - Treat as "pending" status for all access control checks
