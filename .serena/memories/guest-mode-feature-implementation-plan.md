# Guest Mode Feature Implementation Plan

**Date Created:** February 7, 2026  
**Status:** Implementation Plan v1.1 - Enhanced with Assessment Feedback  
**Last Updated:** February 8, 2026

## Summary

Created comprehensive implementation plan for dedicated Guest mode feature allowing users to browse Recipe Sharing System without authentication.

## Assessment Feedback Integration (February 8, 2026)

## Assessment Feedback Integration (February 8, 2026)

After comprehensive review by technical assessor rated 8.5/10, implementation plan was enhanced with following improvements:

### Accepted Recommendations (Fully Implemented)

1. **Session Duration Clarification**
   - Updated FREQ-G-014: "persist in localStorage across page refreshes until explicit logout or browser close"
   - Updated SEC-G-004 to match FREQ-G-014 for consistency
   - Eliminates ambiguity about session persistence

2. **Pattern Matching Robustness**
   - Changed from `guest:{id}` to `__GUEST__{randomId}` prefix
   - Added isGuest flag check as primary detection method
   - Pattern matching as fallback only

3. **localStorage Disabled Handling**
   - Added FREQ-G-016: "System must gracefully handle localStorage disabled"
   - Added GUEST-CON-006: "Guest mode must fail gracefully if localStorage unavailable"
   - Added TASK-002 modification: localStorage availability check in enterGuestMode()

4. **Multiple Tab Synchronization**
   - Added GUEST-CON-007: "Guest state must be synchronized across multiple tabs"
   - Added TASK-046: Implement storage event listener in AuthContext
   - Updated RISK-004 mitigation to include synchronization mechanism

5. **Acceptance Criteria Definition**
   - Added new Section 6: Comprehensive Acceptance Criteria with 30 criteria (AC-001 through AC-030)
   - Covers functional completeness, analytics integrity, testing quality, error handling, integration compatibility
   - Includes clear "Definition of Done" with 7 conditions

6. **Test Data Cleanup**
   - Updated TASK-016: Added "localStorage teardown function to clear state between test runs"
   - Ensures tests don't interfere with each other

7. **Phase-Level Time Estimates**
   - Added rough estimates to all 11 phases (e.g., "Phase 1 (2-3 hours)")
   - Accounts for uncertainty and developer familiarity assumptions
   - More realistic than per-task estimates

8. **Analytics Early Verification**
   - Phase 8 includes "Recommended Early Verification" note
   - Suggests running analytics smoke test after Phase 4
   - Allows early detection of metrics recording issues

### Deferred Recommendations

1. **Detailed UI Mockups/Wireframes**
   - Deferred: Out of scope for current implementation phase
   - Rationale: Existing UI patterns and PAT-G-004 guideline provide sufficient guidance
   - Future consideration: During design phase for major UI overhauls

### Modified Recommendations

1. **Rollback Plan Documentation**
   - Rejected as unnecessary: Client-side localStorage feature
   - Simpler rollback exists: Clear localStorage keys + revert code via version control
   - Documented as ALT-006 in Alternatives section

### Decision Tree Summary

**Accepted** (6 items, fully incorporated): Session clarity, pattern matching, localStorage error handling, tab sync, acceptance criteria, test cleanup, phase estimates, early analytics verification  
**Deferred** (1 item): Detailed UI mockups (future design phase)  
**Rejected** (1 item): Rollback plan (existing mechanism sufficient)

## Key Requirements

### Functional Requirements (FREQ-G-001 to FREQ-G-015)

**Access Level:**
- Read-only access equivalent to Pending/Suspended users
- Can browse Home, Search, and Recipe Detail pages
- Can search and filter recipes

**Restricted Features:**
- CANNOT like recipes
- CANNOT favorite recipes
- CANNOT add reviews
- CANNOT create recipes
- CANNOT access profile pages
- Redirected to login when accessing protected areas

**Analytics & Metrics:**
- NOT counted in daily_active_users
- NOT counted in recipe view statistics
- NOT recorded in user management dashboard
- NO activity logs generated

## Implementation Plan Location

**File:** `plan/feature-guest-mode-1.md` (Version 1.1, Last Updated: 2026-02-08)

## Minor Fixes Applied (2026-02-08)

**Fixed Typo:**
- FREQ-G-014: Removed redundant "duration only" suffix
  - Before: "until explicit logout or browser close duration only"
  - After: "until explicit logout or browser close"
  - Location: Section 1, Line 34

**Updated Data Format Consistency:**
- DATA-G-001: Updated guest ID format documentation
  - Before: `guest-{randomId}`
  - After: `__GUEST__{randomId}`
  - Rationale: Matches implementation decision in TASK-004 and TASK-005
  - Location: Section 1, Line 51

## Plan Structure (Updated v1.1)

### Total Tasks: 46 tasks across 11 phases (added TASK-046 for tab synchronization)
### Phase Estimates Added

- **Phase 1**: Core Guest Mode State Management (2-3 hours)
- **Phase 2**: Guest Mode Entry UI (1-2 hours)
- **Phase 3**: Navigation Updates (1-2 hours)
- **Phase 4**: Feature Blocking (2-3 hours)
- **Phase 5**: Playwright Testing Setup (1-2 hours)
- **Phase 6**: Guest Mode Functionality Testing (3-4 hours)
- **Phase 7**: Analytics Verification Testing (2-3 hours)
- **Phase 8**: Mode Transition Testing (1-2 hours)
- **Phase 9**: Chrome DevTools Testing (1-2 hours)
- **Phase 10**: Cross-Browser Testing (2-3 hours)
- **Phase 11**: Documentation (estimated within Phase 10)

**Total Estimated Time: 18-27 hours** (2-4 days of focused development + testing)

#### Phase 1: Core Guest Mode State Management (5 tasks)
- Update `AuthContext.jsx` with `isGuest` state
- Add `enterGuestMode()` function
- Update `canInteract` logic
- Modify `storage.js` to skip guest metrics in `recordView()`
- Modify `storage.js` to skip guest metrics in `recordActiveUser()` and `recordNewUser()`

#### Phase 2: Guest Mode Entry UI (2 tasks)
- Add "Continue as Guest" button to Login.jsx
- Add "Continue as Guest" button to Signup.jsx

#### Phase 3: Navigation Updates (2 tasks)
- Update Navbar.jsx to show guest status and login/signup buttons
- Update Sidebar.jsx for guest mode menu items

#### Phase 4: Feature Blocking (4 tasks)
- Block guest interactions in RecipeDetail.jsx
- Block recipe creation in CreateRecipe.jsx
- Redirect guests from Profile.jsx
- Verify admin pages block guests

#### Phase 5: Playwright Testing Setup (3 tasks)
- Install Playwright dependencies
- Create playwright.config.js
- Create tests/guest-mode.spec.js

#### Phase 6: Guest Mode Testing (5 tasks)
- Test guest entry from Login and Signup
- Test guest browsing (Home, Search, RecipeDetail)
- Test feature blocking (like, favorite, review, create)

#### Phase 7: Analytics Verification (4 tasks)
- Create tests/guest-analytics.spec.js
- Verify guest views not in daily_stats
- Verify guests not in active users
- Verify guest search history only in localStorage

#### Phase 8: Mode Transition Testing (5 tasks)
- Create tests/guest-transitions.spec.js
- Test Guest → Login
- Test Guest → Signup → Login
- Test Logout → Guest
- Test guest session persistence

#### Phase 9: Chrome DevTools Testing (5 tasks)
- Create devtools-checklist.md
- Document localStorage inspection procedures
- Document React DevTools inspection
- Document Network tab inspection
- Document console error checking

#### Phase 10: Cross-Browser Testing (5 tasks)
- Test in Google Chrome
- Test in Mozilla Firefox
- Test in Microsoft Edge
- Test in Apple Safari

#### Phase 11: Documentation (5 tasks)
- Create browser compatibility matrix
- Document all testing procedures
- Update project documentation

## Key Technical Decisions

### State Management
- **AuthContext.jsx**: Extended with `isGuest` state
- **Storage.js**: Modified to skip metrics for guest IDs (pattern: `guest:{id}`)
- **No database records**: Guests remain client-side in localStorage only

### Guest ID Pattern
- Format: `guest-{randomId}`
- Generated by existing `storage.getOrCreateGuestId()`
- Stored in localStorage key: `cookhub_guest_id`
- Cleared on logout or browser close

### Analytics Exclusion
- `recordView()`: Skips `daily_stats.views` for guests
- `recordActiveUser()`: Skips guests
- `recordNewUser()`: Skips guests
- Search history: Stored in localStorage only (client-side)

### UI Blocking Strategy
- Disabled buttons with tooltips: "Login to {action}"
- Protected route redirects: Profile, CreateRecipe
- Clear visual indicators: "Guest" badge in Navbar
- Consistent messaging: "Login to {action}" format

## Technical Constraints

### Must NOT Change
- Existing localStorage schema (GUEST_ID key already exists)
- Current AuthContext structure (only extending)
- Storage.js API surface (modifying behavior only)
- Existing component patterns (following established conventions)

### Must Implement
- Guest mode state tracking
- Metrics exclusion for guests
- Feature blocking at UI level
- Comprehensive Playwright test coverage
- Chrome DevTools testing procedures
- Cross-browser compatibility verification

## Testing Strategy

### Automated Tests (Playwright)
- **Guest-mode.spec.js**: 15+ tests for guest entry, browsing, and blocking
- **Guest-analytics.spec.js**: 8+ tests for metrics verification
- **Guest-transitions.spec.js**: 5+ tests for state transitions

### Manual Tests (Chrome DevTools)
- localStorage inspection
- React DevTools state verification
- Network tab monitoring
- Console error checking

### Cross-Browser Testing
- Chrome, Firefox, Edge, Safari
- Full test suite on each browser
- Browser-specific issue documentation

## Files Affected

### Modified Files (9 files)
1. `src/context/AuthContext.jsx` - State management
2. `src/lib/storage.js` - Metrics exclusion logic
3. `src/pages/Auth/Login.jsx` - Guest entry
4. `src/pages/Auth/Signup.jsx` - Guest entry
5. `src/components/layout/Navbar.jsx` - Guest status display
6. `src/components/layout/Sidebar.jsx` - Guest menu
7. `src/pages/Recipe/RecipeDetail.jsx` - Feature blocking
8. `src/pages/Recipe/CreateRecipe.jsx` - Access blocking
9. `src/pages/Recipe/Profile.jsx` - Protected route

### Created Files (6 files)
1. `playwright.config.js` - Test configuration
2. `tests/guest-mode.spec.js` - Guest mode tests
3. `tests/guest-analytics.spec.js` - Analytics tests
4. `tests/guest-transitions.spec.js` - Transition tests
5. `docs/testing/guest-mode-devtools-checklist.md` - DevTools procedures
6. `docs/testing/guest-mode-browser-compatibility.md` - Browser matrix

## Alternative Approaches Considered

### Rejected Alternatives

1. **Dedicated Guest User Accounts in Database**
   - Reject: Adds DB complexity, contradicts no-metrics requirement
   - Trade-off: Persistent guest data (not desired)

2. **Continue Current Guest Tracking with Post-Hoc Filtering**
   - Reject: Would still record guest metrics in daily_stats
   - Trade-off: Additional filtering logic everywhere

3. **Separate Guest Route/Guard System**
   - Reject: Guest mode is state, not a route
   - Trade-off: Duplicate routing logic

4. **Cookies Instead of localStorage for Guest ID**
   - Reject: Cookies sent with each request (unnecessary overhead)
   - Trade-off: Size limits and expiration complexity

5. **Redux/Zustand for Guest State**
   - Reject: AuthContext already manages auth state
   - Trade-off: State sync complexity

### Chosen Approach

**Extend existing AuthContext and storage.js** - Leverages current infrastructure, maintains consistency, minimal refactoring required.

## Risks & Mitigations

### Implementation Risks

1. **AuthContext Complexity Increases**
   - Risk: State management may become harder to understand
   - Mitigation: Clear documentation and incremental testing

2. **Incomplete Feature Blocking**
   - Risk: Guests might bypass blocks
   - Mitigation: Comprehensive Playwright test coverage

3. **Assumptions About User.state**
   - Risk: Components may have hardcoded logic
   - Mitigation: Code review + incremental testing

4. **localStorage Race Conditions**
   - Risk: Concurrent tabs with same guest ID
   - Mitigation: Test with multiple tabs, use unique IDs

### Technical Debt

1. **Guest Mode Conflicts with Future Backend**
   - Debt: Current changes are localStorage-based
   - Future: Document guest architecture for backend API design

2. **No Guest Account Recovery**
   - Debt: Guest history lost on browser close
   - Future: Optional guest upgrade to registered user

## Next Steps

1. **Start Implementation** with Phase 1 (TASK-001 to TASK-005)
2. **Test Incrementally** after each phase
3. **Run Playwright Suite** after Phase 6 completion
4. **Execute DevTools Checklist** after UI changes
5. **Cross-Browser Testing** before marking complete

## Memory Usage

This memory captures the complete Guest Mode Feature Implementation Plan. 

When implementing:
1. Follow `plan/feature-guest-mode-1.md` step-by-step order
2. Execute phases sequentially, not in parallel
3. Update task completion status after each task
4. Run tests before proceeding to next phase
5. Update this memory when major decisions or changes occur

## Related Memories

- `auth-context` - Current authentication implementation
- `storage-data-model` - Current localStorage structure
- `recipe-features` - Recipe interaction patterns
- `project-overview` - Overall project architecture

## Documentation Links

- **Implementation Plan:** `plan/feature-guest-mode-1.md`
- **React Context:** [useContext Docs](https://react.dev/reference/react/useContext)
- **Playwright:** [Playwright Documentation](https://playwright.dev/docs/intro)
- **Testing**: [React Testing Patterns](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)
